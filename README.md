# project-backend
Convertendo os dados de um arquivo txt para json

## 1. Visão Geral

    Esse projeto foi desenvolvido usando apenas python e seu objetivo é criar um
    sistema capaz de fazer o upload de um arquivo txt e converte-lo em um arquivo
    do tipo json, para ser armazanado em banco de dados relacional.

    No momento o projeto apenas faz as manipulações do arquivo txt e o converte para
    uma lista de dados do tipo json.

## 2. Metedologia de Raciocinio

    Meu primeiro objeivo foi manipular os dados do com o arquivo txt para transformar
    cada linha do arquivo de texto em um objeto do tipo json, para isso eu utilizei do
    sistema de leitura e escrita de arquivo do prórpio python. 
    
    Com isso em mente, meu desafio se tornou entender como separar cada informação, 
    individualmente, e converter em um objeto. Para isso eu utilizei de um FOR aninhado 
    juntamente com uma classe chamada Person, que tinha por objetivo salvar cada 
    instancia criada. 

## 3. Teste Rapido

    Como o projeto não está completo, para testa-lo basta fazer o clone e digitar no terminal
    ```
    python main.py
    ```

## 4. Atualizões Futuras

    Meu objetivo final e desenvolver o projeto utilizando do Django, Django rest_framework e
    postgres.