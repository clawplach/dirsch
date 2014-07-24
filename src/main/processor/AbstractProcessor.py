# Read the LICENSE file in the root folder

class AbstractProcessor():
    def is_directory(self, path): pass
    def is_file(self, path): pass
    def is_valid_name(self, name, regex): pass
    def is_valid_mode(self, path, mode): pass