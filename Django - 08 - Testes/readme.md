# 1. Testes

Testar um website é uma tarefa complexa, porque isto é composto de várias camadas de lógica – do tratamento de requisições no nível HTTP, consultas de modelos, validação e processamento de formulários, e renderização de template.

Para escrever um teste, você deriva de qualquer uma das classes base de teste de Django (ou unittest) (SimpleTestCase, TransactionTestCase, TestCase, LiveServerTestCase) e então escreve métodos separados para verificar se a funcionalidade específica funciona como esperado (testes usam métodos "assert" para testar se a expressão resulta em valores True ou False, ou se os dois valores são iguais, etc.). Quando você inicia a execução de um teste, o framework executa os métodos de teste escolhidos em suas classes derivadas. Os métodos de teste são executados independentemente, com configuração comum e/ou comportamento tear-down definido na classe.


- [1. Testes](#1-testes)
  - [1.1. Estrutura de Pastas](#11-estrutura-de-pastas)
  - [1.2. Lista de Asserts](#12-lista-de-asserts)
    - [1.2.1. Asserts Customizados Django](#121-asserts-customizados-django)
      - [1.2.1.1. assertFieldOutput(fieldclass, valid, invalid, field_args=None, field_kwargs=None, empty_value='')](#1211-assertfieldoutputfieldclass-valid-invalid-field_argsnone-field_kwargsnone-empty_value)
      - [1.2.1.2. assertFormsetError(resposta, formset, form_index, campo, erros, msg_prefix='')](#1212-assertformseterrorresposta-formset-form_index-campo-erros-msg_prefix)
      - [1.2.1.3. assertContains(response, text, count=None, status_code=200)](#1213-assertcontainsresponse-text-countnone-status_code200)
      - [1.2.1.4. assertNotContains(response, text, status_code=200)](#1214-assertnotcontainsresponse-text-status_code200)
      - [1.2.1.5. assertFormError(response, form, field, errors)](#1215-assertformerrorresponse-form-field-errors)
      - [1.2.1.6. assertTemplateUsed(response, template_name)](#1216-asserttemplateusedresponse-template_name)
      - [1.2.1.7. assertTemplateNotUsed(response, template_name)](#1217-asserttemplatenotusedresponse-template_name)
      - [1.2.1.8. assertURLEqual(url1, url2, msg_prefix='')](#1218-asserturlequalurl1-url2-msg_prefix)
    - [1.2.2. Exemplo Básico](#122-exemplo-básico)
  - [1.3. Cliente de Teste](#13-cliente-de-teste)
    - [1.3.1. Requisições](#131-requisições)
      - [1.3.1.1. get(path, data={}, **extra)](#1311-getpath-data-extra)
      - [1.3.1.2. post(path, data={}, content_type=MULTIPART_CONTENT, **extra)](#1312-postpath-data-content_typemultipart_content-extra)
      - [1.3.1.3. login(**credentials)](#1313-logincredentials)
      - [1.3.1.4. logout()](#1314-logout)
      - [1.3.1.5. cookies](#1315-cookies)
      - [1.3.1.6. session](#1316-session)
    - [1.3.2. Objeto Response](#132-objeto-response)
    - [1.3.3. Exemplo](#133-exemplo)
  - [1.4. TestCase](#14-testcase)
    - [1.4.1. TestCase.fixtures](#141-testcasefixtures)
  - [1.5. Teste de Modelos](#15-teste-de-modelos)
    - [1.5.1. Criar Objeto do Modelo Para Testes](#151-criar-objeto-do-modelo-para-testes)
    - [1.5.2. Testar Rótulos do Modelo](#152-testar-rótulos-do-modelo)
    - [1.5.3. Testar Atributos dos Campos do Modelo](#153-testar-atributos-dos-campos-do-modelo)
    - [1.5.4. Testar Métodos do Modelo](#154-testar-métodos-do-modelo)
  - [1.6. Teste de Formulários](#16-teste-de-formulários)
    - [1.6.1. Testar Dados do Formulário](#161-testar-dados-do-formulário)
    - [1.6.2. Testar Atributos dos Campos dos Formulários](#162-testar-atributos-dos-campos-dos-formulários)
    - [1.6.3. Testar HTML dos Formulários](#163-testar-html-dos-formulários)
    - [1.6.4. Testar Mensagens de Erros dos Formulários](#164-testar-mensagens-de-erros-dos-formulários)
  - [1.7. Teste de Modelos de Formulários](#17-teste-de-modelos-de-formulários)
    - [1.7.1. Testar Mensagem de Erro](#171-testar-mensagem-de-erro)
  - [1.8. Teste de Views](#18-teste-de-views)
    - [1.8.1. Testar a URL da View](#181-testar-a-url-da-view)
    - [1.8.2. Testar o Nome da URL da View](#182-testar-o-nome-da-url-da-view)
    - [1.8.3. Verificar o Template da View](#183-verificar-o-template-da-view)
    - [1.8.4. Verificar os Contextos da View](#184-verificar-os-contextos-da-view)
    - [1.8.5. Testar View Restritas](#185-testar-view-restritas)
    - [1.8.6. Testar Views com Formulários](#186-testar-views-com-formulários)
  - [1.9. Marcação de Testes](#19-marcação-de-testes)
  - [1.10. Executar testes](#110-executar-testes)
  - [1.11. API Model-Mommy](#111-api-model-mommy)
  - [1.12. Coverage](#112-coverage)

## 1.1. Estrutura de Pastas

Devemos criar uma pasta dentro da projeto, com um arquivo vazio chamado `__init__.py` para indicar que se trata de um pacote python. En seguida devemos criar junto 3 arquivos de testes, uma para testar nossos modelos, um para testar os formulários e por fim um arquivo de teste para testar as views.  

- /tests/
  - `__init__.py`
  - test_models.py
  - test_forms.py
  - test_views.py

## 1.2. Lista de Asserts

| Método                    | Descrição            |
| ------------------------- | -------------------- |
| assertEqual(a, b)         | a == b               |
| assertNotEqual(a, b)      | a != b               |
| assertTrue(x)             | bool(x) is True      |
| assertFalse(x)            | bool(x) is False     |
| assertIs(a, b)            | a is b               |
| assertIsNot(a, b)         | a is not b           |
| assertIsNone(x)           | x is None            |
| assertIsNotNone(x)        | x is not None        |
| assertIn(a, b)            | a in b               |
| assertNotIn(a, b)         | a not in b           |
| assertIsInstance(a, b)    | isinstance(a, b)     |
| assertNotIsInstance(a, b) | not isinstance(a, b) |

### 1.2.1. Asserts Customizados Django

Como numa classe Python `unittest.TestCase` normal que implementa métodos de asserção como `assertTrue` e `assertEquals`, a classe customizada TestCase do Django disponibiliza alguns métodos de asserção customizados que são úteis para testar aplicações Web.

- [Lista de Asserts Suportadas pelo Django](https://docs.djangoproject.com/en/3.2/topics/testing/tools/#assertions)


#### 1.2.1.1. assertFieldOutput(fieldclass, valid, invalid, field_args=None, field_kwargs=None, empty_value='')

- Afirma que um campo de forma se comporta corretamente com várias entradas.
- Parâmetros:	
    - `fieldclass` – a classe do campo a ser testado.
    - `valid` – um dicionário mapeando entradas válidas para seus valores limpos esperados.
    - `invalid` – um dicionário mapeando entradas inválidas para uma ou mais mensagens de erro levantadas.
    - `field_args` – os `args` passaram para instanciar o campo.
    - `field_kwargs` – os `kwargs` passaram para instanciar o campo.
    - `empty_value` – a saída limpa esperada para entradas em .empty_values
	- `self.assertFieldOutput(EmailField, {'a@a.com': 'a@a.com'}, {'aaa': ['Enter a valid email address.']})`

#### 1.2.1.2. assertFormsetError(resposta, formset, form_index, campo, erros, msg_prefix='')

Afirma que aumenta a lista de erros fornecidos quando `prestados.formset`
    - `formset` - é o nome que a instância foi dada no contexto do `modelo.Formset`
    - `form_index` - é o número do formulário dentro do . Se tiver um valor de erros não-forma (erros que você pode acessar via ) será verificado. `Formsetform_indexNoneformset.non_form_errors()`
    - `field` é o nome do campo no formulário para verificar. Se tiver um valor de erros não-campo (erros que você pode acessar via `form.non_field_errors()` será verificado.fieldNone
    - `errors` é uma sequência de erros, ou uma lista de sequências de erro, que são esperadas como resultado da validação do formulário.

#### 1.2.1.3. assertContains(response, text, count=None, status_code=200)

Testa se uma instância de `Response` produziu o `status_code` informado e que o `text` aparece no conteúdo da resposta. Se `count` é fornecido, `text` deve ocorrer exatamente `count` vezes na resposta.

#### 1.2.1.4. assertNotContains(response, text, status_code=200) 

Testa se uma instância de `Response` produziu o `status_code` informado e que o `text` **não** aparece no conteúdo da resposta.

#### 1.2.1.5. assertFormError(response, form, field, errors)

Testa se um campo no formulário lança a lista de erros fornecida quando gerado no formulário. 
    - `form` é o nome da instância de `Form` informada ao contexto do template.
    - `field` é o nome do campo no formulário para verificar. Se `field` tem um valor de `None`, erros não relacionados a campos (erros que você pode acessar via `form.non_field_errors()`) serão verificados.
    - `errors` é uma string de erro, ou uma lista de strings de erro, que são esperados como resultado da validação do formulário.

#### 1.2.1.6. assertTemplateUsed(response, template_name)

Testa se o template com o nome informado foi usado na geração da resposta. O nome é uma string como `'admin/index.html'`.

#### 1.2.1.7. assertTemplateNotUsed(response, template_name)

Teste se a resposta devolve um status de redirecionamento `status_code`, se redirecionou para a URL `expected_url` (incluindo quaisquer dados GET), e a página subseqüente foi recebida com o `target_status_code`

#### 1.2.1.8. assertURLEqual(url1, url2, msg_prefix='')

Afirma que duas URLs são as mesmas, ignorando a ordem dos parâmetros de sequência de consultas, exceto para parâmetros com o mesmo nome. Por exemplo, `./path/?x=1&y=2/` é igual a `path/?y=2&x=1/`, mas `path/?a=1&a=2/` não é igual a `path/?a=2&a=1`


### 1.2.2. Exemplo Básico

```Python
from django.test import TestCase

class YourTestClass(TestCase):
    def setUp(self):
        # O método é executada antes de cada método de teste.
        pass

    def tearDown(self):
        # O método é executado após cada método de teste.
        pass

    def test_algo_que_vai_passar(self):
        self.assertFalse(False)

    def test_algo_que_vai_falhar(self):
        self.assertTrue(False)

```

## 1.3. Cliente de Teste

- **Fontes**
- [O cliente de teste](https://django-portuguese.readthedocs.io/en/1.0/topics/testing.html#module-django.test.client)
  
O cliente de teste é uma classe Python que age como um navegador Web, permitindo a você testar suas views e interagir com suas aplicações feitas em Django programaticamente.

Algumas das coisas que você pode fazer com o cliente de teste são:

- Simular requisições GET e POST em uma URL e observar a resposta – tudo desde o nível baixo do HTTP (os cabeçalhos de resultado e códigos de status) até o conteúdo da página.
- Testar se a view correta é executada para uma dada URL.
- Testar que uma dada requisição é gerada por um determinado template, com um determinado contexto de template que contém certos valores.


O cliente de teste do Django tem um foco diferente. Em resumo:
- Use o cliente de teste do Django para atestar que a view correta está sendo chamada e que a view está recebendo os dados de contexto corretos.
- Use frameworks in-browser como Twill e Selenium para testar HTML gerados e comportamento de páginas Web, ou seja, funcionalidade JavaScript.

Note algumas coisas importantes sobre como o cliente de teste funciona:

- **O cliente de teste não requer que o servidor Web esteja rodando**. Aliás, ele rodará muito bem sem nenhum servidor Web!
- Ao acessar as páginas, lembre-se de especificar o caminho da URL, e não todo o domínio
  - CERTO: ``cliente.get('/login/')``
  - ERRADO: ``cliente.get('http://www.example.com/login/')``

```Python
from django.test import TestCase

class SimpleTest(TestCase):
    def test_details(self):
        response = self.client.get('/customer/details/')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.client.get('/customer/index/')
        self.assertEqual(response.status_code, 200)
```

### 1.3.1. Requisições

Uma vez que você tenha uma instância de `Client`, você pode chamar qualquer um dos seguintes métodos:

#### 1.3.1.1. get(path, data={}, **extra)

Faz uma requisição GET no `path` informado e devolve um objeto `Response`. Os pares de chave-valor no dicionário data são usados para criar os dados que serão enviados via GET. 
- `cliente.get('/customers/details/', {'name': 'fred', 'age': 7})`
  
Que resulta em: `/customers/details/?name=fred&age=7`

#### 1.3.1.2. post(path, data={}, content_type=MULTIPART_CONTENT, **extra)

Faz uma requisição POST no `path` informado e devolve um objeto `Response`. Os pares de chave-valor no dicionário data são usados para enviar os dados via POST.
- `cliente.post('/login/', {'name': 'fred', 'passwd': 'secret'})`

#### 1.3.1.3. login(**credentials)

Se seu site Django usa o sistema de autenticação e você precisa logar usuários, você pode usar o método `login()` do cliente de testes para simular o efeito de um usuário logando no site. Depois de chamar este método, o cliente de testes terá todos os cookies e dados de sessão necessários para passar a qualquer teste baseado em login que faça parte de uma view.

Você precisa **lembrar-se de criar contas de usuários antes de utilizar este método**. Pois o executor de testes utiliza uma base de dados de teste, que não contém usuários criados. 
- Você precisa criar os usuários como parte de sua test suite – tanto manualmente (utilizando a API de modelos do Django) ou com uma test fixture.

O formato do argumento credentials depende de qual backend de autenticação você está usando (que é configurado pelo parâmetro de configuração AUTHENTICATION_BACKENDS). Se você está usando o backend padrão de autenticação do Django (ModelBackend), credentials deve ser o nome do usuário e a senha, informados como argumentos nomeados:
- `cliente.login(username='fred', password='secret')`

#### 1.3.1.4. logout()

Se o seu site usa o sistema de autenticação do Django, o método `logout()` pode ser utilizado para simular o efeito de um usuário se deslogar do seu site.

Depois de chamar este método, o cliente de teste terá todos os cookies e dados de sessão retornados para os valores padrões. Requisições subsequentes parecerão vir de um usuário anônimo `AnonymousUser`.

#### 1.3.1.5. cookies

Um objeto `SimpleCookie`, contendo os valores atuais de todos os cookies do cliente. 

#### 1.3.1.6. session

Um objeto que se comporta como dicionário contendo informações da sessão.

### 1.3.2. Objeto Response

Especificamente, o objeto `Response` tem os seguintes atributos:
- `client` - O cliente de teste que foi usado para fazer a requisição que resultou na resposta.
- `content` - O corpo da resposta, como uma string. Este é o conteúdo final da página que foi gerada pela view, ou alguma mensagem de erro.
- `context` - A instância Context que foi utilizada pelo template para produzir o conteúdo da resposta. Se a página gerada utilizou múltiplos templates, então o context será uma lista de objetos Context, na ordem em que foram utilizados.
- `request` - Os dados da requisição que provocaram a resposta.
- `status_code` - O status da resposta HTTP, como um inteiro. 
- `template` - A instância de Template que foi utilizada para gerar o conteúdo final. Use template.name para obter o nome do arquivo do template, se o template foi carregado de um arquivo. (O nome é uma string como `'admin/index.html'`.)  Se a página gerada utilizou vários templates – ex: utilizando herança de templates – então template será uma lista de instâncias de Template, na ordem em que eles foram utilizados.

### 1.3.3. Exemplo 

```Python
import unittest
from django.test.client import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Cada teste precisa de um cliente.
        self.client = Client()

    def test_details(self):
        # Faz uma requisição GET.
        response = self.client.get('/customer/details/')

        # Verifica se a resposta foi 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Verifica se o contexto utilizado contém 5 customers.
        self.failUnlessEqual(len(response.context['customers']), 5)
```

## 1.4. TestCase

A melhor classe base para maioria dos testes é `django.test.TestCase.`

- Esta classe de teste **cria um banco de dados limpo antes dos testes serem executados**, e executa todas as funções de teste em sua própria transação.
- A classe também possui um `Client` de teste, que você pode utilizar para **simular um usuário interagindo com o código no nível de view**.
- Testes que necessitam de uma base de dados (nomeadamente, testes de modelo) não usarão seu banco de dados 'real' (produção). Um banco de dados vazio é criado em separado para os testes.
- Independentemente de os testes passarem ou falharem, o banco de dados de teste é destruído quando todos os testes forem executados.
- Por padrão, o nome deste banco de dados de teste é o valor da configuração `DATABASE_NAME` adicionando o prefixo `test_`
- Independentemente do valor do DEBUG do seu arquivo de configuração, todos os testes do Django rodam com `DEBUG=False`. Isto é para assegurar que a saída observada de seu código seja igual ao da aplicação em produção.

###  1.4.1. TestCase.fixtures

- Fontes
  - [Fixture loading](https://docs.djangoproject.com/pt-br/3.2/topics/testing/tools/#topics-testing-fixtures)
  - [Fornecendo dados iniciais para modelos.](https://docs.djangoproject.com/pt-br/3.2/howto/initial-data/)
  - [TestCase.fixtures](https://django-portuguese.readthedocs.io/en/1.0/topics/testing.html#django.test.TestCase.fixtures)

Um teste para um site Web com banco de dados não tem muita utilidade se não existir dados no banco. Para facilitar a carga destes dados no banco, a classe TestCase do Django proporciona uma maneira de carregar fixtures.

- Uma fixture é uma coleção de dados que o Django sabe como importar para um banco de dados. Por exemplo, se o seu site tem contas de usuários, você pode configurar uma fixture de usuários no intuito de popular seu banco durante os testes.

- **Você armazenará este dado em um diretório fixtures dentro de sua aplicação**
  - Por padrão, o Django procura por “fixtures” no diretório fixtures dentro de cada app. Você definir a `FIXTURE_DIRS` como uma lista de diretórios adicionais onde o Django deve procurar.
  - Quando chamar `manage.py loaddata`, você pode especificar um caminho para o arquivo de “fixture”, o qual é procurado no lugar dos diretórios usuais.

```JSON
[
  {
    "model": "myapp.person",
    "pk": 1,
    "fields": {
      "first_name": "John",
      "last_name": "Lennon"
    }
  },
  {
    "model": "myapp.person",
    "pk": 2,
    "fields": {
      "first_name": "Paul",
      "last_name": "McCartney"
    }
  }
]
```

Uma vez que você criou uma fixture e colocou em algum lugar em seu projeto Django, você pode utilizá-la nos seus testes unitários especificando um atributo de classe fixtures na sua subclasse de `django.test.TestCase`

```Python
from django.test import TestCase
from myapp.models import Animal

class AnimalTestCase(TestCase):
    fixtures = ['mammals.json', 'birds']

    def setUp(self):
        # Definições de testes como anteriormente.

    def testFluffyAnimals(self):
        # Um teste que usa fixtures.
```

Algumas observações

- No início de cada test case, antes de `setUp()` ser rodado, o Django limpará o banco de dados, retornando um banco de dados no estado que estava diretamente após a chamada de `syncdb`.
- Em seguida, todas as fixtures nomeadas são instaladas. Nesse exemplo, o Django instalará qualquer fixture JSON chamada mammals, seguida por qualquer fixture chamada birds
- Esse procedimento de limpeza/carga é repetido para cada teste no test case, então você pode ter certeza de que o resultado de um teste não será afetado por outro teste, ou pela ordem de execução dos testes.

## 1.5. Teste de Modelos

- **Fontes**
  - [Testing](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Testing)
- O modelo de Exemplo 

```Python 
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
```

Para testar um modelo devemos importar a biblioteca `TestCase` e os modelos que desejamos testar. Em Seguida, devemos criar a classe testadora que irá herdar a classe TestCase. 

```Python
from django.test import TestCase
from catalog.models import Author

class AuthorModelTest(TestCase):
    pass
```

### 1.5.1. Criar Objeto do Modelo Para Testes

No início do teste, podemos criar um objeto do modelo, atribuindo características relevantes do mesmo, que serão usadas para os demais métodos possam usá-lo em seus testes. 
- Podemos criar um ou vários modelos de testes. 

```Python
from django.test import TestCase
from catalog.models import Author

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Big', last_name='Bob')
```

### 1.5.2. Testar Rótulos do Modelo

1. Podemos testar os rótulos criados pelo modelo, para isso devemos pesquisar o objeto criado: `author = Author.objects.get(id=1)`.
2. Devemos selecionar o campo pelo seu nome de variável e extrair a label do campo com o '`verbose_name`': `author._meta.get_field('field_name').verbose_name`
3. Por fim, devemos verificar se o label do campo retornado na etapa 2 é igual ao esperado: `self.assertEquals(field_label, 'label')`

```Python
from django.test import TestCase
from catalog.models import Author

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_date_of_death_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')
```

### 1.5.3. Testar Atributos dos Campos do Modelo

Podemos verificar se os atributos de um campo do modelo foram argumentados corretamente. 

1. Devemos pesquisar o objeto criado: `author = Author.objects.get(id=1)`.
2. Devemos selecionar o campo pelo seu nome de variável e extrair o atributo que desejamos: `author._meta.get_field('field_name').atributo`
3. Por fim, devemos verificar o valor atribuído ao atributo do campo retornado na etapa 2 é igual ao esperado: `self.assertEquals(atributo_retornado, valor_esperado)`

```Python
from django.test import TestCase
from catalog.models import Author

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)  
```

### 1.5.4. Testar Métodos do Modelo

Também precisamos testar nossos métodos personalizados. Eles, essencialmente, apenas verificam se o nome do objeto foi construído como esperamos

1. Devemos pesquisar o objeto criado: `author = Author.objects.get(id=1)`.
2. Podemos ou não trabalhar a possível resposta do método a ser testado e armazená-la em uma variável. 
3. Por fim, devemos verificar retornado pelo método é igual ao valor esperado. `self.assertEquals(atributo_retornado, valor_esperado)`


```Python
from django.test import TestCase
from catalog.models import Author

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(), '/catalog/author/1')
```

## 1.6. Teste de Formulários

A filosofia para testar seus forms é a mesma que para testar seus models; você precisa testar qualquer coisa que tenha codificado ou seu projeto especifica, mas não o comportamento do framework subjacente e outras bibliotecas de terceiros

### 1.6.1. Testar Dados do Formulário

Caso queiramos testar se um conjunto de dados é válido ou não em um formulário, podemos seguir as seguintes etapas

1. Criar um dicionário com os dados para o formulário, onde a chave deve ser a mesma usada pelo campo do formulário: `{'name': 'something'}` 
2. Devemos criar um objeto do formulário passando o dicionário como argumento: `MyForm(data=form_data)`
3. Por fim, devemos verificar se o formulário é válido: `self.assertTrue(form.is_valid())`

```Python
from django.test import TestCase
from myapp.forms import MyForm

class MyTests(TestCase):
    def test_forms(self):
        form_data = {'something': 'something'}
        form = MyForm(data=form_data)
        self.assertTrue(form.is_valid())
```

### 1.6.2. Testar Atributos dos Campos dos Formulários

Podemos testar os valores  para os atributos dos campos, como os campos `label` e `help_text`. Precisamos testar se o valor do `label` é `None`, porque mesmo que o Django processe o `label` correto, retornará `None` se o valor não estiver definido explicitamente.

1. Temos que criar um formulário vazio: `form = RenewBookForm()`
2. Temos que acessar o campo usando o dicionário de campos especificando qual atributos queremos pegar o valor. `form.fields['renewal_date'].atributo`
3. Por fim, devemos verificar se o valor contido dentro do atributo é o valor esperado. 

```Python
from django.test import TestCase
from catalog.forms import RenewBookForm

class RenewBookFormTest(TestCase):
    def test_renew_form_date_field_label(self):
        form = RenewBookForm()
        self.assertTrue(form.fields['renewal_date'].label == None or form.fields['renewal_date'].label == 'renewal date')

    def test_renew_form_date_field_help_text(self):
        form = RenewBookForm()
        self.assertEqual(form.fields['renewal_date'].help_text, 'Enter a date between now and 4 weeks (default 3).')
```

### 1.6.3. Testar HTML dos Formulários

Os formulários possuem funções que retornam diferentes estruturas de HTML como `form.as_p()` torna o formulário como HTML usando elementos Ps.

Formulário

```Python
class ItemForm(forms.Form):
    item_text = forms.CharField(
        widget=forms.fields.TextInput(attrs={
            'placeholder': 'Enter a to-do item',
            ​'class': 'form-control input-lg',
        }),
    )
```

Teste
```Python
from django.test import TestCase
from lists.forms import ItemForm

class ItemFormTest(TestCase):

    def test_form_item_input_has_placeholder_and_css_classes(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())
```

### 1.6.4. Testar Mensagens de Erros dos Formulários

Existem algumas possibilidades de se testar mensagens de erros gerados pelos campos, abaixo, podemos ver algumas destas maneiras.

```Python
password = forms.RegexField(
    max_length=254,
    error_messages={
        'required': _('This is required.') 
        'invalid': _('It is invalid.')
    }
)
```

```Python
self.assertFalse(form.is_valid())
self.assertIn('password', form.errors.keys())
self.assertIn('It is invalid', form.errors['password'])
self.assertEqual(form.errors['password'][0], 'It is invalid')
```

## 1.7. Teste de Modelos de Formulários

Os formulários estão sempre em conjunto com algum modelo, pois os formulários são sempre usados para entrada de dados para os banco de dados. Abaixo tem um modelo de formulário que será usado nos exemplos a seguir.

- Exemplos completos podem ser acessador em [Simple Form](https://www.obeythetestinggoat.com/book/chapter_simple_form.html)

```Python
from django import forms
from lists.models import Item

class ItemForm(forms.models.ModelForm):
    class Meta:
        ​model = Item
        ​fields = ('text',)
        ​widgets = {
            ​'text': forms.fields.TextInput(attrs={
                ​'placeholder': 'Enter a to-do item',
                ​'class': 'form-control input-lg',
            ​}),
        ​}
        ​error_messages = {
            ​'text': {'required': "You can't have an empty list item"}
        }       ​
```

### 1.7.1. Testar Mensagem de Erro 

1. Temos que criar um modelo de formulário com um dicionário de dados: `form = ModelForm(data={'text': ''})`
2. Após isso queremos que o formulário NÃO sej a válido `self.assertFalse(form.is_valid())`
3. Por fim, devemos verificar se o valor contido dentro do atributo de erro é igual ao valor esperado. 

```Python
def test_form_validation_for_blank_items(self):
    form = ItemForm(data={'text': ''})
    self.assertFalse(form.is_valid())
    self.assertEqual(
        form.errors['text'],
        ["You can't have an empty list item"]
    )
```

## 1.8. Teste de Views

Para validar o comportamento das nossas views, utilizamos Client de teste do Django. Essa classe funciona como um navegador web fictício que podemos usar para simular requisições GET and POST em uma URL e observar a resposta. 

Uma visão que lista 10 autores por página. 

```Python
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10
```

### 1.8.1. Testar a URL da View

Para testar se a URL existe ou está correta, podemos usar um método GET passando o caminho. Em seguida, basta verificar se o objeto Response retornado contém o código de sucesso.  

```Python
def test_view_url_exists_at_desired_location(self):
    response = self.client.get('/catalog/authors/')
    self.assertEqual(response.status_code, 200)
```

### 1.8.2. Testar o Nome da URL da View

Para verificar se a view pode ser acessada pelo apelido atribuída para a visão no arquivo URLs como argumento para a função reverse. 

```Python
def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
```

### 1.8.3. Verificar o Template da View

Para testar qual templete é usado pela View, basta solicitar uma requisição GET para o apelido ou caminho da View, em seguida basta comparar o nome do objeto Response Retornado. 

```Python
def test_view_uses_correct_template(self):
    response = self.client.get(reverse('authors'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'catalog/author_list.html')
```

### 1.8.4. Verificar os Contextos da View

Podemos testar também o contexto retornado por uma view, para isto, basta fazer uma solicitação GET para a View, e verificar se o objeto desejado está no contexto da View. 

Também podemos verificar, o valor contido dentro do contexto, se é condizente com o que a página deveria retorna como resposta. 

No exemplo estamos usando uma View que retorna uma página com uma lista de 10 Autores, além disto a View usa uma ClassBasedView do tipo de Paginação, ou seja, ela irá criar automaticamente páginas para os demais autores, caso hajam mais de 10 autores a serem listados. 

```Python

class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_authors = 13

        for author_id in range(number_of_authors):
            Author.objects.create(
                first_name=f'Christian {author_id}',
                last_name=f'Surname {author_id}',
            )

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['author_list']) == 10)

    def test_lists_all_authors(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('authors')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['author_list']) == 3)
```

### 1.8.5. Testar View Restritas

Em alguns casos, você desejará testar uma view que é restrita apenas aos usuários logados. E neste contexto precisamos criar um usuário e registrá-lo no banco de dados temporário. 

```Python
class LoanedBookInstancesByUserListViewTest(TestCase):
    def setUp(self):
        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()
```

Neste contexto devemos testar o redirecionamento dos usuários, caso ele esteja logado ou não. Para simular um **usuário não logado** devemos apenas fazer uma solicitação GET para a página restritas e verificar se a URL redirecionada é condizente com o contexto de login. 

```Python
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('my-borrowed'))
        self.assertRedirects(response, '/accounts/login/?next=/catalog/mybooks/')
```

Para simularmos um usuário autenticado devemos chamar o método **login** do objeto cliente, sem seguida devemos fazer uma solicitação GET para a página restrita verificando no contexto da resposta o nome do usuário, se a solicitação obteve sucesso. Além disto, ainda podemos verificar o templete usado. 

```Python
def test_logged_in_uses_correct_template(self):
    login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
    response = self.client.get(reverse('my-borrowed'))

    self.assertEqual(str(response.context['user']), 'testuser1')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'catalog/bookinstance_list_borrowed_user.html')
```


### 1.8.6. Testar Views com Formulários

https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Testing


## 1.9. Marcação de Testes 

Você pode marcar seus testes para que você possa executar facilmente um subconjunto específico. Podemos rotular os testes, e ao executar os testes podemos especificar qual subconjunto queremos testar. 

```Python
from django.test import tag

class SampleTestCase(TestCase):

    @tag('fast')
    def test_fast(self):
        ...

    @tag('slow')
    def test_slow(self):
        ...

    @tag('slow', 'core')
    def test_slow_but_core(self):
        ...
```

Você também pode marcar um caso de teste:

```Python
@tag('slow', 'core')
class SampleTestCase(TestCase):
    ...
```

Subclasses herdam tags de superclasses, e métodos herdam tags de sua classe. dado:

```Python
@tag('foo')
class SampleTestCaseChild(SampleTestCase):

    @tag('bar')
    def test(self):
        ...
```

SampleTestCaseChild.test será rotulado com 'slow', 'core', 'bar' e 'foo'.

## 1.10. Executar testes

O comando para executar todos os testes dentro do projeto é:

> python manage.py test

O parâmetro `--verbosity` com os argumentos entre 0, 1, 2, e 3 que definem os níveis de detalhamento da saída do teste.

Se você deseja executar um subconjunto de seus testes, você pode fazer isso especificando o caminho completo para o(s) pacote(s), módulos, subclasse TestCase ou método:

```shell
# Run the specified module
python manage.py test catalog.tests

# Run the specified module
python manage.py test catalog.tests.test_models

# Run the specified class
python manage.py test catalog.tests.test_models.YourTestClass

# Run the specified method
python manage.py test catalog.tests.test_models.YourTestClass.test_one_plus_one_equals_two
```

## 1.11. API Model-Mommy

- [Model Mommy](https://model-mommy.readthedocs.io/en/latest/basic_usage.html)

> pip install model-mommy

Model Mommy é usado para criar objetos de forma aleatória respeitando as características e restrições dos objetos. . Ele é extremamente útil para testes, pois facilita na criação dos objetos, principalmente objetos que precisam que outros objetos sejam instanciados, como um livro precisa de um autor. Neste caso o Model Mommy irá criar um objeto autor aleatoriamente para criar um objeto livre. 


Exemplo de um Modelo 

```Python
class Kid(models.Model):
    happy = models.BooleanField()
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    bio = models.TextField()
    wanted_games_qtd = models.BigIntegerField()
    birthday = models.DateField()
    appointment = models.DateTimeField()

    class Meta:
        verbose_name = _(u'Kid')
        verbose_name_plural = _(u'Kids')

    def __unicode__(self):
        return u'%s' % (self.name)

class Dog(models.Model):
    owner = models.ForeignKey('Kid')       
```

Parar criar um objeto do modelo, basta usar o método 'make' passando o Modelo importando.
 
```Python
from django.test import TestCase
from model_mommy import mommy
from .models import Kid

class KidTestModel(TestCase):
    def setUp(self):
        self.kid = mommy.make(Kid)
```

E ainda fica melhor, a mommy permite criar objetos sem necessariamente importá-lo. Caso o modelo seja único em todas as aplicações do sistema, basta especificar o nome entre aspas 'Modelo' e o mommy irá fazer todo o trabalho. 

Caso haja mais de um modelo com o mesmo nome entre as aplicações, deve especificar de qual a aplicação a mommy deve usar 'app.Model'.

```Python
from django.test import TestCase
from model_mommy import mommy

class KidTestModel(TestCase):
    def setUp(self):
        self.kid = mommy.make("Kid")
```

No exemplo abaixo, o Cachorro tem uma criança com seu dono (**ForeignKey**), ou seja, precisaríamos ter que criar uma criança para então criar um objeto cachorro. Mas a mommy já faz tudo isto de forma automática. 

```Python
from django.test import TestCase
from model_mommy import mommy

class DogTestModel(TestCase):
    def setUp(self):
        self.rex = mommy.make('family.Dog')

```

Caso você queria que o **objeto criado tenha algum atributo específico**, e não um valor aleatório, basta passá-lo como parâmetro. 

```Python
class KidTestModel(TestCase):
    def setUp(self):
        self.kid = mommy.make(Kid, age=3)
        self.another_kid = mommy.make('family.Kid',age=6)
```

Atributos de objetos relacionados também são alcançáveis pelo nome ou nomes relacionados:

```Python
class DogTestModel(TestCase):
    def setUp(self):
        self.bobs_dog = mommy.make('family.Dog', owner__name='Bob')
```

Para **criar várias instâncias** do modelo, você pode usar o parâmetro `_quantity`:

```Python
kids = mommy.make('family.Kid', _quantity=3)
```


**Criando arquivos** - Mamãe não cria arquivos para tipos fileField. Se você precisar ter os arquivos criados, você pode passar o flag _create_files=True (padrão para False) para mommy.make ou mommy.make_recipe. Importante: A mommy não faz nenhum tipo de limpeza de arquivo, então cabe a você excluir os arquivos criados por ele.


## 1.12. Coverage

`Coverage.py` é uma ferramenta para medir a cobertura de código de programas Python. Ele monitora seu programa, observando quais partes do código foram executadas, então analisa a fonte para identificar o código que poderia ter sido executado, mas não foi.

A medição da cobertura é normalmente usada para medir a eficácia dos testes. Ele pode mostrar quais partes do seu código estão sendo exercidas por testes, e quais não são.

> pip install coverage

Após a instalação do coverage precisamos criar um arquivo (no mesmo nível do arquivo manage.py) chamado `.coveragerc` que será usado como um arquivo de configuração do coverage. 

Dentro do arquivo digite a sintaxe, ela irá fazer com que ele execute apenas dentro do projeto, além de ignorar os demais arquivos dentro da aplicação. 

```txt
[run]
source = .

omit =
    */__init__.py
    */settings.py
    */manage.py
    */wsgi.py
    */apps.py
    */urls.py
    */admin.py
    */migrations/*
    */tests/*
```

Para rodar os testes usamos o comando

> coverage run manage.py test

Para gerar um relatório simplificado do que foi e o que não foi testado, usamos o comando

> coverage report

Para gerar um  relatório personalizado em HTML mais descritivo, podendo ver trechos destacados do que ainda não foi testado, usamos o comando

> coverage html

O comando acima irá gerar uma pasta chamada `htmlcov` com os arquivos HTML do relatório gerado. Para visualizar o relatório, acessamos a pasta `cd htmlcov/` e executamos o servidor embutido do Python WEB com o comando

> python -m http.server