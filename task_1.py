
def total_salary(path):
    
    try:
        total = 0
        count = 0
        
        # Відкриваємо файл
        with open(path, 'r') as file:
            for line in file:
                # Видаляємо пробіли на початку та в кінці рядка
                line = line.strip()
                
                # Пропускаємо порожні рядки
                if not line:
                    continue
                
                try:
                    # Розділяємо рядок за комою
                    parts = line.split(',')
                    
                    # Перевіряємо, чи є достатньо частин
                    if len(parts) != 2:
                        print(f"Попередження: Неправильний формат рядка: {line}")
                        continue
                    
                    # Отримуємо зарплату (другу частину)
                    salary = float(parts[1])
                    
                    # Додаємо до загальної суми
                    total += salary
                    count += 1
                    
                except ValueError:
                    print(f"Попередження: Неможливо перетворити зарплату в число: {line}")
                    continue
        
        # Перевіряємо, чи знайдено хоча б одного розробника
        if count == 0:
            raise ValueError("Файл не містить даних про зарплати")
        
        # Обчислюємо середню зарплату
        average = total / count
        
        return (total, average)
        
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено")
        raise
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        raise
