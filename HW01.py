import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Рекурсивне копіювання та сортування файлів.')
    parser.add_argument('source_dir', type=str, help='Шлях до вихідної директорії')
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням dist)')
    return parser.parse_args()

def copy_files_recursively(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        if os.path.isdir(source_item):
            copy_files_recursively(source_item, dest_dir)
        else:
            file_extension = os.path.splitext(item)[1][1:]  # Отримуємо розширення файлу без крапки
            if file_extension:  # Перевіряємо, чи є розширення
                dest_subdir = os.path.join(dest_dir, file_extension)
                if not os.path.exists(dest_subdir):
                    os.makedirs(dest_subdir)
                shutil.copy2(source_item, dest_subdir)
            else:
                dest_subdir = os.path.join(dest_dir, 'no_extension')
                if not os.path.exists(dest_subdir):
                    os.makedirs(dest_subdir)
                shutil.copy2(source_item, dest_subdir)

def main():
    args = parse_arguments()
    try:
        copy_files_recursively(args.source_dir, args.dest_dir)
        print(f'Файли успішно скопійовані та відсортовані у директорії {args.dest_dir}')
    except Exception as e:
        print(f'Сталася помилка: {e}')

if __name__ == '__main__':
    main()
