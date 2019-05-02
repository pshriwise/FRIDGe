import fridge.Constituent.Constituent as Constituent
import fridge.Material.Material
import fridge.utilities.mcnpCreatorFunctions as mcnpCF


class Smear(Constituent.Constituent):
    """Creates a constituent which is a smear of materials."""
    def __init__(self, unitInfo, voidMaterial='', voidPercent=1.0):
        self.universe = unitInfo[0][0]
        self.cellNum = unitInfo[0][1]
        self.surfaceNum = unitInfo[0][2]
        self.materialXCLibrary = unitInfo[0][4]
        self.material = unitInfo[0][3]
        self.position = unitInfo[0][5]
        self.materialNum = unitInfo[0][6]
        self.componentName = unitInfo[2]
        if voidPercent == 1.0:
            self.material = fridge.Material.Material.get_smeared_material(self.material)
        else:
            self.material = fridge.Material.Material.get_smeared_material(self.material, void_material=voidMaterial, void_percent=voidPercent)
        self.makeComponent(unitInfo[1])
        self.getMaterialCard(self.material)
        self.flat2flat = unitInfo[1][0]
        self.height = unitInfo[1][1]

    def makeComponent(self, ductInfo):
        self.flat2flat = ductInfo[0]
        self.height = ductInfo[1]
        surfaceComment = "$Assembly: {}".format(self.componentName)
        cellComment = "$Assembly: {}".format(self.componentName)
        self.surfaceCard = mcnpCF.getRHPRotated(self.flat2flat, self.height, self.position, self.surfaceNum, surfaceComment)
        self.cellCard = mcnpCF.getSingleCell(self.cellNum, self.materialNum, self.material.atomDensity,
                                             self.surfaceNum, self.universe, cellComment)

    def getMaterialCard(self, materialName):
        self.materialCard = mcnpCF.getMaterialCard(self.material, self.materialXCLibrary, self.materialNum)
