from kivymd.uix.screen import MDScreen
from kivy.lang import Builder 
from kivy.properties import NumericProperty,StringProperty
from visual_automata.fa.nfa import VisualNFA

class Cal_Bin_Nfa(MDScreen):
    label_text = StringProperty()
    def __init__(self, **kw):
        Builder.load_file("kv/cal_bin_nfa.kv")
        super().__init__(**kw)
    def run_dfa(self):
        dfa = VisualNFA(
        states={"q0", "q1", "q2", "q3", "q4"},
        input_symbols={"0", "1"},
        transitions={
            'q0': {'0': {'q0'}, '1': {'q0', 'q1'}},
            'q1': {'0': {'q2'}, '1': {'q0'}},
            'q2': {'0': {'q3', 'q4'}, '1': {}},
            'q3': {'0': {'q3', 'q4'}, '1': {'q3'}},
            'q4': {'0': {}, '1': {}},
        },
        initial_state="q0",
        final_states={"q4"},
        )
        hasil = self.ids.fix_bin.text
        result = dfa.input_check(hasil)
        self.ids.output_label.text = str(result)