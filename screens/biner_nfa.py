from kivymd.uix.screen import MDScreen 
from kivy.lang import Builder
from kivy.properties import NumericProperty,StringProperty

class BinerNfa(MDScreen):
    label_text = StringProperty()
    def __init__(self, **kw):
        Builder.load_file("kv/biner_nfa.kv")
        super().__init__(**kw)