from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

PRIMARY_COLOR = (0.2, 0.6, 1, 1)  # màu xanh dương
BACKGROUND_COLOR = (0.95, 0.95, 0.95, 1)  # màu xám nhạt

# Xanh dương chính cho nút
PRIMARY_COLOR = (0.18, 0.55, 0.93, 1)
PRIMARY_DARK = (0.09, 0.36, 0.66, 1)

# Cam nổi bật (dự phòng dùng làm accent)
ACCENT_COLOR = (0.99, 0.77, 0.35, 1)

# Nền tối hiện đại
BACKGROUND_COLOR = (0.05, 0.09, 0.16, 1)

# Thẻ nội dung tối hơn một chút
CARD_COLOR = (0.13, 0.17, 0.26, 1)

# Chữ trắng / xám sáng trên nền tối
TEXT_PRIMARY = (1, 1, 1, 1)
TEXT_SECONDARY = (0.82, 0.86, 0.94, 1)

# Nút đáp án mặc định cùng tông với thẻ
ANSWER_DEFAULT_BG = CARD_COLOR

# Màu cho đáp án đúng/sai (theo palette ban đầu)
CORRECT_COLOR = (0.23, 0.70, 0.44, 1)
WRONG_COLOR = (0.86, 0.30, 0.30, 1)


def make_card_layout(orientation: str = "vertical") -> BoxLayout:
    """Tạo một BoxLayout dạng "card" với nền tối nhẹ.

    Dùng để chứa nội dung chính của mỗi màn hình.
    """

    layout = BoxLayout(orientation=orientation, padding=dp(18), spacing=dp(12))

    with layout.canvas.before:
        Color(*CARD_COLOR)
        rect = Rectangle(size=layout.size, pos=layout.pos)

    def _update_rect(instance, _value):
        rect.size = instance.size
        rect.pos = instance.pos

    layout.bind(size=_update_rect, pos=_update_rect)
    return layout


def make_title(text):
    return Label(
        text=text, font_size="28sp", bold=True, size_hint_y=None, height=dp(50)
    )


def make_subtitle(text):
    return Label(
        text=text, font_size="24sp", bold=True, size_hint_y=None, height=dp(50)
    )


def make_primary_button(text, on_press):
    btn = Button(
        text=text, size_hint=(0.6, None), height=dp(50), background_color=PRIMARY_COLOR
    )
    btn.bind(on_press=on_press)
    return btn


def make_answer_button(prefix: str) -> Button:
    return Button(
        text=f"[{prefix}]",
        font_size="18sp",
        size_hint=(1, None),
        height=dp(56),
        background_normal="",
        background_color=ANSWER_DEFAULT_BG,
        color=TEXT_PRIMARY,
    )
