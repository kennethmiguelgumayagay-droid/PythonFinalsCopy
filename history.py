# history.py
from datetime import datetime

class HistoryManager:
    def __init__(self):
        self.items = []

    def add(self, expression, result):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.items.append((timestamp, expression, result))

    def show(self):
        if not self.items:
            print("History is empty.")
            return

        print("\nHistory:")
        for ts, expr, res in self.items:
            print(f"[{ts}] {expr} = {res}")

    def clear(self):
        self.items.clear()
        print("History cleared.")
