import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
from core.directorytree import DirectoryTree
from core.ignorefilereader import IgnoreFileReader
from core.jsonwriter import JSONWriter
from core.texttreewriter import TextTreeWriter


class DirectoryExplorerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("目录提取工具")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)


        self.project_path = tk.StringVar()
        self.ignore_file_path = tk.StringVar()
        self.output_format = tk.StringVar(value="TXT")
        self.directory_structure = {}


        self.create_widgets()
        self.update_layout()
        self.root.bind("<Configure>", self.update_layout)

    def create_widgets(self):

        frame_top = tk.Frame(self.root)
        frame_top.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(frame_top, text="项目目录:").pack(side=tk.LEFT, padx=5)
        self.entry_project = tk.Entry(frame_top, textvariable=self.project_path)
        self.entry_project.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        tk.Button(frame_top, text="浏览", command=self.select_project_path).pack(side=tk.RIGHT, padx=5)


        frame_ignore = tk.Frame(self.root)
        frame_ignore.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(frame_ignore, text="忽略文件:").pack(side=tk.LEFT, padx=5)
        self.entry_ignore = tk.Entry(frame_ignore, textvariable=self.ignore_file_path)
        self.entry_ignore.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        tk.Button(frame_ignore, text="浏览", command=self.select_ignore_file).pack(side=tk.RIGHT, padx=5)


        frame_format = tk.Frame(self.root)
        frame_format.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(frame_format, text="导出格式:").pack(side=tk.LEFT, padx=5)
        self.combo_format = ttk.Combobox(frame_format, textvariable=self.output_format, values=["TXT", "JSON"],
                                         state="readonly")
        self.combo_format.pack(side=tk.LEFT, padx=5)
        self.combo_format.bind("<<ComboboxSelected>>", self.update_text_display)


        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(fill=tk.X, side=tk.BOTTOM, padx=10, pady=5)  # 关键调整: side=tk.BOTTOM

        self.btn_generate = tk.Button(frame_buttons, text="开始遍历", command=self.generate_tree)
        self.btn_generate.pack(side=tk.LEFT, expand=True, padx=5, pady=5)

        self.btn_save = tk.Button(frame_buttons, text="保存文件", command=self.save_to_file)
        self.btn_save.pack(side=tk.RIGHT, expand=True, padx=5, pady=5)


        frame_text = tk.Frame(self.root)
        frame_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)  # 关键调整: expand=True

        tk.Label(frame_text, text="目录结构:").pack(anchor="w")

        self.text_area = scrolledtext.ScrolledText(frame_text, wrap=tk.WORD)
        self.text_area.pack(fill=tk.BOTH, expand=True)

    def update_layout(self, event=None):

        self.entry_project.config(width=self.root.winfo_width() // 10)
        self.entry_ignore.config(width=self.root.winfo_width() // 10)
        self.text_area.config(width=self.root.winfo_width() // 10, height=self.root.winfo_height() // 20)

    def select_project_path(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.project_path.set(folder_selected)

    def select_ignore_file(self):
        file_selected = filedialog.askopenfilename(filetypes=[("Ignore Files", "*.gitignore;*.txt"), ("All Files", "*.*")])
        if file_selected:
            self.ignore_file_path.set(file_selected)

    def generate_tree(self):
        root_path = self.project_path.get()
        ignore_path = self.ignore_file_path.get()

        if not os.path.isdir(root_path):
            messagebox.showerror("错误", "请选择有效的项目目录！")
            return

        ignore_patterns = []
        if ignore_path and os.path.exists(ignore_path):
            reader = IgnoreFileReader(root_path=os.path.dirname(ignore_path), ignore_files=[os.path.basename(ignore_path)])
            ignore_patterns = reader.get_ignore_list()

        tree = DirectoryTree(root_path, ignore_patterns)
        self.directory_structure = tree.get_tree()

        self.update_text_display()

    def update_text_display(self, event=None):
        selected_format = self.output_format.get()
        self.text_area.delete(1.0, tk.END)

        if not self.directory_structure:
            return

        if selected_format == "TXT":
            writer = TextTreeWriter(self.directory_structure)
            formatted_text = writer.get_text()
        else:
            formatted_text = json.dumps(self.directory_structure, indent=4, ensure_ascii=False)

        self.text_area.insert(tk.END, formatted_text)

    def save_to_file(self):

        if not self.directory_structure:
            messagebox.showerror("错误", "请先遍历目录！")
            return

        save_directory = filedialog.askdirectory()
        if not save_directory:
            return

        output_format = self.output_format.get()

        if output_format == "JSON":
            writer = JSONWriter(self.directory_structure)
            save_successful = writer.write_to_file(save_directory)
        else:
            writer = TextTreeWriter(self.directory_structure)
            save_successful = writer.write_to_file(save_directory)

        if save_successful:
            messagebox.showinfo("保存成功", f"已成功保存为 {output_format} 文件！")
        else:
            messagebox.showerror("保存失败", f"保存 {output_format} 文件失败，请检查是否有写入权限或磁盘空间。")


if __name__ == "__main__":
    root = tk.Tk()
    app = DirectoryExplorerApp(root)
    root.mainloop()