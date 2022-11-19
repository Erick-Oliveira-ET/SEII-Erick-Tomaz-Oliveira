# importing widgets
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# The App class dictates the window name


class SayHello(App):
    def build(self):
        # returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1

        # image widget
        self.window.add_widget(Image(source="logo.png"))

        return self.window


# run Say Hello App Calss
if __name__ == "__main__":
    SayHello().run()
