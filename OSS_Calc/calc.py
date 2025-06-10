import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")  # 비밀번호 입력창 때문에 약간 높임

        self.password = "12"  # 2자리 비밀번호
        self.expression = ""
        self.is_unlocked = False  # 비밀번호 확인 상태

        # 비밀번호 입력창
        self.pw_label = tk.Label(root, text="비밀번호를 입력하세요 (2자리)", font=("Arial", 14))
        self.pw_label.pack(pady=(10, 5))

        self.pw_entry = tk.Entry(root, font=("Arial", 18), show="*")
        self.pw_entry.pack(ipadx=10, ipady=8, padx=40, pady=5)

        self.pw_button = tk.Button(root, text="확인", font=("Arial", 14), command=self.check_password)
        self.pw_button.pack(pady=(0, 15))

        # 계산기 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def check_password(self):
        entered_pw = self.pw_entry.get()
        if entered_pw == self.password:
            self.is_unlocked = True
            self.pw_label.config(text="비밀번호 확인 완료")
            self.pw_entry.config(state="disabled")
            self.pw_button.config(state="disabled")
        else:
            self.pw_label.config(text="비밀번호가 틀렸습니다. 다시 입력하세요")
            self.pw_entry.delete(0, tk.END)

    def on_click(self, char):
        if not self.is_unlocked:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "비밀번호 확인 필요")
            return

        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



