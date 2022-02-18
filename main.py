from kivy.app import App
from kivy.lang import Builder
import os
from sys import platform

kv = Builder.load_string("""
#:import KivyLexer kivy.extras.highlight.KivyLexer

BoxLayout:
    orientation: "horizontal"
    CodeInput:
        style_name: "native"
        lexer: KivyLexer()
        id: kv_code
        on_text: app.update(text=self.text)
    BoxLayout:
        id: view_space
        size_hint_x: 0.6
""")

class app(App):
    def update(self, text):
        try:
            kv.ids.view_space.clear_widgets()
            kv.ids.view_space.add_widget(Builder.load_string(text))
            with open("saved_kv.kv", "w") as file:
                file.write(text)
                file.close()
        except Exception as e:
            if platform == "linux" or platform == "linux2" or platform == "darwin":
                os.system("clear")
            elif platform == "win32":
                os.system("cls")
            print(e)
    def build(self):
        return kv

app().run()
