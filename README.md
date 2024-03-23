# demo-predicao-classes-vinhos-em-batch

## Estrutura de diretórios
```
│   .gitignore
│   Dockerfile                 #imagem docker responsável por encapsular a API python
│   requirements.txt           #dependências python
│
├───app
│       main.py                #definição da API python
│       model.pkl              #modelo de classificação de vinhos previamente treinado e exportado via Pickle
│
└───exemplos de request        #exemplo de payload para requisição. Seguem a mesma estrutura usada gerada pelo Vertex
        request1.json
        request2.json
        request3.json
```     
