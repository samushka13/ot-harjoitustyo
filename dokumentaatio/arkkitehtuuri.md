# Arkkitehtuurikuvaus

## Rakenne

Sovelluksen arkkitehtuuri on kolmitasoinen:

![Arkkitehtuurikuvaus](arkkitehtuurikuvaus.png)

- Pakkaus "ui" tarkoittaa käyttöliittymästä vastaavaa koodia.
- Pakkaus "services" tarkoittaa sovelluslogiikasta vastaavaa koodia.
- Pakkaus "repository" tarkoittaa tietojen tallennuksesta vastaavaa koodia.

Lisäksi: pakkaus "entities" kuvastaa sovelluksen käyttämien tietokohteiden luokkia.

## Käyttöliittymä

Käyttöliittymä on eristetty sovelluslogiikasta ja kutsuu tarvittaessa eri services-luokkia ja niiden metodeja. Käyttöliittymä koostuu neljästä erillisestä päänäkymästä:

- "Login or Create Username",
- "Game Settings",
- "Custom Content",
- "Game Session".

Lisäksi

- "Custom Content" sisältää erillisen "Edit"-alanäkymän,
- "Game Settings" ja "Game Session" sisältävät erillisen "Rules"-alanäkymän,
- "Game Session" sisältää erillisen "Statistics"-alanäkymän.

Kaikki pää- ja alanäkymät on toteutettu omina luokkinaan. Pääsääntöisesti vain yksi näistä näkyy käyttäjälle kerrallaan, poikkeuksena "Rules"- ja "Statistics"-alanäkymät.
