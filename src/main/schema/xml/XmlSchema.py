# Read the LICENSE file in the root folder

from schema import AbstractSchema, AbstractSchemaFile

class XmlSchema(AbstractSchema, AbstractSchemaFile):
    def parse(self, string):
        raise NotImplementedError
    def parse_file(self, file):
        raise NotImplementedError
    def is_correct_file_ext(self, filename):
        raise NotImplementedError