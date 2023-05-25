from kivymd.uix.screen import MDScreen
from kivy.lang import Builder 
from kivy.properties import NumericProperty,StringProperty
from visual_automata.fa.nfa import VisualNFA

class Cal_Des_Nfa(MDScreen):
    label_text = StringProperty()
    def __init__(self, **kw):
        Builder.load_file("kv/cal_des_nfa.kv")
        super().__init__(**kw)
        self.input = "Biner"
        self.label_text = str(self.input)
    def coba(self,text,*args):
        self.input = text
        self.label_text = str(self.input)
        print('Teks yang dikirim:', text)
    def decimal_to_binary(self,*args):
        decimal = int(self.ids.input_des_nfa.text)
        binary = bin(decimal)[2:]  # Mengkonversi desimal ke biner
        #self.ids.id_binary.text = binary
        self.label_text = binary
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