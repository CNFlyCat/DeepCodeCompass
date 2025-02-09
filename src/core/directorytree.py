import os
import fnmatch


class DirectoryTree:
    def __init__(self, root_path, ignore_list=None):

        self.root_path = os.path.abspath(root_path)
        self.tree = {}
        self.ignore_list = ignore_list if ignore_list else []

    def should_ignore(self, path, name, is_dir):

        relative_path = os.path.relpath(path, self.root_path)
        normalized_path = relative_path.replace("\\", "/")

        for pattern in self.ignore_list:

            if is_dir and pattern.endswith('/'):
                if fnmatch.fnmatch(normalized_path + '/', pattern) or fnmatch.fnmatch(name + '/', pattern):
                    return True


            if fnmatch.fnmatch(name, pattern) or fnmatch.fnmatch(normalized_path, pattern):
                return True


            if is_dir and pattern in normalized_path.split('/'):
                return True

        return False

    def build_tree(self, current_path=None):

        if current_path is None:
            current_path = self.root_path

        tree_structure = {}


        if self.should_ignore(current_path, os.path.basename(current_path), is_dir=True):
            return tree_structure

        try:

            for entry in os.scandir(current_path):
                full_path = entry.path
                name = entry.name


                if self.should_ignore(full_path, name, entry.is_dir()):
                    continue

                if entry.is_dir():

                    tree_structure[name] = self.build_tree(full_path)
                else:
                    tree_structure[name] = "file"
        except PermissionError:
            tree_structure = {"error": "Permission Denied"}

        return tree_structure

    def get_tree(self):

        if not self.tree:
            self.tree = self.build_tree()
        return self.tree

