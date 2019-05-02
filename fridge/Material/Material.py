import numpy as np
import glob
import os
import yaml
import fridge.Material.Element as Element

AVOGADROS_NUMBER = 0.6022140857
# Requirements for the material reader
cur_dir = os.path.dirname(__file__)
material_dir = os.path.join(cur_dir, '../data/materials/')


class Material(object):
    """Creates a material consisting of elements based on the Material database."""
    def __init__(self):
        self.enrichmentDict = {}
        self.isotopeDict = {}
        self.weightPercent = {}
        self.atomPercent = {}
        self.atomDensity = 0.0
        self.elementDict = {}
        self.name = ''
        self.elements = []
        self.zaids = []
        self.weightFraction = []
        self.density = 0.0
        self.linearCoeffExpansion = 0.0
        self.enrichmentZaids = []
        self.enrichmentIsotopes = []
        self.enrichmentVector = []
        self.materialName = ''

    def setMaterial(self, material):
        self.name = material
        self.readMaterial(self.name)
        self.getMaterial()

    def readMaterial(self, material):
        """Read in the material data from the material database."""
        materialFile = glob.glob(os.path.join(material_dir, material + '.yaml'))

        if not materialFile:
            raise AssertionError("Material {}, not found in material database. Please create material file for {}."
                                 .format(material, material))

        with open(materialFile[0], "r") as file:
            inputs = yaml.safe_load(file)
            self.name = inputs['Name']
            self.materialName = material
            self.elements = inputs['Elements']
            self.zaids = inputs['ZAIDs']
            self.weightFraction = inputs['Weight Fractions'] if 'Weight Fractions' in inputs else []
            self.density = inputs['Density']
            self.linearCoeffExpansion = inputs['Linear Coefficient of Expansion']
            self.enrichmentZaids = inputs['Enrichment ZAIDs'] if 'Enrichment ZAIDs' in inputs else []
            self.enrichmentIsotopes = inputs['Enrichment Isotopes'] if 'Enrichment Isotopes' in inputs else []
            self.enrichmentVector = inputs['Enrichment Vector'] if 'Enrichment Vector' in inputs else []

    def getMaterial(self):
        """Create a material based on the data from the material database."""
        for num, zaid in enumerate(self.enrichmentZaids):
            enrichedIsotopeDict = {}
            for isoNum, isotopes in enumerate(self.enrichmentIsotopes[num]):
                enrichedIsotopeDict[isotopes] = self.enrichmentVector[num][isoNum]
            self.enrichmentDict[zaid] = enrichedIsotopeDict
        for num, element in enumerate(self.elements):
            self.elementDict[self.zaids[num]] = Element.Element(element)
        self.adjustEnrichments()
        self.getWeightPercent()
        self.atomDensity, self.atomPercent = getAtomPercent(self.weightPercent, self.density,
                                                            self.elementDict)

    def adjustEnrichments(self):
        """Adjust the element's natural abundance to compensate for enrichment."""
        for elementEnrichement, zaidVector in self.enrichmentDict.items():
            for zaid, enrichmentPercent in zaidVector.items():
                self.elementDict[elementEnrichement].weightPercentDict[zaid] = enrichmentPercent

    def getWeightPercent(self, voidPercent=1.0):
        """Calculates the weight percent of a material."""
        weightTotal = 0.0
        for zaidNum, zaid in enumerate(self.zaids):
            for isotope, isotopeFraction in self.elementDict[zaid].weightPercentDict.items():
                if isotopeFraction != 0.0:
                    self.weightPercent[isotope] = isotopeFraction * self.weightFraction[zaidNum] * voidPercent
                    weightTotal += self.weightPercent[isotope]
        try:
            assert np.allclose(weightTotal, 1.0 * voidPercent)
        except AssertionError:
            print("Weight percent does not sum to 1.0 for {}. Check the material file.".format(self.name))

    def voidMaterial(self, voidPercent):
        self.getWeightPercent(voidPercent)
        self.atomDensity, self.atomPercent = getAtomPercent(self.weightPercent, self.density,
                                                            self.elementDict)


def getAtomPercent(weightPercents, density, elementDict):
    """Converts the weight percent of a material to the atom percent and atom density."""
    atomDensities = {}
    atomPercent = {}
    for zaid, weight in weightPercents.items():
        element = str(zaid)
        if len(element) < 5:
            currentElement = int(element[:1] + '000')
        else:
            currentElement = int(element[:2] + '000')
        atomDensities[zaid] = weight * density * AVOGADROS_NUMBER / elementDict[currentElement].molecularMassDict[zaid]
    atomDensity = sum(atomDensities.values())

    for zaid, atomicDensity in atomDensities.items():
        atomPercent[zaid] = atomicDensity / atomDensity
    return atomDensity, atomPercent
