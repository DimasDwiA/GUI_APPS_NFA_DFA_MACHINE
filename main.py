from kivymd.tools.hotreload.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase

from screens.screens import *

class WindowManager(ScreenManager):
    pass

class DFA_NFA(MDApp):
    CLASSES = {
        'Welcome' : 'screens.welcome'
    }
    AUTORELOADER_PATHS= [
        ('.', {'recursive' : True})
    ]
    KV_FILES = [
        'kv\welcome.kv'
    ]
    def build(self):
        self.wm = WindowManager()
        screens = [
            Home(name="home"),
            Menu(name="menu"),
            Dfa(name="dfa"),
            Nfa(name="nfa"),
            DesimalNfa(name="desimal_nfa"),
            BinerNfa(name="biner_nfa"),
            DesimalDfa(name="desimal_dfa"),
            BinerDfa(name="biner_dfa"),
            Cal_Des_Dfa(name="cal_des_dfa"),
            Cal_Bin_Dfa(name="cal_bin_dfa"),
            Cal_Des_Nfa(name="cal_des_nfa"),
            Cal_Bin_Nfa(name="cal_bin_nfa"),
            About(name="about"),
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm

if __name__ == '__main__':
    LabelBase.register(name="timesnewroman", fn_regular="assets/Things/timesnewroman.ttf")
    LabelBase.register(name="timesnewroman_bold", fn_regular="assets/Things/timesnewroman_bold.ttf")
    LabelBase.register(name="Poppins-SemiBold", fn_regular="assets/Things/Poppins-SemiBold.ttf")
    LabelBase.register(name="Poppins-Bold", fn_regular="assets/Things/Poppins-Bold.ttf")
    DFA_NFA().run()
