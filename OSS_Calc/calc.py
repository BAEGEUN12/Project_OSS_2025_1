import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

        self.password = "12"
        self.expression = ""
        self.is_unlocked = False

        self.inactivity_timer = None  # 타이머 ID 저장

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

        self.reset_timer()  # 초기 타이머 시작

        # 모든 키 입력 이벤트에 대해 타이머 리셋
        self.root.bind_all("<Any-KeyPress>", self.reset_timer_event)
        self.root.bind_all("<Button>", self.reset_timer_event)

    def check_password(self):
        self.reset_timer()
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
        self.reset_timer()
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

    def reset_timer_event(self, event=None):
        self.reset_timer()

    def reset_timer(self):
        if self.inactivity_timer is not None:
            self.root.after_cancel(self.inactivity_timer)
        self.inactivity_timer = self.root.after(60000, self.auto_shutdown)

    def auto_shutdown(self):
        self.root.destroy()  # 1분 후 자동 종료


