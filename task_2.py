def get_cats_info(path):
    
    cats_list = []
    
    try:
        # Відкриваємо файл
        with open(path, 'r', encoding='utf-8') as file:
            # Читаємо фацл
            for line in file:
                # Видаляємо зайві пробіли та символи нового рядка
                line = line.strip()
                
                # Пропускаємо порожні рядки
                if not line:
                    continue
                
                try:
                    # Розділяємо рядок за комами
                    parts = line.split(',')
                    
                    # Перевіряємо, що рядок містить рівно 3 частини
                    if len(parts) != 3:
                        print(f"Попередження: рядок '{line}' має неправильний формат, пропускаємо")
                        continue
                    
                    # Створюємо словник з даними про кота
                    cat_info = {
                        "id": parts[0].strip(),
                        "name": parts[1].strip(),
                        "age": parts[2].strip()
                    }
                    
                    # Додаємо словник до списку
                    cats_list.append(cat_info)
                    
                except Exception as e:
                    print(f"Помилка при обробці рядка '{line}': {e}")
                    continue
    
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено")
        raise
    except PermissionError:
        print(f"Немає доступу до файлу '{path}'")
        raise
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        raise
    
    return cats_list
