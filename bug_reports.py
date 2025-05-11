# Исходный список баг-репортов
bug_reports = [
    {"id": 1, "title": "Ошибка авторизации", "priority": "high"},
    {"id": 2, "title": "Не работает кнопка 'Сохранить'", "priority": "high"},
    {"id": 3, "title": "Опечатка в тексте", "priority": "low"},
    {"id": 4, "title": "Медленная загрузка страницы", "priority": "high"},
    {"id": 5, "title": "Некорректный цвет кнопки", "priority": "low"}
]


# Функция для добавления нового бага
def add_bug(bug_list):
    bug_id = len(bug_list) + 1
    title = input("Введите название бага: ")
    priority = input("Введите приоритет (high/low): ").lower()
    while priority not in ["high", "low"]:
        print("Ошибка! Приоритет должен быть 'high' или 'low'")
        priority = input("Введите приоритет (high/low): ").lower()

    new_bug = {"id": bug_id, "title": title, "priority": priority}
    bug_list.append(new_bug)
    print(f"Баг '{title}' успешно добавлен!")


# Функция для удаления багов с низким приоритетом
def remove_low_priority(bug_list):
    initial_count = len(bug_list)
    bug_list[:] = [bug for bug in bug_list if bug["priority"] != "low"]
    removed_count = initial_count - len(bug_list)
    print(f"Удалено {removed_count} баг(ов) с низким приоритетом.")


# Функция для сортировки багов по приоритету (high сначала)
def sort_by_priority(bug_list):
    bug_list.sort(key=lambda x: x["priority"], reverse=True)
    print("Баг-репорты отсортированы по приоритету.")


# Функция для вывода списка багов
def print_bugs(bug_list):
    print("\nСписок баг-репортов:")
    for bug in bug_list:
        print(f"ID: {bug['id']}, Название: {bug['title']}, Приоритет: {bug['priority']}")
    print()


# Основной цикл программы
while True:
    print("\nМеню:")
    print("1. Показать все баги")
    print("2. Добавить новый баг")
    print("3. Удалить баги с низким приоритетом")
    print("4. Сортировать баги по приоритету")
    print("5. Выйти")

    choice = input("Выберите действие (1-5): ")

    if choice == "1":
        print_bugs(bug_reports)
    elif choice == "2":
        add_bug(bug_reports)
    elif choice == "3":
        remove_low_priority(bug_reports)
    elif choice == "4":
        sort_by_priority(bug_reports)
    elif choice == "5":
        print("Выход из программы.")
        break
    else:
        print("Неверный ввод. Пожалуйста, выберите от 1 до 5.")
