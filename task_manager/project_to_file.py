import os

def write_project_to_file(project_dir, output_file):
    """
    Рекурсивно обходит директории проекта и записывает содержимое всех файлов в один выходной файл.
    Исключает файлы __init__.py, apps.py, tests.py, manage.py, а также директории с названием 'migrations' и 'static'.
    Включает HTML-файлы из директорий 'templates', а также файлы с расширениями .conf.template, .env, .ini и .sh.

    Args:
        project_dir (str): Путь к корневой директории проекта.
        output_file (str): Путь к выходному файлу.
    """
    with open(output_file, "w", encoding="utf-8") as f:
        for root, dirs, files in os.walk(project_dir):
            # Исключаем директорию 'migrations' и 'static'
            if "migrations" in dirs:
                dirs.remove("migrations")
            if "static" in dirs:
                dirs.remove("static")

            for file in files:
                file_path = os.path.join(root, file)

                # Исключаем файлы __init__.py, apps.py, tests.py, manage.py ...
                if file in [
                    "__init__.py",
                    "apps.py",
                    "tests.py",
                    "manage.py",
                    "asgi.py",
                    "wsgi.py",
                    "project_to_file.py",
                    "admin.py",
                ]:
                    continue

                # Включаем HTML-файлы из директорий 'templates'
                if file.endswith(".html") and "templates" in root:
                    with open(file_path, "r", encoding="utf-8") as source_file:
                        f.write(f"# {file_path}\n")
                        f.write(source_file.read() + "\n\n")

                # Включаем файлы с расширениями .conf.template, .env, .ini и .sh
                elif file.endswith((".conf.template", ".env", ".ini", ".sh")):
                    with open(file_path, "r", encoding="utf-8") as source_file:
                        f.write(f"# {file_path}\n")
                        f.write(source_file.read() + "\n\n")

                # Включаем Python-файлы
                elif file.endswith(".py"):
                    with open(file_path, "r", encoding="utf-8") as source_file:
                        f.write(f"# {file_path}\n")
                        f.write(source_file.read() + "\n\n")


if __name__ == "__main__":
    project_dir = "D:/django/taskManager/task_manager/"
    output_file = "tasks_project_code.txt"
    write_project_to_file(project_dir, output_file)
    print(f"Код проекта записан в файл {output_file}")
