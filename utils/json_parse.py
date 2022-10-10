import json


class JSONParser:

    @staticmethod
    def read_file(filepath: str) -> list[dict]:
        
        file = open(filepath, "r")
        
        lines = file.readlines()

        file.close()

        return lines

    @staticmethod
    def retrieve(filepath: str) -> list[dict]:

        with open(filepath, "r") as file:
            return json.load(file)

    @staticmethod
    def save(filepath: str, payload) -> None:

        with open(filepath, "w") as file:
            json.dump(payload, file, indent=2, ensure_ascii=False)
