# 📅 Roadmap de 3 Semanas

## 🔹 Semana 1 – Setup + Bronze

### Ambiente

- Criar repo Git (main/dev/feature).

- Configurar docker-compose (PostgreSQL + Jupyter).

### Modelagem

- Definir MER/DER.

- Criar tabelas BRONZE no banco.

- Iniciar dicionário de dados (colunas, tipos).

- Ingestão inicial

- Scripts Python para carregar dados brutos (CSV/API).

- Validações básicas (COUNT, MAX, NULLS).

## 🔹 Semana 2 – Silver + Transformações

- ETL/ELT

- Criar jobs (Python ou SQL) → BRONZE → SILVER.

- Normalização, limpeza, joins.

- Camada GOLD (parcial)

- Criar primeiras tabelas agregadas (KPIs principais).

- Testar consultas simples (contagens, índices).

- Documentação

- Atualizar dicionário com BRONZE + SILVER.

- Desenho da arquitetura (MER, DER, DLD).

##🔹 Semana 3 – BI + Entrega Final

- Transformação final

- Refinar GOLD (tabelas analíticas prontas).

- Testar consistência vs. SILVER.

- Dashboards

- Conectar Power BI e Tableau nas tabelas GOLD.

- Criar telas principais (indicadores, relatórios).

- Documentação final

- Completar dicionário (BRONZE, SILVER, GOLD).

- Detalhar pipeline (jobs ETL, fluxograma).

- Preparar guia de execução (docker-compose up).

- Entrega/POC

- Subir ambiente com Docker.

- Mostrar pipeline + dashboards funcionando.

## ✅ Marcos Semanais

- Semana 1: Infra + BRONZE.

- Semana 2: ETL + SILVER/GOLD inicial.

- Semana 3: BI + GOLD final + documentação.
