# views/result_screen.py

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle

from .widgets import (
    make_title,
    make_primary_button,
    make_card_layout,
    BACKGROUND_COLOR,
)


class ResultScreen(Screen):
    """Màn hình hiển thị kết quả cuối cùng."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Nền tối toàn màn
        with self.canvas.before:
            Color(*BACKGROUND_COLOR)
            self._bg_rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        outer = BoxLayout(orientation="vertical", padding=dp(18))
        root = make_card_layout("vertical")

        root.add_widget(make_title("KẾT QUẢ"))

        self.score_label = Label(
            text="Bạn đúng: 0/0",
            font_size="20sp",
            size_hint_y=None,
            height=dp(42),
        )
        root.add_widget(self.score_label)

        self.level_label = Label(
            text="Xếp loại: -",
            font_size="18sp",
            size_hint_y=None,
            height=dp(36),
        )
        root.add_widget(self.level_label)

        root.add_widget(Label())  # spacer

        btn_row = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(64),
            spacing=dp(12),
        )
        btn_row.add_widget(Label())

        again_btn = make_primary_button("CHƠI LẠI", self.on_play_again)
        exit_btn = make_primary_button("THOÁT", self.on_exit)

        btn_row.add_widget(again_btn)
        btn_row.add_widget(exit_btn)

        btn_row.add_widget(Label())
        root.add_widget(btn_row)

        outer.add_widget(root)
        self.add_widget(outer)

    def show_result(self, score: int, total: int):
        self.score_label.text = f"Bạn đúng: {score}/{total}"

        # Đánh giá đơn giản
        if total == 0:
            level = "-"
        else:
            if score <= 2:
                level = "CẦN CỐ GẮNG"
            elif score <= total - 1:
                level = "TỐT"
            else:
                level = "XUẤT SẮC"

        self.level_label.text = f"Xếp loại: {level}"

    def on_play_again(self, *_):
        app = App.get_running_app()
        app.restart_quiz()

    def on_exit(self, *_):
        App.get_running_app().stop()

    def _update_bg(self, *_):
        self._bg_rect.size = self.size
        self._bg_rect.pos = self.pos
