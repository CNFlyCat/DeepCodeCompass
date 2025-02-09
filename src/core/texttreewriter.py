import os

class TextTreeWriter:
    def __init__(self, data, output_file="TextTree.txt", indent="    "):

        self.data = data
        self.output_file = output_file
        self.indent = indent

    def _format_tree(self, data, prefix=""):

        lines = []
        entries = sorted(data.keys())
        total = len(entries)

        for index, name in enumerate(entries):
            is_last = (index == total - 1)
            connector = "└── " if is_last else "├── "

            if isinstance(data[name], dict):
                lines.append(f"{prefix}{connector}{name}")
                new_prefix = prefix + ("    " if is_last else "│   ")
                lines.extend(self._format_tree(data[name], new_prefix))
            else:
                lines.append(f"{prefix}{connector}{name}")

        return lines

    def write_to_file(self, save_directory="./"):

        os.makedirs(save_directory, exist_ok=True)

        full_path = os.path.join(save_directory, self.output_file)
        try:
            formatted_tree = self._format_tree(self.data)
            with open(full_path, "w", encoding="utf-8") as file:
                file.write("\n".join(formatted_tree))
            return True
        except IOError as e:
            return False

    def get_text(self):

        return "\n".join(self._format_tree(self.data))