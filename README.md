# Primeiros Passos no ElasticSearch e kibana

...

### Ativando ElasticSearch e Kibana

```bash
docker compose -p elasticsearch -f docker-compose.yaml up -d
```


### Acessando o Dev Tools (Kibana)

[http://localhost:5601/app/dev_tools#/console](http://localhost:5601/app/dev_tools#/console)

> ***Obs.:*** Usuário e senha no arquivo [docker-compose.yaml](docker-compose.yaml).

### Operações no ElasticSearch via Kibana

+ Listando todos os índices existentes

```json
GET _cat/indices
```

+ Criando o mapping do índice ```detalhes-vendas```

```json
PUT detalhes-vendas
{
  "mappings" : {
    "properties" : {
      "cpf" : {
        "type" : "keyword"
      },
      "nome" : {
        "type" : "text"
      },
      "quantidade_itens" : {
        "type" : "long"
      },
      "valor_total" : {
        "type" : "float"
      },
      "detalhes" : {
        "type" : "text"
      }
    }
  }
}
```

+ Visualizando o mapping do índice ```detalhes-vendas```

```json
GET detalhes-vendas/_mapping
```

+ Adicionando os primeiros documentos no índice ```detalhes-vendas```

```json
POST detalhes-vendas/_doc/1
{
  "cpf": "999.999.999-99",
  "nome": "FULANO DE TAL",
  "quantidade_itens": 20,
  "valor_total": 101.99,
  "detalhes": "O cliente adquiriu vários produtos nessa visita."
}

POST detalhes-vendas/_doc/2
{
  "cpf": "888.888.888-88",
  "nome": "SICRANO DE TAL",
  "quantidade_itens": 10,
  "valor_total": 150.99,
  "detalhes": "O cliente adquiriu vários produtos nessa visita."
}
```

+ Listando todos os documentos do índice ```detalhes-vendas```

```json
GET detalhes-vendas/_search
```

+ Consultando um CPF no índice ```detalhes-vendas```

```json
GET detalhes-vendas/_search
{
  "query": {
    "match": {
      "cpf": "888.888.888-88"
    }
  }
}
```