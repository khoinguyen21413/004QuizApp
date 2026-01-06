# views/start_screen.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle

from .widgets import (
    make_title,
    make_subtitle,
    make_primary_button,
    make_card_layout,
    BACKGROUND_COLOR,
)


class StartScreen(Screen):
    """Màn hình bắt đầu (welcome / hướng dẫn)."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Nền chung tối, hiện đại
        with self.canvas.before:
            Color(*BACKGROUND_COLOR)
            self._bg_rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        outer = BoxLayout(orientation="vertical", padding=dp(18))

        card = make_card_layout("vertical")
        card.add_widget(make_title("QUIZ APP"))
        card.add_widget(
            Label(
                text="(Kivy - Simple Version)",
                font_size="14sp",
                size_hint_y=None,
                height=dp(24),
            )
        )

        instructions = (
            "Hướng dẫn:\n"
            "- Bấm chọn đáp án đúng A/B/C/D\n"
            "- Mỗi câu chỉ chọn 1 lần\n"
            "- Xem điểm sau khi hoàn thành"
        )
        card.add_widget(make_subtitle(instructions))

        btn_row = BoxLayout(orientation="horizontal", size_hint_y=None, height=dp(64))
        btn_row.add_widget(Label())  # spacer
        start_btn = make_primary_button("BẮT ĐẦU", self.on_start_pressed)
        btn_row.add_widget(start_btn)
        btn_row.add_widget(Label())  # spacer
        card.add_widget(btn_row)

        outer.add_widget(card)
        outer.add_widget(Label(size_hint_y=None, height=dp(12)))  # khoảng thở bên dưới
        self.add_widget(outer)

    def _update_bg(self, *_):
        self._bg_rect.size = self.size
        self._bg_rect.pos = self.pos

    def on_start_pressed(self, *_):
        app = App.get_running_app()
        app.start_quiz()
