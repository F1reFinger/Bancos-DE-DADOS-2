# Projeto de Análise de Dados Pokédex - Sistemas de Banco de Dados 2

Este projeto tem como objetivo aplicar os conceitos de engenharia de dados para extrair, tratar e visualizar informações do dataset Pokédex. A metodologia utilizada é a **Arquitetura Medalhão**, organizando o fluxo em três camadas: Bronze, Silver e Gold.

A ferramenta principal para a transformação dos dados será o **PySpark**, para simular um ambiente de Big Data e praticar as operações distribuídas.


## 🚀 Estrutura do Projeto

O fluxo de dados seguirá as seguintes etapas:

1.  **Camada Bronze:** Ingestão dos dados brutos.
2.  **Camada Silver:** Limpeza e transformação dos dados com PySpark.
3.  **Camada Gold:** Modelagem dos dados em um Data Warehouse.
4.  **Visualização:** Criação de um dashboard interativo.


### 🥉 Camada Bronze (Raw Data)

* **Objetivo:** Armazenar uma cópia fiel e imutável dos dados originais, exatamente como foram coletados da fonte.
* **Ferramentas:** Nenhuma (apenas download manual).
* **Entregáveis:**
    * O arquivo `pokedex.csv` original, localizado na pasta `/data/bronze/`.

### 🥈 Camada Silver (Cleaned & Enriched Data)

* **Objetivo:** Transformar os dados brutos em informações confiáveis e limpas. É nesta camada que ocorre o processo de ETL (Extração, Transformação e Carga).
* **Ferramentas:** `Python`, `PySpark`, `Jupyter Notebook`.
* **Entregáveis:**
    * Um arquivo tratado (ex: em formato Parquet) na pasta `/data/silver/`.
    * O notebook `1_processamento_etl_pyspark.ipynb` com todo o código de limpeza e tratamento, localizado na pasta `/notebooks/`.
    * Um **Dicionário de Dados** que explica cada coluna da tabela tratada.

### 🥇 Camada Gold (Business-Ready Data)

* **Objetivo:** Modelar os dados da camada Silver em um formato otimizado para análises de negócio, geralmente um **Data Warehouse** com **Esquema Estrela**.
* **Ferramentas:** `Python`, `PySpark`, `PostgreSQL`, `Docker`.
* **Entregáveis:**
    * Um banco de dados PostgreSQL conteinerizado com a estrutura do Data Warehouse.
    * Scripts Python (`.py`) na pasta `/scripts/` que usam PySpark para carregar os dados nas tabelas **Fato** e **Dimensão**.
    * Um arquivo `docker-compose.yml` para iniciar o ambiente do banco de dados.

### 📊 Camada de Visualização

* **Objetivo:** Consumir os dados da Camada Gold para criar visualizações e dashboards que permitam extrair insights.
* **Ferramentas:** `Microsoft Power BI`.
* **Entregáveis:**
    * Um arquivo de dashboard (`.pbix`) conectado diretamente ao banco de dados PostgreSQL.
