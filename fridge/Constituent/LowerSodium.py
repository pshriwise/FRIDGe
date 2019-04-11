import FRIDGe.fridge.Constituent.Constituent as Constituent
import FRIDGe.fridge.utilities.mcnpCreatorFunctions as mcnpCF
import copy


class LowerSodium(Constituent.Constituent):
    def __init__(self, unitInfo):
        super().__init__(unitInfo)
        self.getMaterialCard(unitInfo[0][3])
        self.makeComponent(unitInfo[1])

    def makeComponent(self, lowerSodiumInfo):
        outerShell = lowerSodiumInfo[0]
        flatToFlat = lowerSodiumInfo[1]
        surfaceComment = "$Assembly: Lower Sodium"
        cellComment = "$Assembly: Lower Sodium"
        lowerNaPosition = copy.deepcopy(outerShell.positionBottomAssembly)
        lowerNaPosition[2] -= 0.1
        lowerNaHeight = outerShell.excessNaHeight+0.1
        self.surfaceCard = mcnpCF.getRHP(flatToFlat, lowerNaHeight, lowerNaPosition, self.surfaceNum, surfaceComment)
        self.cellCard = mcnpCF.getSingleCell(self.cellNum, self.materialNum, self.material.atomDensity, self.surfaceNum,
                                             self.universe, cellComment)
