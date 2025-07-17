import random
import time

class MathGame:
    def __init__(self, course):
        self.course = course
        self.score = 0
        self.max_score = 50  # 最終的なスコアの上限
        self.game_over = False
        self.operation = ''
        self.generate_problem()

    def generate_problem(self):
        """問題を生成"""
        if self.course == 'beginner':
            self.generate_beginner_problem()
        elif self.course == 'intermediate':
            self.generate_intermediate_problem()
        elif self.course == 'advanced':
            self.generate_advanced_problem()

    def generate_beginner_problem(self):
        """初級コース：四則演算をそれぞれのコースで出題"""
        operations = ['+', '-', '*', '/']
        num1 = random.randint(0, 20)
        num2 = random.randint(0, 20)
        self.operation = random.choice(operations)
        self.problem = f"{num1} {self.operation} {num2}"

    def generate_intermediate_problem(self):
        """中級コース：スコアに応じて四則演算を変更"""
        if self.score < 10:
            self.operation = '+'
        elif self.score < 20:
            self.operation = '-'
        elif self.score < 30:
            self.operation = '*'
        else:
            self.operation = '/'
        
        num1 = random.randint(0, 30)
        num2 = random.randint(1, 30)  # 除算時、0除算を避ける
        self.problem = f"{num1} {self.operation} {num2}"

    def generate_advanced_problem(self):
        """上級コース：四則演算をランダムで出題"""
        operations = ['+', '-', '*', '/']
        self.operation = random.choice(operations)
        num1 = random.randint(0, 50)
        num2 = random.randint(1, 50)  # 除算時、0除算を避ける
        self.problem = f"{num1} {self.operation} {num2}"

    def check_answer(self, answer):
        """ユーザーの解答をチェック"""
        try:
            correct_answer = eval(self.problem)
            if abs(float(answer) - correct_answer) < 0.01:  # 精度を微調整
                return True
            else:
                return False
        except Exception as e:
            print(f"Error in checking answer: {e}")
            return False

    def update_score(self):
        """スコアを更新"""
        self.score += 1

    def play_game(self):
        """ゲームの進行"""
        print(f"Starting {self.course} course...")
        while not self.game_over and self.score < self.max_score:
            print(f"Current Score: {self.score}")
            print(f"Problem: {self.problem}")
            answer = input("Your answer: ")

            if self.check_answer(answer):
                print("Correct!")
                self.update_score()
            else:
                print("Incorrect. Try again.")
            
            time.sleep(1)  # 少し待つ
            self.generate_problem()

        if self.score >= self.max_score:
            self.game_over = True
            print("Congratulations! You've completed the game.")

def select_course():
    """コース選択"""
    print("Select a course:")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        return 'beginner'
    elif choice == '2':
        return 'intermediate'
    elif choice == '3':
        return 'advanced'
    else:
        print("Invalid choice. Please select again.")
        return select_course()

def main():
    """ゲームのメインフロー"""
    course = select_course()
    game = MathGame(course)
    game.play_game()

if __name__ == '__main__':
    main()
