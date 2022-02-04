from pydoc import plain
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
    spacefive = True

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
        self.spacefive = True

    def displaySpaceFive(self):
        while self.spacefive:
            modifiedString = readMode.spaceFive(self.ciphertext.toPlainText())
            self.ciphertext.setText(modifiedString)
            self.spacefive = False

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
    
    def decrypting(self):
        cipher = self.ciphertext.toPlainText()
        key = self.key.toPlainText()

        plain = playfairCipher.decryptTextPFC(cipher, key)

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
    spaceFive = True
    def __init__(self):
        super(vigenereCipherExtEnc, self).__init__()
        loadUi("vigenereCipherExtEnc.ui", self)
        self.menu.clicked.connect(self.gotoMenu)
        self.decrypt.clicked.connect(self.gotoVigenereExtDec)
        self.encrypt.clicked.connect(self.encrypting)
        self.savecipher.clicked.connect(self.saveCipher)
        self.nospace.clicked.connect(self.displayNoSpace)
        self.space5.clicked.connect(self.displaySpaceFive)
    
    def encrypting(self):
        plaintext = self.plaintext.toPlainText()
        key = self.key.toPlainText()

        cipherKey = extendedVigenereCipher.generateKeyExtendedVige(plaintext, key)
        extendedVigenereCipher.saveKey(cipherKey)
        encryptedString = extendedVigenereCipher.encryptTextExtendedVige(plaintext, cipherKey)

        self.ciphertext.setText(encryptedString)        

    def saveCipher(self):
        ciphertext = self.ciphertext.toPlainText()
        extendedVigenereCipher.saveCipher(ciphertext)

    def displayNoSpace(self):
        modifiedString = readMode.noSpaceDiff(self.ciphertext.toPlainText())
        self.ciphertext.setText(modifiedString)
        self.spacefive = True

    def displaySpaceFive(self):
        while self.spacefive:
            modifiedString = readMode.spaceFive(self.ciphertext.toPlainText())
            self.ciphertext.setText(modifiedString)
            self.spacefive = False

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
        self.decrypt.clicked.connect(self.decrypting)
    
    def decrypting(self):
        cipher = self.ciphertext.toPlainText()
        key = self.key.toPlainText()
        generatedKey = extendedVigenereCipher.generateKeyExtendedVige(cipher, key)

        plain = extendedVigenereCipher.decryptTextExtendedVige(cipher,generatedKey)

        self.plaintext.setText(plain)

    def gotoMenu(self):
        menu = menuScreen()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoVigenereExtEnc(self):
        vigenereExtDec = vigenereCipherExtEnc()
        widget.addWidget(vigenereExtDec)
        widget.setCurrentIndex(widget.currentIndex()+1)

class vigenereCipherEnc(QDialog):
    spacefive = True

    def __init__(self):
        super(vigenereCipherEnc, self).__init__()
        loadUi("vigenereCipherEnc.ui", self)
        self.menu.clicked.connect(self.gotoMenu)
        self.decrypt.clicked.connect(self.gotoVigenereDec)
        self.encrypt.clicked.connect(self.encrypting)
        self.savecipher.clicked.connect(self.saveCipher)
        self.nospace.clicked.connect(self.displayNoSpace)
        self.space5.clicked.connect(self.displaySpaceFive)
    
    def encrypting(self):
        plaintext = self.plaintext.toPlainText()
        key = self.key.toPlainText()

        cipherKey = vigenereCipher.generateKeyVige(plaintext, key)
        vigenereCipher.saveKey(cipherKey)
        encryptedString = vigenereCipher.encryptTextVige(plaintext, cipherKey)

        self.ciphertext.setText(encryptedString)

        vigenereCipher.saveMemory(encryptedString)
        
    def saveCipher(self):
        ciphertext = self.ciphertext.toPlainText()
        vigenereCipher.saveCipher(ciphertext)

    def displayNoSpace(self):
        modifiedString = readMode.noSpace(self.ciphertext.toPlainText())
        self.ciphertext.setText(modifiedString)
        self.spacefive = True

    def displaySpaceFive(self):
        while self.spacefive:
            modifiedString = readMode.spaceFive(self.ciphertext.toPlainText())
            self.ciphertext.setText(modifiedString)
            self.spacefive = False
    
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
        self.decrypt.clicked.connect(self.decrypting)
        # cipher = vigenereCipher.readMemory()
        # key = vigenereCipher.readKey()
        # self.ciphertext.setText(cipher)
        # self.key.setText(key)
    
    def decrypting(self):
        cipher = self.ciphertext.toPlainText()
        key = self.key.toPlainText()
        generatedKey = vigenereCipher.generateKeyVige(cipher, key)

        plain = vigenereCipher.decryptTextVige(cipher,generatedKey)

        self.plaintext.setText(plain)
    
    def gotoMenu(self):
        menu = menuScreen()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoVigenereEnc(self):
        vigenereDec = vigenereCipherEnc()
        widget.addWidget(vigenereDec)
        widget.setCurrentIndex(widget.currentIndex()+1)

