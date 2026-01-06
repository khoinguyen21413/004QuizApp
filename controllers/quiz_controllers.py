class QuizController:
    def __init__(self, model, screen_manager, quiz_screen, result_screen):
        self.model = model
        self.sm = screen_manager
        self.quiz_screen = quiz_screen
        self.result_screen = result_screen

    def start_quiz(self):
        self.model.reset()
        self.sm.current = "quiz"
        self._show_current_question()

    def check_answer(self, choice_index):
        return self.model.check_answer(choice_index)

    def next_question(self):
        self.model.next_question()
        self._show_current_question()

    def _show_current_question(self):
        question = self.model.get_current_question()
        if question is None:  # Hết câu hỏi
            score, total = self.model.get_summary()
            self.result_screen.show_result(score, total)
            self.sm.current = "result"
        else:  # Còn câu
            q_index = self.model.current_index + 1
            total = len(self.model.get_active_questions())
            score = self.model.score
            self.quiz_screen.show_question(question, q_index, total, score)

    def restart_quiz(self):
        self.start_quiz()
