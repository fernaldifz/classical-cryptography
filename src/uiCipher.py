import sys
import playfairCipher, vigenereCipher, extendedVigenereCipher, enigmaCipher, oneTimePad, readMode
from os import curdir, environ
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QTabWidget, QWidget, QMessageBox, QPushButton, QFileDialog, QVBoxLayout



class menuScreen(QDialog):
    def __init__(self):
        super(menuScreen, self).__init__()
        loadUi("menu.ui", self)
        self.playfair.clicked.connect(self.gotoPlayfair)
        self.vigenere.clicked.connect(self.gotoVigenere)
        self.vigenere_ext.clicked.connect(self.gotoVigenereExt)
        self.one_time_pad.clicked.connect(self.gotoOTPEnc)
        self.enigma.clicked.connect(self.gotoEnigma)
    
    def gotoPlayfair(self):
        playfairEnc = playfairCipherEnc()
        widget.addWidget(playfairEnc)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoVigenere(self):
        vigenereEnc = vigenereCipherEnc()
        widget.addWidget(vigenereEnc)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoVigenereExt(self):
        vigenereExtEnc = vigenereCipherExtEnc()
        widget.addWidget(vigenereExtEnc)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoOTPEnc(self):
        OTPEncr = OTPEnc()
        widget.addWidget(OTPEncr)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoEnigma(self):
        enigmaEnc = enigmaCipherEnc()
        widget.addWidget(enigmaEnc)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
class playfairCipherEnc(QDialog):
    def __init__(self):
        super(playfairCipherEnc, self).__init__()
        loadUi("playfairCipherEnc.ui", self)
        self.menu.clicked.connect(self.gotoMenu)
        self.decrypt.clicked.connect(self.gotoPFCDecrypt)
        self.encrypt.clicked.connect(self.encrypting)
        self.savecipher.clicked.connect(self.saveCipher)
        self.nospace.clicked.connect(self.displayNoSpace)
        self.space5.clicked.connect(self.displaySpaceFive)

    
    def encrypting(self):
        plaintext = self.plaintext.toPlainText()
        key = self.key.toPlainText()

        newPlaintext, jMemory = playfairCipher.encryptTextPFC(plaintext, key)
        cipher = playfairCipher.toText(newPlaintext)

        self.ciphertext.setText(cipher)

        playfairCipher.toFileTXT(cipher, jMemory)

    def saveCipher(self):
        playfairCipher.saveCiphertext(self.ciphertext.toPlainText())

    def displayNoSpace(self):
        modifiedString = readMode.noSpace(self.ciphertext.toPlainText())
        self.ciphertext.setText(modifiedString)

    def displaySpaceFive(self):
        modifiedString = readMode.spaceFive(self.ciphertext.toPlainText())
        self.ciphertext.setText(modifiedString)

    def gotoMenu(self):
        menu = menuScreen()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoPFCDecrypt(self):
        playfairDec = playfairCipherDec()
        widget.addWidget(playfairDec)
        widget.setCurrentIndex(widget.currentIndex()+1)

