from pprint import pprint
import re

# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# приводим телефоны к нужному формату
for contact in contacts_list:
    phone = contact[5]
    phone = re.sub(r'(\+7|8)?[\s\(\-\)]*(\d{3})[\s\-\)]*(\d{3})[\s\-\)]*(\d{2})[\s\-]*(\d{2})[\s\-]*доб\.?\s*(\d+)?', r'+7(\2)\3-\4-\5 доб.\6', phone)
    contact[5] = phone

# объединяем дублирующиеся записи по ФИ
new_contacts_list = []
for contact in contacts_list:
    if contact not in new_contacts_list:
        new_contacts_list.append(contact)
    else:
        index = new_contacts_list.index(contact)
        for i in range(len(contact)):
            if new_contacts_list[index][i] == '':
                new_contacts_list[index][i] = contact[i]

# преобразуем ФИО в Ф, И, О
for contact in new_contacts_list:
    fullname = contact[0].split()
    if len(fullname) == 1:
        contact.insert(1, '')
        contact.insert(2, '')
    elif len(fullname) == 2:
        contact[0] = fullname[0]
        contact.insert(1, fullname[1])
        contact.insert(2, '')
    else:
        contact[0] = fullname[0]
        contact[1] = fullname[1]
        contact[2] = fullname[2]

# сохраняем получившиеся данные в другой файл
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts_list)
