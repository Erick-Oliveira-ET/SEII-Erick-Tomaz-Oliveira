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
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # image widget
        self.window.add_widget(Image(source="logo.png"))

        self.greeting = Label(text="What's your name?",
                              font_size=18, color="#00FFCE", bold="True")

        # label widget
        self.window.add_widget(self.greeting)

        self.userName = TextInput(
            multiline=False, padding_y=(20, 20), size_hint=(1, 0.5))

        # text input widget
        self.window.add_widget(self.userName)

        self.button = Button(text="GREET", size_hint=(
            1, 0.5), bold=True, background_color="#00FFCE")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        self.greeting.text = "Hello " + self.userName.text + "!"


# run Say Hello App Calss
if __name__ == "__main__":
    SayHello().run()
