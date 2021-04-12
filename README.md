# Ohjelmistotekniikka, harjoitustyö

## Trivioboros (Python)

Sovellus on Trivial Pursuitin kaltainen tietopeli, jonka pelisessiot ovat kustomoitavissa (kuvaus tarkentuu myöhemmin). Käyttäjät voivat lisäksi luoda omia kysymyksiä ja kategorioita. Sovelluksen kieli on englanti.

Sovelluksen toiminta on testattu Python-versiolla 3.9.2., mutta sen tulisi toimia myös versiolla 3.6. Yhteensopivuutta tätä vanhempien Python-versioiden kanssa ei voida taata.

### Dokumentaatio

[Vaatimusmäärittely](https://github.com/samushka13/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/samushka13/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

### Asennus

1. Varmista, että koneellasi on asianmukainen Python-versio (^3.9. suositeltu, mutta ^3.6 riittää).

2. Varmista, että koneellasi on asianmukainen Poetry-versio (^1.1.5).

3. Asenna projektin riippuvuudet komennolla:

       poetry install

4. Käynnistä projekti komennolla:

       poetry run invoke start

### Testaus

1. Testit voi suorittaa komennolla: 

       poetry run invoke test

2. Testikattavuusraportin voi luoda komennolla:

       poetry run invoke coverage-report

3. Tai vaihtoehtoisesti HTML-muodossa komennolla:

       poetry run invoke coverage-report-html

4. Laatuvaatimukset voi tarkistaa komennolla:

       poetry run invoke lint
