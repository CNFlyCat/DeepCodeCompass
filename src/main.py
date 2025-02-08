# from core.directorytrre import DirectoryTree
# from core.jsonwriter import JSONWriter
# from core.texttreewriter import TextTreeWriter
#
# if __name__ == "__main__":
#     ignore_patterns = [".git/", "node_modules", "*.log", ".venv/", ".idea/"]
#
#     # 创建 DirectoryTree 实例
#     dir_tree = DirectoryTree(r"D:\Python_Project\DeepCodeCompass", ignore_list=ignore_patterns)
#
#     # 获取目录结构
#     tree_structure = dir_tree.get_tree()
#
#     text_writer = TextTreeWriter(tree_structure)
#     text_writer.write_to_file(r"D:\Python_Project\DeepCodeCompass\测试a")
#
#     json_writer = JSONWriter(tree_structure)
#     json_writer.write_to_file(r"D:\Python_Project\DeepCodeCompass\测试a")

    # test_directory_tree()
    # test_json_writer()

import os
import json
import tkinter as tk
from tkinter import filedialog, ttk, scrolledtext
from core.directorytree import DirectoryTree
from core.jsonwriter import JSONWriter
from core.texttreewriter import TextTreeWriter  # 假设你已经创建这个类

class DirectoryTreeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("目录遍历工具")

        # 📌 大文本框（用来显示结果）
        self.text_area = scrolledtext.ScrolledText(root, width=80, height=25, wrap=tk.WORD)
        self.text_area.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # 📌 "选择路径" 按钮
        self.select_path_button = tk.Button(root, text="选择路径", command=self.choose_directory)
        self.select_path_button.grid(row=1, column=0, padx=5, pady=5)

        # 📌 显示选中路径的 Label
        self.selected_path = tk.StringVar()
        self.path_label = tk.Label(root, textvariable=self.selected_path, width=50, anchor="w")
        self.path_label.grid(row=1, column=1, padx=5, pady=5)

        # 📌 JSON/TXT 选择框
        self.format_option = tk.StringVar(value="json")  # 默认 "json"
        self.format_menu = ttk.Combobox(root, textvariable=self.format_option, values=["json", "txt"], state="readonly")
        self.format_menu.grid(row=1, column=2, padx=5, pady=5)

        # 📌 "确定" 按钮
        self.confirm_button = tk.Button(root, text="确定", command=self.process_directory)
        self.confirm_button.grid(row=1, column=3, padx=5, pady=5)

    def choose_directory(self):
        """ 选择要遍历的文件夹 """
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.selected_path.set(folder_selected)

    def process_directory(self):
        """ 遍历目录，生成 JSON 或 TXT 格式，并展示在文本框 """
        directory_path = self.selected_path.get()
        output_format = self.format_option.get()

        if not directory_path:
            self.text_area.insert(tk.END, "❌ 请先选择目录！\n")
            return

        # 📌 使用 DirectoryTree 获取目录结构
        dir_tree = DirectoryTree(directory_path, ignore_list=["*.pyc", ".git/"])
        tree_data = dir_tree.get_tree()

        # 📌 根据选中的格式处理
        if output_format == "json":
            json_writer = JSONWriter(tree_data)
            result_text = json_writer.get_json_string()
        else:  # "txt"
            text_writer = TextTreeWriter(tree_data)
            result_text = text_writer.get_text()

        # 📌 清除旧的文本，插入新内容
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, result_text)

# 📌 运行 GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = DirectoryTreeGUI(root)
    root.mainloop()