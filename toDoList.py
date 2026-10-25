# Список дел
import datetime

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

def add_tasks(tasks):
    text = input('Введите задачу: ').strip()
    if not text:
        print('Текст задачи не может быть пустым.')
        return

    new_id = max((t['id'] for t in tasks), default = 0) + 1
    new_task = {
        'id': new_id,
        'text': text,
        'done': False,
        'created': datetime.date.today().isoformat()
    }
    tasks.append(new_task)
    print(f'Задача #{new_id} добавлена')


def main():
    print('=== To-Do List ===')
    tasks = []
    
    while True:
        show_menu()
        choice = get_choice()

        if choice == 1:
            show_tasks(tasks)
        elif choice == 2:
            add_tasks(tasks)
        elif choice == 3:
            print('(здесь будет отметка)')
        elif choice == 4:
            print('(здесь будет удаление)')
        elif choice == 5:
            print('До встречи!')
            break

if __name__ == '__main__':
        main()