from fileinput import filename
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.QtGui import QFont


"""" Importamos las ventanas"""
from vista.home import *
from AnalizadorLexico import *
from AnalizadorSintactico import *


class Main(QMainWindow):
    """ Clase principal de la app """
    def __init__(self):
        """ Iniciamos nuestra app """
        QMainWindow.__init__(self)


        # Instaciamos la ventana principal
        self.home = Ui_home()
        self.home.setupUi(self)
        self.home.bt_archivo.setParent(self)
        self.home.bt_limpiar.setParent(self)
        self.home.bt_archivo.show()
        self.home.bt_limpiar.show()
        self.home.bt_archivo.setGeometry(500, 20, 140, 35)   
        self.home.bt_limpiar.setGeometry(650, 20, 140, 35)  
        self.estilo_ventana()


        self.home.bt_lexico.setText("Análisis Léxico")
        self.home.bt_sintactico.setText("Análisis Sintáctico")
        self.home.bt_archivo.setText("Cargar Archivo")
        self.home.bt_limpiar.setText("Limpiar Campos")


        #Eventos
        self.home.bt_lexico.clicked.connect(self.ev_lexico)
        self.home.bt_sintactico.clicked.connect(self.ev_sintactico)


        self.home.bt_archivo.clicked.connect(self.ev_archivo)
        self.home.bt_limpiar.clicked.connect(self.ev_limpiar)


        #Desarrolladores
        self.home.estado.showMessage("Compildores CIAF - 2026")
        
    def estilo_ventana(self):
        self.setStyleSheet("""
       
        QMainWindow {
            background-color: #FFF5F7;
        }


        QPushButton {
            background-color: #9F4565;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 8px 16px;
            font-size: 14px;
        }


     QPushButton#bt_archivo {
            min-width: 140px;
            max-width: 140px;
            min-height: 35px;
            max-height: 35px;
        }


        QPushButton#bt_limpiar {
            min-width: 140px;
            max-width: 140px;
            min-height: 35px;
            max-height: 35px;
        }


        QPushButton:hover {
            background-color: #C76B8A;
        }


        QTextEdit {
            background-color: white;
            color: #333333;
            border: 1px solid #D9A6B8;
            border-radius: 10px;
            padding: 6px 16px;
            font-size: 13px;
        }


        QLabel {
            color: #74364D;
            font-size: 14px;
        }


        QStatusBar {
            background-color: #F8E1E9;
            color: #74364D;
        }
    """)
        self.setFont(QFont("Segoe UI", 10))


    def ev_lexico(self):
        '''
        Manejo de analisis de expresion lexemas 
        :return:'''


        #print ("lexico")


        #limpiamos
        self.home.tx_lexico.setText('')


        #obtenemos los datos ingresados
        datos = self.home.tx_ingreso.toPlainText().strip()


        #analizamos los lexemas de los datos ingresados
        resultado_lexico = prueba(datos)


        #self.home.tx_lexico.setText("Analizando Lexico")
        cadena = ''
        for lex in resultado_lexico:
            cadena += lex + "\n"
        self.home.tx_lexico.setText(cadena)


    def ev_sintactico(self):
        '''
        Manejo de analisis de expresion sintactico
        :return:
        '''


        #print ("sintactico")


        #limpiamos
        self.home.tx_sintactico.setText('')


        #obtenemos los datos ingresados
        datos = self.home.tx_ingreso.toPlainText().strip()


        #analizamos los lexemas de los datos ingresados
        resultado_sintactico = prueba_sintactica(datos)
        cadena = ''


        #Armanos la cadena a mostrar
        for lex in resultado_sintactico:
            cadena += lex + "\n"
            #mostramos en pantalla
        self.home.tx_sintactico.setText(cadena)


    def ev_archivo(self):
        '''
        Manejo de subir archivo
        :return:
        '''


        dlg = QFileDialog()


        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')


            with f:
                data = f.read().strip()
                if data:
                    self.home.tx_ingreso.setText(data+"\n")




    def ev_limpiar(self):
        '''
        Manejo de limpieza de campos
        :return:
        '''


        self.home.tx_ingreso.setText('')
        self.home.tx_lexico.setText('')
        self.home.tx_sintactico.setText('')




def iniciar():
    app = QApplication(sys.argv)
    #Instaciamos nuestra ventana 
    ventana = Main()
    #Mostramos la app
    ventana.show()
    #Controlamos el cierre de la app
    sys.exit(app.exec_())


if __name__ == "__main__":
    iniciar()