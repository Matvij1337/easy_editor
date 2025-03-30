from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QApplication, QWidget, QFileDialog)
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter
import os

app = QApplication([])
from design import design
app.setStyleSheet(design)
from interface import *

workdir = ''

def open_folder():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, ext):
    filtered = []
    for file in files:
        for e in ext:
            if file.endswith(e):
                filtered.append(file)
    return filtered

def get_files():
    open_folder()
    ext = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
    files = filter(os.listdir(workdir), ext)
    list_for_file.clear()
    list_for_file.addItems(files)

class ImageProcessor():
    def __init__(self):
        self.image  = None
        self.dir  = None
        self.filename  = None
        self.save_dir = "Modified/"

    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_rigth(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    def do_sharp(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_binary(self):
        self.image = self.image.convert("1")
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_back(self):
        image_path = os.path.join(self.dir, self.filename)
        self.showImage(image_path)


    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def showImage(self, path):
        lbl_pictures.hide()
        pixmapimage = QPixmap(path)
        w, h = lbl_pictures.width(), lbl_pictures.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lbl_pictures.setPixmap(pixmapimage)
        lbl_pictures.show()

def showChosenImage():
    if list_for_file.currentRow() >= 0:
        filename = list_for_file.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)
        
list_for_file.currentRowChanged.connect(showChosenImage)
btn_files.clicked.connect(get_files)
workimage = ImageProcessor()
btn_black_white.clicked.connect(workimage.do_bw)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_rigth)
btn_sharp.clicked.connect(workimage.do_sharp)
btn_to_mirror.clicked.connect(workimage.do_mirror)
btn_blur.clicked.connect(workimage.do_blur)
btn_pixel.clicked.connect(workimage.do_binary)
btn_back.clicked.connect(workimage.do_back)
window.show()
app.exec_()
