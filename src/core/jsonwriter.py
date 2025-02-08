import json
import os


class JSONWriter:
    def __init__(self, data, output_file="FileDirectory.json", indent=4, ensure_ascii=False):
        """
        将目录树数据保存为 JSON 文件的类

        :param data: 需要写入 JSON 的字典数据
        :param output_file: JSON 文件的输出路径
        :param indent: JSON 格式缩进级别（默认 4）
        :param ensure_ascii: 是否使用 ASCII 编码（默认 False 允许中文）
        """
        self.data = data
        self.output_file = output_file
        self.indent = indent
        self.ensure_ascii = ensure_ascii

    def write_to_file(self, save_directory="./"):
        """ 将字典数据写入 JSON 文件 """

        # 如果目录不存在，则创建它
        os.makedirs(save_directory, exist_ok=True)

        # 生成完整的保存路径
        full_path = os.path.join(save_directory, self.output_file)

        try:
            with open(full_path, "w", encoding="utf-8") as json_file:
                json.dump(self.data, json_file, indent=self.indent, ensure_ascii=self.ensure_ascii)
            print(f"✅ 目录结构已成功保存为 JSON 文件: {full_path}")
        except IOError as e:
            print(f"❌ 写入 JSON 文件失败: {e}")

    def get_json_string(self):
        """ 获取 JSON 格式的字符串（可用于打印或其他用途） """
        return json.dumps(self.data, indent=self.indent, ensure_ascii=self.ensure_ascii)
