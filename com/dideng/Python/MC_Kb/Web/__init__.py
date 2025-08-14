import webbrowser
from com.dideng.Python.MC_Kb.logger import *
import sys
def open_resource_Web():
    webbrowser.open_new_tab(f"{os.getcwd()}/data/resources/html/resources.html")
    info(f"成功打开html（资源网页），路径 {os.getcwd()}/data/resources/html/resources.html")
def open_MC_Nav():
    webbrowser.open_new_tab("https://www.mcnav.net/")
    info(f"成功打开MC Nav,网页：https://www.mcnav.net/")