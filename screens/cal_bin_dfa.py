from kivymd.uix.screen import MDScreen
from kivy.lang import Builder 
from kivy.properties import NumericProperty,StringProperty
from visual_automata.fa.dfa import VisualDFA


class Cal_Bin_Dfa(MDScreen):
    label_text = StringProperty()
    def __init__(self, **kw):
        Builder.load_file("kv/cal_bin_dfa.kv")
        super().__init__(**kw)
    def run_dfa(self):
        dfa = VisualDFA(
        states={"q0", "q1", "q2", "q3", "q4"},
        input_symbols={"0", "1"},
        transitions={
            'q0': {'0': 'q1', '1': 'q0'},
            'q1': {'0': 'q2', '1': 'q0'},
            'q2': {'0': 'q3', '1': 'q0'},
            'q3': {'0': 'q4', '1': 'q0'},
            'q4': {'0': 'q4', '1': 'q4'},
        },
        initial_state="q0",
        final_states={"q4"},
        )
        hasil = self.ids.fix_bin.text
        result = dfa.input_check(hasil)
        self.ids.output_label.text = str(result)
    
   