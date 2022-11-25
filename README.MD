# Celery APP

A Aplicação foi feita utilizando a:
api: https://www.weatherbit.io/api
Celery: https://docs.celeryq.dev/en/stable/
Existe um limite diário permitido de requisições (1500).

## Objetivo

Esta aplicação foi criada com o intuito de obter informações de previsões temporais de todos os concelhos de Portugal de modo assíncrono para preencher uma base de dados não relacional (mongodb).
Com o preenchimento prévio da base, o objetivo principal é disponibilizar os dados para que a API possa consumir.

## Informações sobre a aplicação

As dependências da aplicação que é o mongodb, broker e o rabbitmq que estão disponiveis através do docker com imagens oficiais recomendadas pela documentação, o Celery utiliza o rabbitMQ como broker das tarefas e um mongodb para armazenamento dos dados finais.

sendo assim é necessário possuir o docker na máquina para que consiga utiliziar a aplicação

# Utilizando a aplicação

## Disponibilizando dependências (Containers)

Clonando repositório:

```bash
git clone https://github.com/LuAugusto/Celery-application.git
```

Para utilizar a aplicação é necessário dispor os containers

```bash
python3 -m venv venv
```

Ativando venv -> Linux

```bash
source venv/bin/activate
```

Ativando venv -> Windows

```bash
venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

```bash
docker-compose build
```

```bash
docker-compose up
```

```bash
Porta: 5000
http://localhost:5000
```

Após iniciar os containers o celery iniciara o trabalho de verificar nossa base de dados para preencher dados
ausentes ou até mesmo preencher toda a base caso não exista nenhum dado na nossa base.

o Celery esta programado para fazer uma varredura todos os dias à meia-noite para que nossa base de dados
permaneça atualizada, todo esse processamento é feito de modo assíncrono para cada localidade (concelhos de
Portugal).

Podemos consumir a API, visto que esse processamento esta sendo feito de modo assíncrono, mas pode exigir um tempo até que nossa base de dados esteja completa.

## Endpoints:

    ```bash
    Port: 5000
    get: /
        description: retorna todas as localidades disponiveis


    get: /locations/sunrises/earlier/<day>
        day:
            type: number
            example: 28
        description: retorna os 10 concelhos em que o sol nasce mais cedo para um dia escolhido pelo utilizador

    get: /locations/wind
        description:
            os 10 concelhos com menos vento por dia (uma média dos 5 dias)

    get  /locations/average/temperature/<city>
        city:
            type: string
            example: Aveiro
        description:
            média da temperatura mínima e máxima para cada dia (nos próximos 5 dias) para um
            concelho escolhido pelo utilizador

    ```
