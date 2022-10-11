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
   
    return get()


def main():

    post_file()
    print(f'list_lenght: {get()}')
    

if __name__ == '__main__':
    main()
