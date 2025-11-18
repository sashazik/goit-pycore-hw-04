def get_cats_info(path: str) -> list[dict]:
    """
    Читає файл з даними котів та повертає список словників.

    Args:
        path (str): Шлях до текстового файлу.

    Returns:
        list[dict]: Список словників з інформацією про котів.
    """
    cats_info = []
    
    try:
        # 1. Використання with для читання файлу
        # 2. Встановлення кодування utf-8
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                try:
                    # 3. Розділення даних
                    cat_id, name, age = line.split(',')
                    
                    # 4. Формування словника та додавання до списку
                    cats_info.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                except (IndexError, ValueError):
                    # Обробка, якщо рядок має неправильну структуру
                    print(f"Помилка: Неправильний формат рядка: '{line}'")

    # 5. Обробка винятків
    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return []
    except IOError:
        print(f"Помилка: Не вдалося прочитати файл '{path}'.")
        return []
    except Exception as e:
        print(f"Виникла непередбачувана помилка: {e}")
        return []
        
    return cats_info