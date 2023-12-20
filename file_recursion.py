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

# ця штука має приймати аргументи з терміналу?
# не розумію де має бути тека нова "діст" якшо вона не була вказана, треба її робити в тій самі теці звідки відбувалось копіювання? чи в місці виклику?
# оброка винятків?
# p.exists() - рмк чекери наявності
from pathlib import Path
import shutil

base_folder = Path()


def create_directory(path, directory_name):
    # Ensure path is a pathlib.Path object
    path = Path(path)
    # Create the new directory inside the specified path
    new_directory_path = path / directory_name
    try:
        # Create the directory
        new_directory_path.mkdir()
        return new_directory_path
    except FileExistsError:
        print(f"Directory '{new_directory_path}' already exists at {directory_name}")
        return new_directory_path
    except Exception as e:
        print(f"Error creating directory: {e}")


def folder_cheker(file_ext, dist_path):
    folder_list = dist_path.iterdir()
    folder_list_name = [data.name for data in folder_list]
    if file_ext in folder_list_name:
        path = dist_path / file_ext
        return path
    else:
        path = create_directory(dist_path, file_ext)
        print(f"New folder has been created with name {file_ext}")
        return path


def file_copy_handler(file, dest_path):
    file_suf = file.suffix
    destination_folder = folder_cheker(file_suf, dest_path)
    dest_file_list = destination_folder.iterdir()
    list_file_name = [data.name for data in dest_file_list]

    if file.name in list_file_name:
        print(f"In directory '{destination_folder}' already exists file {file.name}")
    else:
        source_path = Path(file)
        destination_path = Path(destination_folder)
        # Copy the file using shutil.copy
        try:
            shutil.copy(source_path, destination_path)
        except Exception as ex:
            print(f"File {file.name} cannot be copied. Reason: {ex}")
        print(f"File {file.name} is succesfuly copied at {destination_path}")


def folder_handler(path, new_directory_path):
    current_file_list = path.iterdir()
    for data in current_file_list:
        if data.is_file():
            file_copy_handler(data, new_directory_path)
        else:
            folder_handler(data, new_directory_path)


def copy_handler(origin_path, destination_folder="dist2"):
    if type(destination_folder) == str:
        p = Path()
        destination_folder = create_directory(p, destination_folder)
    folder_handler(origin_path, destination_folder)


test_path = base_folder / "test_dir"
dest_path = create_directory(base_folder, "manual_dist")

copy_handler(test_path)
