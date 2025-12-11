# main.py
from parser import evaluate_expression
from history import HistoryManager

def print_menu():
    print("\nAdvanced Calculator")
    print(" 1) Enter mathematical expression")
    print(" 2) Show history")
    print(" 3) Clear history")
    print(" 4) Exit\n")

def main():
    history = HistoryManager()

    while True:
        print_menu()
        choice = input("Choose option: ").strip()

        if choice == "4":
            print("Goodbye.")
            break

        elif choice == "2":
            history.show()

        elif choice == "3":
            history.clear()

        elif choice == "1":
            expr = input("Enter expression: ").strip()

            try:
                result = evaluate_expression(expr)
                print(f"Result: {result}")
                history.add(expr, result)
            except Exception as e:
                print("Error:", e)

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
