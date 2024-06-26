# Хакатон Вайлдберриз 2024
![Wildberries](https://avatars.githubusercontent.com/u/66719899?s=200&v=4)
## Обзор
Этот репозиторий содержит проект, разработанный для Хакатона WB 24.  
Проект включает алгоритм рекомендаций и связанные с ними данные

### Данные
Здесь используется облегченная версия данных.Изначальный датасет весил более 20гб.
В датасете 4 колонки:
order_dt - дата заказа
user_id - id пользователя,сделавшего заказ,
nm_id - id предмета,который заказали,
subject_id - id категории,которую заказывали.

	    order_dt	user_id	nm_id	subject_id
    0	2024-01-28	344304584	666592012	2100
    1	2024-01-05	189230488	590142760	2892
    2	2024-01-22	22930004	55893688	5244
    3	2024-01-14	323996748	667504032	2512
    4	2024-03-29	76050976	129627900	6648

Все данные были предварительно зашифрованы и не ведут к реальным пользователям или товарам.  
С помощью облегченных данных можно было поэкспериментировать и проверить различные гипотезы.

### Задача
**Проблематика**:
Пользователи зачастую оказываются в пузыре своих интересов и нужны инструменты для того, чтобы из него выйти.
**Задача**:
Необходимо на основании покупок пользователей предсказать товары из новых для юзера категорий И Предложить пользователю товары категорий, с которыми он еще не взаимодействовал.

### Решение
Предложенное решение заключается в построении матрицы взаимодействий, которая показывает, сколько раз каждый пользователь взаимодействовал с каждой категорией товаров. На основе этой матрицы используется алгоритм рекомендательных систем, такой как коллаборативная фильтрация, чтобы предсказать категории, с которыми пользователи еще не взаимодействовали. В результате для каждого пользователя генерируется список рекомендаций товаров из новых для него категорий, что помогает ему выйти за пределы своего привычного круга интересов.

## Содержимое
- `Rec_alg.ipynb`: Jupyter Notebook с алгоритмом рекомендаций.
- `data/`: Каталог, содержащий файлы данных.
- `utils/split.py`: Cкрипт для разделения изначального датасета.


## Использование
1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/Konstagit/Hacaton_WB_24.git
    ```

2. Перейдите в каталог репозитория и устанвоите зависимости:
    ```bash
    cd Hacaton_WB_24
    pip install -r requirements.txt
    ```

3. Разделите данные(При необходимости):
    ```bash
    python utils/split.py
    ```

4. Откройте Jupyter Notebook:
    ```bash
    python -m notebook Rec_alg.ipynb
    ```

## Требования
- Python 3.x
- Jupyter Notebook
- Соответствующие библиотеки Python (указаны в блокноте)

## Лицензия
Этот проект лиспользует открыую лицензию.

## Контакт
Для получения полного датасета, а также для любых вопросов или предложений, пожалуйста, свяжитесь:
Konstagit  
Email: [konstantinovpavelgit@gmail.com](mailto:konstantinovpavelgit@gmail.com)
