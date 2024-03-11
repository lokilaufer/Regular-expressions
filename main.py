from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

import re

# Объявляем функцию для преобразования телефонов в нужный формат
def format_phone(phone):
    # Ищем номер телефона в строке
    phone_number = re.search(r'(\+?\d{1,2})(\d{3})(\d{3})(\d{2})(\d{2})', phone)
    # Форматируем номер в нужный вид
    if phone_number:
        return f"+{phone_number.group(1)}({phone_number.group(2)}){phone_number.group(3)}-{phone_number.group(4)}-{phone_number.group(5)}"
    return phone

# Создаем словарь для группировки контактов по ФИО
contacts_dict = {}

# Проходим по списку контактов и обновляем информацию
for contact in contacts_list:
    full_name = contact[0] + " " + contact[1] + " " + contact[2]
    if full_name in contacts_dict:
        # Если такой контакт уже есть, обновляем информацию (фамилию, имя, отчество)
        contacts_dict[full_name][0] = contact[0]
        contacts_dict[full_name][1] = contact[1]
        contacts_dict[full_name][2] = contact[2]
        # Обновляем телефон в нужном формате
        contacts_dict[full_name][5] = format_phone(contact[5])
        # Обновляем email (оставляем последний встреченный)
        contacts_dict[full_name][6] = contact[6]
    else:
        # Если такого контакта нет, добавляем его в словарь
        contacts_dict[full_name] = contact
        # Форматируем телефон
        contacts_dict[full_name][5] = format_phone(contact[5])

# Преобразуем словарь обратно в список для записи в файл
contacts_list = list(contacts_dict.values())

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)

