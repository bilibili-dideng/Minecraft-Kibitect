import sys
import math
import tkinter as tk
from tkinter import ttk, messagebox, StringVar, Label, Frame, Entry
from com.dideng.Python.MC_Kb.utlis import auto_detect_language
from com.dideng.Python.MC_Kb.Translations import tr, load_language

# 全局翻译表
translation_table = {}

# ------------------ Tool Func ------------------

def create_label_entry(parent, text_key, default_text, row):
    """创建带标签和输入框的行"""
    label = ttk.Label(parent, text=tr(text_key, translation_table, default_text))
    entry = ttk.Entry(parent, width=25)
    label.grid(row=row, column=0, padx=10, pady=5, sticky='e')
    entry.grid(row=row, column=1, padx=10, pady=5, sticky='w')
    return entry

# ------------------ Tab 1: Coordinate calculation ------------------

class MCCoordinateCalculator(Frame):
    def __init__(self, parent, translation_table):
        super().__init__(parent)
        self.translation_table = translation_table
        self.setup_ui()

    def setup_ui(self):
        # 表单布局
        lbl = ttk.Label(self, text=tr(
            "com.dideng.Python.MC_Kb.Coordinate_calculation.MCCoordinateCalculator.Title",
            self.translation_table,
            "输入两个坐标点"
        ), font=("Segoe UI", 12, "bold"))
        lbl.grid(row=0, column=0, columnspan=2, pady=15)

        # 输入框
        self.x1 = create_label_entry(self,
            "com.dideng.Python.MC_Kb.Coordinate_calculation.MCCoordinateCalculator.Label.X1",
            "坐标 1 - X:", 1)
        self.z1 = create_label_entry(self,
            "com.dideng.Python.MC_Kb.Coordinate_calculation.MCCoordinateCalculator.Label.Z1",
            "坐标 1 - Z:", 2)
        self.x2 = create_label_entry(self,
            "com.dideng.Python.MC_Kb.Coordinate_calculation.MCCoordinateCalculator.Label.X2",
            "坐标 2 - X:", 3)
        self.z2 = create_label_entry(self,
            "com.dideng.Python.MC_Kb.Coordinate_calculation.MCCoordinateCalculator.Label.Z2",
            "坐标 2 - Z:", 4)

        # 计算按钮
        self.calc_btn = ttk.Button(self,
            text=tr("com.dideng.Python.MC_Kb.Coordinate_calculation.MCCoordinateCalculator.Button.Calculate",
                    self.translation_table, "计算距离"),
            command=self.calculate)
        self.calc_btn.grid(row=5, column=0, columnspan=2, pady=15)

        # 结果显示
        self.result_var = StringVar()
        self.result_var.set(tr(
            "com.dideng.Python.MC_Kb.Coordinate_calculation.MCCoordinateCalculator.Result.Waiting",
            self.translation_table, "等待计算..."))
        self.result_label = ttk.Label(self, textvariable=self.result_var, wraplength=400, anchor='center', font=("Segoe UI", 10))
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10)

    def calculate(self):
        try:
            x1 = float(self.x1.get().strip())
            z1 = float(self.z1.get().strip())
            x2 = float(self.x2.get().strip())
            z2 = float(self.z2.get().strip())
            distance = math.sqrt((x2 - x1)**2 + (z2 - z1)**2)
            result_text = f"<{tr('com.dideng.Python.MC_Kb.Coordinate_calculation.MCCoordinateCalculator.Result.Distance', self.translation_table, '两点距离：')}> {distance:.2f} 格"
            self.result_var.set(result_text)
        except ValueError:
            messagebox.showwarning(
                title=tr("com.dideng.Python.MC_Kb.Coordinate_calculation.MCCoordinateCalculator.Error.Title",
                         self.translation_table, "输入错误"),
                message=tr("com.dideng.Python.MC_Kb.Coordinate_calculation.MCCoordinateCalculator.Error.InvalidInput",
                           self.translation_table, "请输入有效的坐标数字！")
            )


# ------------------ Tab 2: Nether distance conversion ------------------

