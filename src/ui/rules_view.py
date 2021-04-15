import tkinter as tk
from tkinter import DISABLED
from ui.stylings import (
    get_window_settings,
    RULES_WINDOW_NAME,
    RULES_WINDOW_SIZE,
    TITLE_FONT,
    TEXT_FONT,
)
from ui.widgets import (
    get_display_textbox,
    get_basic_button,
)

class RulesView:
    """Class that describes the UI of the rules view."""

    def __init__(self):
        """Class constructor that initializes the window
        with appropriate settings and widgets."""

        self.rules_window = tk.Tk()
        get_window_settings(self.rules_window, RULES_WINDOW_NAME, RULES_WINDOW_SIZE)
        self._build_widgets()
        self.rules_window.mainloop()

    def _build_widgets(self):
        """Build the widgets of the parent window."""

        title = get_display_textbox(self.rules_window, 1, 85, TITLE_FONT)
        title.place(x=30, y=30)
        title.insert(tk.END, "Trivioboros")
        title.config(state=DISABLED)

        rules = get_display_textbox(self.rules_window, 40, 85, TEXT_FONT)
        rules.place(x=30, y=80)
        rules.insert(tk.END, self.get_game_rules_text())
        rules.config(state=DISABLED)

        get_basic_button(
            self.rules_window,
            "Got it!",
            command=self._close_window,
        ).place(x=370, y=620, anchor="center")


    def get_game_rules_text(self):
        """Provides the text content for the game rules view.

        Returns:
            The text as a multiline string value.
        """

        return """Yleistä:

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

    - Pelin voittaa se, joka ensimmäisenä pääsee aloitusruutuun tai sen yli kaikkien kategoriapisteiden kera.
    - Mikäli samalla kierroksella useampi pelaaja onnistuu tässä, voitto jaetaan.


    Vaikeustaso:

    - Pelin vaikeustasoon voi vaikuttaa monella tapaa, ja yhdistelmiä on useita. 
    - Pääsääntöisesti vaikeustaso kasvaa pelilaudan kokoa tai kysymyskategorioiden määrää kasvattamalla.
    - Erilaisia yhdistelmiä kannattaa rohkeasti kokeilla!
    """

    def _close_window(self):
        """Destroys the current window."""

        self.rules_window.destroy()
