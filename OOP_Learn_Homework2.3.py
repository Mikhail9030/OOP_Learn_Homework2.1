import os

def process_and_merge_files(input_files: list, output_file: str, encoding: str = 'utf-8'):

    files_data = []

    # 1. Чтение файлов
    for file_path in input_files:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding=encoding) as file:
                lines = file.readlines()
                files_data.append({
                    'path': file_path,
                    'name': os.path.basename(file_path),
                    'line_count': len(lines),
                    'content': lines
                })
        else:
            print(f"Предупреждение: Файл {file_path} не найден и будет пропущен.")

    # 2. Сортировка по количеству строк (по ключу 'line_count')
    files_data.sort(key=lambda x: x['line_count'])

    # 3. Запись в итоговый файл
    with open(output_file, 'w', encoding=encoding) as out_file:
        for data in files_data:
            out_file.write(f"{data['name']}\n")
            out_file.write(f"{data['line_count']}\n")

            for line in data['content']:
                out_file.write(line)

                if not line.endswith('\n'):
                    out_file.write('\n')

    print(f"Успешно! Файлы объединены в {output_file}")


def main_file_merger():
    folder_name = 'Cooking Book'

    file_names = ['1.txt', '2.txt', '3.txt']

    files_to_merge = [os.path.join(folder_name, file) for file in file_names]

    result_file = 'result.txt'

    process_and_merge_files(files_to_merge, result_file)


if __name__ == '__main__':
    main_file_merger()