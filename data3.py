import csv
from datetime import datetime
import plotly.graph_objects as go


# Функція для обчислення віку на поточну дату
def calculate_age(birthdate):
    today = datetime.now().date()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))


# Функція для зчитування CSV файлу і обробки даних
def process_csv(csv_filename):
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            records = [row for row in reader]
            print("Ok, файл CSV відкрито успішно.")
            return records
    except FileNotFoundError:
        print("Повідомлення про відсутність або проблеми при відкритті файлу CSV.")
        return None


# Функція для підрахунку кількості співробітників чоловічої і жіночої статі
def count_gender(records):
    male_count = sum(1 for r in records if r['Стать'] == 'Чоловік')
    female_count = sum(1 for r in records if r['Стать'] == 'Жінка')

    # Виведення результатів у консоль
    print(f"Кількість чоловіків: {male_count}")
    print(f"Кількість жінок: {female_count}")

    # Побудова діаграми по статі
    labels = ['Чоловіки', 'Жінки']
    counts = [male_count, female_count]

    fig = go.Figure(data=[go.Pie(labels=labels, values=counts, hole=.3)])
    fig.update_layout(title_text='Розподіл співробітників за статтю')
    fig.show()


# Функція для підрахунку кількості співробітників кожної вікової категорії
def count_age_categories(records):
    age_categories = {'younger_18': 0, '18-45': 0, '45-70': 0, 'older_70': 0}

    for r in records:
        try:
            birthdate = datetime.strptime(r['Дата народження'], '%Y-%m-%d').date()
            age = calculate_age(birthdate)
            if age < 18:
                age_categories['younger_18'] += 1
            elif 18 <= age <= 45:
                age_categories['18-45'] += 1
            elif 46 <= age <= 70:
                age_categories['45-70'] += 1
            else:
                age_categories['older_70'] += 1
        except ValueError:
            continue  # Пропускаємо записи з некоректною датою

    # Виведення результатів у консоль
    print(f"Кількість співробітників до 18 років: {age_categories['younger_18']}")
    print(f"Кількість співробітників 18-45 років: {age_categories['18-45']}")
    print(f"Кількість співробітників 46-70 років: {age_categories['45-70']}")
    print(f"Кількість співробітників старших за 70 років: {age_categories['older_70']}")

    # Побудова діаграми по віковим категоріям
    labels = ['До 18 років', '18-45 років', '46-70 років', 'Старші за 70']
    counts = [age_categories['younger_18'], age_categories['18-45'], age_categories['45-70'],
              age_categories['older_70']]

    fig = go.Figure(data=[go.Bar(x=labels, y=counts, marker_color='indianred')])
    fig.update_layout(title_text='Розподіл співробітників за віковими категоріями',
                      xaxis_title='Вікові категорії',
                      yaxis_title='Кількість')
    fig.show()


# Основна функція
def main():
    csv_filename = 'people.csv'  # Вкажіть шлях до вашого CSV файлу
    records = process_csv(csv_filename)

    if records is None:
        return  # Якщо файл не відкрився, завершити програму

    count_gender(records)
    count_age_categories(records)


# Виклик основної функції
if __name__ == "__main__":
    main()
