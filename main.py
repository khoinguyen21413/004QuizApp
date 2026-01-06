"""main.py

Điểm khởi chạy ứng dụng Kivy, nối các phần Model - View - Controller
đã được tách ra các module riêng.
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.core.window import Window

from models.quiz_model import QuizModel
from views.start_screen import StartScreen
from views.quiz_screen import QuizScreen
from views.result_screen import ResultScreen
from controllers.quiz_controllers import QuizController


class QuizApp(App):
    """Lớp App chủ yếu dùng để khởi tạo ScreenManager
    và giữ tham chiếu tới Controller.
    """

    def build(self):
        self.title = "Quiz App (Kivy)"

        # ScreenManager (quản lý các màn hình - View)
        self.sm = ScreenManager(transition=FadeTransition(duration=0.15))

        self.start_screen = StartScreen(name="start")
        self.quiz_screen = QuizScreen(name="quiz")
        self.result_screen = ResultScreen(name="result")

        self.sm.add_widget(self.start_screen)
        self.sm.add_widget(self.quiz_screen)
        self.sm.add_widget(self.result_screen)

        # Model + Controller
        self.model = QuizModel(total_questions=5)
        self.controller = QuizController(
            model=self.model,
            screen_manager=self.sm,
            quiz_screen=self.quiz_screen,
            result_screen=self.result_screen,
        )

        self.sm.current = "start"
        return self.sm

    # ----- Các hàm wrapper để View gọi thông qua App -----
    def start_quiz(self):
        self.controller.start_quiz()

    def restart_quiz(self):
        self.controller.restart_quiz()

    def check_answer(self, choice_index: int) -> bool:
        return self.controller.check_answer(choice_index)

    def next_question(self):
        self.controller.next_question()


if __name__ == "__main__":
    # Khi chạy trên desktop, đặt kích thước cửa sổ giống tỉ lệ mobile (dọc)
    try:
        Window.size = (800, 800)
    except Exception:
        pass

    QuizApp().run()
