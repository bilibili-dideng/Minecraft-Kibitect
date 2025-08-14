from tkinter import messagebox
from PySide6 import QtGui
from PySide6.QtWidgets import (QApplication)
from com.dideng.Python.MC_Kb.Translations import *
from com.dideng.Python.MC_Kb.logger import *
from com.dideng.Python.MC_Kb import GUI
from com.dideng.Python.MC_Kb.VMAV import start_VMAV
from com.dideng.Python.MC_Kb.Web import *
import locale
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def auto_detect_language() -> str:
    lang = locale.getdefaultlocale()[0]
    if lang.startswith("zh"):
        return "zh_cn"
    elif lang.startswith("en"):
        return "en_us"
    return "en_us"

def Signal_Processing():
    window_data = window.get_ui()
    window_data.Open_VMAV.clicked.connect(start_VMAV)
    window_data.Open_web.clicked.connect(open_resource_Web)
    window_data.MC_Nav.clicked.connect(open_MC_Nav)

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
        sys.exit(app.exec())
    except Exception as e:
        messagebox.showerror("错误",f"程序发生错误，错误原因： {e}，日志已生成！")
        critical(f"启动程序失败！失败原因: {e}")