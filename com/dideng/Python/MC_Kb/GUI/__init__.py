from com.dideng.Python.MC_Kb.Translations import tr
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
                               QStatusBar, QTabWidget, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QToolBar)

class MainWindow(QMainWindow):
    def __init__(self,translation_table: dict):
        super().__init__()
        self.ui = Ui_MainWindow(translation_table)
        self.ui.setupUi(self)
    def get_ui(self):
        return self.ui

    def tr(self, text):
        return QCoreApplication.translate("MainWindow", text)

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def __init__(self, translation_table: dict):
        self.translation_table = translation_table  # 保存翻译表
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(644, 309)
        MainWindow.setStyleSheet(u"QPushButton{\n"
"	border-radius:5px;\n"
"	background-color:rgb(0, 196, 255);\n"
"	color:rgb(0,0,0);\n"
"	outline: none;\n"
"}\n"
"QPushButton:hover {\n"
"	border-radius:5px;\n"
"	background-color:rgb(100, 196, 255);\n"
"	color:rgb(0,0,0);\n"
"	outline: none;\n"
"}\n"
"QPushButton:pressed {\n"
"	border-radius:5px;\n"
"	background-color:rgb(150, 236, 255);\n"
"	color:rgb(0,0,0);\n"
"	outline: none;\n"
"}\n"
"QPushButton:disabled {\n"
"	border-radius:5px;\n"
"	background-color:rgb(100, 100, 100);\n"
"	color:rgb(0,0,0);\n"
"	outline: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Cksn = QVBoxLayout()
        self.Cksn.setObjectName(u"Cksn")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.Open_VMAV = QPushButton(self.tab_3)
        self.Open_VMAV.setObjectName(u"Open_VMAV")
        self.Open_VMAV.setMinimumSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.Open_VMAV)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout = QVBoxLayout(self.tab_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Open_web = QPushButton(self.tab_4)
        self.Open_web.setObjectName(u"Open_web")
        self.Open_web.setEnabled(True)
        self.Open_web.setMinimumSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.Open_web)

        self.MC_Nav = QPushButton(self.tab_4)
        self.MC_Nav.setObjectName(u"MC_Nav")
        self.MC_Nav.setMinimumSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.MC_Nav)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.Cksn.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addLayout(self.Cksn)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            tr("com.dideng.Python.MC_Kb.GUI.Window_Title", self.translation_table, "Minecraft-Kibitect")
        )
        self.Open_VMAV.setText(
            tr("com.dideng.Python.MC_Kb.GUI.Open_VMAV", self.translation_table, "Open Vanction Minecraft Archive Viewer")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3),
            tr("com.dideng.Python.MC_Kb.GUI.Tab_1", self.translation_table, "dideng homemade")
        )
        self.Open_web.setText(
            tr("com.dideng.Python.MC_Kb.GUI.QPushButton_Open_Web_Tool", self.translation_table, "Web Tool")
        )
        self.MC_Nav.setText(
            tr("com.dideng.Python.MC_Kb.GUI.QPushButton_Open_MC_Nav", self.translation_table, "MC Nav")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_4),
            tr("com.dideng.Python.MC_Kb.GUI.Tab_2", self.translation_table, "Web")
        )