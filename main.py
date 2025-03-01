from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout

import json

notes = {
    "Ілля Сидорчук": {
        "текст": "Хороший хлопчик", 
        "теги": "сміхотунчик"
    }
}

with open("notes_data.json", "w") as file:
    json.dump(notes, file)

app = QApplication([])

notes_win = QWidget()
notes_win.setWindowTitle('Розумні замітки')
notes_win.resize(900, 600)

list_notes = QListWidget()
list_notes_label = QLabel('Список заміток')
button_note_create = QPushButton('Створити замітку') # з'являється вікно з полем "Введіть ім'я замітки"
button_note_del = QPushButton('Видалити замітку')
button_note_save = QPushButton('Зберегти замітку')
field_text = QTextEdit()

'''
field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введіть тег...')
field_text = QTextEdit()
button_tag_add = QPushButton('Додати до замітки')
button_tag_del = QPushButton('Відкріпити від замітки')
button_tag_search = QPushButton('Шукати замітки за тегом')
list_tags = QListWidget()
list_tag_label = QLabel('Список тегів')
'''

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)


col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)

#col_2.addWidget(list_tag_label)
#col_2.addWidget(list_tags)
#col_2.addWidget(field_tag)


row_3 = QHBoxLayout()
#row_3.addWidget(button_tag_add)
#row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
#row_4.addWidget(button_tag_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)

def add_note():
    note_mane, ok = QInputDialog.getText(notes_win, "Додати замітку", "Назва замітки:")
    if ok and note_mane != '':
        notes[note_mane] = {"текст": ""}
        list_notes.addItem(note_mane)
        #list_tags.addItems(notes[note_mane]["теги"])
        print(notes)

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["текст"])
    #list_tags.clear()
    #list_tags.addItems(notes[key]["теги"])

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["текст"] = field_text.toPlainText()
        with open('notes_data.json', 'w') as file:
            json.dump(notes,file, sort_keys = True, ensure_ascii = False)
        print(notes)
    else:
        print('Замітка для збереження не вибрана!')

def note_del():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open('notes_data.json', 'w') as file:
            json.dump(notes,file, sort_keys = True, ensure_ascii = False)
        print(notes)
    else:
        print('Замітка для вилучення не обрана!')

'''
def add_tag():
    if list_notes.selectedItems():
        key = layout_notes.selectedItems()[0].text()
        #tag = field_tag.text()
        if not tag in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            #list_tags.addItem(tag)
            #field_tag.clear
        with open('notes_data.json', "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Замітка для додавання тега не обрана!")

def del_tag():
    if list_tags.seLectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]["теги"])
        with open("notes_data.json", "w") as file:
            json.dump(notes,file, sort_keys=True, ensure_ascii=False)
    else:
        print("Теги для вилучення не обраний!")

def search_tag():
    print(button_tag_search.text())
    tag = field_tag.text()
    if button_tag_search.text()=='Шукати замітку по тегу'and tag:
        print(tag)
        note_filtered = {}
        for note in notes:
            if tag in notes[note]['теги']:
                note_filtered[note] = notes[note]
        button_tag_search.setText('Скинути пошук')
        list_notes.clear()
        list_tags.clear()
        list_notes.addItem(note_filtered)
        print(button_tag_search.text())
    elif button_tag_search.text()== 'Скинути пошук': 
        field_tag.clear()
        list_notes.clear()
        list_text.clear()
        list_notes.addItems(notes)
        button_tag_search.setText("Шукати замітку по тегу")
        print(button_tag_search.text())
    else:
        pass
'''


button_note_create.clicked.connect(add_note)
list_notes.itemClicked.connect(show_note)
button_note_save.clicked.connect(save_note)
button_note_del.clicked.connect(note_del)
#button_tag_add.clicked.connect(add_tag)
#button_tag_del.clicked.connect(del_tag)
#button_tag_search.clicked.connect(search_tag)




with open('notes_data.json', 'r') as file:
    notes = json.load(file)
list_notes.addItems(notes)

notes_win.show()
app.exec_()
