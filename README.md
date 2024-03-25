## demo-predicao-classes-vinhos-em-batch
### Código adaptado para uso com o Vertex Model Registry e Vertex Batch Predictions

### Diretórios e arquivos
```
│   .gitignore
│   Dockerfile				#imagem docker responsável por encapsular a API python
│   README.md
│   requirements.txt			#dependências python
│
├───app
│       main.py				#definição da API python
│       model.pkl			#modelo de classificação de vinhos previamente treinado e exportado via Pickle
│
├───exemplo-notebook-pipeline	        #exemplos notebooks com definição de pipeline
│       demo_vertex_pipelines.ipynb
│
├───exemplos-arquivo-jsonl		#exemplos de arquivos jsonl que devem ser usados como input para uma Vertex Batch Prediction
│       instances.jsonl
│
└───exemplos-request			#exemplos de payload para teste de requisição via API. Seguem a mesma estrutura usada gerada pelo Vertex
        request1.json
        request2.json
        request3.json
```     

#### Nota: O modelo utilizado nessa demo foi treinado com o dataset Wine
https://scikit-learn.org/stable/datasets/toy_dataset.html#wine-recognition-dataset
