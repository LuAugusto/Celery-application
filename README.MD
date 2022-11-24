# Celery APP

A Aplicação foi feita utilizando a api: https://www.weatherbit.io/api
Existe um limite diário permitido de requisições (1500).

## Objetivo

Esta aplicação foi criada com o intuito de obter informações de previsões temporais de todos os concelhos de Portugal de modo assíncrono para preencher uma base de dados não relacional (mongodb).
Com o preenchimento prévio da base, o objetivo principal é disponibilizar os dados para que uma API possa consumir.

## Informações sobre a aplicação

As dependências da aplicação que é o mongodb e o rabbitmq que estão disponiveis através do docker com imagens oficiais recomendadas pela documentação, o Celery utiliza o rabbitMQ como broker das tarefas e um mongodb para armazenamento dos dados finais.

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
docker-compose up
```

## Preenchendo previamente a base de dados com informações de previsões temporais com o Celery

Executando nosso worker para que o celery esteja pronto para receber tasks:
Obs: Esse comando deixa o terminal em modo 'attached' para visualizar o trabalho do worker.

```bash
celery -A task worker -l info --pool=solo
```

Adicionando task manualmente :

```bash
python app.py
```

Após o comando a task será adicionada a fila e será executada assim que nosso worker estiver livre.

## Cronjob diário

A aplicação esta programada para realizar atualizações na base de dados para completar informações.
Para que o Celery consiga iniciar o trabalho com tarefas agendadas podemos utilizar o comando:
(É necessário que nosso worker esteja executando)

```bash
celery -A task beat -l info
```

O Celery esta programado para executar a task diariamente à meia-noite.
Mas caso queira visualizar o funcionamento basta executar de forma manual
como:

```bash
python app.py
```

Após isso o nosso worker vai iniciar um trabalho com nossas tasks.
Cada tarefa é executada de modo assíncrono para cada localidade.

Podemos ver o andamento das nossas tasks no terminal ou
podemos utilizar um software para visualizar nossa base de dados com mais clareza, recomendações:
robo3t ou mongo compass.

Visto que o mongo é executado nosso container docker, podemos conectar na URL: mongodb://localhost:27017
