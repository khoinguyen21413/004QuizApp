from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton


class QuizApp(App):
    def __init__(self, **kwargs):
        super(QuizApp, self).__init__(**kwargs)


def main():
    QuizApp().run()


if __name__ == "__main__":
    main()
