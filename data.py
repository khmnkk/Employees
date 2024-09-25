import csv
from faker import Faker
from random import choice, randint

# Ініціалізація Faker з українською локалізацією
fake = Faker(locale='uk_UA')

# Словники для по батькові
male_patronymics = [
    'Олександрович', 'Сергійович', 'Іванович', 'Петрович', 'Михайлович',
    'Володимирович', 'Юрійович', 'Андрійович', 'Богданович', 'Дмитрович',
    'Олегович', 'Євгенович', 'Максимович', 'Тарасович', 'Григорійович',
    'Романович', 'Миколайович', 'Вікторович', 'Павлович', 'Федорович'
]

female_patronymics = [
    'Олександрівна', 'Сергіївна', 'Іванівна', 'Петрівна', 'Михайлівна',
    'Володимирівна', 'Юріївна', 'Андріївна', 'Богданівна', 'Дмитрівна',
    'Олегівна', 'Євгенівна', 'Максимівна', 'Тарасівна', 'Григоріївна',
    'Романівна', 'Миколаївна', 'Вікторівна', 'Павлівна', 'Федорівна'
]

# Створюємо функцію для генерування даних
def generate_person(gender):
    if gender == 'Чоловік':
        first_name = fake.first_name_male()
        patronymic = choice(male_patronymics)
    else:
        first_name = fake.first_name_female()
        patronymic = choice(female_patronymics)

    surname = fake.last_name()
    birthdate = fake.date_of_birth(minimum_age=16, maximum_age=85)
    job = fake.job()
    city = fake.city()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()

    return [surname, first_name, patronymic, gender, birthdate, job, city, address, phone, email]

# Генеруємо дані
def generate_data(num_records=2000):
    records = []
    num_male = int(num_records * 0.6)
    num_female = num_records - num_male

    for _ in range(num_male):
        records.append(generate_person('Чоловік'))

    for _ in range(num_female):
        records.append(generate_person('Жінка'))

    return records

# Зберігаємо дані в CSV-файл
def save_to_csv(filename, records):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Заголовки
        writer.writerow([
            'Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження',
            'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email'
        ])
        # Записи
        writer.writerows(records)

# Генеруємо 2000 записів і зберігаємо у файл
records = generate_data(2000)
save_to_csv('people.csv', records)

print("Дані збережено у файл 'people.csv'.")
