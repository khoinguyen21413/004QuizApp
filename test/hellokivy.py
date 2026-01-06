from views import widgets
from kivy.app import App


class AppTitle(App):
    def __init__(self, **kwargs):
        super(AppTitle, self).__init__(**kwargs)

    def build(self):
        widgets.make_title("Hello")


def main():
    AppTitle().run()


if __name__ == "__main__":
    main()
