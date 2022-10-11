from persons.person import Person
from utils.json_parse import JSONParser


def get():

    result =JSONParser.retrieve("database.json")

    return len(result)


def get_file():

    result = JSONParser.read_file("file.txt")

    return result

def post_file():

    Tipo   =   ""
    Data   =   ""
    Valor  =   ""
    Cpf    =   ""
    Cartao =   ""
    Hora   =   ""
    DonoLoja = ""
    nomeLoja = ""

    file = JSONParser.read_file("file.txt")

    for line in file:
        line = line.strip()
        for index, letra in enumerate(line):
            if (index < 1):
                Tipo += letra
            if (index >= 1 and index < 9):
                Data += letra
            if (index >= 9 and index < 19):
                Valor += letra
            if (index >= 19 and index < 30):
                Cpf += letra
            if (index >= 30 and index < 42):
                Cartao += letra
            if (index >= 42 and index < 48):
                Hora += letra
            if (index >= 48 and index < 62):
                DonoLoja += letra
            if (index >= 62 and index < 82):
                nomeLoja += letra

        person = Person(tipo=Tipo, 
                        data=(Data[0]+Data[1]+Data[2]+Data[3]+"-"+Data[4]+Data[5]+"-"+Data[6]+Data[7]), 
                        valor=str(int(Valor)/100), 
                        cpf=(Cpf[0]+Cpf[1]+Cpf[2]+"-"+Cpf[3]+Cpf[4]+Cpf[5]+"-"+Cpf[6]+Cpf[7]+Cpf[8]+"-"+Cpf[9]+Cpf[10]), 
                        cartao=Cartao, 
                        hora=(Hora[0]+Hora[1]+":"+Hora[2]+Hora[3]+":"+Hora[4]+Hora[5]), 
                        donoDaLoja=DonoLoja, 
                        nomeDaLoja=nomeLoja
                    )

        person.save()

        Tipo   = ""
        Data   = ""
        Valor  = ""
        Cpf    = ""
        Cartao = ""
        Hora   = ""
        DonoLoja = ""
        nomeLoja = ""
    
    post_list_info()

    return get()


def post_list_info():

    result = JSONParser.retrieve("database.json")

    db = JSONParser.retrieve("db_info.json")

    list_length = get()

    entradas = 0
    saidas   = 0
    valor    = 0

    list = ["BAR DO JOAO", "LOJA DO O - MATRIZ",  "MERCADO DA AVENIDA", "MERCEARIA 3 IRMAOS"]

    for pos in range(4):
        for index in range(list_length):
            if(result[index]["nomeDaLoja"] == list[pos]):
                # print(result[index]["nomeDaLoja"])
                if(result[index]["tipo"] == "1"):
                    entradas += 1
                    valor += float(result[index]["valor"])
                if(result[index]["tipo"] == "2"):
                    saidas += 1
                    valor -= float(result[index]["valor"])
                if(result[index]["tipo"] == "3"):
                    saidas += 1
                    valor -= float(result[index]["valor"])
                if(result[index]["tipo"] == "4"):
                    entradas += 1
                    valor += float(result[index]["valor"])
                if(result[index]["tipo"] == "5"):
                    entradas += 1
                    valor += float(result[index]["valor"])
                if(result[index]["tipo"] == "6"):
                    entradas += 1
                    valor += float(result[index]["valor"])
                if(result[index]["tipo"] == "7"):
                    entradas += 1
                    valor += float(result[index]["valor"])
                if(result[index]["tipo"] == "8"):
                    entradas += 1
                    valor += float(result[index]["valor"])
                if(result[index]["tipo"] == "9"):
                    saidas += 1
                    valor += float(result[index]["valor"])
    
                objeto = {
                    "entradas": entradas,
                    "saidas": saidas,
                    "valor": int(valor),
                    "donoDaLoja": result[index]["donoDaLoja"],
                    "nomeDaLoja": result[index]["nomeDaLoja"]
                }
        db.append(objeto)
        JSONParser.save("db_info.json", db)
        entradas = 0
        saidas   = 0
        valor    = 0

    return db



def main():

    post_file()

    print(f'list_lenght: {get()}')
    

if __name__ == '__main__':
    main()
