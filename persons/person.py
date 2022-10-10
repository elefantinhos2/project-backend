from utils.json_parse import JSONParser


class Person(JSONParser):

    database = "database.json"

    file = "file.txt"


    def __init__(self, tipo: str, data: str, valor: str, cpf: str, cartao: str, hora:str, donoDaLoja: str, nomeDaLoja: str) :
        self.tipo   = tipo
        self.data   = data
        self.valor  = valor
        self.cpf    = cpf
        self.cartao = cartao
        self.hora   = hora
        self.donoDaLoja = donoDaLoja
        self.nomeDaLoja = nomeDaLoja


    def save(self) -> None:

        persons = super().retrieve(self.database)

        persons.append(self.__dict__)

        super().save(self.database, persons)


    @classmethod
    def retrieve(cls) -> list[dict]:

        return super().retrieve(cls.database)
