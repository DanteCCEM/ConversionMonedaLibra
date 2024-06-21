import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic

class Dialogo(QMainWindow):
    # Tipos de cambio 20240619
    USDtoPEN = 3.84
    USDtoEUR = 0.93
    USDtoGBP = 0.79  # Añadido el tipo de cambio de USD a GBP

    def __init__(self):
        super(Dialogo, self).__init__()
        uic.loadUi(r"D:\Snippets CurrencyConvert\src\vista\currencyConvert.ui", self)  # Ruta actualizada

        self.pbTipoCambio.clicked.connect(self.calcularConversion)

    def calcularConversion(self):
        try:
            inicial = float(self.leImporte.text())
        except ValueError:
            QMessageBox.warning(self, "Error de entrada", "Por favor ingrese un número válido.")
            return

        # Determina la moneda de origen y convierte a USD
        if self.rbDeUSD.isChecked():
            convertido = inicial
        elif self.rbDeEUR.isChecked():
            convertido = inicial / self.USDtoEUR
        elif self.rbDePEN.isChecked():
            convertido = inicial / self.USDtoPEN
        elif self.rbDeGBP.isChecked():
            convertido = inicial / self.USDtoGBP
        else:
            QMessageBox.warning(self, "Error de entrada", "Por favor seleccione una moneda de origen.")
            return

        # Convierte de USD a la moneda destino
        if self.rbAUSD.isChecked():
            pass  # USD to USD
        elif self.rbAEUR.isChecked():
            convertido *= self.USDtoEUR
        elif self.rbAPEN.isChecked():
            convertido *= self.USDtoPEN
        elif self.rbAGBP.isChecked():
            convertido *= self.USDtoGBP
        else:
            QMessageBox.warning(self, "Error de entrada", "Por favor seleccione una moneda de destino.")
            return

        self.lblCambio.setText(f"{convertido:.2f}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = Dialogo()
    dialogo.show()
    sys.exit(app.exec_())
