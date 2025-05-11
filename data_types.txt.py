# Создаем словарь с информацией о баге (изменяемый тип)
bug_report = {
    "id": 1,
    "title": "Кнопка 'Отправить' не работает",
    "status": "open"
}

print("Исходный баг-репорт:", bug_report)

# Изменяем статус бага
bug_report["status"] = "closed"

print("Измененный баг-репорт:", bug_report)