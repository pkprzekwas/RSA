# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from generator import KeyGenerator

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Form(QtGui.QWidget):
    """
    Project resources:
    https://www.youtube.com/watch?v=qfgYfyyBRcY
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    http://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python:_Probably_correct_answers
    https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
    https://en.wikipedia.org/wiki/Modular_exponentiation
    https://en.wikipedia.org/wiki/RSA_(cryptosystem)
    """

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.key_gen = KeyGenerator(8**37, 8**38, 50)

    def setupUi(self, Form):
        """
        Building form.
        :param Form: form
        :return: Built form
        """
        Form.setObjectName(_fromUtf8("RSA Key Generator"))
        Form.resize(827, 737)

        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.title = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.title.setFont(font)
        self.title.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setFrameShape(QtGui.QFrame.NoFrame)
        self.title.setTextFormat(QtCore.Qt.AutoText)
        self.title.setScaledContents(False)
        self.title.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.title.setIndent(-4)
        self.title.setObjectName(_fromUtf8("title"))
        self.verticalLayout.addWidget(self.title)

        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(40)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))

        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.generatorKey_btn = QtGui.QPushButton(Form)
        self.generatorKey_btn.setIconSize(QtCore.QSize(24, 24))
        self.generatorKey_btn.setAutoRepeatDelay(300)
        self.generatorKey_btn.setObjectName(_fromUtf8("generatorKey_btn"))
        self.horizontalLayout_4.addWidget(self.generatorKey_btn)

        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))

        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)

        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_3.addWidget(self.lineEdit)

        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)

        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout_3.addWidget(self.lineEdit_2)

        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)

        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.verticalLayout_3.addWidget(self.lineEdit_3)

        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.line_4 = QtGui.QFrame(Form)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout.addWidget(self.line_4)

        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)

        self.message = QtGui.QTextEdit(Form)
        self.message.setObjectName(_fromUtf8("message"))
        self.verticalLayout.addWidget(self.message)

        self.encrypt_btn = QtGui.QPushButton(Form)
        self.encrypt_btn.setObjectName(_fromUtf8("encrypt_btn"))
        self.verticalLayout.addWidget(self.encrypt_btn)

        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)

        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)

        self.encrypted_message = QtGui.QTextEdit(Form)
        self.encrypted_message.setObjectName(_fromUtf8("encrypted_message"))
        self.verticalLayout.addWidget(self.encrypted_message)

        self.decrypt_btn = QtGui.QPushButton(Form)
        self.decrypt_btn.setObjectName(_fromUtf8("decrypt_btn"))
        self.verticalLayout.addWidget(self.decrypt_btn)

        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)

        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)

        self.decrypted_message = QtGui.QTextEdit(Form)
        self.decrypted_message.setObjectName(_fromUtf8("decrypted_message"))
        self.verticalLayout.addWidget(self.decrypted_message)

        self.author = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.author.setFont(font)
        self.author.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.author.setObjectName(_fromUtf8("author"))
        self.verticalLayout.addWidget(self.author)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """
        Filling form with values and buttons management.
        :param Form: form
        :return: Filled form.
        """
        Form.setWindowTitle(_translate("RSA Key Generator", "RSA Key Generator", None))
        self.title.setText(_translate("RSA Key Generator", "Projekt WNO semestr 5 - RSA Key Generator", None))
        self.generatorKey_btn.setText(_translate("Form", "Generate Keys", None))
        self.generatorKey_btn.clicked.connect(self.generate)

        self.label.setText(_translate("Form", "Modulus:", None))
        self.label_2.setText(_translate("Form", "Private Key:", None))
        self.label_3.setText(_translate("Form", "Public Key:", None))
        self.label_4.setText(_translate("Form", "Your message:", None))

        self.encrypt_btn.setText(_translate("Form", "Encrypt your message", None))
        self.encrypt_btn.clicked.connect(self.get_message)

        self.label_5.setText(_translate("Form", "Encrypted message:", None))

        self.decrypt_btn.setText(_translate("Form", "Decrypt your message", None))
        self.decrypt_btn.clicked.connect(self.decrypt_message)

        self.label_6.setText(_translate("Form", "Decrypted message:", None))

        self.author.setText(_translate("Form", "© Patryk Przekwas", None))

    def generate(self):
        """
        Button handling. Generates encrypted message form keys and message.
        :return:
        """
        self.n, self.e, self.d = self.key_gen.generate_keys()
        self.lineEdit.setText(str(self.n))
        self.lineEdit_2.setText(str(self.e))
        self.lineEdit_3.setText(str(self.d))

    def get_message(self):
        try:
            message = unicode(self.message.toPlainText())
            self.n = long(self.lineEdit.text())
            self.e = long(self.lineEdit_3.text())
            encrypted_msg = self.key_gen.encrypt(message, self.n, self.e)
            self.encrypted_message.setText(unicode(encrypted_msg))
        except:
             QtGui.QMessageBox.about(self, 'Message', "Failed. Check your public key.")

    def decrypt_message(self):
        """
        Button handling. Decryptes encrypted message.
        :return:
        """
        try:
            message = (self.encrypted_message.toPlainText())
            message = self.clear_message(message)

            self.n = long(self.lineEdit.text())
            self.d = long(self.lineEdit_2.text())

            decrypted_msg = self.key_gen.decrypt(message, self.n, self.d)
            self.decrypted_message.setText(decrypted_msg)
        except:
            QtGui.QMessageBox.about(self, 'Message', "Failed. Check your private key.")

    @staticmethod
    def clear_message(message):
        """
        Removes unneeded signs from our message.
        :param message:
        :return:
        """
        message = message.split(',')
        message[0] = message[0][1:]
        message[-1] = message[-1][:-1]
        return [long(number) for number in message]


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())
