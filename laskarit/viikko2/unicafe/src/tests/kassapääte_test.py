import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate(100000, 0, 0)
        self.maksukortti = Maksukortti(10000)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_konstruktori_asettaa_rahat_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_konstruktori_asettaa_lounaat_oikein(self):
        self.lounaat = 0
        self.assertEqual(self.lounaat, 0)

    def test_onnistunut_kateismaksu_edullisesta_ateriasta_kasvattaa_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_onnistunut_kateismaksu_edullisesta_ateriasta_antaa_oikean_vaihtorahan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

    def test_onnistunut_kateismaksu_edullisesta_ateriasta_kasvattaa_myytyjen_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_riittämätön_kateismaksu_edullisesta_ateriasta_ei_muuta_mitään(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_onnistunut_kateismaksu_maukkaasta_ateriasta_kasvattaa_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_onnistunut_kateismaksu_maukkaasta_ateriasta_antaa_oikean_vaihtorahan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_onnistunut_kateismaksu_maukkaasta_ateriasta_kasvattaa_myytyjen_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_riittämätön_kateismaksu_maukkaasta_ateriasta_ei_muuta_mitään(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    def test_onnistunut_korttimaksu_edullisesta_ateriasta_kasvattaa_myytyjen_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_onnistunut_korttimaksu_edullisesta_ateriasta_palauttaa_truen(self):
        self.assertIs(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_epäonnistunut_korttimaksu_edullisesta_ateriasta_palauttaa_falsen_eika_maarat_muutu(self):
        self.assertIs(self.kassapaate.syo_edullisesti_kortilla(Maksukortti(100)), False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_onnistunut_korttimaksu_maukkaasta_ateriasta_kasvattaa_myytyjen_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_onnistunut_korttimaksu_maukkaasta_ateriasta_palauttaa_truen(self):
        self.assertIs(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_epäonnistunut_korttimaksu_maukkaasta_ateriasta_palauttaa_falsen_eika_maarat_muutu(self):
        self.assertIs(self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(100)), False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_onnistunut_lataus_muuttaa_kortin_saldoa_ja_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(self.maksukortti.saldo, 11000)

    def test_negatiivinen_lataus_ei_muuta_saldoa_ja_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 10000)
