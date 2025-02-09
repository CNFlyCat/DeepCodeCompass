import json
import os


class JSONWriter:
    def __init__(self, data, output_file="FileDirectory.json", indent=4, ensure_ascii=False):

        self.data = data
        self.output_file = output_file
        self.indent = indent
        self.ensure_ascii = ensure_ascii

    def write_to_file(self, save_directory="./"):

        os.makedirs(save_directory, exist_ok=True)

        full_path = os.path.join(save_directory, self.output_file)
        try:
            with open(full_path, "w", encoding="utf-8") as json_file:
                json.dump(self.data, json_file, indent=self.indent, ensure_ascii=self.ensure_ascii)
            return True
        except IOError as e:
            return False

    def get_json_string(self):

        return json.dumps(self.data, indent=self.indent, ensure_ascii=self.ensure_ascii)
