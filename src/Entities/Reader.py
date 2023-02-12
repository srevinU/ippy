import json


class Reader:

    @staticmethod
    def read_json_file(file_path):
        with open(f"../data/{file_path}") as decimal_binary_file:
            return json.load(decimal_binary_file)
