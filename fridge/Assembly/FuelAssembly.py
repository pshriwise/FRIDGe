import fridge.Assembly.Assembly as Assembly
import fridge.Constituent.FuelPin as Fuelpin
import fridge.Constituent.FuelBond as Fuelbond
import fridge.Constituent.FuelClad as Fuelclad
import fridge.Constituent.FuelCoolant as Fuelcoolant
import fridge.Constituent.BlankCoolant as Blankcoolant
import fridge.Constituent.FuelUniverse as Fueluniverse
import fridge.Constituent.InnerDuct as Innerduct
import fridge.Constituent.Duct as Outerduct
import fridge.Constituent.Smear as Smeared
import fridge.Constituent.OuterShell as Outershell
import fridge.Constituent.UpperCoolant as Uppersodium
import fridge.Constituent.LowerCoolant as Lowersodium
import fridge.Constituent.EveryThingElse as Everythingelse
import fridge.Material.Material
import fridge.utilities.mcnpCreatorFunctions as mcnpCF
import fridge.utilities.utilities as utilities
import math

import fridge.utilities.utilities


class FuelAssembly(Assembly.Assembly):
    """
    Subclass of base assembly for fuel assemblies.

    Fuel assembly consists of upper/lower sodium region, upper/lower reflector regions,
    a plenum region, and a fuel region. All information for fuel, reflector and plenum regions are read in from the
    assembly yaml file.
    """

    def __init__(self, assemblyInformation):
        super().__init__(assemblyInformation)
        self.assemblyUniverse = 0
        self.pinUniverse = 0
        self.fuel = None
        self.bond = None
        self.clad = None
        self.coolant = None
        self.blankUniverse = None
        self.blankCoolant = None
        self.latticeUniverse = None
        self.fuelUniverse = None
        self.innerDuct = None
        self.duct = None
        self.plenum = None
        self.upperReflector = None
        self.lowerReflector = None
        self.upperSodium = None
        self.lowerSodium = None
        self.assemblyShell = None
        self.upperReflectorPosition = []
        self.lowerReflectorPosition = []
        self.assemblyCellList = []
        self.assemblySurfaceList = []
        self.assemblyMaterialList = []
        self.everythingElse = None

        self.position = []
        self.cladOD = 0
        self.cladID = 0
        self.fuelDiameter = 0
        self.fuelPitch = 0
        self.wireWrapDiameter = 0
        self.bondAboveFuel = 0.0
        self.fuelHeight = 0
        self.fuelMaterial = ''
        self.cladMaterial = ''
        self.bondMaterial = ''

        self.plenumHeight = 0
        self.plenumMaterial = ''
        self.plenumPosition = []

        self.reflectorHeight = 0
        self.reflectorMaterial = ''

        self.read_assembly_data()
        self.getAssembly()

    def read_assembly_data(self):
        """ Reads in data from assembly yaml file."""
        self.getAssemblyInfo(self.inputs)
        self.getFuelRegionInfo(self.inputs)
        self.getPlenumRegionInfo(self.inputs)
        self.getReflectorInfo(self.inputs)

    def getAssembly(self):
        """Creates each component of the assembly."""
        self.fuelHeightWithBond = self.fuelHeight + self.bondAboveFuel
        definedHeight = 2 * self.reflectorHeight + self.fuelHeightWithBond + self.plenumHeight
        excessCoolantHeight = (self.assemblyHeight - definedHeight) / 2
        heightToUpperCoolant = definedHeight - self.reflectorHeight
        heightToUpperReflector = self.fuelHeightWithBond + self.plenumHeight
        upperCoolantPosition = fridge.utilities.utilities.getPosition(self.assemblyPosition, self.assemblyPitch, heightToUpperCoolant)
        upperReflectorPosition = fridge.utilities.utilities.getPosition(self.assemblyPosition, self.assemblyPitch, heightToUpperReflector)
        lowerReflectorPosition = fridge.utilities.utilities.getPosition(self.assemblyPosition, self.assemblyPitch, -self.reflectorHeight)
        bottomCoolantPosition = fridge.utilities.utilities.getPosition(self.assemblyPosition, self.assemblyPitch,
                                                                       -(self.reflectorHeight + excessCoolantHeight))

        self.assemblyUniverse = self.universe
        self.universe += 1
        self.pinUniverse = self.universe
        self.fuel = Fuelpin.FuelPin([[self.universe, self.cellNum, self.surfaceNum, self.fuelMaterial, self.xcSet,
                                      self.position, self.materialNum], [self.fuelDiameter, self.fuelHeight]])

        self.updateIdentifiers(False)
        self.bond = Fuelbond.FuelBond([[self.universe, self.cellNum, self.surfaceNum, self.bondMaterial, self.xcSet,
                                        self.position, self.materialNum],
                                       [self.cladID, self.fuelHeightWithBond, self.fuel.surfaceNum]])

        self.updateIdentifiers(False)
        self.clad = Fuelclad.FuelClad([[self.universe, self.cellNum, self.surfaceNum, self.cladMaterial, self.xcSet,
                                        self.position, self.materialNum],
                                       [self.cladOD, self.fuelHeightWithBond, self.bond.surfaceNum]])

        self.updateIdentifiers(False)
        smearedCoolantInfo = [self.fuelHeightWithBond, self.cladOD, self.wireWrapDiameter,
                              self.wireWrapAxialPitch, self.fuelPitch, self.coolantMaterial, self.cladMaterial]
        smearedCoolantMaterial = fridge.Material.Material.smear_coolant_wirewrap(smearedCoolantInfo)
        self.coolant = Fuelcoolant.FuelCoolant([[self.universe, self.cellNum, self.surfaceNum, smearedCoolantMaterial,
                                                 self.xcSet, self.position, self.materialNum],
                                                [self.fuelPitch, self.fuelHeightWithBond, self.clad.surfaceNum],
                                                'Wire Wrap + Coolant'], voidMaterial=self.coolantMaterial,
                                               voidPercent=self.voidPercent)
        self.updateIdentifiers(True)
        self.blankUniverse = self.universe
        self.blankCoolant = Blankcoolant.BlankCoolant([[self.universe, self.cellNum, self.surfaceNum,
                                                        self.coolantMaterial, self.xcSet, self.position,
                                                        self.materialNum],
                                                       [self.fuelPitch, self.fuelHeightWithBond,
                                                        self.coolant.surfaceNum]], voidPercent=self.voidPercent)
        self.updateIdentifiers(True)
        self.latticeUniverse = self.universe
        self.fuelUniverse = Fueluniverse.FuelUniverse([self.pinUniverse, self.blankUniverse, self.pinsPerAssembly,
                                                       self.cellNum, self.blankCoolant.cellNum, self.latticeUniverse])

        self.updateIdentifiers(True)
        self.innerDuct = Innerduct.InnerDuct([[self.universe, self.cellNum, self.surfaceNum, '', self.xcSet,
                                               self.position, self.materialNum],
                                              [self.assemblyUniverse, self.latticeUniverse, self.ductInnerFlatToFlat,
                                               self.fuelHeightWithBond]])

        self.updateIdentifiers(False)
        self.plenum = Smeared.Smear([[self.assemblyUniverse, self.cellNum, self.surfaceNum, self.plenumMaterial,
                                      self.xcSet, self.plenumPosition, self.materialNum],
                                     [self.ductInnerFlatToFlat, self.plenumHeight], 'Plenum'],
                                    voidMaterial=self.coolantMaterial, voidPercent=self.voidPercent)

        self.updateIdentifiers(False)
        self.upperReflector = Smeared.Smear([[self.assemblyUniverse, self.cellNum, self.surfaceNum,
                                              self.reflectorMaterial, self.xcSet, upperReflectorPosition,
                                              self.materialNum],
                                             [self.ductInnerFlatToFlat, self.reflectorHeight], 'Upper Reflector'],
                                            voidMaterial=self.coolantMaterial, voidPercent=self.voidPercent)

        self.updateIdentifiers(False)
        self.lowerReflector = Smeared.Smear([[self.assemblyUniverse, self.cellNum, self.surfaceNum,
                                              self.reflectorMaterial, self.xcSet, lowerReflectorPosition,
                                              self.materialNum],
                                             [self.ductInnerFlatToFlat, self.reflectorHeight], 'Lower Reflector'],
                                            voidMaterial=self.coolantMaterial, voidPercent=self.voidPercent)

        self.updateIdentifiers(False)
        innerSurfaceNums = [self.innerDuct.surfaceNum, self.lowerReflector.surfaceNum, self. upperReflector.surfaceNum,
                            self.plenum.surfaceNum]
        self.duct = Outerduct.Duct([[self.assemblyUniverse, self.cellNum, self.surfaceNum, self.assemblyMaterial,
                                     self.xcSet, lowerReflectorPosition, self.materialNum],
                                    [self.ductOuterFlatToFlatMCNPEdge, definedHeight, innerSurfaceNums]])

        self.updateIdentifiers(False)
        self.lowerSodium = Lowersodium.LowerCoolant([[self.assemblyUniverse, self.cellNum, self.surfaceNum,
                                                      self.coolantMaterial, self.xcSet, bottomCoolantPosition,
                                                      self.materialNum],
                                                     [excessCoolantHeight,
                                                     self.ductOuterFlatToFlatMCNPEdge]], voidPercent=self.voidPercent)

        self.updateIdentifiers(False)
        self.upperSodium = Uppersodium.UpperCoolant([[self.assemblyUniverse, self.cellNum, self.surfaceNum,
                                                      self.coolantMaterial, self.xcSet, upperCoolantPosition,
                                                      self.materialNum],
                                                     [excessCoolantHeight,
                                                     self.ductOuterFlatToFlatMCNPEdge]], voidPercent=self.voidPercent)

        self.updateIdentifiers(False)
        self.assemblyShell = Outershell.OuterShell([[self.assemblyUniverse, self.cellNum, self.surfaceNum,
                                                     self.coolantMaterial, self.xcSet, bottomCoolantPosition,
                                                     self.materialNum],
                                                    [self.assemblyHeight,  self.ductOuterFlatToFlat]])

        self.assemblyCellList = [self.fuel, self.bond, self.clad, self.coolant, self.blankCoolant, self.fuelUniverse,
                                 self.innerDuct, self.plenum, self.upperReflector, self.lowerReflector,
                                 self.duct, self. lowerSodium, self.upperSodium, self.assemblyShell]
        self.assemblySurfaceList = [self.fuel, self.bond, self.clad, self.coolant, self.blankCoolant, self.innerDuct, self.plenum,
                                    self.upperReflector, self.lowerReflector, self.duct, self. lowerSodium,
                                    self.upperSodium, self.assemblyShell]
        self.assemblyMaterialList = [self.fuel, self.bond, self.clad, self.coolant, self.blankCoolant, self.innerDuct, self.plenum,
                                     self.upperReflector, self.lowerReflector, self.duct, self. lowerSodium,
                                     self.upperSodium]

        if 'Single' in self.globalVars.input_type:
            self.updateIdentifiers(False)
            self.everythingElse = Everythingelse.EveryThingElse([self.cellNum, self.assemblyShell.surfaceNum])
            self.assemblyCellList.append(self.everythingElse)

    def getFuelRegionInfo(self, inputs):
        """Reads in the fuel region data from the assembly yaml file."""
        self.position = fridge.utilities.utilities.getPosition(self.assemblyPosition, self.assemblyPitch, 0.0)
        self.cladOD = float(inputs['Pin Diameter'])
        self.cladID = self.cladOD - 2*float(inputs['Clad Thickness'])
        try:
            self.fuelDiameter = float(inputs["Fuel Diameter"])
        except KeyError:
            self.fuelDiameter = math.sqrt(float(inputs['Fuel Smear'])) * self.cladID
        self.fuelPitch = float(inputs['Pitch'])
        self.wireWrapDiameter = float(inputs['Wire Wrap Diameter'])
        self.wireWrapAxialPitch = float(inputs['Wire Wrap Axial Pitch'])
        self.fuelHeight = float(inputs['Fuel Height'])
        self.fuelMaterial = inputs['Fuel']
        self.cladMaterial = inputs['Clad']
        self.bondMaterial = inputs['Bond']
        self.bondAboveFuel = float(inputs["Bond Above Fuel"]) \
            if 'Bond Above Fuel' in inputs else 0.0

    def getPlenumRegionInfo(self, inputs):
        """Reads in the plenum region data from the assembly yaml file."""
        self.plenumHeight = float(inputs['Plenum Height'])
        self.plenumPosition = fridge.utilities.utilities.getPosition(self.assemblyPosition, self.assemblyPitch,
                                                                     self.fuelHeight + self.bondAboveFuel)
        self.plenumMaterial = inputs['Plenum Smear']

    def getReflectorInfo(self, inputs):
        """Reads in the reflector region data form the assembly yaml file."""
        self.reflectorHeight = float(inputs['Reflector Height'])
        self.reflectorMaterial = inputs['Reflector Smear']

