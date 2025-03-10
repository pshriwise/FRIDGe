import fridge.Material.Element
import fridge.Material.Material as materialReader
import numpy as np


def test_element_Unknown():
    e = 1.0
    try:
        e = fridge.Material.Element.Element('Unknown')
    except AssertionError:
        assert e == 1.0


def test_material_ImproperSum():
    pass


def test_element_C():
    e = fridge.Material.Element.Element('C')
    assert e.name == 'Carbon'
    assert e.zaid == 6000
    assert e.isotopes == [6000]
    assert e.molecularMass == [12.0107]
    assert e.abundance == [1]
    assert e.density == 1.8
    assert e.linearCoeffExpansion == 0.0


def test_element_Fe():
    e = fridge.Material.Element.Element('Fe')
    assert e.name == 'Iron'
    assert e.zaid == 26000
    assert e.isotopes == [26054, 26056, 26057, 26058]
    assert e.molecularMass == [53.939608, 55.934935, 56.935392, 57.933273]
    assert e.abundance == [0.05845, 0.91754, 0.02119, 0.00282]
    assert e.density == 7.874
    assert e.linearCoeffExpansion == 0.0


def test_element_Pu():
    e = fridge.Material.Element.Element('Pu')
    assert e.name == 'Plutonium'
    assert e.zaid == 94000
    assert e.isotopes == [94238, 94239, 94240, 94241, 94242]
    assert e.molecularMass == [238.0495582, 239.0521617, 240.0538118, 241.0538497, 242.0587410]
    assert e.abundance == [0.0, 0.0, 0.0, 0.0, 0.0]
    assert e.density == 19.84
    assert e.linearCoeffExpansion == 0.0


def test_material():
    m = materialReader.Material()
    assert m.enrichmentDict == {}
    assert m.weightPercent == {}
    assert m.atomPercent == {}
    assert m.atomDensity == 0.0
    assert m.elementDict == {}
    assert m.name == ''
    assert m.elements == []
    assert m.zaids == []
    assert m.weightFraction == []
    assert m.density == 0.0
    assert m.linearCoeffExpansion == 0.0
    assert m.enrichmentZaids == []
    assert m.enrichmentIsotopes == []
    assert m.enrichmentVector == []


def test_material_liqduiNa():
    m = materialReader.Material()
    m.set_material('LiquidNa')
    assert m.name == 'Liquid Sodium'
    assert m.elements == ['Na']
    assert m.zaids == [11000]
    assert m.weightFraction == [1.0]
    assert m.enrichmentZaids == []
    assert m.enrichmentIsotopes == []
    assert m.enrichmentVector == []
    assert m.density == 0.927
    assert np.allclose(m.atomDensity, 0.0242826)
    assert m.atomPercent == {11023: 1.0}


def test_material_liqduiPbBi():
    m = materialReader.Material()
    m.set_material('LiquidPbBi')
    assert m.name == 'Liquid Lead Bismuth (Eutectic)'
    assert m.elements == ['Pb', 'Bi']
    assert m.zaids == [82000, 83000]
    assert m.weightFraction == [0.445, 0.555]
    assert m.enrichmentZaids == []
    assert m.enrichmentIsotopes == []
    assert m.enrichmentVector == []
    assert m.density == 11.096
    knownAtomPercent = {82204: 0.006259, 82206: 0.107749, 82207: 0.098808, 82208: 0.234277, 83209: 0.552907}
    for k, v in knownAtomPercent.items():
        assert np.allclose(m.atomPercent[k], v, 5)
    assert np.allclose(m.atomDensity, 0.032096, 5)


def test_material_liqduiPb():
    m = materialReader.Material()
    m.set_material('LiquidPb')
    assert m.name == 'Liquid Lead'
    assert m.elements == ['Pb']
    assert m.zaids == [82000]
    assert m.weightFraction == [1.0]
    assert m.enrichmentZaids == []
    assert m.enrichmentIsotopes == []
    assert m.enrichmentVector == []
    assert m.density == 10.678
    knownAtomPercent = {82204: 0.014, 82206: 0.241, 82207: 0.221, 82208: 0.524}
    for k, v in knownAtomPercent.items():
        assert np.allclose(m.atomPercent[k], v, 5)
    assert np.allclose(m.atomDensity, 0.032956, 5)


def test_material_voidLiquidNa():
    m = materialReader.Material()
    m.set_material('LiquidNa')
    m.set_void(0.1)
    assert m.name == 'Liquid Sodium'
    assert m.elements == ['Na']
    assert m.zaids == [11000]
    assert m.weightFraction == [1.0]
    assert m.enrichmentZaids == []
    assert m.enrichmentIsotopes == []
    assert m.enrichmentVector == []
    assert m.density == 0.927
    assert np.allclose(m.atomDensity, 0.00242826)
    assert m.atomPercent == {11023: 1.0}


def test_material_5Pu22U10Zr():
    m = materialReader.Material()
    m.set_material('5Pu22U10Zr')
    assert m.name == '5Pu22U10Zr'
    assert m.elements == ['U', 'Pu', 'Zr']
    assert m.zaids == [92000, 94000, 40000]
    assert m.weightFraction == [0.85, 0.05, 0.1]
    assert m.enrichmentZaids == [92000, 94000]
    assert m.enrichmentIsotopes == [[92234, 92235, 92236, 92238], [94239, 94240]]
    assert m.enrichmentVector == [[0.0, 0.2588, 0.0, 0.7412], [0.94, 0.060]]


