# 1. Django Conceitos Básicos

- Django é um framework web Python de alto nível que permite o rápido desenvolvimento de sites seguros e de fácil manutenção.
- É gratuito e de código aberto, tem uma comunidade próspera e ativa, ótima documentação e muitas opções de suporte gratuito e pago. 
- Características
  - Completo - Fornece quase tudo que um desenvolvedor precisa para trabalhar.
  - Versátil - Pode ser utilizado para qualquer tipo de serviço, trabalha com qualquer frameworks de front-end, além de trabalhar com qualquer formato de arquivo, como HTML, XML, JSON, etc. 
  - Seguro - Possui um sistema de contas de usuário embutido, possui proteção contra SQL-Injection, cross-site scripting, cross-site request forgery e "clickjacking".
  - Escalável - Possui uma separação clara das suas funcionalidades, podendo extender suas funcionalidades e módulos com facilidade.  
  - Sustentável - O código do Django é escrito usando princípios de design e padrões que encorajam a criação de código sustentável (que facilita a manutenção) e reusável.
  - Portátil - Django é escrito em Python, que executa em muitas plataformas. Isso significa que você não esta preso em nenhuma plataforma de servidor em particular, e pode executar seus aplicativos em muitas distribuições do Linux, Windows e Mac OS X.

## 1.1. Sumário

- [1. Django Conceitos Básicos](#1-django-conceitos-básicos)
  - [1.1. Sumário](#11-sumário)
- [2. Configurando um ambiente de desenvolvimento Django](#2-configurando-um-ambiente-de-desenvolvimento-django)
  - [2.1. Instalando Python 3](#21-instalando-python-3)
  - [2.2. Ambiente Virtual](#22-ambiente-virtual)
  - [2.3. Instalando o Django](#23-instalando-o-django)
- [3. Primeira Execução](#3-primeira-execução)


# 2. Configurando um ambiente de desenvolvimento Django

- O ambiente de desenvolvimento é uma instalação do Django em seu computador local para que você use-o para desenvolver e testar apps Django antes de implementá-los em um ambiente de produção

## 2.1. Instalando Python 3

```properties
sudo apt install python3-pip
python3 -V
```

## 2.2. Ambiente Virtual

No VSCode será necessário instalar e iniciar o ambiente virtual com o virtualenv dentro da pasta em que iremos trabalhar. Após a instalação da ferramenta poderemos criar uma pasta chamada env, e por fim poderemos carregar o ambiente virtual.

```properties
pip install virtualenv
virtualenv -p python env
./env/Scripts/activate  
```
Exitem outras formas de instalar e trabalhar com ambientes virtuais, como o venv que já vem como padrão dentro do python3, ou então usando o pyenv.

```properties
python -m venv env
./env/Scripts/activate  
```

Pode ser necessário atualizar o pip

```properties
python -m pip install --upgrade pip
```

## 2.3. Instalando o Django

Após instalar e iniciar o ambiente virtual, podemos executar o comando abaixo para instalar o django dentro do nosso ambiente.

```properties
pip install Django
```

Para verificar a versão e ver se a instalação ocorreu corretamente, execute o comando

```properties
python -m django --version
```


# 3. Primeira Execução

Após a instalação do Django, iremos executar um sequência de comandos:

1. Iniciaremos o projeto Django dentro da pasta pasta atual ( caso queria criar uma subpasta remova o ponto).

```properties
django-admin startproject projeto .
```

2. Criaremos um arquivo chamado requirements.txt, que conterá as bibliotecas usadas no projeto.

```properties
cd projeto/ (caso usou o .)
pip freeze > requirements.txt
```

3. Criaremos uma aplicação chamada core (pode ser qualquer nome que desejar)

```properties
cd projeto/ (caso não tenha entrado)
django-admin startapp core
```

4. Iremos executar o projeto (na mesma pasta em que contém o arquivo chamado manage.py).

```properties
python manage.py runserver
```

5. Por fim, basta abrir a página inicial do Django em http://127.0.0.1:8000/.




