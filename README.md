# Primeiros Passos no ElasticSearch e kibana

O ***Elasticsearch*** é um mecanismo de busca e análise distribuído, desenvolvido para lidar com grandes volumes de dados em tempo real. Ele é baseado no motor de busca ***Apache Lucene*** e oferece uma forma rápida e eficiente de armazenar, pesquisar e analisar dados ***estruturados*** ou ***não estruturados***. Muito utilizado em casos como logs de servidor, análise de textos, monitoramento de sistemas e motores de busca personalizados, o Elasticsearch permite buscas full-text, agregações e filtragens, oferecendo alta escalabilidade e flexibilidade. Ele é uma peça fundamental no ***ecossistema ELK*** (Elasticsearch, Logstash, Kibana), sendo amplamente utilizado em soluções de ***big data*** e ***observabilidade***.

<!--
https://www.youtube.com/@renato-coelho

# Apresentação em vídeo

<p align="center">
  <a href="https://www.youtube.com/@renato-coelho" target="_blank"><img src="thumbnail/ElasticSearchPrimeirosPassos.png" alt="Vídeo de apresentação"></a>
</p>
-->


### Requisitos

+ ![Git](https://img.shields.io/badge/Git-2.25.1%2B-E3E3E3)

+ ![Docker](https://img.shields.io/badge/Docker-27.2.1%2B-E3E3E3)

+ ![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04%2B-E3E3E3)

+ ![Docker-compose](https://img.shields.io/badge/Docker--compose-2.29.2%2B-E3E3E3)


### Ativando ElasticSearch e Kibana


+ Clonando o repositório:

```bash
git clone https://github.com/Renatoelho/elasticsearch-primeiros-passos.git elasticsearch-primeiros-passos
```

+ Acessando o repositório:

```bash
cd elasticsearch-primeiros-passos/
```

+ Ativando os serviços via Docker Compose:

```bash
docker compose -p elasticsearch -f docker-compose.yaml up -d
```

### Acessando o Dev Tools (Kibana)

[http://localhost:5601/app/dev_tools#/console](http://localhost:5601/app/dev_tools#/console)

> ***Obs.:*** Usuário e senha no arquivo [docker-compose.yaml](docker-compose.yaml).

### Operações no ElasticSearch via Kibana

+ Listando todos os índices existentes

```bash
GET _cat/indices
```

+ Criando o mapping do índice ```detalhes-vendas```

```bash
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

```bash
GET detalhes-vendas/_mapping
```

+ Adicionando os primeiros documentos no índice ```detalhes-vendas```

```bash
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

```bash
GET detalhes-vendas/_search
```

+ Consultando um CPF no índice ```detalhes-vendas```

```bash
GET detalhes-vendas/_search
{
  "query": {
    "match": {
      "cpf": "888.888.888-88"
    }
  }
}
```

# Referências

REST APIs **Elasticsearch Guide.** Disponível em: <https://www.elastic.co/guide/en/elasticsearch/reference/7.17/rest-apis.html>. Acesso em: 10 set. 2024.

Elasticsearch Docker Official Image **https://hub.docker.com** Disponível em: <https://hub.docker.com/_/elasticsearch>. Acesso em: 10 set. 2024.
