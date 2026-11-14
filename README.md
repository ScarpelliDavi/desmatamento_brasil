# Análise do Desmatamento na Amazônia Legal

## Sobre o projeto

Este projeto tem como objetivo analisar a evolução do desmatamento na Amazônia Legal, utilizando dados anuais referentes ao período de 1988 a 2022.

Através de técnicas de ETL (Extract, Transform, Load), análise exploratória de dados (EDA) e visualização gráfica, busca-se compreender o comportamento histórico do desmatamento e sua distribuição entre os estados que compõem a região.

O projeto foi desenvolvido como parte de uma atividade acadêmica.

## Objetivos

- Analisar a evolução temporal do desmatamento na Amazônia Legal.
- Identificar os estados com maior área de desmatamento acumulado.
- Comparar o comportamento do desmatamento entre os estados.
- Aplicar técnicas de tratamento, análise e visualização de dados utilizando Python.

## Perguntas de pesquisa

1. Como o desmatamento na Amazônia Legal evoluiu ao longo do período analisado?
2. Quais estados da Amazônia Legal apresentam os maiores índices de desmatamento acumulado no período analisado?

## Dataset

O dataset utilizado contém registros anuais de desmatamento na Amazônia Legal, abrangendo o período de 1988 a 2022.

As informações estão organizadas por estado, além de uma coluna que representa a área total desmatada em cada ano.

A área desmatada é expressa em quilômetros quadrados (km²).

O dicionário de dados está disponível em:

`data/data_dictionary.md`

## Tecnologias utilizadas

- Python
- Pandas
- Plotly
- Jupyter Notebook
- Git e GitHub

## Estrutura do projeto

```text
projetoAv2/
├── data/
│   ├── raw/
│   │   └── desmatamento_prodes.csv
│   ├── processed/
│   │   └── desmatamento_tratado.csv
│   └── data_dictionary.md
├── notebooks/
│   └── analise_exploratoria.ipynb
├── src/
│   ├── __init__.py
│   └── etl.py
├── README.md
├── requirements.txt
└── LICENSE
```

## Processo de ETL

O processo de ETL foi desenvolvido em Python e está localizado em `src/etl.py`.

O processo é dividido em três etapas:

### Extract

Leitura do dataset original armazenado em `data/raw/`.

### Transform

- Renomeação de colunas para padronização.
- Verificação de valores ausentes.
- Verificação de registros duplicados.
- Verificação de valores negativos.
- Validação da correspondência entre a soma das áreas desmatadas por estado e a área total.

### Load

Exportação do dataset tratado para `data/processed/desmatamento_tratado.csv`.

## Análise exploratória

A análise exploratória foi realizada utilizando Jupyter Notebook e Pandas.

Foram desenvolvidas visualizações com Plotly para investigar:

- Evolução do desmatamento total ao longo dos anos.
- Desmatamento acumulado por estado.
- Evolução do desmatamento por estado.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone desmatamento_brasil
```

### 2. Acessar o diretório

```bash
cd projetoAv2
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o ETL

```bash
python -m src.etl
```

O arquivo tratado será gerado em `data/processed/`.

### 5. Executar a análise

Abra o notebook localizado em `notebooks/` utilizando Jupyter Notebook ou JupyterLab.

## Resultados

A análise exploratória identificou uma tendência de redução do desmatamento a partir do final da década de 2000, em comparação aos níveis observados nas décadas anteriores.

Também foi observada uma concentração expressiva do desmatamento acumulado nos estados do Pará e de Mato Grosso.

Esses resultados contribuem para a compreensão da evolução histórica e da distribuição territorial do desmatamento na Amazônia Legal.

## Licença

Este projeto está disponível sob a licença definida no arquivo `LICENSE`.
