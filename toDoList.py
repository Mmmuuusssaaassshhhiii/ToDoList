# Список дел
import datetime
import json

FILE_NAME = 'tasks.json'

def load_tasks():
    try:
        with open(FILE_NAME, encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

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
    save_tasks(tasks)
    print(f'Задача #{new_id} добавлена')

def mark_done(tasks):
    if not tasks:
        print('Список пуст')
        return

    show_tasks(tasks)
    try:
        target_id = int(input('Введите номер задачи для отметки: '))
    except ValueError:
        print('Ошибка: введите число')
        return

    for task in tasks:
        if task['id'] == target_id:
            if task['done']:
                print('Задача выполнена')
            else:
                task['done'] = True
                save_tasks(tasks)
                print(f'Задача #{target_id} отмечена выполненной')
            return

    print(f'Задача #{target_id} не найдена')

def delete_task(tasks):
    if not tasks:
        print('Список пуст')
        return

    show_tasks(tasks)
    try:
        target_id = int(input('Введите номер задачи для удаления: '))
    except ValueError:
        print('Ошибка: введите число')
        return

    found = any(t['id'] == target_id for t in tasks)
    if not found:
        print(f'Задача #{target_id} не найдена')
        return

    tasks[:] = [t for t in tasks if t['id'] != target_id]
    print(f'Задача #{target_id} удалена')
    save_tasks(tasks)
    
def main():
    print('=== To-Do List ===')
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = get_choice()

        if choice == 1:
            show_tasks(tasks)
        elif choice == 2:
            add_tasks(tasks)
        elif choice == 3:
            mark_done(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            print('До встречи!')
            break

if __name__ == '__main__':
        main()
