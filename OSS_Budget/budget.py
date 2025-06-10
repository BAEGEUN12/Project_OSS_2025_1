import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def set_brightness(self):
        while True:
            try:
                level = int(input("밝기를 1(가장 어둡게)부터 5(가장 밝게)까지 입력하세요: "))
                if 1 <= level <= 5:
                    print(f"밝기를 {level}로 설정합니다.")
                    break
                else:
                    print("1부터 5 사이의 숫자를 입력해주세요.")
            except ValueError:
                print("문자말고 숫자만 입력해주세요.") 