def test_material_UO2():
    """
    Test material is from the Compendium of Material Composition Data for Radiation Transport Modeling: Revision 1.
    """
    m = materialReader.Material()
    m.set_material('UO2')
    assert m.name == 'Uranium Dioxide'
    assert m.elements == ['U', 'O']
    assert m.zaids == [92000, 8000]
    assert m.weightFraction == [0.881467, 0.118533]
    assert m.enrichmentZaids == [92000, 8000]
    assert m.enrichmentIsotopes == [[92234, 92235, 92236, 92238], [8016, 8017, 8018]]
    assert m.enrichmentVector == [[0.00026660018529341, 0.029999988655276, 0.0001384056351514, 0.96959500496104],
                                  [1.0, 0.0, 0.0]]
    assert m.density == 10.96
    assert np.allclose(m.atomDensity, 0.07335, 6)
    atomPercentKnown = {92234: 0.000090, 92235: 0.010124, 92236: 0.000046, 92238: 0.323072, 8016: 0.666667}
    for k, v in atomPercentKnown.items():
        assert np.allclose(m.atomPercent[k], v, 6)


def test_material_HT9():
    """
    Test material is from the Compendium of Material Composition Data for Radiation Transport Modeling: Revision 1.
    """
    m = materialReader.Material()
    m.set_material('HT9')
    assert m.name == 'HT9'
    assert m.elements == ['C', 'Si', 'P', 'S', 'V', 'Cr', 'Mn', 'Fe', 'Ni', 'Mo', 'W']
    assert m.zaids == [6000, 14000, 15000, 16000, 23000, 24000, 25000, 26000, 28000, 42000, 74000]
    assert m.weightFraction == [0.0020, 0.0040, 0.0003, 0.0002, 0.0030, 0.1150, 0.0060, 0.8495, 0.0050, 0.0100, 0.0050]
    assert m.enrichmentZaids == []
    assert m.enrichmentIsotopes == []
    assert m.enrichmentVector == []
    assert m.density == 7.874
    assert np.allclose(m.atomDensity, 8.598e-2, 6)
    atomPercentKnown = {6000: 9.183e-3,
                        14028: 7.244e-3, 14029: 3.680e-4, 14030: 2.428e-4,
                        15031: 5.34e-4,
                        16032: 3.268e-4, 16033: 2.58e-6, 16034: 1.462e-5, 16036: 3.44e-8,
                        23050: 8.12e-6, 23051: 3.240e-3,
                        24050: 5.300e-3, 24052: 1.02198e-1, 24053: 1.15885e-2, 24054: 2.885e-3,
                        25055: 0.006023,
                        26054: 4.96533e-2, 26056: 7.7945e-1, 26057: 1.80009e-2, 26058: 2.3956e-3,
                        28058: 3.19826e-3, 28060: 1.23196e-3, 28061: 5.35572e-5, 28062: 1.70772e-4, 28064: 4.34565e-5,
                        42092: 8.35184e-4, 42094: 5.25942e-4, 42095: 9.10483e-4, 42096: 9.58192e-4, 42097: 5.51808e-4,
                        42098: 1.40194e-3, 42100: 5.64454e-4,
                        74180: 1.8e-6, 74182: 3.975e-4, 74183: 2.1465e-4, 74184: 4.596e-4, 74186: 4.2645e-4}
    for k, v in atomPercentKnown.items():
        assert np.allclose(m.atomPercent[k], v, 5)


def test_material_SS316():
    """
    Test material is from the Compendium of Material Composition Data for Radiation Transport Modeling: Revision 1.
    """
    m = materialReader.Material()
    m.set_material('SS316')
    assert m.name == 'Stainless Steel 316'
    assert m.elements == ['C', 'Si', 'P', 'S', 'Cr', 'Mn', 'Fe', 'Ni', 'Mo']
    assert m.zaids == [6000, 14000, 15000, 16000, 24000, 25000, 26000, 28000, 42000]
    assert m.weightFraction == [0.00041, 0.00507, 0.00023, 0.00015, 0.17, 0.01014, 0.669, 0.12, 0.025]
    assert m.enrichmentZaids == []
    assert m.enrichmentIsotopes == []
    assert m.enrichmentVector == []
    assert m.density == 8.0
    assert np.allclose(m.atomDensity, 8.655e-2, 5)
    atomPercentKnown = {6000: 1.900e-3,
                        14028: 9.231e-3, 14029: 4.857e-4, 14030: 3.316e-4,
                        15031: 4.133e-4,
                        16032: 2.466e-4, 16033: 2.008e-6, 16034: 1.172e-5, 16036: 2.921e-8,
                        24050: 7.596e-3, 24052: 1.523e-1, 24053: 1.760e-2, 24054: 4.465e-3,
                        25055: 1.027e-2,
                        26054: 3.765e-2, 26056: 6.128e-1, 26057: 1.441e-2, 26058: 1.951e-3,
                        28058: 7.647e-2, 28060: 3.047e-2, 28061: 1.347e-3, 28062: 4.365e-3, 28064: 1.147e-3,
                        42092: 2.018e-3, 42094: 1.298e-3, 42095: 2.272e-3, 42096: 2.416e-3, 42097: 1.406e-3,
                        42098: 3.609e-3, 42100: 1.483e-3}
    for k, v in atomPercentKnown.items():
        assert np.allclose(m.atomPercent[k], v, 5)


def test_material_BadWtPer():
    m = materialReader.Material()
    m.set_material('BadMaterial')
    assert m.weightPercent != 1.0


def test_material_NoMaterial():
    m = materialReader.Material()
    try:
        m.set_material('NoMaterial')
    except IndexError:
        m.density = 0.0
