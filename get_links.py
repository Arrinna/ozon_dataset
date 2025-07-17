# Извлечем JSON-строку из каждой строки вручную через поиск фигурных скобок

import os
import re
import json
import pandas as pd
# import ace_tools as tools

# Путь к файлу
file_path = "./eng_categories.txt"

# Получаем директорию исходного файла
output_dir = os.path.dirname(file_path)
output_path = os.path.join(output_dir, "ozon_categories_links.csv")

# Считываем строки
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()


data = []
problematic_lines = []

for line in lines:
    match = re.search(r'(\{.*\})', line)
    if match:
        json_str = match.group(1)
        try:
            entry = json.loads(json_str)
            label = entry.get("label", "")
            key = entry.get("key", "")
            if key.startswith("_"):
                key = key[1:]
            url = f"https://data.ozon.ru/app/categories-comparison?category=2_{key}&period=year&group=group_brand&metric=metric_gmv&sortingColumn=metric_gmv&sortingOrder=direction_desc"
            data.append((label, url))
        except Exception as e:
            problematic_lines.append((json_str, str(e)))

# Создание DataFrame
df = pd.DataFrame(data, columns=["Label", "URL"])

# Показываем результат
# tools.display_dataframe_to_user(name="Ozon Category Links (Корректный парсинг)", dataframe=df)

# Сохраняем как CSV
csv_path = "/mnt/data/ozon_categories_links.csv"
df.to_csv(output_path, index=False)
