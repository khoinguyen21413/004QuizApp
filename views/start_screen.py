from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from .widgets import make_title, make_subtitle, make_primary_button


class StartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=15)
        layout.add_widget(Label())  # spacer trên
        layout.add_widget(make_title("Quiz App"))
        layout.add_widget(make_subtitle("Phiên bản 1.0"))
        layout.add_widget(make_subtitle("Chọn đáp đúng cho mỗi câu hỏi"))
        layout.add_widget(Label)  # spacer giữa

        layout.add_widget(make_primary_button("BẮT ĐẦU", self.on_start_pressed))

        layout.add_widget(Label())
        self.add_widget(layout)  # spacer dưới

    def on_start_pressed(btn):
        app = App.get_running_app
        app.start_quiz()
