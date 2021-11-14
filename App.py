from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.core.text import Label as CoreLabel
from kivy.graphics import Color

__author__ = "reza0310"

layout = []


class HUD:

    def __init__(self):
        self.longueur, self.largeur = Window.size
        self.boutons = []

    def bind(self, emplacement, taille, action, type="Bouton"):
        print("Binding",action,'sur x variant de',(emplacement[0]-(taille[0]//2), emplacement[0]+(taille[0]//2)),'et y',(emplacement[1]-(taille[1]//2), emplacement[1]+(taille[1]//2)))
        self.boutons.append({"type": type, "x": (emplacement[0]-(taille[0]//2), emplacement[0]+(taille[0]//2)), "y": (emplacement[1]-(taille[1]//2), emplacement[1]+(taille[1]//2)), "action": action})

    def unbind(self, unbin="all"):
        if unbin == 'all':
            self.boutons = []
        else:
            for bouton in self.boutons:
                if bouton["action"] == unbin:
                    self.boutons.remove(bouton)

    def press(self, touch):
        for bouton in self.boutons:
            if bouton["x"][0] < touch.spos[0]*1000 < bouton["x"][1] and bouton["y"][0] < touch.spos[1]*1000 < bouton["y"][1]:
                print(bouton["action"])
                eval(bouton["action"])  # Handle joysticks

    def recoordonner(self, tupl):
        return int((tupl[0] / 1000) * self.longueur), int((tupl[1] / 1000) * self.largeur)

    def recoordonner_double(self, tupl):
        return int((tupl[0] / 1000) * self.longueur), int((tupl[1] / 1000) * self.largeur), int((tupl[2] / 1000) * self.longueur), int((tupl[3] / 1000) * self.largeur)

    def texte(self, x, y, texte, remove = True):
        label = CoreLabel(text=str(texte), font_size=20)
        label.refresh()
        text = label.texture
        rec = Rectangle(size=text.size, pos=self.recoordonner((x, y)), texture=text)
        layout.canvas.add(rec)
        if remove:
            def rmv(dt):
                layout.canvas.remove(rec)
            Clock.schedule_once(rmv, 1/30)

    def actualiser(self, dt):
        self.longueur, self.largeur = Window.size


class JEU:

    def initialiser(self):
        self.event = Clock.schedule_interval(self.actualiser, 1/60)  # 60 fps

    def actualiser(self, dt):
        pass


hud = HUD()
jeu = JEU()


class Layout(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_entity(self, entity):
        self.entities.add(entity)
        self.canvas.add(entity.image)

    def remove_entity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)
            self.canvas.remove(entity.image)

    def on_touch_down(self, touch):
        hud.press(touch)


class MYApp(App):
    def build(self):
        global layout
        Window.clearcolor = (1, 1, 1, 1)
        self.title = 'MY'
        layout = Layout()
        jeu.initialiser()
        return layout


MYApp().run()