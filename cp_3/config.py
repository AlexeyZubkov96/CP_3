from pathlib import Path

# Путь коренной папки программы
ROOT_PATH = Path(__file__).parent.parent
# Путь до дериктории "cp_3"
PATH_CP_3 = ROOT_PATH.joinpath("cp_3")
# Путь до файлу "operations.json"
PATH_OPERATIONS = PATH_CP_3.joinpath("operations.json")

# Количество нужных операций
count_operations = 5