class OTPEnc(QDialog):
    spacefive = True
    

    def __init__(self):
        super(OTPEnc, self).__init__()
        loadUi("OTPEnc.ui", self)
        self.menu.clicked.connect(self.gotoMenu)
        self.decrypt.clicked.connect(self.gotoOTPDec)
        self.encrypt.clicked.connect(self.encrypting)
        self.savecipher.clicked.connect(self.saveCipher)
        self.nospace.clicked.connect(self.displayNoSpace)
        oneTimePad.createKeyOTP()
        key = oneTimePad.getKeyOTP()

        self.key.setText(key)
        self.space5.clicked.connect(self.displaySpaceFive)
    
    def encrypting(self):
        plaintext = self.plaintext.toPlainText()
        key = self.key.toPlainText()

        oneTimePad.saveKey(key)
        encryptedString = oneTimePad.encryptTextOTP(plaintext, key)

        self.ciphertext.setText(encryptedString)

        oneTimePad.saveMemory(encryptedString)
        
    def saveCipher(self):
        ciphertext = self.ciphertext.toPlainText()
        oneTimePad.saveCipher(ciphertext)

    def displayNoSpace(self):
        modifiedString = readMode.noSpace(self.ciphertext.toPlainText())
        self.ciphertext.setText(modifiedString)
        self.spacefive = True

    def displaySpaceFive(self):
        while self.spacefive:
            modifiedString = readMode.spaceFive(self.ciphertext.toPlainText())
            self.ciphertext.setText(modifiedString)
            self.spacefive = False
    
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
        self.decrypt.clicked.connect(self.decrypting)
        # cipher = oneTimePad.readMemory()
        key = oneTimePad.readKey()
        # self.ciphertext.setText(cipher)
        self.key.setText(key)
    
    def decrypting(self):
        cipher = self.ciphertext.toPlainText()
        key = self.key.toPlainText()
        
        plain = oneTimePad.decryptTextOTP(cipher, key)

        self.plaintext.setText(plain)
    
    def gotoMenu(self):
        menu = menuScreen()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoOTPEnc(self):
        OTPEncr = OTPEnc()
        widget.addWidget(OTPEncr)
        widget.setCurrentIndex(widget.currentIndex()+1)

class enigmaCipherEnc(QDialog):
    spacefive = True

    def __init__(self):
        super(enigmaCipherEnc, self).__init__()
        loadUi("enigmaCipherEnc.ui", self)
        self.menu.clicked.connect(self.gotoMenu)
        self.decrypt.clicked.connect(self.gotoEnigmaDec)
        self.encrypt.clicked.connect(self.encrypting)
        self.savecipher_2.clicked.connect(self.saveCipher)
        self.nospace_2.clicked.connect(self.displayNoSpace)
        self.space5_2.clicked.connect(self.displaySpaceFive)

    def encrypting(self):
        reflector = self.reflector.currentText()
        rotor_1 = self.rotor_1.currentText()
        rotor_2 = self.rotor_2.currentText()
        rotor_3 = self.rotor_3.currentText()
        ring_1 = self.ring_1.currentText()
        ring_2 = self.ring_2.currentText()
        ring_3 = self.ring_3.currentText()
        init_1 = self.init_1.currentText()
        init_2 = self.init_2.currentText()
        init_3 = self.init_3.currentText()

        wheelOrder = rotor_1 + " " + rotor_2 + " " + rotor_3
        ringSettings = [int(ring_1), int(ring_2), int(ring_3)]
        initPosition = init_1 + init_2 + init_3

        plaintext = self.plaintext.toPlainText()

        machine = enigmaCipher.initEnigma(wheelOrder, ringSettings, reflector, 'AV BS CG DL FU HZ IN KM OW RX')

        ciphertext = enigmaCipher.enigma(machine, initPosition, 'KCH', plaintext)

        self.ciphertext.setText(ciphertext)
        
    def saveCipher(self):
        ciphertext = self.ciphertext.toPlainText()
        enigmaCipher.saveEncryption(ciphertext)

    def displayNoSpace(self):
        modifiedString = readMode.noSpace(self.ciphertext.toPlainText())
        self.ciphertext.setText(modifiedString)
        self.spacefive = True

    def displaySpaceFive(self):
        while self.spacefive:
            modifiedString = readMode.spaceFive(self.ciphertext.toPlainText())
            self.ciphertext.setText(modifiedString)
            self.spacefive = False


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
        self.decrypt.clicked.connect(self.decrypting)

    def decrypting(self):
        reflector = self.reflector.currentText()
        rotor_1 = self.rotor_1.currentText()
        rotor_2 = self.rotor_2.currentText()
        rotor_3 = self.rotor_3.currentText()
        ring_1 = self.ring_1.currentText()
        ring_2 = self.ring_2.currentText()
        ring_3 = self.ring_3.currentText()
        init_1 = self.init_1.currentText()
        init_2 = self.init_2.currentText()
        init_3 = self.init_3.currentText()

        wheelOrder = rotor_1 + " " + rotor_2 + " " + rotor_3
        ringSettings = [int(ring_1), int(ring_2), int(ring_3)]
        initPosition = init_1 + init_2 + init_3

        ciphertext = self.ciphertext.toPlainText()

        machine = enigmaCipher.initEnigma(wheelOrder, ringSettings, reflector, 'AV BS CG DL FU HZ IN KM OW RX')

        plaintext = enigmaCipher.enigma(machine, initPosition, 'KCH', ciphertext)

        self.plaintext.setText(plaintext)
    
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