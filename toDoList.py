# Список дел
def show_menu():
    print('1. Показать задачи')
    print('2. Добавить задачу')
    print('3. Отметить выполненной')
    print('4. Удалить задачу')
    print('5. Выход')

def get_choice():
    while True:
        choice = input('Ваш выбор: ').strip()
        if choice in ('1', '2', '3', '4', '5'):
            return int(choice)
        print('Не понял, введите число от 1 до 5')

def show_tasks(tasks):
    if not tasks:
        print('Список пуст')
        return

    for task in tasks:
        status = '[x]' if task['done'] else '[ ]'
        print(f"{task['id']}. {status} {task['text']} (создано: {task['created']})")


def main():
    print('=== To-Do List ===')
    while True:
        show_menu()
        choice = get_choice()
        tasks = [
        {"id": 1, "text": "Купить хлеб", "done": False, "created": "2026-10-25"},
        {"id": 2, "text": "Помыть посуду", "done": True, "created": "2026-10-24"},
        {"id": 3, "text": "Позвонить маме", "done": False, "created": "2026-10-23"},
        ]

        if choice == 1:
            show_tasks(tasks)
        elif choice == 2:
            print('(здесь будет добавление)')
        elif choice == 3:
            print('(здесь будет отметка)')
        elif choice == 4:
            print('(здесь будет удаление)')
        elif choice == 5:
            print('До встречи!')
            break

if __name__ == '__main__':
        main()