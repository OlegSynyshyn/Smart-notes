from PyQt5.QtWidgets import QApplication, QTextEdit, QListWidget, QTextEdit, QWidget, QPushButton, QLineEdit, QListWidget, QHBoxLayout, QVBoxLayout
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



















window.show()
app.exec_()