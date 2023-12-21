from pathlib import Path
import os

# Отримання абсолютного шляху за допомогою os.path.abspath
absolute_path_str = os.path.abspath("example.txt")

# Конвертація в об'єкт шляху з pathlib
absolute_path = Path(absolute_path_str)

# Тепер absolute_path - це об'єкт шляху з pathlib
print(f"Type of absolute_path: {type(absolute_path)}")
print(f"Path object: {absolute_path}")
