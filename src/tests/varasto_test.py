import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(0, -1)
        self.varasto3 = Varasto(1, 2)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto2.saldo, 0)
        self.assertAlmostEqual(self.varasto3.saldo, 1)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto3.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 8)
        self.assertAlmostEqual(self.varasto3.saldo, 1)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto2.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)
        saatu_maara2 = self.varasto2.ota_varastosta(2)
        saatu_maara3 = self.varasto3.ota_varastosta(-1)

        self.assertAlmostEqual(saatu_maara, 2)
        self.assertAlmostEqual(saatu_maara2, 0)
        self.assertAlmostEqual(saatu_maara3, 0)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_str_tuloste(self):
        tuloste = self.varasto3.__str__()

        assert tuloste == f"saldo = 1, vielä tilaa 1"

    # def test_saldoa_enempaa_ei_voi_ottaa(self):
    #     pass

    # def test_tilavuutta_enempaa_ei_voi_lista(self):
    #     pass
