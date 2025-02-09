import os

class IgnoreFileReader:
    def __init__(self, root_path=".", ignore_files=None):

        self.root_path = os.path.abspath(root_path)  # 转为绝对路径
        self.ignore_files = ignore_files if ignore_files else [".gitignore", "fileignore.txt"]
        self.ignore_patterns = []

    def read_ignore_file(self, file_path):

        if not os.path.exists(file_path):
            return

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        self.ignore_patterns.append(line)
        except IOError as e:
            print(f"读取 {file_path} 失败: {e}")

    def load_ignore_patterns(self):

        self.ignore_patterns.clear()
        for file_name in self.ignore_files:
            file_path = os.path.join(self.root_path, file_name)
            self.read_ignore_file(file_path)

    def get_ignore_list(self):

        if not self.ignore_patterns:
            self.load_ignore_patterns()
        return self.ignore_patterns

