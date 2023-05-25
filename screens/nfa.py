from kivymd.uix.screen import MDScreen
from kivy.lang import Builder 
from kivy.properties import NumericProperty,StringProperty

class Nfa(MDScreen):
    label_text = StringProperty()
    def __init__(self, **kw):
        Builder.load_file("kv/nfa.kv")
        super().__init__(**kw)