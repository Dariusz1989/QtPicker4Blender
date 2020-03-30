import sys
import bpy
import threading

if sys.platform == 'win64': 
    from pip._internal import main as pip
    def install(package):
        pip(["install", package])

    try:
        from PyQt5 import QtCore, QtGui, QtWidgets
    except:
        try:
            install("PyQt5")
            from PyQt5 import QtCore, QtGui, QtWidgets
        except:
            pass
elif sys.platform == 'linux' or sys.platform == 'linux2':
    try:
        from PyQt5 import QtCore, QtGui, QtWidgets
    except:
        print("Please, INSTALL PyGt5! >>> pip install PyQt5")
else:
    try:
        from PyQt5 import QtCore, QtGui, QtWidgets
    except:
        print("Please, INSTALL PyGt5! >>> pip install PyQt5")

bone_list = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(180, 120)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        #self.textEdit.setGeometry(QtCore.QRect(10, 110, 180, 31))
        #self.textEdit.setObjectName("textEdit")

        self.combo = QtWidgets.QComboBox(self.centralwidget) # must be self but bueno,.....
        self.combo.setObjectName("combo")
        self.combo.addItems(bone_list)
        self.combo.move(10, 10)
        #combo.activated[str].connect(self.onActivated)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onClick)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def onClick(self):
        # Modificar propiedades directamente funciona bien
        #bpy.context.window_manager.target_bone_name = self.textEdit.toPlainText()
        bpy.context.window_manager.target_bone_index = self.combo.currentIndex()
        #bpy.data.objects["Cube"].location.x += 1 

        #self.textEdit.setText("Esfera añadida con éxito!")

        # OPERADOR HACE QUE CRASHEE
        #bpy.ops.mesh.primitive_uv_sphere_add() 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Select Bone"))
'''
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Bone Name</p></body></html>"))
'''
        


# 1º Método Usando threads

def Invoke():
    d = threading.Thread(target=LoadWindow, name='Daemon')
    d.daemon = True
    d.start()

def LoadWindow():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()


# 2º Método Usando un handler
'''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def  Invoke():
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    bpy.app.handlers.load_post.append(handler)

def handler():
    #MainWindow.show()
    app.exec_()
'''