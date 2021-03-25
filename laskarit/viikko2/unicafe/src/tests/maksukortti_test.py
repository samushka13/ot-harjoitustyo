import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 100.0")

    def test_lataa_rahaa_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(2000)
        self.assertEqual(str(self.maksukortti), "saldo: 120.0")

    def test_ota_rahaa_palauttaa_oikean_saldon_jos_saldoa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5000)
        self.assertEqual(str(self.maksukortti), "saldo: 50.0")

    def test_ota_rahaa_palauttaa_truen_jos_saldoa_on_tarpeeksi(self):
        self.assertIs(self.maksukortti.ota_rahaa(5000), True)

    def test_liika_ottaminen_ei_muuta_saldoa(self):
        self.maksukortti.ota_rahaa(50000)
        self.assertEqual(str(self.maksukortti), "saldo: 100.0")

    def test_ota_rahaa_palauttaa_falsen_jos_saldoa_ei_ole_tarpeeksi(self):
        self.assertIs(self.maksukortti.ota_rahaa(50000), False)
