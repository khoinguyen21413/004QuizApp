from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class StartScreen(App):
    def build(self):
        box = BoxLayout(orientation="vertical")

        tilte_label = Label(text="Quiz App")
        box.add_widget(tilte_label)

        instruct_label = Label(
            text="Hướng dẫn:\n- Chọn đáp án đúng A/B/C/D\n- Xem điểm sau khi hoàn thành"
        )
        box.add_widget(instruct_label)
        return box


def main():
    StartScreen().run()


if __name__ == "__main__":
    main()