class NetherDistanceConverter(Frame):
    def __init__(self, parent, translation_table):
        super().__init__(parent)
        self.translation_table = translation_table
        self.setup_ui()

    def setup_ui(self):
        lbl = ttk.Label(self, text=tr(
            "com.dideng.Python.MC_Kb.Coordinate_calculation.NetherDistanceConverter.Title",
            self.translation_table,
            "下界距离换算"
        ), font=("Segoe UI", 12, "bold"))
        lbl.grid(row=0, column=0, columnspan=2, pady=15)

        # 输入距离
        self.distance_input = create_label_entry(self,
            "com.dideng.Python.MC_Kb.Coordinate_calculation.NetherDistanceConverter.Label.Distance",
            "输入距离:", 1)

        # 维度选择
        dim_label = ttk.Label(self, text=tr(
            "com.dideng.Python.MC_Kb.Coordinate_calculation.NetherDistanceConverter.Label.Dimension",
            self.translation_table, "所在维度:"))
        dim_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')

        self.dimension_var = StringVar()
        self.dimension_combo = ttk.Combobox(self, textvariable=self.dimension_var, state="readonly", width=23)
        self.dimension_combo['values'] = [
            tr("com.dideng.Python.MC_Kb.Coordinate_calculation.NetherDistanceConverter.Option.Overworld",
               self.translation_table, "主世界 (Overworld)"),
            tr("com.dideng.Python.MC_Kb.Coordinate_calculation.NetherDistanceConverter.Option.Nether",
               self.translation_table, "下界 (Nether)")
        ]
        self.dimension_combo.current(0)  # 默认主世界
        self.dimension_combo.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        # 换算按钮
        self.convert_btn = ttk.Button(self,
            text=tr("com.dideng.Python.MC_Kb.Coordinate_calculation.NetherDistanceConverter.Button.Convert",
                    self.translation_table, "换算"),
            command=self.convert)
        self.convert_btn.grid(row=3, column=0, columnspan=2, pady=15)

        # 结果显示
        self.result_var = StringVar()
        self.result_var.set(tr(
            "com.dideng.Python.MC_Kb.Coordinate_calculation.MCCoordinateCalculator.Result.Waiting",
            self.translation_table, "等待换算..."))
        self.result_label = ttk.Label(self, textvariable=self.result_var, wraplength=400, anchor='center', font=("Segoe UI", 10))
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def convert(self):
        try:
            dist = float(self.distance_input.get().strip())
            selected = self.dimension_var.get()
            is_overworld = selected == tr("com.dideng.Python.MC_Kb.Coordinate_calculation.NetherDistanceConverter.Option.Overworld",
                                          self.translation_table, "主世界 (Overworld)")

            if is_overworld:
                ow = round(dist, 2)
                nt = round(dist / 8, 2)
                result = (f"<{tr('com.dideng.Python.MC_Kb.Coordinate_calculation.NetherDistanceConverter.Result.Overworld', self.translation_table, '主世界：')}> {ow} 格\n"
                          f"<{tr('com.dideng.Python.MC_Kb.Coordinate_calculation.NetherDistanceConverter.Result.Nether', self.translation_table, '下界：')}> {nt} 格")
            else:
                nt = round(dist, 2)
                ow = round(dist * 8, 2)
                result = (f"<{tr('com.dideng.Python.MC_Kb.Coordinate_calculation.NetherDistanceConverter.Result.Nether', self.translation_table, '下界：')}> {nt} 格\n"
                          f"<{tr('com.dideng.Python.MC_Kb.Coordinate_calculation.NetherDistanceConverter.Result.Overworld', self.translation_table, '主世界：')}> {ow} 格")
            self.result_var.set(result)
        except ValueError:
            messagebox.showwarning(
                title=tr("com.dideng.Python.MC_Kb.Coordinate_calculation.NetherDistanceConverter.Error.Title",
                         self.translation_table, "输入错误"),
                message=tr("com.dideng.Python.MC_Kb.Coordinate_calculation.NetherDistanceConverter.Error.InvalidInput",
                           self.translation_table, "请输入有效的距离数值！")
            )


# ------------------ MainWindow ------------------

class MainWindow_CC(tk.Tk):
    def __init__(self, translation_table):
        super().__init__()
        self.translation_table = translation_table
        self.title(tr("com.dideng.Python.MC_Kb.Coordinate_calculation.Title", translation_table, "Minecraft Coordinate Calculator"))
        self.geometry("281x420")
        self.resizable(False, False)
        self.setup_ui()

    def setup_ui(self):
        # 标签页容器
        notebook = ttk.Notebook(self)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # 创建两个标签页
        tab1 = MCCoordinateCalculator(notebook, self.translation_table)
        tab2 = NetherDistanceConverter(notebook, self.translation_table)

        notebook.add(tab1, text=tr("com.dideng.Python.MC_Kb.Coordinate_calculation.NetherDistanceConverter.Coordinate_calculation", self.translation_table, "坐标计算"))
        notebook.add(tab2, text=tr("com.dideng.Python.MC_Kb.Coordinate_calculation.NetherDistanceConverter.Button.Convert", self.translation_table, "下界换算"))

def main():
    global translation_table
    Language = auto_detect_language()
    translation_table = load_language(Language)

    app = MainWindow_CC(translation_table)
    app.mainloop()

def start_CC_X():
    """ Startup function for external calling """
    global translation_table
    Language = auto_detect_language()
    translation_table = load_language(Language)

    app = MainWindow_CC(translation_table)
    app.mainloop()


if __name__ == '__main__':
    main()