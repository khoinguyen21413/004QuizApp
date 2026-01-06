# views/quiz_screen.py

from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle

from .widgets import (
    make_primary_button,
    make_answer_button,
    make_card_layout,
    BACKGROUND_COLOR,
    ANSWER_DEFAULT_BG,
    CORRECT_COLOR,
    WRONG_COLOR,
)


class QuizScreen(Screen):
    """Màn hình làm bài quiz."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.selected = False
        self._next_auto_event = None

        # Nền tối toàn màn hình
        with self.canvas.before:
            Color(*BACKGROUND_COLOR)
            self._bg_rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        outer = BoxLayout(orientation="vertical", padding=dp(18))
        root = make_card_layout("vertical")

        # Thanh trên: số câu + điểm
        self.top_info = Label(
            text="Câu 1/5                 Điểm: 0",
            font_size="16sp",
            size_hint_y=None,
            height=dp(28),
        )
        root.add_widget(self.top_info)

        # Câu hỏi
        self.question_label = Label(
            text="Câu hỏi sẽ hiện ở đây",
            font_size="20sp",
            halign="left",
            valign="middle",
            text_size=(dp(520), None),
        )
        root.add_widget(self.question_label)
        # cho cảm giác mobile: text tự wrap theo chiều ngang widget
        self.question_label.bind(size=self._update_question_text_size)

        # Lưới đáp án
        self.answers_grid = GridLayout(cols=1, spacing=dp(10), size_hint_y=None)
        self.answers_grid.bind(minimum_height=self.answers_grid.setter("height"))

        self.answer_buttons = []
        for i, prefix in enumerate(["A", "B", "C", "D"]):
            btn = make_answer_button(prefix)
            btn.bind(on_press=self.make_answer_handler(i))
            self.answer_buttons.append(btn)
            self.answers_grid.add_widget(btn)

        root.add_widget(self.answers_grid)

        # Feedback
        self.feedback_label = Label(
            text="",
            font_size="16sp",
            size_hint_y=None,
            height=dp(34),
        )
        root.add_widget(self.feedback_label)

        # Hàng nút "Câu tiếp"
        btn_row = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(64),
            spacing=dp(10),
        )
        btn_row.add_widget(Label())  # spacer
        self.next_btn = make_primary_button("CÂU TIẾP", self.on_next_pressed)
        self.next_btn.disabled = True
        btn_row.add_widget(self.next_btn)
        btn_row.add_widget(Label())  # spacer
        root.add_widget(btn_row)

        outer.add_widget(root)
        self.add_widget(outer)

    def on_pre_leave(self, *args):
        # Huỷ schedule auto-next nếu còn
        if self._next_auto_event:
            self._next_auto_event.cancel()
            self._next_auto_event = None
        return super().on_pre_leave(*args)

    def make_answer_handler(self, choice_index: int):
        def handler(_btn):
            if self.selected:
                return
            self.selected = True
            self.next_btn.disabled = False
            self.disable_answers(True)

            app = App.get_running_app()
            is_correct = app.check_answer(choice_index)

            self.feedback_label.text = "✅ Đúng rồi!" if is_correct else "❌ Sai rồi!"
            # Tô màu nút vừa chọn
            if is_correct:
                _btn.background_color = CORRECT_COLOR
            else:
                _btn.background_color = WRONG_COLOR
            # Tự chuyển sang câu tiếp theo sau 1s
            self._next_auto_event = Clock.schedule_once(
                lambda *_: self.on_next_pressed(), 1.0
            )

        return handler

    def disable_answers(self, disabled: bool):
        for b in self.answer_buttons:
            b.disabled = disabled

    def show_question(self, question_data: dict, q_index: int, total: int, score: int):
        # Reset trạng thái mỗi câu
        self.selected = False
        self.feedback_label.text = ""
        self.next_btn.disabled = True
        self.disable_answers(False)

        # Cập nhật label
        self.top_info.text = f"Câu {q_index}/{total}                 Điểm: {score}"
        self.question_label.text = f"Câu hỏi:\n\"{question_data['question']}\""

        # Cập nhật đáp án
        choices = question_data["choices"]
        for i, btn in enumerate(self.answer_buttons):
            prefix = ["A", "B", "C", "D"][i]
            btn.text = f"[{prefix}] {choices[i]}"
            btn.background_color = ANSWER_DEFAULT_BG

    def on_next_pressed(self, *_):
        if self._next_auto_event:
            self._next_auto_event.cancel()
            self._next_auto_event = None

        app = App.get_running_app()
        app.next_question()

    def _update_question_text_size(self, instance, _value):
        # đảm bảo câu hỏi tự xuống dòng theo bề ngang màn hình
        instance.text_size = (instance.width, None)

    def _update_bg(self, *_):
        self._bg_rect.size = self.size
        self._bg_rect.pos = self.pos
