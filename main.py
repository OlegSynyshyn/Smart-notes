from PyQt5.QtWidgets import (QApplication, 
QTextEdit, QListWidget, QTextEdit, QWidget, 
QPushButton, QLineEdit, QListWidget, QHBoxLayout, 
QVBoxLayout, QInputDialog, QMessageBox)
import json
app = QApplication([])
window = QWidget()
error_save = QMessageBox()
text = QTextEdit()
add_teg = QLineEdit()
notes_list = QListWidget()
line_list = QLineEdit()
tags_list = QListWidget()
main_line = QHBoxLayout()
line1 = QVBoxLayout()
line2 = QVBoxLayout()
window.setWindowTitle("Notes V1.2")
create_note_btn = QPushButton("Створити замітку")
remove_note_btn = QPushButton("Видалити замітку")
save_note_btn = QPushButton("Зберегти замітку")
add_teg_btn = QPushButton("Додати до замітки")
unpin_teg_btn = QPushButton("Відкріпити від замітки")
search_teg_btn = QPushButton("Шукати замітки по тегу")

text.setStyleSheet('''
background-color: #9bf542;
color: #8f0000                 
''')
notes_list.setStyleSheet('''
background-color: #8f0000;
color: #9bf542                 
''')
line_list.setStyleSheet('''
background-color: #9bf542;
color: #8f0000                 
''')
tags_list.setStyleSheet('''
background-color: #8f0000;
color: #9bf542                 
''')

add_teg.setStyleSheet('''
background-color: #9bf542;
color: #8f0000                 
''')

create_note_btn.setStyleSheet('''
background-color: #d9c82e;
color: #8f0000                 
''')

remove_note_btn.setStyleSheet('''
background-color: #d9c82e;
color: #8f0000                 
''')

save_note_btn.setStyleSheet('''
background-color: #d9c82e;
color: #8f0000                 
''')

add_teg_btn.setStyleSheet('''
background-color: #d9c82e;
color: #8f0000                 
''')

unpin_teg_btn.setStyleSheet('''
background-color: #d9c82e;
color: #8f0000                 
''')

search_teg_btn.setStyleSheet('''
background-color: #d9c82e;
color: #8f0000                 
''')




line1.addWidget(text)
line2.addWidget(notes_list)

h_line = QHBoxLayout()

h_line.addWidget(create_note_btn)
h_line.addWidget(remove_note_btn)

line2.addLayout(h_line)
line2.addWidget(save_note_btn)
line2.addWidget(tags_list)


line2.addWidget(add_teg)

h2_line = QHBoxLayout()
h2_line.addWidget(add_teg_btn)
h2_line.addWidget(unpin_teg_btn)
line2.addLayout(h2_line)
line2.addWidget(search_teg_btn)

main_line.addLayout(line1)
main_line.addLayout(line2)

window.setLayout(main_line)

notes = {}

try:
    with open("notes.json", "r", encoding="utf-8") as file:
        notes = json.load(file)
except:
    print("File not found")

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
    try:
        note_name = notes_list.currentItem().text()
        tag = add_teg.text()
        
        notes[note_name]["tags"].append(tag)
        tags_list.addItem(tag)
        writeFile()
    except:
        error_save.setWindowTitle("ERROR")
        error_save.setText("Виберіть нотатку для додавання тегу")
        
        error_save.exec_()
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


def search_by_tag():
    tag = add_teg.text()
    if(search_teg_btn.text()=="Шукати замітки по тегу"):
        filtered = {}
        
        for key in notes: 
            
            
            if tag in notes[key]['tags']:
            
                filtered[key] = notes[key]
                
        
        notes_list.clear()
        notes_list.addItems(filtered)
        tags_list.clear()
        line_list.clear()
        
        search_teg_btn.setText("Відмінити пошук")
    else:
        add_teg.clear()
        search_teg_btn.setText("Шукати замітки по тегу")
        notes_list.clear()
        notes_list.addItems(notes)
        tags_list.clear()
search_teg_btn.clicked.connect(search_by_tag)





def dell_tag():
    try: 
        note_name = notes_list.currentItem().text()
        tag_name = tags_list.currentItem().text()
        notes[note_name]['tags'].remove(tag_name)
        tags_list.clear()
        tags_list.addItems(notes[note_name]["tags"])
        writeFile()
    except:
        error_save.setWindowTitle("ERROR")
        error_save.setText("Виберіть нотатку для відкріплення тегу")
        
        error_save.exec_()
unpin_teg_btn.clicked.connect(dell_tag)


def dell_note():
    try:
        note_name = notes_list.currentItem().text()
        del notes[note_name]
        notes_list.takeItem(notes_list.currentRow())
        text.clear()
        writeFile()
    except:
        error_save.setWindowTitle("ERROR")
        error_save.setText("Виберіть нотатку для видалення")
        
        error_save.exec_()
remove_note_btn.clicked.connect(dell_note)


def save_note():
    try:
        note_text = text.toPlainText()
        
        note_name = notes_list.currentItem().text()

        notes[note_name]['text'] = note_text
        writeFile()
    except:
      

        error_save.setWindowTitle("ERROR")
        error_save.setText("Виберіть нотатку для збереження")
        
        error_save.exec_()
save_note_btn.clicked.connect(save_note)


window.show()
app.exec_()