# ----------------------------------------------
# Player settings:
# ----------------------------------------------

DEFAULT_PLAYERS = [
    "Player 1",
    "Player 2",
    "Player 3",
    "Player 4",
    "Player 5",
    "Player 6",
]
PLAYER_COLORS = [
    "red",
    "brown",
    "green",
    "purple",
    "orange",
    "blue",
]

# ----------------------------------------------
# Board settings:
# ----------------------------------------------

BOARD_SIZES = [
    ("Tiny (least difficult)", 1),
    ("Small", 3),
    ("Medium", 5),
    ("Large", 7),
    ("Insane (most difficult)", 9),
]

CATEGORY_COLORS = [
    "black",
    "red",
    "gold",
    "green",
    "purple",
    "orange",
    "blue",
    "grey",
    "brown",
    "pink",
    "magenta",
    "turquoise",
]

# ----------------------------------------------
# Difficulty settings:
# ----------------------------------------------

DIFFICULTY_NAMES = [
    "Easy",
    "Intermediate",
    "Advanced Triviliast"
]

# ----------------------------------------------
# Game rules:
# ----------------------------------------------

GAME_RULES_TITLE = "Trivioboros"
GAME_RULES_TEXT = """ Yleistä:

- Pelaajat aloittavat mustasta ruudusta ('aloitusruutu').
- Pelin aloittaa Pelaaja 1, ja vuorot vaihtuvat järjestyksessä.
- Jokaista peliin valittua kategoriaa edustaa yksi kategoriapiste.
- Pistetilannetta voi seurata pelilaudan vasemmasta ylälaidasta löytyvän pistetaulukon avulla.


Pelin kulku:

1. Vuorossa oleva pelaaja heittää noppaa.
2. Pelaaja siirtyy laudalla myötäpäivään nopan osoittaman silmäluvun verran.
3. Pelaajalle esitetään kysymys kategoriasta, jonka edustamaan ruutuun tämä on siirryttyään päätynyt.
    - Mikäli pelaaja vastaa oikein, hän saa pisteen kyseisestä kategoriasta.
    - Mikäli pelaajalla on jo kategoriasta piste, tämä ei saa uutta pistettä.
    - Mikäli pelaaja vastaa väärin, hän menettää kategoriapisteen.
    - Mikäli pelaajalla ei ole kategoriassa pistettä, tämä ei menetä mitään.
4. Vuoro vaihtuu.


Pelin päättyminen:

- Pelin voittaa se, joka ensimmäisenä pääsee aloitusruutuun tai sen yli kaikkien kategoriapisteiden kanssa.
- Mikäli samalla kierroksella useampi pelaaja onnistuu tässä, voitto jaetaan.


Vaikeustaso:

- Pelin vaikeustasoon voi vaikuttaa monella tapaa, ja yhdistelmiä on useita. 
- Pääsääntöisesti vaikeustaso kasvaa pelilaudan kokoa tai kysymyskategorioiden määrää kasvattamalla.
- Erilaisia yhdistelmiä kannattaa rohkeasti kokeilla! """
