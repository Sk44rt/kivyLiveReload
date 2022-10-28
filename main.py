from kivy.app import App
from kivy.lang import Builder

# .kv of main_window
main_window = Builder.load_string("""
#:import KivyLexer kivy.extras.highlight.KivyLexer

BoxLayout:
    orientation: "horizontal"
    CodeInput:
        id: kv_code
        style_name: "native"
        lexer: KivyLexer()
        on_text: app.update(text=self.text)
    BoxLayout:
        id: view_space
        size_hint_x: 0.6
""")

# kivy app class
class app(App):
    def update(self, text):
        if len(text) == 0: # .kv is empty
            return
        try: # .kv is correct
            self.widget = Builder.load_string(text)
        except: # else don't load
            pass

        # load correct .kv
        main_window.ids.view_space.clear_widgets()
        main_window.ids.view_space.add_widget(self.widget)

        # save correct .kv
        with open("correct.kv", "w") as file:
            file.write(text)
            file.close()

    # kivy main function
    def build(self):
        self.widget = Builder.load_string("BoxLayout:")

        return main_window

# kivy run
app().run()
