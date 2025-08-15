from tkinter import messagebox
from PySide6 import QtGui
from PySide6.QtWidgets import (QApplication)
from com.dideng.Python.MC_Kb.Translations import *
from com.dideng.Python.MC_Kb.Web import open_resource_Web, open_MC_Nav
from com.dideng.Python.MC_Kb.logger import *
from com.dideng.Python.MC_Kb import GUI
from com.dideng.Python.MC_Kb.VMAV import start_VMAV
from com.dideng.Python.MC_Kb.Coordinate_calculation import start_CC
from com.dideng.Python.MC_Kb.utlis import auto_detect_language
import locale
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


def Signal_Processing():
    info("正在初始化信号管理")
    try:
        window_data = window.get_ui()
        window_data.Open_VMAV.clicked.connect(start_VMAV)
        window_data.Open_CC.clicked.connect(start_CC)
        window_data.Open_web.clicked.connect(open_resource_Web)
        window_data.MC_Nav.clicked.connect(open_MC_Nav)
        info("初始化信号管理成功！")
    except Exception as e:
        error(f"初始化信号管理失败！失败原因：{e}")

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        current_language = auto_detect_language()
        translation_table = load_language(current_language)
        if not translation_table:
            info("未加载到翻译表，使用英文默认值")
            translation_table = {}  # 空表，tr 会返回 default
        window = GUI.MainWindow(translation_table)
        Signal_Processing()
        window.show()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./data/resources/icon/main_icon/icon.ico"))
        window.setWindowIcon(icon)
        info(f"启动程序成功！")
        app.exec()
        info(f"程序退出！退出代码为 0")
        sys.exit(0)
    except Exception as e:
        messagebox.showerror("错误",f"程序发生错误，错误原因： {e}，日志已生成！")
        critical(f"启动程序失败！失败原因: {e}")
        critical("程序崩溃！")
        raise e