class playfairCipherDec(QDialog):
    def __init__(self):
        super(playfairCipherDec, self).__init__()
        loadUi("playfairCipherDec.ui", self)
        self.menu.clicked.connect(self.gotoMenu)
        self.encrypt.clicked.connect(self.gotoPFCEncrypt)
        self.decrypt.clicked.connect(self.decrypting)
        self.autodecrypt.clicked.connect(self.autoDecrypting)
    
    def autoDecrypting(self):
        self.ciphertext.setText(playfairCipher.readCipher())
        key = self.key.toPlainText()

        plain = playfairCipher.decryptTextPFC(key)

        self.plaintext.setText(plain)

    def decrypting(self):
        cipher = self.ciphertext.toPlainText()
        key = self.key.toPlainText()

        plain = playfairCipher.decryptTextPFCDiff(cipher, key)

        self.plaintext.setText(plain)

    def gotoMenu(self):
        menu = menuScreen()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoPFCEncrypt(self):
        playfairEnc = playfairCipherEnc()
        widget.addWidget(playfairEnc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class vigenereCipherExtEnc(QDialog):
    def __init__(self):
        super(vigenereCipherExtEnc, self).__init__()
        loadUi("vigenereCipherExtEnc.ui", self)
        self.menu.clicked.connect(self.gotoMenu)
        self.decrypt.clicked.connect(self.gotoVigenereExtDec)
    
    def gotoMenu(self):
        menu = menuScreen()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoVigenereExtDec(self):
        vigenereExtDec = vigenereCipherExtDec()
        widget.addWidget(vigenereExtDec)
        widget.setCurrentIndex(widget.currentIndex()+1)

class vigenereCipherExtDec(QDialog):
    def __init__(self):
        super(vigenereCipherExtDec, self).__init__()
        loadUi("vigenereCipherExtDec.ui", self)
        self.menu.clicked.connect(self.gotoMenu)
        self.encrypt.clicked.connect(self.gotoVigenereExtEnc)
    
    def gotoMenu(self):
        menu = menuScreen()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoVigenereExtEnc(self):
        vigenereExtDec = vigenereCipherExtEnc()
        widget.addWidget(vigenereExtDec)
        widget.setCurrentIndex(widget.currentIndex()+1)

class vigenereCipherEnc(QDialog):
    def __init__(self):
        super(vigenereCipherEnc, self).__init__()
        loadUi("vigenereCipherEnc.ui", self)
        self.menu.clicked.connect(self.gotoMenu)
        self.decrypt.clicked.connect(self.gotoVigenereDec)
    
    def gotoMenu(self):
        menu = menuScreen()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoVigenereDec(self):
        vigenereDec = vigenereCipherDec()
        widget.addWidget(vigenereDec)
        widget.setCurrentIndex(widget.currentIndex()+1)

class vigenereCipherDec(QDialog):
    def __init__(self):
        super(vigenereCipherDec, self).__init__()
        loadUi("vigenereCipherDec.ui", self)
        self.menu.clicked.connect(self.gotoMenu)
        self.encrypt.clicked.connect(self.gotoVigenereEnc)
    
    def gotoMenu(self):
        menu = menuScreen()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoVigenereEnc(self):
        vigenereDec = vigenereCipherEnc()
        widget.addWidget(vigenereDec)
        widget.setCurrentIndex(widget.currentIndex()+1)

class OTPEnc(QDialog):
    def __init__(self):
        super(OTPEnc, self).__init__()
        loadUi("OTPEnc.ui", self)
        self.menu.clicked.connect(self.gotoMenu)
        self.decrypt.clicked.connect(self.gotoOTPDec)
    
    def gotoMenu(self):
        menu = menuScreen()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoOTPDec(self):
        OTPDecr = OTPDec()
        widget.addWidget(OTPDecr)
        widget.setCurrentIndex(widget.currentIndex()+1)

class OTPDec(QDialog):
    def __init__(self):
        super(OTPDec, self).__init__()
        loadUi("OTPDec.ui", self)
        self.menu.clicked.connect(self.gotoMenu)
        self.encrypt.clicked.connect(self.gotoOTPEnc)
    
    def gotoMenu(self):
        menu = menuScreen()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoOTPEnc(self):
        OTPEncr = OTPEnc()
        widget.addWidget(OTPEncr)
        widget.setCurrentIndex(widget.currentIndex()+1)

class enigmaCipherEnc(QDialog):
    def __init__(self):
        super(enigmaCipherEnc, self).__init__()
        loadUi("enigmaCipherEnc.ui", self)
        self.menu.clicked.connect(self.gotoMenu)
        self.decrypt.clicked.connect(self.gotoEnigmaDec)
    
    def gotoMenu(self):
        menu = menuScreen()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoEnigmaDec(self):
        enigmaDec = enigmaCipherDec()
        widget.addWidget(enigmaDec)
        widget.setCurrentIndex(widget.currentIndex()+1)

class enigmaCipherDec(QDialog):
    def __init__(self):
        super(enigmaCipherDec, self).__init__()
        loadUi("enigmaCipherDec.ui", self)
        self.menu.clicked.connect(self.gotoMenu)
        self.encrypt.clicked.connect(self.gotoEnigmaEnc)
    
    def gotoMenu(self):
        menu = menuScreen()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoEnigmaEnc(self):
        enigmaEnc = enigmaCipherEnc()
        widget.addWidget(enigmaEnc)
        widget.setCurrentIndex(widget.currentIndex()+1)

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

def run():
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")

def run():
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")

suppress_qt_warnings()
app = QApplication(sys.argv)
menu = menuScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(menu)
widget.setFixedHeight(512)
widget.setFixedWidth(720)
run()