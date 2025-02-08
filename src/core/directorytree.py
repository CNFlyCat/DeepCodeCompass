import os
import fnmatch


class DirectoryTree:
    def __init__(self, root_path, ignore_list=None):
        """
        用于遍历目录的类，支持忽略目录、文件及通配符匹配

        :param root_path: 需要遍历的根目录路径
        :param ignore_list: 需要忽略的文件/文件夹列表（支持通配符）
        """
        self.root_path = os.path.abspath(root_path)  # 规范化路径
        self.tree = {}
        self.ignore_list = ignore_list if ignore_list else []

    def should_ignore(self, path, name, is_dir):
        """
        判断是否应该忽略某个文件/文件夹

        :param path: 当前文件/目录的完整路径
        :param name: 当前文件/目录的名称
        :param is_dir: 是否为目录
        :return: 如果应忽略，则返回 True，否则返回 False
        """
        relative_path = os.path.relpath(path, self.root_path)
        normalized_path = relative_path.replace("\\", "/")

        for pattern in self.ignore_list:

            if is_dir and pattern.endswith('/') and fnmatch.fnmatch(normalized_path + '/', pattern):
                return True

            if not is_dir and fnmatch.fnmatch(name, pattern):
                return True

        return False

    def build_tree(self, current_path=None):
        """
        递归地遍历目录并构建目录树

        :param current_path: 当前遍历的目录路径
        """
        if current_path is None:
            current_path = self.root_path

        tree_structure = {}

        # **检查是否应忽略整个目录**
        if self.should_ignore(current_path, os.path.basename(current_path), is_dir=True):
            return tree_structure

        try:
            # 遍历当前目录下的所有文件和文件夹
            for entry in os.scandir(current_path):
                full_path = entry.path
                name = entry.name

                # **检查是否应忽略当前文件/目录**
                if self.should_ignore(full_path, name, entry.is_dir()):
                    continue  # 跳过该文件/目录

                if entry.is_dir():
                    # **递归构建子目录**
                    tree_structure[name] = self.build_tree(full_path)
                else:
                    tree_structure[name] = "file"
        except PermissionError:
            tree_structure = {"error": "Permission Denied"}

        return tree_structure

    def get_tree(self):
        """
        返回构建好的目录树（字典格式）

        :return: 以字典形式表示的目录结构
        """
        if not self.tree:
            self.tree = self.build_tree()
        return self.tree

# ignore_patterns = [".git/", "node_modules", "*.log",".venv/",".idea/"]
#
# # 创建 DirectoryTree 实例
# dir_tree = DirectoryTree(r"D:\Python_Project\DeepCodeCompass", ignore_list=ignore_patterns)
#
# # 获取目录结构
# tree_structure = dir_tree.get_tree()
#
# # 输出结果
# import json
# print(json.dumps(tree_structure, indent=4, ensure_ascii=False))