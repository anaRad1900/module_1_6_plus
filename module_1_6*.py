# Данные входа
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Упорядочим имена студентов по алфавиту
sorted_students = sorted(students)

# Создаём пустой словарь для хранения средних баллов
average_grades = {}

# Вычисляем средний балл для каждого студента
for i, student in enumerate(sorted_students):
    average_score = sum(grades[i]) / len(grades[i])
    average_grades[student] = average_score

# Выводим результат
print(average_grades)