<h1 align="center">
    📣 <a href="https://gerenciador-anuncios.herokuapp.com/" alt="Sistema gerenciador de anúncios"> Gerenciador de anúncios </a>
</h1>

<h3 align="center">
    Desafio lançado pela Academia Capgemini / Proway
</h3>
<br>

<img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">

</p>

📜 Tabela de conteúdos
=================
<!--ts-->
   * [Sobre o projeto](#sobre-o-projeto)
   * [Funcionalidades](#-funcionalidades)
   * [Como executar o projeto](#-como-executar-o-projeto)
     * [Pré-requisitos](#user-content--pré-requisitos)
     * [Executando o projeto](#user-content--executando-o-projeto)
     * [Executando os testes](#user-content--executando-os-testes)
   * [Tecnologias](#-tecnologias)
     * [Ambiente de desenvolvimento](#user-content-ambiente-de-desenvolvimento)
     * [Backend](#user-content--backend)
     * [Fontend](#user-content--frontend)
   * [Autor](#-autor)
   * [Licença](#user-content--licença)
<!--te-->

---

## 💻 Sobre o projeto

🏆 Projeto desenvolvido para o desafio de seleção da [Capgemini Brasil](http://capgemini.proway.com.br/). Clique [aqui](https://gerenciador-anuncios.herokuapp.com/) para acessá-lo.

![](https://i.imgur.com/2MEjGW2.png)

---

## ⚙️ Funcionalidades

- [x] Cadastro de Clientes:
  - [x] Adicionar um novo cliente
  - [x] Exibir detalhes do cliente
  - [x] Editar um cliente
  - [x] Excluir um cliente
  - [x] Listar clientes

- [x] Cadastro de Anúncios:
  - [x] Adicionar um novo anúncio
  - [x] Exibir detalhes do anúncio
  - [x] Editar um anúncio
  - [x] Excluir um anúncio
  - [x] Listar anúncios

- [x] Relatório:
  - [x] Exibir listagem de anúncios com estimativas de:
    - [x] Valor total investido
    - [x] Total de visualizações recebidas
    - [x] Total de cliques convertidos
    - [x] Total de compartilhamentos conquistados
  - [x] Filtrar anúncios por cliente
  - [x] Filtrar anúncios por intervalo de datas

---

##  Como executar o projeto

### 🚨 Pré-requisitos

Antes de começar, você vai precisar ter as seguintes ferramentas instaladas em sua máquina:
[Git](https://git-scm.com/downloads), [Docker](https://docs.docker.com/engine/install/) e [Docker Compose](https://docs.docker.com/compose/install/).


#### 🎮 Executando o projeto

```bash

# Clone este repositório
$ git clone https://github.com/diogo-alves/gerenciador_anuncios.git

# Acesse a pasta do projeto no terminal/cmd
$ cd gerenciador_anuncios

# Execute este comando para iniciar os servidores web e de banco de dados
$ docker-compose up -d

# Aplique as migrations do django para criar a estrutura do banco de dados
$ docker-compose exec web python manage.py migrate

# Acesse o sistema pelo seu navegador usando o endereço http://localhost:8000

```

#### 🤔 Executando os testes

```bash
# Com os servidores rodando, digite o seguinte comando
$ docker-compose exec web python manage.py test
```

---

## ⚒ Tecnologias

Neste projeto optei por utilizar as seguintes tecnologias:


#### **Ambiente de desenvolvimento**

-   **[Docker](https://docs.docker.com/engine/install/)**
-   **[Docker Compose](https://docs.docker.com/compose/install/)**
-   **[Pipenv](https://pypi.org/project/pipenv/)**
-   **[Git](https://git-scm.com/downloads)**


#### **Backend**

-   **[Python](https://www.python.org/)**
-   **[Django](https://www.djangoproject.com/)**
-   **[PostgreSQL](https://www.postgresql.org/)**
-   **[python-decouple](https://pypi.org/project/python-decouple/)**
-   **[django-tables2](https://pypi.org/project/django-tables2/)**
-   **[django-filter](https://pypi.org/project/django-filter/)**
-   **[django-crispy-forms](https://pypi.org/project/django-crispy-forms/)**
-   **[crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/)**

#### **Frontend**

-   **[HTML5](https://developer.mozilla.org/pt-BR/docs/Web/Guide/HTML/HTML5)**
-   **[CSS3](https://developer.mozilla.org/pt-BR/docs/Web/CSS)**
-   **[Javascript](https://getbootstrap.com/docs/5.0/getting-started/introduction/)**
-   **[Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)**
-   **[Bootstrap Icons](https://icons.getbootstrap.com/)**
-   **[Fonte Nunito](https://fonts.google.com/specimen/Nunito)**
-   **[Plugin Inputmask](https://github.com/RobinHerbots/Inputmask)**

---

## 👷 Autor

<a href="https://www.linkedin.com/in/diogoalvesti/">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/diogo-alves" width="100px;" alt=""/>
 <br />
 <sub><b>Diogo Alves</b></sub></a> <a href="https://www.linkedin.com/in/diogoalvesti/" title="Diogo Alves"></a>
 <br />

[![Twitter Badge](https://img.shields.io/badge/-@diogo_dev-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=twitter.com%2Fdiogo_dev)](https://twitter.com/diogo_dev) [![Linkedin Badge](https://img.shields.io/badge/-diogoalvesti-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/diogoalvesti/)](https://www.linkedin.com/in/diogoalvesti/)
[![Gmail Badge](https://img.shields.io/badge/-diogo.alves.ti@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:diogo.alves.ti@gmail.com)](mailto:diogo.alves.ti@gmail.com)

---

## 📝 Licença

Este projeto está sob a licença [MIT](./LICENSE).

Feito com ❤️ por Diogo Alves 👋 [Entre em contato!](https://www.linkedin.com/in/diogoalvesti/)
