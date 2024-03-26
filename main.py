from pprint import pprint
import re
import csv

def format_phone(phone):
    phone = re.sub(r'(\+7|8)?[\s\(\-\)]*(\d{3})[\s\-\)]*(\d{3})[\s\-\)]*(\d{2})[\s\-]*(\d{2})[\s\-]*доб\.?\s*(\d+)?', r'+7(\2)\3-\4-\5 доб.\6', phone)
    return phone

def extract_name(name):
    name = name.split()
    if len(name) == 1:
        return [name[0], '', '']
    elif len(name) == 2:
        return [name[0], name[1], '']
    else:
        return [name[0], name[1], name[2]]

def process_contacts(contacts_list):
    unique_contacts = {}
    for contact in contacts_list:
        full_name = ' '.join(contact[:3])
        if full_name in unique_contacts:
            for i in range(len(contact)):
                if unique_contacts[full_name][i] == '':
                    unique_contacts[full_name][i] = contact[i]
        else:
            unique_contacts[full_name] = contact

    new_contacts_list = [values for values in unique_contacts.values()]
    return new_contacts_list

# читаем адресную книгу в формате CSV в список contacts_list

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# приводим телефоны к нужному формату

for contact in contacts_list:
    contact[5] = format_phone(contact[5])

# преобразуем фамилию, имя и отчество

for contact in contacts_list:
    contact[:3] = extract_name(contact[0])

new_contacts_list = process_contacts(contacts_list)

# сохраняем получившиеся данные в другой файл

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts_list)
