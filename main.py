from PyQt5.QtWidgets import (QApplication, 
QTextEdit, QListWidget, QTextEdit, QWidget, 
QPushButton, QLineEdit, QListWidget, QHBoxLayout, 
QVBoxLayout, QInputDialog)
import json
app = QApplication([])
window = QWidget()

text = QTextEdit()
add_teg = QLineEdit()
notes_list = QListWidget()
line_list = QLineEdit()
tags_list = QListWidget()


main_line = QHBoxLayout()
line1 = QVBoxLayout()
line2 = QVBoxLayout()

create_note_btn = QPushButton("Створити замітку")
remove_note_btn = QPushButton("Видалити замітку")
save_note_btn = QPushButton("Зберегти замітку")
add_teg_btn = QPushButton("Додати до замітки")
unpin_teg_btn = QPushButton("Відкріпити від замітки")
search_teg_btn = QPushButton("Шукати замітки по тегу")



main_line.addLayout(line1)
main_line.addLayout(line2)

window.setLayout(main_line)


line1.addWidget(text)
line2.addWidget(notes_list)
line2.addWidget(create_note_btn)
line2.addWidget(remove_note_btn)
line2.addWidget(save_note_btn)
line2.addWidget(tags_list)
line2.addWidget(add_teg)
line2.addWidget(add_teg_btn)
line2.addWidget(unpin_teg_btn)
line2.addWidget(search_teg_btn)

notes = {}


def writeFile():
    with open("notes.json", "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=True, sort_keys=True, indent=4)



main_line.addLayout(line1, stretch=2)
main_line.addLayout(line2, stretch=1)
window.setLayout(main_line)


def show_note():
    note_name = notes_list.currentItem().text()
    print(notes)
    text.setText(notes[note_name]['text'])
    tags_list.clear()
    tags_list.addItems(notes[note_name]['tags'])
notes_list.itemClicked.connect(show_note)
notes_list.addItems(notes)


def add_tag():
    note_name = notes_list.currentItem().text()
    tag = add_teg.text()
    
    notes[note_name]["tags"].append(tag)
    tags_list.addItem(tag)
    writeFile()
    
add_teg_btn.clicked.connect(add_tag)


def add_note():
    note_name, ok = QInputDialog.getText(window, "Нова замітка", "Введіть назву замітки")
    if ok and note_name != "":
        notes[note_name] = {
            "text": "", 
            "tags": [],
        }
        notes_list.addItem(note_name)
create_note_btn.clicked.connect(add_note)


with open("notes.json", "r", encoding="utf-8") as file:
    notes = json.load(file)

notes_list.addItems(notes)
def search_by_tag():
    note_name = notes_list.currentItem().text()
    tag = add_teg.text()
    text.setText(notes[note_name]['text'])
def dell_tag():
    note_name = notes_list.currentItem().text()
    tag_name = tags_list.currentItem().text()
    notes[note_name]['tags'].remove(tag_name)
    tags_list.clear()
    tags_list.addItems(notes[note_name]["tags"])
    writeFile()
unpin_teg_btn.clicked.connect(dell_tag)


def dell_note():
    note_name = notes_list.currentItem().text()
    del notes[note_name]
    notes_list.takeItem(notes_list.currentRow())
    text.clear()
    writeFile()
remove_note_btn.clicked.connect(dell_note)


def save_note():
    note_text = text.toPlainText()
    note_name = notes_list.currentItem().text()
    notes[note_name]['text'] = note_text
    writeFile()
save_note_btn.clicked.connect(save_note)


window.show()
app.exec_()