# import dữ liệu
from models.quiz_data import QUIZ_QUESTIONS


class QuizModel:
    def __init__(self, total_questions=5):
        # Chua toan bo thong tin cau hoi
        self.all_question = QUIZ_QUESTIONS[:]
        # Tong so cau hoi
        self.total_question = min(total_questions, len(self.all_question))
        # Index cau hoi hien tai
        self.current_index = 0
        # So diem
        self.score = 0

    # reset dữ liệu
    def reset(self):
        self.current_index = 0
        self.score = 0

    # Lấy n câu đầu
    def get_active_questions(self):
        return self.all_question[: self.total_question]

    # lấy câu hiện tại
    def get_current_question(self):
        if self.current_index >= len(self.get_active_questions()):
            return None
        return self.get_active_questions()[self.current_index]

    # kiểm tra dap an và tính điểm
    def check_answer(self, choice_index):
        question = self.get_current_question()
        if question is None:
            return False
        correct = choice_index == question["answer_index"]
        if correct:
            self.score += 1
            return correct
        return False

    # chuyển câu tiếp
    def next_question(self):
        self.current_index += 1

    def get_summary(self):
        """Trả về (score, total).

        score: số câu đúng
        total: tổng số câu trong bài
        """
        total = len(self.get_active_questions())
        return self.score, total


# Test don gian
if __name__ == "__main__":
    model = QuizModel()
    print(model.get_current_question())

    print(model.get_active_questions())

    # Test kiem tra dap an
    print("Check cau dung: ", model.check_answer(0))
    print("Check cau sai: ", model.check_answer(1))

    # Kiem tra next QA
    print("current_index: ", model.current_index)
    model.next_question()
    print("current_index: ", model.current_index)
    model.reset()
    print("current_index: ", model.current_index)
