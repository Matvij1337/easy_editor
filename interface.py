from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QLabel, QListWidget, QPushButton, QWidget)

window = QWidget()
window.resize(800, 600)
window.setWindowTitle("Easy Editor")

btn_files = QPushButton("Папки")

list_for_file = QListWidget()

lbl_pictures = QLabel("Картинка")

btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_to_mirror = QPushButton("Відзеркалити")
btn_sharp = QPushButton("Різкість")
btn_black_white = QPushButton("Ч/Б")
btn_blur = QPushButton("Розмитя")
btn_pixel = QPushButton("Двійковий")
btn_back = QPushButton("Повернути")

h1 = QHBoxLayout()
h1.addWidget(btn_left)
h1.addWidget(btn_right)
h1.addWidget(btn_to_mirror)
h1.addWidget(btn_sharp)
h1.addWidget(btn_black_white)
h1.addWidget(btn_blur)
h1.addWidget(btn_pixel)
h1.addWidget(btn_back)

v1 = QVBoxLayout()
v1.addWidget(btn_files)
v1.addWidget(list_for_file)

v2 = QVBoxLayout()
v2.addWidget(lbl_pictures)
v2.addLayout(h1)

h_main = QHBoxLayout()
h_main.addLayout(v1, 20)
h_main.addLayout(v2, 80)

window.setLayout(h_main)