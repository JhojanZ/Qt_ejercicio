# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget 
from PySide6.QtWidgets import QMessageBox


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.verificarCampos)

    def verificarCampos(self):
        # Suponiendo que tienes campos llamados campo1, campo2, etc.
        if (self.ui.plainTextEdit_1.toPlainText() and
            self.ui.plainTextEdit_2.toPlainText() and
            self.ui.plainTextEdit_3.toPlainText() and
            self.ui.plainTextEdit_4.toPlainText() and
            self.ui.plainTextEdit_5.toPlainText()):
            QMessageBox.information(self, "Éxito", "Todos los campos están completos.")
        else:
            QMessageBox.warning(self, "Error", "Faltan campos por completar.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
