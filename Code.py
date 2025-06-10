import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class Calculatrice(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculatrice.ui", self)

        self.boutonAjouter.clicked.connect(self.addition)
        self.boutonSoustraire.clicked.connect(self.soustraction)
        self.boutonMultiplier.clicked.connect(self.multiplication)
        self.boutonDiviser.clicked.connect(self.division)

    def addition(self):
        try:
            x = float(self.champX.text())
            y = float(self.champY.text())
            self.labelResultat.setText(str(x + y))
        except ValueError:
            QMessageBox.critical(self, "Erreur", "Veuillez entrer deux nombres valides.")
            self.champX.clear()
            self.champY.clear()
            self.labelResultat.clear()

    def soustraction(self):
        try:
            x = float(self.champX.text())
            y = float(self.champY.text())
            self.labelResultat.setText(str(x - y))
        except ValueError:
            QMessageBox.critical(self, "Erreur", "Veuillez entrer deux nombres valides.")
            self.champX.clear()
            self.champY.clear()
            self.labelResultat.clear()

    def multiplication(self):
        try:
            x = float(self.champX.text())
            y = float(self.champY.text())
            self.labelResultat.setText(str(x * y))
        except ValueError:
            QMessageBox.critical(self, "Erreur", "Veuillez entrer deux nombres valides.")
            self.champX.clear()
            self.champY.clear()
            self.labelResultat.clear()

    def division(self):
        try:
            x = float(self.champX.text())
            y = float(self.champY.text())
            if y != 0:
                self.labelResultat.setText(f"{x / y:.2f}")
            else:
                QMessageBox.critical(self, "Erreur", "Division par zéro interdite.")
                self.champX.clear()
                self.champY.clear()
                self.labelResultat.clear()
        except ValueError:
            QMessageBox.critical(self, "Erreur", "Veuillez entrer deux nombres valides.")
            self.champX.clear()
            self.champY.clear()
            self.labelResultat.clear()


# Programme principal
app = QApplication(sys.argv)
fenetre = Calculatrice()
fenetre.show()
sys.exit(app.exec_())
