# Ohjelmistotekniikka, harjoitustyö

## Trivioboros

Sovellus on tietopeli, jonka pelisessiot ovat laajasti kustomoitavissa. Käyttäjät voivat lisäksi luoda omia kysymyksiä ja kategorioita. Sovelluksen kieli on englanti.

Sovellus on kehitetty Python-versiolla 3.9.2 ja sen toiminta on testattu Python-versiolla 3.6.9. Yhteensopivuutta tätä vanhempien Python-versioiden kanssa ei voida taata.

Huomioithan, että peli on originaali konsepti, joten mahdollisesta matkimisesta ja sillä rahastamisesta tai konseptin omana ideana esittämisestä saattaa tulla kovastikin kuonoon :)

### Dokumentaatio

[Käyttöohje](https://github.com/samushka13/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/samushka13/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](https://github.com/samushka13/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/samushka13/ot-harjoitustyo/blob/master/dokumentaatio/testausdokumentti.md)

[Työaikakirjanpito](https://github.com/samushka13/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

### Pika-asennus

1. Lataa uusin [release](https://github.com/samushka13/ot-harjoitustyo/releases).

2. Varmista, että koneellasi on asianmukainen Python-versio (^3.6) ja Poetry-versio (^1.1.5 suositeltu).

3. Asenna projektin riippuvuudet komennolla:

       poetry install

4. Käynnistä sovellus komennolla:

       poetry run invoke start

Mikäli asennuksessa ilmenee ongelmia, käänny [käyttöohjeen](https://github.com/samushka13/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) puoleen.

### Testaus

1. Testit voi suorittaa komennolla: 

       poetry run invoke test

2. Testikattavuusraportin voi luoda komennolla:

       poetry run invoke coverage-report

3. Tai vaihtoehtoisesti HTML-muodossa komennolla (tulostuu hakemistoon "htmlcov"):

       poetry run invoke coverage-report-html

4. Laatuvaatimukset voi tarkistaa komennolla:

       poetry run invoke lint
