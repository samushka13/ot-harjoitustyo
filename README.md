# Ohjelmistotekniikka, harjoitustyö

## Trivioboros (Python)

Sovellus on Trivial Pursuitin kaltainen tietopeli, jonka pelisessiot ovat kustomoitavissa (kuvaus tarkentuu myöhemmin). Rekisteröityneet käyttäjät voivat lisäksi luoda omia kysymyksiä ja kategorioita.

Sovelluksen toiminta on testattu Python-versiolla 3.9.2. Yhteensopivuutta vanhempien Python-versioiden kanssa ei siten voida taata.

### Dokumentaatio

[Vaatimusmäärittely](https://github.com/samushka13/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/samushka13/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

### Asennus

1. Varmista, että koneellasi on asianmukainen Python-versio (^3.9).

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

## Tehtävät

### Viikko 1

[gitlog.txt](https://github.com/samushka13/ot-harjoitustyo/blob/master/laskarit/viikko1/gitlog.txt)

[komentorivi.txt](https://github.com/samushka13/ot-harjoitustyo/blob/master/laskarit/viikko1/komentorivi.txt)

### Viikko 2

[Kattavuusraportti](https://github.com/samushka13/ot-harjoitustyo/blob/master/laskarit/viikko2/kattavuusraportti.png)

### Viikko 3

[Tehtävä 1](https://github.com/samushka13/ot-harjoitustyo/blob/master/laskarit/viikko3/1_monopoly_luokkakaavio.png)

[Tehtävä 2](https://github.com/samushka13/ot-harjoitustyo/blob/master/laskarit/viikko3/2_monopoly_luokkakaavio.png)

[Tehtävä 3](https://github.com/samushka13/ot-harjoitustyo/blob/master/laskarit/viikko3/3_sekvenssikaavio.png)

[Tehtävä 4](https://github.com/samushka13/ot-harjoitustyo/blob/master/laskarit/viikko3/4_sekvenssikaavio.png)
