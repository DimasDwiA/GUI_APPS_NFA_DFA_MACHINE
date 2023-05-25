from kivymd.uix.screen import MDScreen  
from kivy.lang import Builder
from kivy.properties import NumericProperty,StringProperty

class About(MDScreen):
    label_text = StringProperty()
    def __init__(self, **kw):
        Builder.load_file("kv/about.kv")
        super().__init__(**kw)