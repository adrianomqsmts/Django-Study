# 1. Modelos de Banco de Dados

Aplicativos Django acessam e gerenciam dados através de objetos Python chamados de modelos (models). Modelos definem a estrutura dos dados armazenados, incluindo os tipos de campos e possivelmente também o seu tamanho máximo, valores default, opções de listas de seleção, texto de ajuda para documentação, texto de labels para formulários, etc.

Tudo ocorre de forma independente com o banco de dados, pois tudo é abstraído, ou seja, pode escolher qualquer banco de dados, desde que devidamente configurado nas configurações. 

- [1. Modelos de Banco de Dados](#1-modelos-de-banco-de-dados)
  - [1.1. Configurando o MySQL](#11-configurando-o-mysql)
  - [1.2. Configurando o PostGre](#12-configurando-o-postgre)
- [2. ORM (Object-Relational-Mapping)](#2-orm-object-relational-mapping)
  - [2.1. Principais Campos](#21-principais-campos)
  - [2.2. Os principais parâmetros dos campos](#22-os-principais-parâmetros-dos-campos)
  - [2.3. Tipos de Relacionamentos em Models](#23-tipos-de-relacionamentos-em-models)
    - [2.3.1. Relacionamento 1:1 - OneToOne](#231-relacionamento-11---onetoone)
    - [2.3.2. Relacionamento 1:N - ForeignKey](#232-relacionamento-1n---foreignkey)
    - [2.3.3. Relacionamento N:N ManyToMany](#233-relacionamento-nn-manytomany)
  - [2.4. Herança de modelos](#24-herança-de-modelos)
  - [2.5. Classes e métodos para os nossos modelos](#25-classes-e-métodos-para-os-nossos-modelos)
  - [2.6. Gerando os bancos de dados](#26-gerando-os-bancos-de-dados)
  - [2.7. ORM - Consultas](#27-orm---consultas)
    - [2.7.1. objects.create - Criando um objeto e salvando no banco de dados](#271-objectscreate---criando-um-objeto-e-salvando-no-banco-de-dados)
    - [2.7.2. objects.all() - Encontrando um ou vários objetos](#272-objectsall---encontrando-um-ou-vários-objetos)
    - [2.7.3. objects.only() - Consultando apenas alguma colunas](#273-objectsonly---consultando-apenas-alguma-colunas)
    - [2.7.4. objects.values().distinct() - Selecionado apenas os dados distintos](#274-objectsvaluesdistinct---selecionado-apenas-os-dados-distintos)
    - [2.7.5. Limit e Offset - Consultando um número específico de linhas](#275-limit-e-offset---consultando-um-número-específico-de-linhas)
    - [2.7.6. objects.get - Recuperando um único Objeto](#276-objectsget---recuperando-um-único-objeto)
    - [2.7.7. objects.filter - Filtrando a consulta de dados](#277-objectsfilter---filtrando-a-consulta-de-dados)
      - [2.7.7.1. Filtrando pelos operadores de comparação](#2771-filtrando-pelos-operadores-de-comparação)
      - [2.7.7.2. Filtrando com o operador Between](#2772-filtrando-com-o-operador-between)
      - [2.7.7.3. Filtrando com o operador LIKE](#2773-filtrando-com-o-operador-like)
      - [2.7.7.4. Filtrando com o operador IN](#2774-filtrando-com-o-operador-in)
      - [2.7.7.5. Filtrando com o operador AND](#2775-filtrando-com-o-operador-and)
      - [2.7.7.6. Filtrando com o operador OR](#2776-filtrando-com-o-operador-or)
      - [2.7.7.7. Filtrando com o operador NOT](#2777-filtrando-com-o-operador-not)
      - [2.7.7.8. Filtrando com o operador NULL](#2778-filtrando-com-o-operador-null)
      - [2.7.7.9. Filtrando com o operador NOT NULL](#2779-filtrando-com-o-operador-not-null)
    - [2.7.8. objects.order_by - Ordenando consultas](#278-objectsorder_by---ordenando-consultas)
    - [2.7.9. UPDATE](#279-update)
    - [2.7.10. DELETE](#2710-delete)
      - [2.7.10.1. Funções SQL - MIN, MAX, AVG, SUM E COUNT](#27101-funções-sql---min-max-avg-sum-e-count)
    - [2.7.11. GROUP BY](#2711-group-by)
      - [2.7.11.1. HAVING](#27111-having)
    - [2.7.12. Consultas Personalizadas](#2712-consultas-personalizadas)
      - [2.7.12.1. Passando parâmetros para consultas personalizadas](#27121-passando-parâmetros-para-consultas-personalizadas)
      - [2.7.12.2. Referências completas de ORM Django](#27122-referências-completas-de-orm-django)
  - [2.8. Exemplo de Views e Models](#28-exemplo-de-views-e-models)
      - [2.8.0.1. Rota produto](#2801-rota-produto)
  - [ModelForms](#modelforms)
    - [O Método Save](#o-método-save)
    - [Especificando Campos do Modelo no Formulário](#especificando-campos-do-modelo-no-formulário)
    - [Alterar Tipo do Campo Model-Form](#alterar-tipo-do-campo-model-form)
    - [Herança de Formulário](#herança-de-formulário)
    - [Alterando Widgets](#alterando-widgets)
    - [Passando Valores Iniciais](#passando-valores-iniciais)

Algumas bibliotecas podem ser importantes:

- **PyMySQL** - Driver do servidor de conexão python-mysql
- **dj_database_url** - Responsável por configurar o banco em produção. Usado para transmitir os dados do banco de dados local para o heroku
- **psycopg2.binary** - É o responsável pelo bando PostGreeSQL

## 1.1. Configurando o MySQL

Altere o arquivo **settings** dentro do projeto, caso ocorra algum erro, acesse: [Erro no Django com a conexão MySQL](https://pt.stackoverflow.com/questions/395744/erro-no-django-2-2-conex%C3%A3o-com-o-mysql)

```Django
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'django2',
        'USER': 'root',
        'PASSWORD': 'SENHA',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## 1.2. Configurando o PostGre

```Django
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fusion',
        'USER': 'root',
        'PASSWORD': 'Senha',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

ou então

```Django
DATABASES = {
    'default': dj_database_url.config()
}
```

# 2. ORM (Object-Relational-Mapping)

Todos os nossos modelos devem ser guardados dentro do arquivo **models** dentro da aplicação, que deve ser nossa única fonte de dados.

```Django
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

Este modelo acima, irá gerar a seguinte tabela no banco de dados:

```SQL
CREATE TABLE myapp_person (
    "id" NOT NULL PRIMARY KEY,
    "first_name" VARCHAR(30) NOT NULL,
    "last_name" VARCHAR(30) NOT NULL
);

```

OBS: Como pode observar, o campo ID é gerado automaticamente, mas pode ser sobrescrito caso necessário.

## 2.1. Principais Campos

- **CharField** é usado para definir um tamanho fixo (médio a curto) para a string. Você deve especificar o max_length (tamanho máximo) para o dado que será armazenado.
- **TextField** é usado para grandes strings de comprimento variado. Você pode especificar um max_length (tamanho máximo) para o campo, mas isso é usado somente quando o campo é exibido em formulários (forms) (ele não é imposto no nível do banco de dados).
- **IntegerField** é um campo para armazenar números inteiros e para validar valores inseridos como números inteiros em formulários.
- **DateField** e **DateTimeField** são usados para armazenar/representar datas e informações de data/hora. Esses campos também podem declarar os parâmetros (mutuamente exclusivos) auto_now = True (para definir o campo para a data atual toda vez que o modelo é salvo), auto_now_add (para definir a data em que o primeiro modelo foi criado) e default (para definir uma data padrão que pode ser substituída pelo usuário).
- **EmailField** é usada para armazenar e validar em endereço de email.
- **FileField** e **ImageField** são usados para carregar arquivos e imagens respectivamente, (o ImageField simplesmente valida de forma adicional que o arquivo enviado é uma imagem). Eles têm parâmetros para definir como e onde os arquivos enviados são armazenados.
- **AutoField** é um tipo especial de IntegerField que é incrementada automaticamente. Uma chave primária desse tipo é adicionada de forma automática ao seu modelo, se você não especificar explicitamente um.
- **ForeignKey** é usado para especificar um relacionamento um-para-muitos com outro modelo do banco de dados (por exemplo, um carro tem um fabricante, mas um fabricante pode fazer muitos carros). O lado "um" do relacionamento é o modelo que contém a "chave" (os modelos que contêm uma "chave estrangeira" referem-se a essa "chave" e estão no lado "muitos" de tal relacionamento).
- **ManyToManyField** é usado para especificar um relacionamento muitos-para-muitos (por exemplo, um livro pode ter vários gêneros e cada gênero pode conter vários livros). Em nosso aplicativo de biblioteca, usaremos isso de maneira muito semelhante às ForeignKeys, mas elas podem ser usadas de maneiras mais complicadas para descrever as relações entre os grupos. Eles têm o parâmetro on_delete para definir o que acontece quando o registro associado é excluído (por exemplo, um valor de models.SET_NULL simplesmente definiria o valor como NULL).

##  2.2. Os principais parâmetros dos campos

- **null** - Se **True** permite valores vazios para o campo
- **blank** - Se **True** permite valores em branco para o campo
- **choices** - Uma sequência que consiste em iteráveis ​​de exatamente dois itens (por exemplo, [(A, B), (A, B) ...]) para usar como opções para este campo, gerando para o campo uma caixa de seleção.
- **db_column** - O nome da coluna do banco de dados a ser usado para este campo. Se não for fornecido, Django usará o nome do campo.
- **db_index** - Se for **True**, um índice de banco de dados será criado para este campo.
- **default** - Define um valor padrão para o campo.
- **editable** - Se **False**, o campo não será exibido no admin ou em qualquer outro ModelForm. Eles também são ignorados durante a validação do modelo. O padrão é **True**.
- **error_messages** - O argumento error_messages permite que você substitua as mensagens padrão que o campo irá gerar. Passe um dicionário com chaves que correspondam às mensagens de erro que você deseja substituir.
- **help_text** - Texto extra de ajuda para ser mostrado com o “widget” do formulário. É útil para documentar mesmo que seu campo não seja usado em um formulário.
- **primary_key** - Se **True**, este campo será a chave-primária do seu model
- **unique** - Se ***True***, este campo deve ser único dentro da tabela
- **unique_for_date**, **unique_for_month**, **nique_for_year** - Defina como o nome de um DateField ou DateTimeField para exigir que este campo seja exclusivo para o valor do campo de data.
- **verbose_name** - Um nome legível para o campo. Se o nome detalhado não for fornecido, o Django o criará automaticamente usando o nome do atributo do campo, convertendo sublinhados em espaços.
- **validators** - Uma lista de validadores a serem executados para este campo. 

Os principais campos podem ser acessados em [Tipos de campos](https://docs.djangoproject.com/en/dev/ref/models/fields/#field-types)

## 2.3. Tipos de Relacionamentos em Models

### 2.3.1. Relacionamento 1:1 - OneToOne

O relacionamento 1-1 define que um item de uma entidade só poderá se relacionar com um item de outra entidade e o inverso também será verdade. Como exemplo podemos supor que na regra de negócio um determinado cliente pode ter apenas um único endereço, e o endereço pode estar atribuído a um único cliente.

```python
class Endereco(models.Model):
    # Definimos seus atributos

class Cliente(models.Model):
    # Definimos seus atributos
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
```

### 2.3.2. Relacionamento 1:N - ForeignKey

Um relacionamento 1-N define que um item de uma tabela pode se relacionar com vários itens de uma outra tabela, mas que o inverso não seja verdade. Um exemplo seria um cliente que pode fazer vários pedidos, mas cada pedido pode estar relacionado a um único cliente.

```python
class Endereco(models.Model):
    # Definimos seus atributos

class Pedido(models.Model):
    # Definimos seus atributos
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, related_name='pedidos')

class Cliente(models.Model):
    # Definimos seus atributos
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
```

### 2.3.3. Relacionamento N:N ManyToMany

O relacionamento NN define que um item de uma tabela pode se relacionar com vários itens de uma outra tabela e vice-versa. Um exemplo seria um produto que pode ser vendido em vários pedidos e consequentemente vários pedidos poderão ter o mesmo produto. 

```python
class Endereco(models.Model):
    # Definimos seus atributos

class Pedido(models.Model):
    # Definimos seus atributos
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, related_name='pedidos')
    produtos = models.ManyToManyField(Produto)

class Produto(models.Model):
    # Definimos seus atributos

class Cliente(models.Model):
    # Definimos seus atributos
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
```


-> O Exemplo completo pode ser acessado em: [Relacionamento 1-1, 1-N e N-N com Django](https://www.treinaweb.com.br/blog/relacionamento-1-1-1-n-e-n-n-com-django/)

## 2.4. Herança de modelos

Podemos herdar um modelo em outro, como se fosse uma base para evitar repetir muitos os dados que são  comuns em vários modelos. A referência completa de herança pode ser acessa em [Model inheritance](https://docs.djangoproject.com/en/dev/topics/db/models/#model-inheritance)

```python
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
```

## 2.5. Classes e métodos para os nossos modelos

Métodos muitas vezes retornam (return) algo. Um exemplo disto é o método __str__() que irá retornar um nome significativo para o modelo, podendo ser o nome completo do usuário, ou uma combinação de colunas do modelo.

Os métodos podem assumir várias funcionalidades extras para o modelo, como calcular_desconto  ou realizar algum tratamento de dados antes de salvar no banco de dados.

 Referência completa pode ser acessada em: [Model methods](https://docs.djangoproject.com/en/dev/topics/db/models/#model-methods)

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
```
O exemplo acima pode ser visto com  mais detalhes em: [Models em views](https://tutorial.djangogirls.org/pt/django_models/)

```python
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='blogpost')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
```

Também é comum sobrescrever a classe **meta** (uma classe interna em modelos Django) que funciona como contêiner de classe com algumas opções (metadados) anexadas ao modelo. 

A classe define permissões disponíveis, nome da tabela de banco de dados associada, se o modelo é abstrato ou não, versões no singular e plural do nome, etc. Para saber mais acesse: [Meta](https://docs.djangoproject.com/en/dev/topics/db/models/#meta-options) ou então [Meta Completo](https://docs.djangoproject.com/en/dev/ref/models/options/)


```python
class Cargo(models.Model):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo
```

Um dos recursos mais úteis desses metadados é controlar a ordem padrão dos registros retornados, quando você consulta o tipo de modelo. Você faz isso especificando a ordem de correspondência em uma lista de nomes para ordenar (ordering) o atributo. A ordem dependerá do tipo de campo (os campos de caractere são classificados em ordem alfabética, enquanto os campos de data são classificados em ordem cronológica). Como mostrado acima, você pode prefixar o nome do campo com um símbolo de menos (-) para inverter a ordem de classificação.

```
ordering = ['title', '-pubdate']
```


## 2.6. Gerando os bancos de dados

Para gerar os bancos de dados precisamos executar o comando **makemigrations**. Este comando irá gerar um histórico do banco e manter a integridade entre as versões. Após os testes de integridade forem checados, devemos usar o comando **migrate** para gerar as tabelas do banco. Podemos também especificar o nome de aplicação caso necessário, ao invés de executar para todas todas. 

```python
>>python manage.py makemigrations
>>python manage.py migrate
```
## 2.7. ORM - Consultas

Podemos usar uma API para acessar os dados do nosso modelo, que contém diversas abstrações de comandos que nos permitem trabalhar com os objetos, principalmente dentro de uma view.

### 2.7.1. objects.create - Criando um objeto e salvando no banco de dados

O comando objects.create executa um comando SQL INSERT por detrás dos panos. O Django não acessa o banco de dados até que você chame explicitamente o método save(). O método save() não retorna um valor. Para criar e salvar um objeto em um único passo, use o método create(). 

[Criando Objetos](https://docs.djangoproject.com/pt-br/dev/ref/models/querysets/#create)

```python
p = Person.objects.create(first_name="Bruce", last_name="Springsteen")
```

ou [Salvando objetos](https://docs.djangoproject.com/pt-br/dev/ref/models/instances/#saving-objects)

```python
p = Person(first_name="Bruce", last_name="Springsteen")
p.save(force_insert=True)
```

Comando SQL
```SQL
INSERT INTO Person VALUES('Mano', '23', 'male')
```

Comando Django
```Python
Person.objects.create(name="Mano", age="23", gender="male")
```

### 2.7.2. objects.all() - Encontrando um ou vários objetos

A maneira mais simples de recuperar objeto de uma tabela é pegar todos eles. Para fazer isso, use o método all() na Manager:

    A Manager é a principal fonte de QuerySets para um modelo. Por exemplo, Blog.objects.all() retorna uma QuerySet que contém todos os objetos do tipo Blog do banco de dados.

    Os Managers são acessíveis somente através das classes de modelo, e não de instâncias de modelos, para reforçar a separação entre operações no “nível das tabelas” e operações no “nível dos registros”.

```python
all_entries = Person.objects.all()
```

É equivalente à algo do tipo:

```SQL
SELECT * FROM Person;
```

Exemplo: 

```python
persons = Person.objects.all()

for person in persons:
    print(person.name)
    print(person.gender)
    print(person.age)
```

### 2.7.3. objects.only() - Consultando apenas alguma colunas

Comando em SQL
```SQL
SELECT name, age FROM Person;
```
Comando em Django
```python
Person.objects.only('name', 'age')
```

### 2.7.4. objects.values().distinct() - Selecionado apenas os dados distintos
Consulta SQL
```SQL
SELECT DISTINCT name, age FROM Person;
```
Comando Django
```python
Person.objects.values('name', 'age').distinct()
```

### 2.7.5. Limit e Offset - Consultando um número específico de linhas

Entretanto podemos limitar as consultas de uma consulta, que pode ser usada para criar, por exemplo, o conceito de **PAGINAÇÃO**. Se um subconjunto da syntax de fatias de array Python para limitar seu QuerySet para um certo número de resultados. Este é o equivalente às cláusulas SQL Limit e OFFSET.

Comando SQL
```SQL
SELECT * FROM Person LIMIT 5;
SELECT * FROM Person OFFSET 5 LIMIT 5;
```

Comando Django
```python
Limit5 = Person.objects.all()[:5]
offset5_limit5 = Person.objects.all()[5:10]
```
### 2.7.6. objects.get - Recuperando um único Objeto

O filter() sempre lhe dará um QuerySet, mesmo se um único objeto combina com a consulta - neste caso, ele será uma QuerySet que contém um único elemento.Se você sabe que somente um objeto combina com sua consulta, você pode usar o método get() em uma Manager o qual retorna o objeto diretamente:

```python
one_entry = Entry.objects.get(pk=1)
```

### 2.7.7. objects.filter - Filtrando a consulta de dados

Para criar o subconjunto, você refina o QuerySet inicial, adicionando filtros de condições. As duas maneiras mais comuns de refinar um QuerySet são:

- filter(**kwargs)
    - Retorna uma nova QuerySet contendo objetos que combinem com os parâmetros de filtros dados.
- exclude(**kwargs)
    - Retornam uma nova QuerySet contendo objetos que não combinem com os parâmetros de filtros dados. 

```python
selected_entries = Entry.objects.filter(pub_date__year=2006)
no_selected_entries = Entry.objects.all().filter(pub_date__year=2006)
```
O resultado de um refinamento de uma QuerySet é ela mesma: uma QuerySet, tal que é possível encadear refinamentos. Por exemplo:

```python
selected_entries = Entry.objects.filter( headline__startswith='What').exclude(pub_date__gte=datetime.date.today()).filter(pub_date__gte=datetime.date(2005, 1, 30))
```
    QuerySets são preguiçosos (“lazy”) – o ato de criar uma QuerySet não envolve nenhuma atividade no banco de dados. Você pode empilhar filtros o dia inteiro, e o Django não irá executar a consulta realmente até que a QuerySet seja interpretada.

Comando SQL
```SQL
SELECT * FROM Person WHERE id = 1
```

Comando Django
```Django
Person.objects.filter(id=1)
```


#### 2.7.7.1. Filtrando pelos operadores de comparação

Comandos SQL
```SQL
WHERE age > 18;
WHERE age >= 18;
WHERE age < 18;
WHERE age <= 18;
WHERE age != 18;
```

Comandos Django
```Python
Person.objects.filter(age__gt=18)
Person.objects.filter(age__gte=18)
Person.objects.filter(age__lt=18)
Person.objects.filter(age__lt3=18)
Person.objects.exclude(=18)
```

#### 2.7.7.2. Filtrando com o operador Between

Comandos SQL
```SQL
SELECT * FROM Person WHERE age BETWEEN 10 AND 20;
```

Comandos Django
```Python
Person.objects.filter(age__range=(10,20))
```

#### 2.7.7.3. Filtrando com o operador LIKE

Comandos SQL
```SQL
WHERE name LIKE '%A%';
WHERE name LIKE 'A%';
WHERE name LIKE '%A';
```

Comandos Django
```Python
Person.objects.filter(name__icontains='A')
Person.objects.filter(name__istartswith='A')
Person.objects.filter(name__iendswith='A')
```

#### 2.7.7.4. Filtrando com o operador IN

Comandos SQL
```SQL
WHERE id IN (1,2);
```

Comandos Django
```Python
Person.objects.filter(id__in=[1,2])
```

#### 2.7.7.5. Filtrando com o operador AND

Comandos SQL
```SQL
SELECT * FROM PERSON WHERE gender='male' AND age > 25;
```

Comandos Django
```Python
Person.objects.filter(gander='male', age__gt=25)
```

#### 2.7.7.6. Filtrando com o operador OR

Comandos SQL
```SQL
SELECT * FROM PERSON WHERE gender='male' OR age > 25;
```

Comandos Django
```Python
FROM django.db.models import Q
Person.objects.filter(Q(gander='male') | Q(age__gt=25))
```

#### 2.7.7.7. Filtrando com o operador NOT

Comandos SQL
```SQL
SELECT * FROM PERSON WHERE NOT gender='male';
```

Comandos Django
```Python
Person.objects.exclude(gander='male')
```

#### 2.7.7.8. Filtrando com o operador NULL

Comandos SQL
```SQL
SELECT * FROM PERSON WHERE age IS NULL;
```

Comandos Django
```Python
Person.objects.filter(age__isnull=True)
# OU 
Person.objects.filter(age=None)
```

#### 2.7.7.9. Filtrando com o operador NOT NULL

Comandos SQL
```SQL
SELECT * FROM PERSON WHERE age IS NOT NULL;
```

Comandos Django
```Python
Person.objects.filter(age__isnull=False)
# OU 
Person.objects.exclude(age=None)
```

PARA VER MAIS POSSIBILIDADES E EXEMPLOS ACESSE [Field lookups](https://docs.djangoproject.com/en/dev/ref/models/querysets/#field-lookups)

### 2.7.8. objects.order_by - Ordenando consultas

Podemos usar o OrderBy para ordenar nossas consultas, de forma descendente (-), ascendente(padrão), de forma aleatória (?) ou dentre outras formas. [ORDER BY](https://docs.djangoproject.com/en/dev/ref/models/querysets/#order-by) 

```python
Entry.objects.filter(pub_date__year=2005).order_by('-pub_date', 'headline')
Entry.objects.order_by('?')
```

Comando SQL
```SQL
SELECT * FROM Person ORDER BY age;
SELECT * FROM Person ORDER BY age DESC;
```

Comando Django
```python
Person.objects.order_by('age')
Person.objects.order_by('-age')
```

### 2.7.9. UPDATE

Comando SQL
```SQL
UPDATE Person SET age = 20 WHERE id = 1;
#Múltiplas Linhas
UPDATE Person SET age = age * 1.5ç
```

Comando Django
```Python
person = Person.objects.get(id=1)
person.age = 20
person.save
# Múltiplas linhas
from django.db.models import F
Person.objects.update(age=F('age')*1.5)
```


### 2.7.10. DELETE

Comando SQL
```SQL
DELETE FROM Person;
DELETE FROM Person WHERE age < 10;
```

Comando Django
```Python
Person.objects.all().delete()
Person.objects.filter(age_lt=10).delete()
```

#### 2.7.10.1. Funções SQL - MIN, MAX, AVG, SUM E COUNT

```SQL
SELECT MIN(age) FROM Person;
SELECT MAX(age) FROM Person;
SELECT AVG(age) FROM Person;
SELECT SUM(age) FROM Person;
SELECT COUNT(*) FROM Person;
```

Comando Django
```Python
from django.db.models import Min, Max, Avg, Sum

Person.objects.all().aggregate(Min('age'))
{'age__min': 0}

Person.objects.all().aggregate(Max('age'))
{'age__max': 100}

Person.objects.all().aggregate(Sum('age'))
{'age__sum': 5050}

Person.objects.all().count()
```

### 2.7.11. GROUP BY

```SQL
SELECT gender, COUNT(*) AS count FROM Person GROUP BY gender;
```

Comando Django
```Python
Person.objects.values('gender').annotate(count=Count('gender'))
```

#### 2.7.11.1. HAVING
```SQL
SELECT gender, COUNT(*) AS count FROM Person GROUP BY gender HAVING count > 1;
```

Comando Django
```Python
Person.objects.values('gender').annotate(count=Count('gender')).values('gender', 'count').filter(count_gt=1)
```

### 2.7.12. Consultas Personalizadas

O ORM ainda nos permite consultas de SQL em estado BRUTO, para podermos realizar consultas mais complexas, ou até mesmo, se quisermos evitar ter que aprender SQL de outra forma.

```Python
Person.objects.raw('SELECT * FROM myapp_person')
Person.objects.raw('SELECT id, first_name, last_name, birth_date FROM myapp_person')
Person.objects.raw('SELECT last_name, birth_date, first_name, id FROM myapp_person')
```

#### 2.7.12.1. Passando parâmetros para consultas personalizadas

Existem cuidados que devemos tomar, e mais opções de personalizações que podem ser acessadas em 
[Passing parameters into raw()](https://docs.djangoproject.com/en/dev/topics/db/sql/#passing-parameters-into-raw)

```python
lname = 'Doe'
>>> Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])
```


#### 2.7.12.2. Referências completas de ORM Django

- [Consultas](https://docs.djangoproject.com/en/dev/topics/db/queries/)
- [QuerySet API reference](https://docs.djangoproject.com/en/dev/ref/models/querysets/)
- [Como funciona o ORM do Django](https://www.gilenofilho.com.br/como-funciona-o-orm-do-django/)
- [Performing raw SQL queries](https://docs.djangoproject.com/en/dev/topics/db/sql/)

## 2.8. Exemplo de Views e Models

- urls.py
```python
from .views import index, produto

urlpatterns = [
    path('', index),
    path('contact', contact),
    ## Iremos gerar um rota com um inteiro que que é o ID do produto como /produtos/1
    path('produtos/<int:pk>', produto, name = 'produto'),
]
```

- models.py
```python
class Produto(models.Model):
  #models.tipoDeDados CharField("label", tamanho máximo)
  nome = models.CharField('Nome', max_length=100)
  #decimal_places = quantidade de casas decimais e max_digits é a quantidade de dígitos máximo
  preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
  estoque = models.IntegerField('Quantidade em estoque')
  #Apresenta o objeto instanciado pelo nome dele no admin
  def __str__(self):
    return self.nome
```

- views.py
```python
from .models import Produto

def index(request):
  #Dados do Models
  produtos = Produto.objects.all()
  context = {
    'produtos' : produtos
  }
  return render(request, 'index.html', context)
```

- index.html
```Django
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">

  <head>
    <title>Django</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <link rel="stylesheet" href="{% static 'css/estilos.css' %}">
  </head>

  <body>
    <table>
      <thead>
        <tr>
          <th>Produto</th>
          <th>Preço</th>
        </tr>
      </thead>
      <tbody>
        {% for produto  in produtos  %}
        <tr>
          <td><a href="{% url 'produto' produto.id %}">{{produto.nome}}</a></td>
          <td>{{produto.preco}}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
<button onclick="teste();">CLIQUE!</button>
<script src="{% static 'js/script.js' %}"></script>
  </body>
</html>
```

#### 2.8.0.1. Rota produto

- views.py
```python
def produto(request, pk):
  produtos = Produto.objects.get(id=pk)
  context = {
    'produto' : produtos
  }
  return render(request, 'produto.html', context)
```

- produto.html

```Django
<!DOCTYPE html>
<html lang="pt-bt">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
      <table>
      <thead>
        <tr>
          <th>Produto</th>
          <th>Preco</th>
          <th>Estoque</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{produto.nome}}</td>
          <td>{{produto.preco}}</td>
          <td>{{produto.estoque}}</td>
        </tr>
      </tbody>
    </table>
</body>
</html>
```
## ModelForms

Se você está construindo uma aplicação baseada em banco de dados, existe uma grande chance de que seus formulários corresponderão com os seus modelos Django. Neste caso, seria redundante definir os tipos de campo no seu formulário, porque isso já foi feito no seu modelo. Por este motivo, o Django disponibiliza uma classe de ajuda que possibilita a criação de uma classe Form a partir de um modelo Django.

FONTE (Criando formulários a partir de models)[https://django-portuguese.readthedocs.io/en/1.0/topics/forms/modelforms.html]

**Possui os mesmos campos e atributos que os formulários, com algumas observações!**
- ForeignKey é representado por django.forms.ModelChoiceField, que é um ChoiceField em que choices é um QuerySet do modelo.
- ManyToManyField é representado por django.forms.ModelMultipleChoiceField, que é um MultipleChoiceField em que choices é um QuerySet do modelo.
- O atributo label do campo de formulário será igual ao verbose_name do campo de modelo, com o primeiro caractere em maiúsculo
- Se um campo de modelo tem blank=True, então o valor de required será False no campo de formulário. Caso contrário, required=True.
- O help_text do campo de formulário é igual ao help_text do campo de modelo.
- Se o campo de modelo tem o atributo choices definido, então o widget do campo de formulário será o Select, com a lista de opções vindas do atributo choices do campo de modelo. As opções normalmente incluirão o valor em branco, que é selecionado por padrão. Se o campo é requerido, isso força o usuário a fazer uma escolha. O valor em branco não será incluído se o campo de modelo tem atributo blank=False e um valor de default explícito (em vez disso o valor de default será selecionado inicialmente).

Exemplos:

Arquivo models.py
```Python
from django.db import models

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

```

Arquivo forms.py

```Python
from django.forms import ModelForm

class AuthorForm(ModelForm):
    class Meta:
        model = Author

class BookForm(ModelForm):
    class Meta:
        model = Book
```

### O Método Save

Este método `save()` aceita um argumento nomeado opcional commit, que aceita ou True ou False. Se você chamar `save()` com commit=False, então ele devolverá um objeto que ainda não foi gravado no banco de dados. Neste caso, é sua responsabilidade chamar `save()` na instância de modelo. Isso é útil se você quer fazer algum processamento customizado no objeto antes de gravá-lo, ou se você quer usar um umas das opções de gravação de modelo especializadas. commit é True por padrão.

### Especificando Campos do Modelo no Formulário

Em alguns casos, você não quer que todos os campos do modelo apareçam no formulário gerado. Existem três maneiras de dizer ao ModelForm para usar somente alguns campos do modelo:

1. Coloque `editable=False` no campo do modelo. Como resultado, qualquer formulário criado via ModelForm não incluirá este campo.
2. Use o atributo fields da classe interna `Meta` do ModelForm. Esse atributo, se especificado, deve ser uma lista de nomes de campos a serem incluídos no formulário.
3. Use o atributo exclude da classe interna `Meta` do ModelForm. Esse atributo, se especificado, deve ser uma lista de nomes de campos a serem excluídos do formulário.
  
Exemplos

```Python
class PartialAuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'title')

class PartialAuthorForm(ModelForm):
    class Meta:
        model = Author
        exclude = ('birth_date',)
```

### Alterar Tipo do Campo Model-Form

Os tipos de campos padrão, Mas o ModelForm te dá a flexibilidade de mudar o campo de formulário para um determinado campo de modelo. Para alterar o tipo, basta declarar o campo novamente no formulário, parar sobrescreve-lo. 

```Python
class ArticleForm(ModelForm):
  pub_date = MyDateFormField()

  class Meta:
    model = Article
```

### Herança de Formulário

Como nos formulários básicos, você pode extender e reutilizar ModelForms através da herança. Isso é útil se você precisa declarar campos ou métodos adicionais em uma classe pai para uso em alguns formulários derivados de modelos. 

### Alterando Widgets 

Podemos especificar um dicionário com o nome dos campos e qual widgets queremos alterar no campo 

```Python
class CommentCreationForm(forms.ModelForm):

  class Meta:
    model = Comment
    fields = ('author', 'body', 'post')

    widgets = {
      'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'type': 'hidden'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
      'post': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'type': 'hidden'}),
    }
```

### Passando Valores Iniciais 

Podemos passar valores como parâmetros para os ModelsForms através do método construtor INIT. 

Extraída somente as partes relevantes dos exemplos. 

```Python
class CommentCreationForm(forms.ModelForm):

  def __init__(self, user, post, *args, **kwargs):
    super(CommentCreationForm, self).__init__(*args, **kwargs)
    self.fields['author'].initial = user.pk
    self.fields['post'].initial = post.pk
```

View

```Python
class CommentCreateView(CreateView):

  def get_form_kwargs(self):
    form = super().get_form_kwargs()
    form['user'] = self.request.user
    form['post'] = Post.objects.get(pk=self.kwargs['pk'])
    return form
```
