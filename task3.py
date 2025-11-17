import sys
from pathlib import Path
from colorama import init, Fore, Style

def display_directory_tree(directory: Path, prefix: str = ""):
    """
    Рекурсивно обходить директорію та виводить її структуру з кольорами.
    """
    
    # Отримуємо список елементів, сортуємо, щоб директорії йшли першими
    try:
        items = sorted(list(directory.iterdir()), key=lambda p: p.is_file())
    except PermissionError:
        print(f"{prefix}{Fore.RED}Немає доступу до {directory.name}{Style.RESET_ALL}")
        return
    except FileNotFoundError:
         print(f"{prefix}{Fore.RED}Директорію не знайдено: {directory.name}{Style.RESET_ALL}")
         return

    for i, item in enumerate(items):
        is_last = (i == len(items) - 1)
        
        # Визначаємо префікси для дерева
        connector = "┗━ " if is_last else "┣━ "
        new_prefix = prefix + ("    " if is_last else "┃   ")
        
        if item.is_dir():
            # Директорії - синім кольором
            print(f"{prefix}{connector}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
            # Рекурсивний виклик для піддиректорії
            display_directory_tree(item, new_prefix)
        else:
            # Файли - зеленим кольором
            print(f"{prefix}{connector}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")

def main():
    # Ініціалізуємо colorama
    init(autoreset=True)
    
    # 1. Перевірка аргументів командного рядка
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Помилка: Необхідно вказати шлях до директорії.")
        print(f"Використання: python {sys.argv[0]} /шлях/до/директорії")
        sys.exit(1)
        
    # 2. Використання pathlib
    dir_path = Path(sys.argv[1])
    
    # 3. Обробка помилок
    if not dir_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{dir_path}' не існує.")
        sys.exit(1)
        
    if not dir_path.is_dir():
        print(f"{Fore.RED}Помилка: '{dir_path}' не є директорією.")
        sys.exit(1)
        
    # Виводимо корінь директорії
    print(f"\n{Fore.YELLOW}📦 {dir_path.resolve().name}")
    # Запускаємо рекурсивний обхід
    display_directory_tree(dir_path)

if __name__ == "__main__":
    main()