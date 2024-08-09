def generate_password(n):
    # Перебор пар чисел от 1 до n
    result = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            # Проверка на делимость
            if n % (i + j) == 0:
                # Добавление пары к результату
                result.append(str(i) + str(j))
    return result

# Чтение числа n
while True:
    try:
        n = int(input("Введите число n (от 3 до 20): "))
        if n < 3 or n > 20:
            print("Число должно быть от 3 до 20.")
            continue
        break
    except ValueError:
        print("Неверный ввод. Попробуйте еще раз.")
        continue

# Генерация пароля
result = ''.join(generate_password(n))
print(result)