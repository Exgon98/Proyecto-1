from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import Label
from kivy.core.text.text_layout import layout_text

from kivy.config import Config
Config.set('graphics', 'width', 1250)
Config.set('graphics', 'height', 700)
Config.set('graphics', 'resizable', 0)

Builder.load_file('Interfaz.kv')

class MyScreenManager(ScreenManager):
    def __init__(self):
        super(MyScreenManager, self).__init__()
     

class VentanaMenu(Screen):
    pass

class VentanaEmpezar(Screen):
	pass

class VentanaOpciones(Screen):
    pass

class VentanaAyuda(Screen):
    pass


class VentanaConection(Screen):
	pass

class myApp(App):
    def build(self):
        return MyScreenManager()

    def on_pause(self):
        return True

    def on_resume(self):
        pass

if __name__ in ('__main__', '__android__'):
    myApp().run()