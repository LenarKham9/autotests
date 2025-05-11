def test_cases_stats():
    days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    test_cases = []

    # Запрашиваем количество тест кейсов для каждого дня недели
    for day in days_of_week:
        while True:
            try:
                cases = int(input(f"Введите количество тест кейсов за {day}: "))
                if cases < 0:
                    print("Количество не может быть отрицательным. Попробуйте еще раз.")
                    continue
                test_cases.append(cases)
                break
            except ValueError:
                print("Пожалуйста, введите целое число.")

    # Вычисляем общее количество и среднее значение
    total = sum(test_cases)
    average = total / len(test_cases)

    # Выводим результаты
    print(f"\nОбщее количество тестов за неделю: {total}")
    print(f"Среднее количество тестов в день: {average:.2f}")

    # Выводим сообщение в зависимости от результата
    if average > 10:
        print("Отличная работа!")
    else:
        print("Попробуй улучшить результат")
test_cases_stats()