__author__ = "reza0310"

from kivy.clock import Clock

from random import randint

from connexions import echanger, recevoir
from structures import Struct
import framework
import globals


class Coeur:

    def initialiser(self):
        pass
        self.event = Clock.schedule_interval(self.actualiser, 1/globals.FPS)  # 60 fps

    def actualiser(self, dt):
        pass
