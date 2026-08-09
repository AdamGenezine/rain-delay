# Rain Delay

Análise do impacto das condições meteorológicas nos atrasos de voos partindo de aeroportos brasileiros utilizando inferência causal.

## Objetivo

Investigar o efeito causal de condições meteorológicas, especialmente chuva, sobre o atraso na partida de voos no Brasil.

O projeto utilizará **Double Machine Learning (DoubleML)** para controlar fatores que também podem influenciar atrasos e estimar o efeito do clima sobre a pontualidade dos voos.

## Dados

### Voos

Dados de Voo Regular Ativo (VRA) disponibilizados pela ANAC.

Período analisado:

- 2022
- 2023
- 2024
- 2025

A base contém informações como:

- aeroporto de origem e destino
- companhia aérea
- horário previsto e realizado
- situação do voo
- modelo da aeronave

### Aeroportos

Cadastro de aeródromos públicos da ANAC utilizado para identificar aeroportos brasileiros e obter suas coordenadas geográficas.

### Clima

Dados meteorológicos históricos serão obtidos através da Open-Meteo Historical Weather API.

## Metodologia

O pipeline do projeto será composto por:

```text
ANAC VRA
   ↓
Preprocessamento dos voos
   ↓
Identificação dos aeroportos brasileiros
   ↓
Dados meteorológicos
   ↓
Construção do dataset analítico
   ↓
Análise exploratória
   ↓
Double Machine Learning
   ↓
Estimativa do efeito causal
```

## Estrutura

```text
rain-delay/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── scripts/
├── src/
│   └── rain_delay/
├── tests/
├── pyproject.toml
└── requirements.txt
```

## Status

🚧 Projeto em desenvolvimento.