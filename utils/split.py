import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split

# Загрузка данных
file_path = './data/data.csv'  # Убедитесь, что путь правильный и экранирован
df = pd.read_csv(file_path)

# Выбор уникальных пользователей
unique_user_ids = df['user_id'].unique()

# Проверка количества уникальных пользователей
total_users = len(unique_user_ids)
print(f"Total unique users: {total_users}")

# Случайная выборка из 250,000 пользователей
sampled_user_ids = pd.Series(unique_user_ids).sample(n=250000)

# Создание нового DataFrame с записями выбранных пользователей
sampled_df = df[df['user_id'].isin(sampled_user_ids)]

# Сохранение выборки в новый файл (опционально)
sampled_df.to_csv('sampled_data_wb.csv', index=False)

