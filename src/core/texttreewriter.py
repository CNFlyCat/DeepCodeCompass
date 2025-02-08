import os

class TextTreeWriter:
    def __init__(self, data, output_file="TextTree.txt", indent="    "):
        """
        将目录数据转换为类似 `tree` 命令格式的文本文件

        :param data: 需要写入的目录树数据（字典格式）
        :param output_file: 生成的 .txt 文件路径
        :param indent: 缩进字符（默认 4 个空格）
        """
        self.data = data
        self.output_file = output_file
        self.indent = indent

    def _format_tree(self, data, prefix=""):
        """
        递归格式化目录树为文本格式

        :param data: 当前目录字典
        :param prefix: 当前层级的前缀（用于缩进对齐）
        :return: 列表，每一项是格式化后的行
        """
        lines = []
        entries = sorted(data.keys())  # 排序，确保输出结构稳定
        total = len(entries)

        for index, name in enumerate(entries):
            is_last = (index == total - 1)
            connector = "└── " if is_last else "├── "  # 目录连接符号

            # 处理目录、文件
            if isinstance(data[name], dict):
                lines.append(f"{prefix}{connector}{name}")
                new_prefix = prefix + ("    " if is_last else "│   ")
                lines.extend(self._format_tree(data[name], new_prefix))
            else:
                lines.append(f"{prefix}{connector}{name}")

        return lines

    def write_to_file(self, save_directory="./"):
        """
        将格式化后的目录结构写入 .txt 文件

        :param save_directory: 指定存储目录（默认为当前目录）
        """
        # 如果目录不存在，则创建它
        os.makedirs(save_directory, exist_ok=True)

        # 生成完整的保存路径
        full_path = os.path.join(save_directory, self.output_file)

        try:
            formatted_tree = self._format_tree(self.data)
            with open(full_path, "w", encoding="utf-8") as file:
                file.write("\n".join(formatted_tree))
            print(f"✅ 目录结构已成功保存为 TXT 文件: {full_path}")
        except IOError as e:
            print(f"❌ 写入 TXT 文件失败: {e}")

    def get_text(self):
        """ 返回格式化后的目录文本（可用于打印或其他用途） """
        return "\n".join(self._format_tree(self.data))