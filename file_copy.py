"""
- створювач папок (де, шо):
   -- перевіримв чи немає вже там цієї папки
   -- звяв де файл знаходиться / додав нову папку
   -- повернув новий шлях

- копіювач файлів (шо, куди):
   --чи єв новому місці цей файл? - якшо та. то шо?
   -- зробив копію
   --повернув "успіх"
  

- рекурсія папок (папка яку перевіряєм):
   -- берем весь список файлів
   -- якшо то файл - 
         --- в точці "призначення" треба перевірити чи є вже папка з розширеям цього файлу якшо є
                  функція копі (шо, і в цю папку)
         ---- якшо немає:
                  функція зробити папку 
                  функція копі туди

   -- якшо то папка - викликати фукнцію себе (папку яку перевіряєм)


- головна функція (звідки взяти файли, куди скинути файли  = або створити папку в "звідки")
   -- виклик перевірки чибув переданий кінцева точка. якшо ні, створити папку в "звідки"
     
"""
# оброка винятків? // // якшо доступ заборонений до файлу??

from pathlib import Path
import shutil
import os
import argparse


def create_directory(path, directory_name):
    new_directory_path = path / directory_name
    if new_directory_path.exists() and new_directory_path.is_dir():
        print(f"Directory '{new_directory_path}' already exists at {directory_name}")
        return new_directory_path
    else:
        try:
            new_directory_path.mkdir(parents=True, exist_ok=True)
            return new_directory_path
        except Exception as e:
            print(f"Error creating directory: {e}")


def get_dir_reciever(file_ext, dist_path):
    dist_folder = dist_path / file_ext
    if dist_folder.exists():
        path = dist_path / file_ext
        return path
    else:
        path = create_directory(dist_path, file_ext)
        print(f"New folder has been created with name {file_ext}")
        return path


def file_copy_handler(file, dest_path):
    destination_folder = get_dir_reciever(file.suffix, dest_path)
    destination_file = destination_folder / file.name

    if destination_file.exists():
        print(f"In directory '{destination_folder}' already exists file {file.name}")
    else:
        source_path = file
        destination_path = Path(destination_folder)
        try:
            shutil.copy(source_path, destination_path)
            print(f"File {file.name} is succesfuly copied at {destination_path}")
        except Exception as ex:
            print(f"File {file.name} cannot be copied. Reason: {ex}")


def folder_handler(path, new_directory_path):
    current_file_list = path.iterdir()
    for data in current_file_list:
        if data.is_file():
            file_copy_handler(data, new_directory_path)
        else:
            folder_handler(data, new_directory_path)


def main():
    parser = argparse.ArgumentParser(description="Process command-line arguments")

    parser.add_argument("--source", "-s", required=True)
    parser.add_argument("--dist", "-d", default="dist")

    args = parser.parse_args()

    source_str = os.path.abspath(args.source)
    source_path = Path(source_str)

    if not source_path.exists():
        print("Sorry, source folder not found")
        return

    if args.dist == "dist":
        p = Path()
        dist_path = create_directory(p, args.dist)

    else:
        dist_str = os.path.abspath(args.dist)
        dist_path = Path(dist_str)

    if not dist_path.exists():
        print("Sorry, destination folder not found")
        return

    folder_handler(source_path, dist_path)


if __name__ == "__main__":
    main()
