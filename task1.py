def total_salary(path: str) -> tuple[int | float, int | float]:
    """
    Аналізує файл зарплат та повертає загальну та середню суму.

    Args:
        path (str): Шлях до текстового файлу.

    Returns:
        tuple[int | float, int | float]: Кортеж із загальною 
                                        та середньою зарплатою.
    """
    total = 0
    count = 0
    
    try:
        # 1. Використання менеджера контексту with
        # 2. Встановлення кодування utf-8
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                # Видаляємо зайві пробіли на початку/в кінці
                line = line.strip() 
                
                # Пропускаємо порожні рядки
                if not line:
                    continue
                
                try:
                    # 3. Розділення даних
                    name, salary_str = line.split(',')
                    
                    # 4. Обчислення суми
                    total += float(salary_str)
                    count += 1
                except ValueError:
                    # Обробка пошкодженого рядка (де зарплата - не число)
                    print(f"Помилка: Неправильний формат даних у рядку: '{line}'")
                except IndexError:
                    # Обробка пошкодженого рядка (немає коми)
                    print(f"Помилка: Неправильний формат рядка: '{line}'")

        # 5. Розрахунок середньої зарплати
        if count == 0:
            # Уникнення ділення на нуль, якщо файл порожній
            return (0, 0)
        
        average = total / count
        
        return (total, average)

    # 6. Обробка винятків
    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return (0, 0)
    except IOError:
        print(f"Помилка: Не вдалося прочитати файл '{path}'.")
        return (0, 0)
    except Exception as e:
        print(f"Виникла непередбачувана помилка: {e}")
        return (0, 0)

