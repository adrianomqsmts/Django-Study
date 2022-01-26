# 1. Django 

- Django é um framework web Python de alto nível que permite o rápido desenvolvimento de sites seguros e de fácil manutenção.
- É gratuito e de código aberto, tem uma comunidade próspera e ativa, ótima documentação e muitas opções de suporte gratuito e pago. 
- Características
  - Completo - Fornece quase tudo que um desenvolvedor precisa para trabalhar.
  - Versátil - Pode ser utilizado para qualquer tipo de serviço, trabalha com qualquer frameworks de front-end, além de trabalhar com qualquer formato de arquivo, como HTML, XML, JSON, etc. 
  - Seguro - Possui um sistema de contas de usuário embutido, possui proteção contra SQL-Injection, cross-site scripting, cross-site request forgery e "clickjacking".
  - Escalável - Possui uma separação clara das suas funcionalidades, podendo extender suas funcionalidades e módulos com facilidade.  
  - Sustentável - O código do Django é escrito usando princípios de design e padrões que encorajam a criação de código sustentável (que facilita a manutenção) e reusável.
  - Portátil - Django é escrito em Python, que executa em muitas plataformas. Isso significa que você não esta preso em nenhuma plataforma de servidor em particular, e pode executar seus aplicativos em muitas distribuições do Linux, Windows e Mac OS X.

*********************************************

**********************************************

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

## 2.4. Primeira Execução

Após a instalação do Django, iremos executar um sequência de comandos:

1. Iniciaremos o projeto Django dentro da pasta pasta atual ( caso queria criar uma subpasta remova o ponto).
``` Properties
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


********************************************


# 3. Projeto Django

Em resumo, um projeto Django é um todo, que irá conter uma ou mais aplicações 

- **\_\_init\_\_.py** - é um arquivo em branco que instrui o Python a tratar esse diretório como um pacote Python.
- **settings.py** - Contém todas as definições do website. É onde nós registramos qualquer aplicação que criarmos, a localização de nossos arquivos estáticos, configurações de banco de dados etc. 
- **urls.py** - define os mapeamentos de URL para visualização do site. Mesmo que esse arquivo possa conter todo o código para mapeamento de URL, é mais comum delegar apenas o mapeamento para aplicativos específicos, como será visto mais adiante.
- **wsgi.py** é usado para ajudar na comunicação entre seu aplicativo Django e o web server. Você pode tratar isso como um boilerplate.
- **manage.py** - O arquivo manage.py dentro do projeto Django é responsável por permitir a execução de comandos Django dentro de um terminal como migrations, makemigrations ou createsuperuser


*********************************


# 4. Aplicação Django

1. Após a criação de uma nova aplicação devemos ir no PROJETO DJANGO e informar em dentro da opção de INSTALLED_APPS o nome da aplicação.
```Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app', # nova aplicação
]
```

## 4.1. Estrutura de Arquivos das Aplicações

Abaixo temos a estrutura inicial de uma aplicação Django:

- **migrations** - O pacote *migrations* é o responsável por mentar todo um histórico de versões do banco de dados.
- **admin** - O arquivo *admin.py* é usado para que possamos mostrar nossos dados dentro da ferramenta admin do Django, além de podermos trabalhar com todo um CRUD através da ferramenta.
- **apps** - O arquivo *apps.py* é responsável por definir o nome da aplicação.
- **models**- O arquivo *models.py* é usado para criar os modelos de dados, tendo a função de persistir os dados dentro de um banco de dados.
- **tests** - O arquivo *tests.py* é usado para criar funções e métodos para testar todas a aplicação Django.
- **views** - O arquivo *view.py* é o principal arquivo da aplicação, onde contém classes e/ou métodos que são chamados dentro do arquivo *urls.py*. Estas classes e/ou métodos irão contextualizar a requisição, podendo tratar formulários, validação de usuários ou simplesmente carregar um template para a visualização.

Entretanto, a estrutura pode ser alterada pelo programador de acordo com as necessidades, como um diretório de arquivos estáticos, diretório para os templates, um arquivos de rotas (abstraindo do projeto), arquivo para formulários, dentre outras opções.

- migrations
- static
  - js
  - css
  - images
- templates
    - index.html
- admin.py
- apps.py
- forms.py
- models.py
- tests.py
- urls.py
- views.py


******************************


# 5. Criar Rotas

Dado um projeto e uma aplicação, precisamos incluir, no arquivo de rota **urls.py** do **PROJETO**, uma referência para o arquivo de rotas urls.py que será criado dentro da nossa aplicação.

``` Django
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

Em seguida precisamos inserir a rota dentro do arquivo **urls.py** da **APLICAÇÃO**. Entretanto existem duas formas de fazer isso, a primeira é usando views baseadas em funções, onde precisamos apenas especificar o caminho, o nome da função dentro do arquivo views.py e dar um nome (apelido) para a rota.

``` Django
from django.urls import path
from .views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
]
```

A segunda forma é usando views baseadas em classes, que consiste na mesma ideia, mas ao invés de usar funções, iremos usar classes.

```Django
from django.urls import path
	from .views import IndexView	
	urlpatterns = [
    		path('', IndexView.as_view(), name='index'),
	]
```

A fonte completa de como criar URLS pode ser acessada em [django urls path](https://docs.djangoproject.com/en/dev/ref/urls/#django.urls.path)

## 5.1. Rotas Dinâmicas

Como criar urls dinâmicas e com expressões regulares acesse [URL dispatcher]([https://link](https://docs.djangoproject.com/en/dev/topics/http/urls/))

- Para capturar valores de um URL devemos usar colchetes angulares (<>) .
- Os valores capturados podem incluir opcionalmente um tipo de conversor como int ou str.
- Não há necessidade de adicionar uma barra inicial, porque todo URL tem isso. 

Exemplo: 
```python
from django.urls import path
from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]
```

- Uma solicitação para a url `/articles/2005/03/` corresponderia à terceira entrada na lista. Django chamaria a função `views.month_archive(request, year=2005, month=3)`.
- Uma solicitação para a url `/articles/2003/` corresponderia ao primeiro padrão da lista, não ao segundo, porque os padrões são testados em ordem, e o primeiro é o primeiro teste a ser aprovado. Aqui, o Django chamaria a função `views.special_case_2003(request)`
- Uma solicitação para a url  `/articles/2003` não corresponderia a nenhum desses padrões, porque cada padrão requer que o URL termine com uma barra.
- Uma solicitação para a url `/articles/2003/03/building-a-django-site/` corresponderia ao padrão final. Django chamaria a função `views.article_detail(request, year=2003, month=3, slug="building-a-django-site")`.

## 5.2. Conversores de Caminhos

Os seguintes conversores de caminho estão disponíveis por padrão:

- **str** - Corresponde a qualquer string não vazia, excluindo o separador de caminho '/'. Este é o padrão se um conversor não estiver incluído na expressão.
- **int** - Corresponde a zero ou qualquer inteiro positivo. Retorna um int.
- **slug** - Corresponde a qualquer string slug consistindo em letras ou números ASCII, mais o hífen e os caracteres de sublinhado. Por exemplo building-your-1st-django-site.
- **uuid** - Corresponde a um UUID formatado. Para evitar que vários URLs sejam mapeados para a mesma página, devem ser incluídos travessões e as letras devem ser minúsculas. Por exemplo 075194d3-6885-417e-a8a8-6c931e272f00. Retorna uma instância UUID .
- **path** - Corresponde a qualquer string não vazia, incluindo o separador de caminho '/',. Isso permite que você compare com um caminho de URL completo em vez de um segmento de um caminho de URL como com str.

[Registrando conversores de caminho personalizado](https://docs.djangoproject.com/en/3.1/topics/http/urls/#registering-custom-path-converters)

## 5.3. Usando Expressões regulares

Se a sintaxe de caminhos e conversores não for suficiente para definir seus padrões de URL, você também pode usar expressões regulares. Para fazer isso, use `re_path()` em vez de `path()`.

Em expressões regulares Python, a sintaxe para grupos nomeados de expressão regular é (? P &lt;nome> padrão), onde nome é o nome do grupo e padrão é algum padrão a ser correspondido.

- **^** - Início do url
- **$** - Fim do url
- **\\** - Escape para valores interpretados
- **|** - Ou lógico
- **\\+** - 1 ou mais ocorrências
- **?** - 0 ou 1 ocorrência
- **{n}** - n ocorrências
- **{n,m}** - Entre n e m ocorrências
- **[]** - Agrupamento de caracteres
- **?P ___** - Capture a ocorrência que corresponde a regexp ___ e atribua-a ao nome
- **.** - Qualquer caractere
- **\\d+** - Um ou mais dígitos. Observe o escape, sem correspondências de escape 'd+' literalmente
- **\\D+** - Um ou mais não dígitos. Note escape, sem correspondências de escape 'D+' literalmente
- **[a-zA-Z0-9_]+** - Um ou mais caracteres de palavra, letra minúscula, número ou sublinhado
- **\w+** Um ou mais caracteres de palavra, equivalente a [a-zA-Z0-9_]. Nota de escape, sem correspondências de escape 'w+'literalmente
- **[-@\w]+** (m ou mais caracteres de palavra, traço ou arroba. Não observe nenhum escape, \\w pois está entre colchetes (ou seja, um agrupamento)

|Expressão regular de url| Descrição | URLs de exemplo |
|--|--| -- |
| re_path(r'^$',.....) | String vazia (página inicial) | http://127.0.0.1/ |
| re_path(r'^stores/',.....) | Quaisquer caracteres finais | http://127.0.0.1/stores/ ou http://127.0.0.1/stores/long+string+with+12345 |
| re_path(r'^about/contact/$',.....) | Exato, sem caracteres finais | http://127.0.0.1/about/contact/ |
| re_path(r'^stores/\d+/',.... | Número | http://127.0.0.1/stores/2/ |
| re_path(r'^drinks/\D+/',.....) | Sem dígitos | http://127.0.0.1/drinks/mocha/ |
| re_path(r'^drinks/mocha|espresso/',.....) | Opções de palavra, quaisquer caracteres finais | http://127.0.0.1/drinks/mocha/ ou http://127.0.0.1/drinks/mochaccino/ ou http://127.0.0.1/drinks/espresso/ |
| re_path(r'^drinks/mocha$|espresso/$',.....) | Opções de palavras exatas, sem caracteres finais | http://127.0.0.1/drinks/mocha/ ou http://127.0.0.1/drinks/espresso/ |
| re_path(r'^stores/\w+/',.....) | Caracteres de palavras (qualquer letra minúscula ou maiúscula, número ou sublinhado) | http://127.0.0.1/stores/sandiego/ ou http://127.0.0.1/stores/1/  |
| re_path(r'^stores/[-\w]+/',.....) | Caracteres de palavra ou traço | http://127.0.0.1/san-diego/ |
| re_path(r'^state/[A-Z]{2}/',.....)| Duas letras maiúsculas | http://127.0.0.1/CA/ |


Aqui está o URL do exemplo anterior, reescrito usando expressões regulares

```python
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail),
]
```

Fontes: 

- [URL dispatcher](https://docs.djangoproject.com/en/dev/topics/http/urls/#registering-custom-path-converters)
- [Url paths and regular expressions]([https://link](https://www.webforefront.com/django/regexpdjangourls.html))


****************************


# 6. Criar View

Podemos criar uma função ou classe simples, apenas para verificarmos se as rotas estão funcionado. Para isso vamos editar o arquivo **views.py** da aplicação da seguinte forma.

```Django
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá mundo!")
```

Quem é HttpResponse? Basicamente é um método que retorna uma resposta a uma requisição HTTP. Iremos então da maneira mais simples testar a rota que é enviar uma resposta para a requisição.

Outra forma, é redirecionar para o arquivo **index.html** que criamos dentro do **diretório templates** dentro da aplicação.

```Django
from django.shortcuts import render

def index(request):
  context = {}
  return render(request, 'index.html', context)
```

A função *render* é responsável por tratar de ligar a requisição (dados enviados do browser) com o template. Ou seja, ele pega os dados da requisição (request), e envia para o template nomeado 'index.html', além de um dicionário dados de contexto (context). Os dados de contexto (context) seria uma variável para enviar dados da própria função para o arquivo index.html, que no momento não temos.

Por fim, podemos usar as classes, que irá herdar diversas funcionalidades e padrões prontos do Django.

```Django
from django.views.generic import TemplateView

class IndexView(TemplateView):
  template_name = 'index.html'
```


**************************************8


# 7. Templates

Um template Django é um documento de texto ou uma string Python marcada usando a linguagem de template Django. Algumas construções são reconhecidas e interpretadas pelo mecanismo de template. Os principais são variáveis ​​e tags. Um modelo é renderizado com um contexto. A renderização substitui variáveis ​​por seus valores, que são pesquisados ​​no contexto, e executa tags. Todo o resto é produzido como está.

##  7.1. Variáveis

Uma variável produz um valor do contexto, que é um objeto do tipo dicionário que mapeia chaves para valores. As variáveis ​​são circundadas por `{{ e }}` (chaves duplas) assim:

```Django
My first name is {{ first_name }}. My last name is {{ last_name }}.
```

Se os valores passados pelo contexto forem `{'first_name': 'John', 'last_name': 'Doe'}`, então o resultado seria: 

```Django
My first name is John. My last name is Doe.
```
As pesquisas de dicionário, de atributo e de índice de lista são implementadas com uma notação de ponto:

```Django
{{ my_dict.key }}
{{ my_object.attribute }}
{{ my_list.0 }}
```

### 7.1.1. TAGS
As tags fornecem lógica arbitrária no processo de renderização. Esta definição é deliberadamente vaga. Por exemplo, uma tag pode produzir conteúdo, servir como uma estrutura de controle, por exemplo, uma instrução `if` ou um loop `for`, obter conteúdo de um banco de dados ou até mesmo permitir o acesso a outras tags de modelo.

As tags são circundadas por `{% e %}` (chave e porcentagem?) assim:

```Django
{% csrf_token %}
```

As tags aceitam parâmetros como:

```Django
{% cycle 'odd' 'even' %}
{% url 'produto/' produto.id %}
```

Algumas tags exigem tags de início e fim:

```Django
{% if user.is_authenticated %} Hello, {{ user.username }}.{% endif %}
```


### 7.1.2. comment

Ignora tudo entre as tags. Uma nota opcional pode ser inserida na primeira tag. Por exemplo, isso é útil ao comentar o código para documentar porque o código foi desativado. `{% comment %}{% endcomment %}`

```Django
<p>Rendered text with {{ pub_date|date:"c" }}</p>
{% comment "Optional note" %}
    <p>Commented out text with {{ create_date|date:"c" }}</p>
{% endcomment %}

Para criar um comentário de uma linha em um modelo, use a sintaxe de comentário: `{# #}`.

```django
{# greeting #}hello
```

### 7.1.3. csrf_token

Essa tag é usada para proteção contra CSRF, conforme descrito na documentação para [Cross Site Request Forgeries]([https://link](https://7xwm2drhn3gdndpwco2driejom--docs-djangoproject-com.translate.goog/en/3.1/ref/csrf/)) .

### 7.1.4. cycle

Produz um de seus argumentos cada vez que essa tag é encontrada. O primeiro argumento é produzido no primeiro encontro, o segundo argumento no segundo encontro e assim por diante. Depois que todos os argumentos são exauridos, a tag passa para o primeiro argumento e o produz novamente.

Esta tag é particularmente útil em um loop:

```django
{% for o in some_list %}
    <tr class="{% cycle 'row1' 'row2' %}">
        ...
    </tr>
{% endfor %}
```
A primeira iteração produz HTML que se refere à classe row1, a segunda a row2, a terceira a row1novamente e assim por diante para cada iteração do loop. Você também pode usar variáveis.


### 7.1.5. debug

Produz uma carga completa de informações de depuração, incluindo o contexto atual e os módulos importados.

### 7.1.6. filter

Filtra o conteúdo do bloco por meio de um ou mais filtros. Vários filtros podem ser especificados com canais e filtros podem ter argumentos, assim como na sintaxe de variável. Observe que o bloco inclui todo o texto entre as tags `filter` e `endfilter`.

```django
{% filter force_escape|lower %}
    This text will be HTML-escaped, and will appear in all lowercase.
{% endfilter %}
```

### 7.1.7. firstof

Produz a primeira variável de argumento que não é 'falsa' (ou seja, existe, não está vazia, não é um valor booleano falso e não é um valor numérico zero). Não produz nada se todas as variáveis ​​passadas forem 'falsas'.

```django
{% firstof var1 var2 var3 %}
```

Isso é equivalente a:
```django
{% if var1 %}
    {{ var1 }}
{% elif var2 %}
    {{ var2 }}
{% elif var3 %}
    {{ var3 }}
{% endif %}
```

### 7.1.8. for

Faz um loop em cada item em uma matriz, tornando o item disponível em uma variável de contexto. Por exemplo, para exibir uma lista de atletas fornecida em athlete_list:

```django
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% endfor %}
</ul>
```
Você pode fazer um loop em uma lista ao contrário usando. `{% for obj in list reversed %}`. Se você precisar fazer um loop em uma lista de listas, poderá descompactar os valores de cada sub-lista em variáveis ​​individuais.

```Django
{% for x, y in points %}
    There is a point at {{ x }},{{ y }}
{% endfor %}
```

### 7.1.9. for… empty

A tag `for` pode receber uma cláusula opcional cujo texto é exibido se a matriz fornecida estiver vazia ou não puder ser encontrada: `{% empty %}`

```django
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% empty %}
    <li>Sorry, no athletes in this list.</li>
{% endfor %}
</ul>
```

### 7.1.10. if

A tag avalia uma variável e se essa variável for 'verdadeira' (ou seja, existe, não está vazia e não é um valor booleano falso), o conteúdo do bloco é gerado: `{% if %}`

```django
{% if athlete_list %}
    Number of athletes: {{ athlete_list|length }}
{% elif athlete_in_locker_room_list %}
    Athletes should be out of the locker room soon!
{% else %}
    No athletes.
{% endif %}
```

### 7.1.11. Operadores booleanos

Os operadores booleanos aceitos são and, or, not, `==` (igualdade), `!=` (desigualdade), `<` (meno que), `>` (maior que), `<=` (menos ou igual que), `=>` (maior ou igual que), `in` (contido dentro de), `is` (identidade do objeto).

```Django 
{% if athlete_list and coach_list or cheerleader_list %}
{% endif %}

{% if somevar == "x" %}
  This appears if variable somevar equals the string "x"
{% endif %}

{% if somevar != "x" %}
  This appears if variable somevar does not equal the string "x",   or if somevar is not found in the context
{% endif %}

{% if somevar < 100 %}
  This appears if variable somevar is less than 100.
{% endif %}

{% if somevar > 0 %}
  This appears if variable somevar is greater than 0.
{% endif %}

{% if somevar <= 100 %}
  This appears if variable somevar is less than 100 or equal to 100.
{% endif %}

{% if somevar >= 1 %}
  This appears if variable somevar is greater than 1 or equal to 1.
{% endif %}

{% if "bc" in "abcdef" %}
  This appears since "bc" is a substring of "abcdef"
{% endif %}

{% if somevar is True %}
  This appears if and only if somevar is True.
{% endif %}

{% if somevar is not True %}
  This appears if somevar is not True, or if somevar is not found in the
  context.
{% endif %}
```


### 7.1.12. lorem

Exibe texto latino 'lorem ipsum' de forma aleatória. Isso é útil para fornecer dados de amostra em modelos. A sintaxe é `{% lorem [count] [method] [random] %}`, onde:

- count - Um número (ou variável) contendo o número de parágrafos ou palavras a serem gerados (o padrão é 1).
- method - Quer por palavras, para HTML parágrafos ou para blocos de parágrafo de texto simples (o padrão é b).
- random - A palavra random, que se dada, não usa o parágrafo comum (“Lorem ipsum dolor sit amet…”) ao gerar texto.

exemplos 

- {% lorem %} produzirá o parágrafo comum “lorem ipsum”.
- {% lorem 3 p %}irá gerar o parágrafo “lorem ipsum” comum e dois parágrafos aleatórios, cada um envolvido em tags P HTML .
- {% lorem 2 w random %} irá produzir duas palavras latinas aleatórias.

### 7.1.13. now 

Exibe a data e/ou hora atual, usando um formato de acordo com a string fornecida. Essa string pode conter caracteres especificadores de formato, conforme descrito na seção de filtro date.

```django 
It is {% now "jS F Y H:i" %}
```

para ver mais opções acesse [now]([https://link](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#now))


### 7.1.14. regroup

Reagrupa uma lista de objetos semelhantes por um atributo comum. Você pode usar a tag para agrupar a lista de cidades por país. O seguinte snippet de código de modelo faria isso: `{% regroup %}`. Para ver o exemplo completo acesse: [regroup](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#regroup)

```django
{% regroup cities by country as country_list %}

<ul>
{% for country in country_list %}
    <li>{{ country.grouper }}
    <ul>
        {% for city in country.list %}
          <li>{{ city.name }}: {{ city.population }}</li>
        {% endfor %}
    </ul>
    </li>
{% endfor %}
</ul>
```

### 7.1.15. resetcycle

Reinicia um ciclo anterior para que ele reinicie de seu primeiro item em seu próximo encontro. Sem argumentos, irá redefinir o último definido no modelo. `{% resetcycle %}{% cycle %}`. A referência completa pode ser acessa em: [resetcycle]([https://link](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#resetcycle))


```django
{% for coach in coach_list %}
    <h1>{{ coach.name }}</h1>
    {% for athlete in coach.athlete_set.all %}
        <p class="{% cycle 'odd' 'even' %}">{{ athlete.name }}</p>
    {% endfor %}
    {% resetcycle %}
{% endfor %}
```

a saída seria algo do tipo

```html
<h1>José Mourinho</h1>
<p class="odd">Thibaut Courtois</p>
<p class="even">John Terry</p>
<p class="odd">Eden Hazard</p>

<h1>Carlo Ancelotti</h1>
<p class="odd">Manuel Neuer</p>
```

### 7.1.16. spaceless

Remove os espaços em branco entre as tags HTML. Isso inclui caracteres de tabulação e novas linhas.

```django
{% spaceless %}
    <p>
        <a href="foo/">Foo</a>
    </p>
{% endspaceless %}
```

resultaria em:

```html
<p><a href="foo/">Foo</a></p>
```

### 7.1.17. url

Retorna uma referência de caminho absoluto (um URL sem o nome de domínio) correspondendo a uma determinada visualização e parâmetros opcionais. Quaisquer caracteres especiais no caminho resultante serão codificados usando `iri_to_uri()`.

```django
{% url 'some-url-name' v1 v2 %}
```
O primeiro argumento é um nome de padrão de URL . Pode ser um literal entre aspas ou qualquer outra variável de contexto. Argumentos adicionais são opcionais e devem ser valores separados por espaço que serão usados ​​como argumentos no URL. 


#### 7.1.17.1. url interagindo com o path

```python
path('client/<int:id>/', app_views.client, name='app-views-client')
```

```django
{% url 'app-views-client' client.id %}
```

#### 7.1.17.2. url com apelidos

Se quiser recuperar um URL sem exibi-lo, você pode usar uma chamada um pouco diferente:

```django
{% url 'some-url-name' arg arg2 as the_url %}
<a href="{{ the_url }}">I'm linking to {{ the_url }}</a>
```

Essa sintaxe não causará erro se a visualização estiver ausente. Na prática, você usará isso para vincular a visualizações que são opcionais: `{% url ... as var %}`

```django
{% url 'some-url-name' as the_url %}
{% if the_url %}
  <a href="{{ the_url }}">Link to optional stuff</a>
{% endif %}
```

### 7.1.18. verbatim

Impede o mecanismo de template de renderizar o conteúdo desta tag de bloco. 

```django
{% verbatim myblock %}
    Avoid template rendering via the {% verbatim %}{% endverbatim %} block.
{% endverbatim myblock %}
```

### 7.1.19. widthratio

Para criar gráficos de barras e outros, esta tag calcula a proporção de um determinado valor a um valor máximo e, em seguida, aplica essa proporção a uma constante. - Referência completa : [widthratio](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#widthratio)

### 7.1.20. width
Armazena em cache uma variável complexa com um nome mais simples. Isso é útil ao acessar um método 'caro' (por exemplo, um que acessa o banco de dados) várias vezes.

```django
{% with total=business.employees.count %}
    {{ total }} employee{{ total|pluralize }}
{% endwith %}
```

A variável preenchida (no exemplo acima, total) está disponível apenas entre as tags `{% with %}{% endwith %}`. Você pode atribuir mais de uma variável de contexto:

```django
{% with alpha=1 beta=2 %}
    ...
{% endwith %}
```

### 7.1.21. load 

Carrega um conjunto de tags de modelo personalizado. Por exemplo, o modelo a seguir carregaria todas as tags e filtros registrados `somelibrary` localizados no pacote package.`otherlibrary`:

```django
{% load somelibrary package.otherlibrary %}
```

Você também pode carregar seletivamente filtros ou tags individuais de uma biblioteca, usando o argumento `foo`. Neste exemplo, as tags/filtros do modelo nomeados `foo` e `bar` serão carregados de somelibrary:

```django 
{% load foo bar from somelibrary %}
```

### 7.1.22. include

Carrega um modelo e o renderiza com o contexto atual. Esta é uma forma de 'incluir' outros modelos em um modelo. O nome do modelo pode ser uma variável ou uma string codificada (entre aspas), entre aspas simples ou duplas. Este exemplo inclui o conteúdo do modelo 'foo/bar.html':

```django
{% include "foo/bar.html" %}
```

Você pode passar contexto adicional para o modelo usando argumentos de palavra-chave:

```django
{% include "name_snippet.html" with person="Jane" greeting="Hello" %}
```

### 7.1.23. Filtros

Filtros transformam os valores de variáveis ​​e argumentos de tag. Eles se parecem com isto:

``` Django
{{ django|title }}
```

### 7.1.24. add 

Adiciona o argumento ao valor: Se value for 4, a saída será 6.

```django 
{{ value|add:"2" }}
```

### 7.1.25. addslashes

Adiciona barras antes das aspas. Útil para sequências de escape em CSV, por exemplo: Se value for "I'm using Django", a saída será ."I\'m using Django"

```django
{{ value|addslashes }}
```

### 7.1.26. capfirst

Capitaliza o primeiro caractere do valor. Se o primeiro caractere não for uma letra, este filtro não terá efeito: Se value for "django", a saída será "Django".

```django
{{ value|capfirst }}
```

### 7.1.27. center

Centraliza o valor em um campo de uma determinada largura: Se value for "Django", a saída será : `"     Django    "`

```django
"{{ value|center:"15" }}"
```

### 7.1.28. cut
Remove todos os valores de arg da string fornecida. Se value for "String with spaces", a saída será "Stringwithspaces"

```django 
{{ value|cut:" " }}
```

### 7.1.29. date

Formata uma data de acordo com o formato fornecido. Se value for um datetime, a saída será a string .'Wed 09 Jan 2008'. Para ver a lista completa de personalização de datas acesse [Date]([https://link](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date))

```django 
{{ value|date:"D d M Y" }}
```

### 7.1.30. Deafult

Se o valor for avaliado como False, usa o padrão fornecido. Caso contrário, usa o valor. Se value for "" (a string vazia), a saída será nothing.

```python
{{ value|default:"nothing" }}
```

### 7.1.31. default_if_none

Se (e somente se) o valor for `None`, usa o padrão fornecido. Caso contrário, usa o valor. Observe que, se uma string vazia for fornecida, o valor padrão não será usado. Se value for None, a saída será nothing.

```django
{{ value|default_if_none:"nothing" }}
```

### 7.1.32. dictsort

Pega uma lista de dicionários e retorna essa lista classificada pela chave fornecida no argumento.  Se value for `[{'name': 'zed', 'age': 19}, {'name': 'amy', 'age': 22}, {'name': 'joe', 'age': 31},]` a saída será `[{'name': 'amy', 'age': 22}, {'name': 'joe', 'age': 31}, {'name': 'zed', 'age': 19},]`

``` python
{{ value|dictsort:"name" }}
```

outro exemplo :

```python
{% for book in books|dictsort:"author.age" %}
    * {{ book.title }} ({{ book.author.name }})
{% endfor %}
```

Se books é:

```python
[
    {'title': '1984', 'author': {'name': 'George', 'age': 45}},
    {'title': 'Timequake', 'author': {'name': 'Kurt', 'age': 75}},
    {'title': 'Alice', 'author': {'name': 'Lewis', 'age': 33}},
]
```

então a saída seria:

* Alice (Lewis)
* 1984 (George)
* Timequake (Kurt)
  
### 7.1.33. dictsortreversed

Pega uma lista de dicionários e retorna essa lista classificada em ordem reversa pela chave fornecida no argumento. Isso funciona exatamente da mesma forma que o filtro acima, mas o valor retornado estará na ordem inversa.

### 7.1.34. divisibleby

Retorna True se o valor for divisível pelo argumento. Se value for 21, a saída seria True.

```django
{{ value|divisibleby:"3" }}
```

### 7.1.35. escape

Escapa do HTML de uma string. Especificamente, ele faz essas substituições:

- < é convertido para \&lt;
- \> é convertido para \&gt;
- ' (aspas simples) é convertido para \&#x27;
- " (aspas duplas) é convertido para \&quot;
- & é convertido para \&amp;

Aplicar escape a uma variável que normalmente teria escape automático aplicado ao resultado resultará em apenas uma rodada de escape. Portanto, é seguro usar essa função mesmo em ambientes com escape automático. Se você quiser que vários passes de escape sejam aplicados, use o filtro force_escape.

```django
{% autoescape off %}
    {{ title|escape }}
{% endautoescape %}
```

### 7.1.36. escapejs

Caracteres de escape para uso em strings JavaScript. Isso não torna a string segura para uso em literais de modelo HTML ou JavaScript, mas protege você de erros de sintaxe ao usar modelos para gerar JavaScript/JSON.

```django
{{ value|escapejs }}
```


### 7.1.37. filesizeformat

Formatos o valor como um tamanho de arquivo 'legível' (ie , , , etc.).'13 KB''4.1 MB''102 bytes'. Se value for 123456789, a saída seria .117.7 MB

```django 
{{ value|filesizeformat }}
```

### 7.1.38. first

Retorna o primeiro item de uma lista. Se value for a lista `['a', 'b', 'c']`, a saída será 'a'.

```django 
{{ value|first }}
```

### 7.1.39. floatformat

Quando usado sem um argumento, arredonda um número de ponto flutuante para uma casa decimal - mas apenas se houver uma parte decimal a ser exibida. Por exemplo: Se value for 34.23234 a saída será 34.2, se 34.00000 será 34, se 34.26000 será 34.3.

```django
{{ value|floatformat }}
```

Se usado com um argumento de número inteiro, `floatformat` arredonda um número para essa quantidade de casas decimais. Por exemplo: Se value for 34.23234 a saída será 34.232, se 34.00000 será 34.000, se 34.26000 será 34.260.

```django
{{ value|floatformat:3 }}
```

- Para ver mais possibilidades de formatação, acesse [floatformat](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#floatformat)

### 7.1.40. get_digit

ado um número inteiro, retorna o dígito solicitado, onde 1 é o dígito mais à direita, 2 é o segundo dígito mais à direita, etc. Retorna o valor original para entrada inválida (se a entrada ou argumento não for um inteiro, ou se argumento é menor que 1). Caso contrário, a saída é sempre um número inteiro. 

```django
{{ value|get_digit:"2" }}
```

Se value for 123456789, a saída será 8.

### 7.1.41. iriencode

Converte um IRI (Identificador de Recurso Internacionalizado) em uma string adequada para inclusão em uma URL. Isso é necessário se você estiver tentando usar strings contendo caracteres não ASCII em um URL. É seguro usar este filtro em uma string que já passou pelo `urlencodefiltro.` Se value for `"?test=1&me=2"`, a saída será `"?test=1&amp;me=2"`.

```django
{{ value|iriencode }}
```

### 7.1.42. join

Junta uma lista com uma string.  Se value for a lista `['a', 'b', 'c']`, a saída será a string `"a // b // c"`.

```python
{{ value|join:" // " }}
```

### 7.1.43. json_script

Produz com segurança um objeto Python como JSON, envolvido em uma \<\script\> tag, pronto para uso com JavaScript.
[json_script](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#json-script)

### 7.1.44. last

Retorna o último item de uma lista. Se value for a lista `['a', 'b', 'c', 'd']`, a saída será a string `"d"`.

``` django
{{ value|last }}
```

### 7.1.45. length

Retorna o comprimento do valor. Isso funciona para strings e listas. Se value for `['a', 'b', 'c', 'd']` ou `"abcd"`, a saída será `4`. O filtro retorna 0para uma variável indefinida.

```django
{{ value|length }}
```


### 7.1.46. length_is

Retorna `True` se o comprimento do valor for o argumento ou `False` caso contrário. Se value for `['a', 'b', 'c', 'd']` ou `"abcd"`, a saída será `True`.

```django
{{ value|length_is:"4" }}
```

### 7.1.47. linebreaks

Substitui quebras de linha em texto simples por HTML apropriado; uma única nova linha torna-se uma quebra de linha HTML ( \<br>) e uma nova linha seguida por uma linha em branco torna-se uma quebra de parágrafo (\<p>). Se value for Joel\nis a slug, a saída será \<p>Joel\<br>is a slug\</p>.

```django
{{ value|linebreaks }}
```

### 7.1.48. linebreaksbr

Converte todas as novas linhas em um pedaço de texto simples em quebras de linha HTML (\<br>). Se value for Joel\nis a slug, a saída será Joel\<br>is a slug.

```python
{{ value|linebreaksbr }}
```

### 7.1.49. linenumbers

Exibe texto com números de linha.

```python
{{ value|linenumbers }}
```

Se value é:

one
two
three

a saída será:

1. one
2. two
3. three

### 7.1.50. force_escape

Aplica escape de HTML a uma string (consulte o filtro escape para obter detalhes). Este filtro é aplicado imediatamente e retorna uma nova string com escape. Isso é útil nos raros casos em que você precisa de vários escapes ou deseja aplicar outros filtros aos resultados de escape. Normalmente, você deseja usar o filtro escape. Por exemplo, se você deseja capturar os elementos \<p> HTML criados pelo `linebreaksfiltro`:

```django
{% autoescape off %}
    {{ body|linebreaks|force_escape }}
{% endautoescape %}
```

### 7.1.51. ljust

Alinha à esquerda o valor em um campo de uma determinada largura. Se value for Django, a saída será `"Django    "`.

```django
"{{ value|ljust:"10" }}"
```

### 7.1.52. lower

Converte uma string em letras minúsculas.Se value for `Totally LOVING this Album!`, a saída será `totally loving this album!`

```django
{{ value|lower }}
```

### 7.1.53. make_list

Retorna o valor transformado em uma lista. Para uma string, é uma lista de caracteres. Para um inteiro, o argumento é convertido em uma string antes de criar uma lista. Se value for a string `"Joel"`, a saída seria a lista `['J', 'o', 'e', 'l']` . Se value for `123`, a saída será a lista `['1', '2', '3']`.

```django 
{{ value|make_list }}
```

### 7.1.54. phone2numeric

Converte um número de telefone (possivelmente contendo letras) em seu equivalente numérico. A entrada não precisa ser um número de telefone válido. Isso irá facilmente converter qualquer string. Se value for 800-COLLECT, a saída será 800-2655328.

```django 
{{ value|phone2numeric }}
```

### 7.1.55. pluralize

Retorna um plural sufixo se o valor não é 1, '1' ou um objeto de comprimento 1. Por padrão, este sufixo é 's'. 
Se num_messages for 1, a saída será `You have 1 message`. Se num_messages for 2a saída será `You have 2 messages`.

```django
You have {{ num_messages }} message{{ num_messages|pluralize }}.
```

Podemos alterar o sufixo caso necessário 

```django
You have {{ num_walruses }} walrus{{ num_walruses|pluralize:"es" }}.
```

Para palavras que não são pluralizadas por sufixo simples, você pode especificar um sufixo no singular e no plural, separados por vírgula

```django 
You have {{ num_cherries }} cherr{{ num_cherries|pluralize:"y,ies" }}.
```

### 7.1.56. random

Retorna um item aleatório da lista fornecida. Se value for a lista `['a', 'b', 'c', 'd']`, a saída pode ser `"b"`.

```django
{{ value|random }}
```

### 7.1.57. rjust

Alinha à direita o valor em um campo de uma determinada largura. Se value for `Django`, a saída será `"    Django"`.

```django
"{{ value|rjust:"10" }}"
```

### 7.1.58. safe

Marca uma string como não exigindo mais escape de HTML antes da saída. Quando o escape automático está desativado, este filtro não tem efeito. Se você estiver encadeando filtros, um filtro aplicado depois safe pode tornar o conteúdo inseguro novamente. Por exemplo, o código a seguir imprime a variável como está, sem escape:

```django
{{ var|safe|escape }}
```

### 7.1.59. safeseq

Entendi nada. Desculpa! [safeseq](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#safeseq)


### 7.1.60. slice

Retorna uma parte da lista.  Se some_list for `['a', 'b', 'c']`, a saída será `['a', 'b']`.

```django 
{{ some_list|slice:":2" }}
```

### 7.1.61. slugify

Converte para ASCII. Converte espaços em hifens. Remove caracteres que não são alfanuméricos, sublinhados ou hifens. Converte em minúsculas. Também remove os espaços em branco à esquerda e à direita. Se value for "Joel is a slug", a saída será "joel-is-a-slug".

```django 
{{ value|slugify }}
```

### 7.1.62. stringformat

Formata a variável de acordo com o argumento, um especificador de formatação de string. Este especificador usa a sintaxe de Formatação de String no estilo `printf`, com a exceção de que o “%” inicial é descartado. Se value for 10, a saída será 1.000000E+01.

```django
{{ value|stringformat:"E" }}
```

### 7.1.63. striptags

Faz todos os esforços possíveis para remover todas as tags HTML. Se value for "\<b>Joel\</b> \<button>is\</button> a \<span>slug\</span>", a saída será "Joel is a slug".

```django
{{ value|striptags }}
```

### 7.1.64. time
Formata uma hora de acordo com o formato fornecido. O formato fornecido pode ser o predefinido TIME_FORMAT ou um formato personalizado, igual ao filtro date. Observe que o formato predefinido depende da localidade. Se value for equivalente a datetime.datetime.now(), a saída será a string "01:23".

```django
{{ value|time:"H:i" }}
```

[time](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#time)

### 7.1.65. timesince

Formata uma data como a hora desde essa data (por exemplo, “4 dias, 6 horas”). Recebe um argumento opcional que é uma variável contendo a data a ser usada como ponto de comparação (sem o argumento, o ponto de comparação é agora ). Por exemplo, se blog_date for uma instância de data representando meia-noite em 1 de junho de 2006 e comment_date for uma instância de data para 08:00 em 1 de junho de 2006, o seguinte retornaria “8 horas”:

```django 
{{ blog_date|timesince:comment_date }}
```

### 7.1.66. timeuntil 

Semelhante a timesince, exceto que mede o tempo de agora até a data ou datetime fornecida. Por exemplo, se hoje é 1 de junho de 2006 e conference_date é uma instância de data que contém 29 de junho de 2006, então retornará “4 semanas”.{{ conference_date|timeuntil }} . ecebe um argumento opcional que é uma variável contendo a data a ser usada como ponto de comparação (em vez de agora ). Se from_date contiver 22 de junho de 2006, o seguinte retornará “1 semana”:

### 7.1.67. title

Converte uma string em caixa de título, fazendo com que as palavras comecem com um caractere maiúsculo e os caracteres restantes com minúsculas. Esta tag não faz nenhum esforço para manter “palavras triviais” em minúsculas. Se value for "my FIRST post", a saída será "My First Post".

```django
{{ value|title }}
```

### 7.1.68. truncatechars

Trunca uma string se for maior que o número especificado de caracteres. As strings truncadas terminarão com um caractere de reticências traduzível (“…”). Se value for "Joel is a slug", a saída será "Joel i…".

```django
{{ value|truncatechars:7 }}
```

### 7.1.69. truncatechars_html

Semelhante a truncatechars, exceto que reconhece tags HTML. Quaisquer tags que são abertas na string e não fechadas antes do ponto de truncamento são fechadas imediatamente após o truncamento. Se value for "\<p>Joel is a slug\</p>", a saída será "\<p>Joel i…\</p>". As novas linhas no conteúdo HTML serão preservadas.

### 7.1.70. truncatewords

Trunca uma string após um certo número de palavras. Se value for "Joel is a slug", a saída será "Joel is …".

```django 
{{ value|truncatewords:2 }}
```

### 7.1.71. truncatewords_html

emelhante a truncatewords, exceto que reconhece tags HTML. Todas as tags que são abertas na string e não fechadas antes do ponto de truncamento são fechadas imediatamente após o truncamento. Isso é menos eficiente do que truncatewords, portanto, só deve ser usado quando estiver recebendo texto HTML. Se value for "\<p>Joel is a slug\</p>", a saída será "\<p>Joel is …\</p>".

### 7.1.72. unordered_list

Pega recursivamente uma lista auto-aninhada e retorna uma lista HTML não ordenada - SEM abrir e fechar as tags \<ul>.  Para ler sobre acesse : 
[unordered_list](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#unordered-list)

### 7.1.73. upper

Converte uma string em maiúsculas. Se value for "Joel is a slug", a saída será "JOEL IS A SLUG".

```django 
{{ value|upper }}
```

### 7.1.74. urlencode

Escapa um valor para uso em um URL. Se value for "https://www.example.org/foo?a=b&c=d", a saída será "https%3A//www.example.org/foo%3Fa%3Db%26c%3Dd"

```django
{{ value|urlencode }}
```

Um argumento opcional contendo os caracteres que não devem ser escapados pode ser fornecido. Se não for fornecido, o caractere '/' será considerado seguro. Uma string vazia pode ser fornecida quando todos os caracteres devem ser escapados. Por exemplo:

```django
{{ value|urlencode:"" }}
```

Se value for "https://www.example.org/", a saída será "https%3A%2F%2Fwww.example.org%2F".

### 7.1.75. urlize

Converte URLs e endereços de e-mail em texto em links clicáveis. Os links podem ter pontuação final (pontos, vírgulas, parênteses próximos) e pontuação inicial (parênteses de abertura) e urlizeainda farão a coisa certa. Se value for "Check out www.djangoproject.com", a saída será ."Check out \<a href="http://www.djangoproject.com" rel="nofollow">www.djangoproject.com\</a>"

```django
{{ value|urlize }}
```

### 7.1.76. urlizetrunc

Converte URLs e endereços de e-mail em links clicáveis ​​assim como urlize , mas trunca URLs mais longos do que o limite de caracteres fornecido. Se value for "Check out www.djangoproject.com", a saída seria 'Check out \<a href="http://www.djangoproject.com" rel="nofollow">www.djangoproj…\</a>'

```django 
{{ value|urlizetrunc:15 }}
```

### 7.1.77. wordcount

Retorna o número de palavras. Se value for `"Joel is a slug"`, a saída será `4`.

```django 
{{ value|wordcount }}
```

### 7.1.78. wordwrap

Encapsula palavras no comprimento de linha especificado.

```django
{{ value|wordwrap:5 }}
```

Se value for Joel is a slug, a saída seria:

Joel
is a
slug

### 7.1.79. yesno

Mapas valores para True, Falsee (opcionalmente) None, para as cadeias de “sim”, “não”, “talvez”, ou um mapeamento personalizado passada como uma lista separada por vírgulas, e retorna uma dessas cadeias de acordo com o valor: Se valor for True, a saída será yeah; se for Flase, será no; se for None, será maybe... Por padrão se não por passado parâmetro, será apenas yes e no.


```django
{{ value|yesno:"yeah,no,maybe" }}
```

### 7.1.80. Filtros Personalizados

- Também é possível criar tags e filtros personalizados. Para isto acesse: [Writing custom template tags](https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/#howto-writing-custom-template-tags)
- 

********************************

# 8. Henraça de templates

A parte mais poderosa - e portanto a mais complexa - do mecanismo de template do Django é a herança de template. A herança do modelo permite que você crie um modelo básico de “esqueleto” que contém todos os elementos comuns do seu site e define os blocos que os modelos filhos podem substituir.


Para criar o modelo base, iremos criar um esquelo que irá conter todo que é comum em todoas as páginas que a herdarem, como links de bibliotecas, menus, barras laterais, rodapé, etc. 

exemplo de um arquivo base.html

```django
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="style.css">
    <title>{% block title %}My amazing site{% endblock %}</title>
</head>

<body>
    <div id="sidebar">
        {% block sidebar %}
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/blog/">Blog</a></li>
        </ul>
        {% endblock %}
    </div>

    <div id="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

Usando as TAGS **Blocks**, podemos sobreescrever o que estiver contido dento deles usando o nome que a atribuímos no arquivo que herdar o documento base.  Exemplo de documento que herda de base. Para herdar, usamos a tag **extends**

```django
{% extends "base.html" %}

{% block title %}My amazing blog{% endblock %}

{% block content %}
{% for entry in blog_entries %}
    <h2>{{ entry.title }}</h2>
    <p>{{ entry.body }}</p>
{% endfor %}
{% endblock %}
```

## 8.1. Dicas para usar a herança
- Se você usar em um modelo, `{% extends %}` deve ser a primeira tag de modelo nesse modelo. A herança do modelo não funcionará, caso contrário.
-  Mais tags `{% block %}` em seus modelos básicos são melhores. Lembre-se de que os modelos filhos não precisam definir todos os blocos pais, portanto, você pode preencher padrões razoáveis ​​em vários blocos e, em seguida, definir apenas aqueles de que precisa mais tarde. É melhor ter mais ganchos do que menos ganchos.
-  Se você estiver duplicando conteúdo em vários modelos, provavelmente significa que você deve mover esse conteúdo para um `{% block %}` em um modelo pai.
-  Se você precisar obter o conteúdo do bloco do template pai, a variável `{{ block.super }}{{ block.super }}` fará o truque. Isso é útil se você deseja adicionar ao conteúdo de um bloco pai em vez de substituí-lo completamente. Os dados inseridos usando não serão escapados automaticamente, uma vez que já foram escapados, se necessário, no modelo pai.
-  Usando o mesmo nome de modelo do qual você está herdando, pode ser usado para herdar um modelo ao mesmo tempo em que o substitui. Combinado com `{% extends %}{{ block.super }}`, esta pode ser uma maneira poderosa de fazer pequenas personalizações. Consulte Estendendo um modelo substituído em Como substituir modelos para obter um exemplo completo.
-  Variáveis ​​criadas fora de usando a sintaxe da tag template não podem ser usadas dentro do bloco. Por exemplo, este modelo não renderiza nada:
```django
{% block %}as{% translate "Title" as title %}
{% block content %}{{ title }}{% endblock %}
```
Para facilitar a leitura extra, você pode opcionalmente dar um nome à sua tag. Por exemplo: `{% endblock %}`

```django
    {% block content %}
    ...
    {% endblock content %}
```

- Em modelos maiores, essa técnica ajuda a ver quais tags `{% block %}` estão sendo fechadas. Finalmente, observe que você não pode definir várias blocktags com o mesmo nome no mesmo modelo. Essa limitação existe porque uma tag de bloco funciona em “ambas” direções. Ou seja, uma tag de bloco não fornece apenas uma lacuna a ser preenchida - ela também define o conteúdo que preenche a lacuna no pai . Se houvesse duas blocktags com nomes semelhantes em um modelo, o pai desse modelo não saberia qual dos conteúdos dos blocos usar.


**************************


# 9. Arquivos Estáticos

Para usar os arquivos estáticos dentro de um template, primeiro devemos configurar corretamente o arquivo **settings** espeficificando o caminhos dos arquivos estáticos. Em seguida devemos ter um diretório chamado static com os arquivos dentro da aplicação. Em seguida, em todos os templates, nas primeiras linhas devemos especificar que iremos usar arquivos estáticos, carregando ele com a tag `{% load static %}`.

```django
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Página de testes</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>

<h1>Olá, mundo</h1>

</body>
</html>
```

## 9.1. Configuração dos Arquivos Estáticos

- Em testes podemos instalar a biblioteca
- **whitenoise** - Responsável por cuidar dos arquivos estáticos em produção, como o JavaScript e CSS
- Em produção devemos instalar a biblioteca 
  - **dj-static** - Responsável por exibir arquivos estáticos e dinâmicos de forma mais segura, substituindo o whitenoise.
- Para incluir imagens, devemos usar a biblioteca
  -  **django-stdimage** - Trabalha com imagens dentro da aplicação (imagens de um produto, por exemplo)
- Devemos alterar as aplicações permitidas dentro do arquivo **settings** para permitir as novas aplicações, como o **stdimage** e o **bootstrap4**. 

- Caso seja usado o whitenoise, devemos **inserir o middleware na segunda linha**. com a seguinte sintaxe: `'whitenoise.middleware.WhiteNoiseMiddleware'`. 
- Para permitir os templates, precisamos criar um diretório na aplicação chamado **templates**, e dentro da linha de configuração **TEMPLATES**, na opção **DIR** devemos especificar o diretório `DIR['templates']`.
- Devemos também informar o diretório dos nosso arquivos estáticos como visto nas configurações acima. 
- 
```python
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

- Para configurar o **dj-static** no lugar do whitenoise, precisamos alterar o arquivo **wsgi**.

```python
import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = Cling(MediaCling(get_wsgi_application()))
```
- Nos arquivos **.html** precismos informar que os mesmos irão trabalhar com arquivos estáticos. Para isso, bastamos usar a sintaxe abaixo

```Django
{% load static %}
<link rel="stylesheet" href="{% static 'css/estilos.css' %}">
```
- O comando abaixo é responsável por coletar todos os arquivos estáticos ao longo das aplicações e a reúnem de forma central dentro do Projeto. 

```python
python manage.py collectstatic
```

- Podemos também especificar os caminhos de mídias que foram especificados dentro do arquivo **settings**, para que o projeto faça o roteamento correto dos arquivos (caso seja necessário no projeto arquivos de mídias).

```python
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 9.2. Estutura de Pastas e Arquivos

- migrations
- static
  - js
  - css
  - images
- templates
  - index.html
- admin.py
- apps.py
- forms.py
- models.py
- tests.py
- urls.py
- views.py

## 9.3. Exemplo com Passagem de Contexto


### 9.3.1. Urls Projeto

```Django
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
] 
```


### 9.3.2. Url da Aplicação
``` Django
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]  
```

### 9.3.3. View da Aplicação
``` Django
from django.shortcuts import render

def index(request):
  context =	{
  "brand": "ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
} 
  return render(request, 'index.html', context)
```

### 9.3.4. Arquivo Index

```html
<html lang="pt-br">

  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exemplo contexto</title>
  </head>

  <body>
    <h1>Marca {{ brand|title }}</h1>

    <h2>Lista de Cores</h2>
    <ul>
      {% for cor in colors %}
      <li>{{cor|upper}}</li>
      {% endfor %}
    </ul>

  </body>

</html>
```

### 9.3.5. Saída

**Marca Ford**

Lista de Cores
  - RED
  - WHITE
  - BLUE



## 9.4. Exemplo Com Herança, Arquivos Estáticos e Inclusão de Arquivos

### 9.4.1. Settings Projeto RESUMIDO

```Django
from pathlib import Path, os
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'core', #Aplicação
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware' #WhiteNoise
]

TEMPLATES = [
        'DIRS': ['templates'],
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

```

### 9.4.2. Urls Projeto

```Django
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 9.4.3. Url da Aplicação
``` Django
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]  
```

### 9.4.4. View da Aplicação
``` Django
from django.shortcuts import render

def index(request):
  context =	{} 
  return render(request, 'index.html', context)
```

### 9.4.5. Template Base

- Contém uma TAG especificando que o arquivo precisará usar arquivos estáticos
  -  `{% load static %}`
- Contém o carregamento de todos os aqruivos estáticos de personalização como CSS, Fonts, JavaScript e outros.
  - `<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">`
  - `<script src="{% static 'js/jquery-min.js' %}"></script>`
  - `<link rel="stylesheet" href=" {% static 'fonts/line-icons.css' %}">`
- Contém um bloco onde irá ser carregado um conteúdo
  - `{% block content %} {% endblock content %}` 
- Contém uma TAG para carregar uma Imagem e uma TAG que irá redirecionar a página para a URL com o nome de 'index'
  - `<a href="{% url 'index' %}" class="navbar-brand"><img src=" {% static 'img/logo.png' %}" alt=""></a>`

### 9.4.6. Template index.html

- O arquivo index herda todas os arquivos carregados, o menu e as imagens do template BASE, abstraindo e simplificando o código
  - `{% extends 'base.html' %}`
- Além disso o arquivo diz logo em seguida que irá carregar arquivos estátricos.
  - `{% load static %}`
- Dentro do Bloco, **de mesmo nome** da base, iremos especificar o conteúdo que será inserido, na mesma posição original do arquivo base. 
  - `{% block content %} ... {% endblock content %}`
- Dentro do bloco iremos incluir arquivos HTML que contém diversos conteúdos, na ordem em que devem aparecer, 
  - `{% include 'footer.html' %}`

### 9.4.7. Arquivo Footer

- Contém o carregamento de arquivos estáticos
  - `{% load static %}`
- Contém todo o código HTML responsável pela formatação do rodapé da pégina. 


### 9.4.8. HTMLs

#### 9.4.8.1. Base

``` Django
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">

  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <title>Fusion</title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <!-- Icon -->
    <link rel="stylesheet" href=" {% static 'fonts/line-icons.css' %}">
    <!-- Owl carousel -->
    <link rel="stylesheet" href="{% static 'css/owl.carousel.min.css' %}">
    <link rel="stylesheet" href="{% static 'css/owl.theme.css' %}">

    <!-- Animate -->
    <link rel="stylesheet" href="{% static 'css/animate.css' %}">
    <!-- Main Style -->
    <link rel="stylesheet" href="{% static 'css/main.css' %}">
    <!-- Responsive Style -->
    <link rel="stylesheet" href="{% static 'css/responsive.css' %}">

  </head>

  <body>

    <!-- Header Area wrapper Starts -->
    <header id="header-wrap">
      <!-- Navbar Start -->
      <nav class="navbar navbar-expand-md bg-inverse fixed-top scrolling-navbar">
        <div class="container">
          <!-- Brand and toggle get grouped for better mobile display -->
          <a href="{% url 'index' %}" class="navbar-brand"><img src=" {% static 'img/logo.png' %}" alt=""></a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
            <i class="lni-menu"></i>
          </button>
          <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav mr-auto w-100 justify-content-end clearfix">
              <li class="nav-item active">
                <a class="nav-link" href="#hero-area">
                  Home
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#services">
                  Services
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#team">
                  Team
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#pricing">
                  Pricing
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#testimonial">
                  Testimonial
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#contact">
                  Contact
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <!-- Navbar End -->

      {% block content %} {% endblock content %}

      <!-- Go to Top Link -->
      <a href="#" class="back-to-top">
        <i class="lni-arrow-up"></i>
      </a>

      <!-- Preloader -->
      <div id="preloader">
        <div class="loader" id="loader-1"></div>
      </div>
      <!-- End Preloader -->

      <!-- jQuery first, then Popper.js, then Bootstrap JS -->
      <script src="{% static 'js/jquery-min.js' %}"></script>
      <script src="{% static 'js/popper.min.js' %} "></script>
      <script src="{% static 'js/bootstrap.min.js' %} "></script>
      <script src="{% static 'js/owl.carousel.min.js' %}"></script>
      <script src="{% static 'js/wow.js' %}"></script>
      <script src="{% static 'js/jquery.nav.js' %}"></script>
      <script src="{% static 'js/scrolling-nav.js' %}"></script>
      <script src="{% static 'js/jquery.easing.min.js' %}"></script>
      <script src="{% static 'js/main.js' %}"></script>
      <script src="{% static 'js/form-validator.min.js' %}"></script>
      <script src="{% static 'js/contact-form-script.min.js' %}"></script>
    </header>
    <!-- Header Area wrapper End -->
  </body>

</html>
```

#### 9.4.8.2. Index

```Django
{% extends 'base.html' %}
{% load static %}

{% block content %}

<!-- Hero Area Start -->
{% include 'hero.html' %}
<!-- Hero Area End -->

<!-- Services Section Start -->
{% include 'services.html' %}
<!-- Services Section End -->

<!-- About Section start -->
{% include 'about.html' %}
<!-- About Section End -->

<!-- Features Section Start -->
{% include 'features.html' %}
<!-- Features Section End -->

<!-- Team Section Start -->
{% include 'team.html' %}
<!-- Team Section End -->

<!-- Pricing section Start -->
{% include 'pricing.html' %}
<!-- Pricing Table Section End -->

<!-- Testimonial Section Start -->
{% include 'testimonial.html' %}
<!-- Testimonial Section End -->

<!-- Call To Action Section Start -->
{% include 'ads.html' %}
<!-- Call To Action Section Start -->

<!-- Contact Section Start -->
{% include 'contact.html' %}
<!-- Contact Section End -->

<!-- Footer Section Start -->
{% include 'footer.html' %}
<!-- Footer Section End -->
{% endblock content %}
```

####

```Django
{% load static %}

<footer id="footer" class="footer-area section-padding">
  <div class="container">
    <div class="container">
      <div class="row">
        <div class="col-lg-3 col-md-6 col-sm-6 col-xs-6 col-mb-12">
          <div class="widget">
            <h3 class="footer-logo"><img src="{% static 'img/logo.png' %}" alt=""></h3>
            <div class="textwidget">
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque lobortis tincidunt est, et euismod purus suscipit quis.</p>
            </div>
            <div class="social-icon">
              <a class="facebook" href="#"><i class="lni-facebook-filled"></i></a>
              <a class="twitter" href="#"><i class="lni-twitter-filled"></i></a>
              <a class="instagram" href="#"><i class="lni-instagram-filled"></i></a>
              <a class="linkedin" href="#"><i class="lni-linkedin-filled"></i></a>
            </div>
          </div>
        </div>
        <div class="col-lg-3 col-md-6 col-sm-12 col-xs-12">
          <h3 class="footer-titel">Products</h3>
          <ul class="footer-link">
            <li><a href="#">Tracking</a></li>
            <li><a href="#">Application</a></li>
            <li><a href="#">Resource Planning</a></li>
            <li><a href="#">Enterprise</a></li>
            <li><a href="#">Employee Management</a></li>
          </ul>
        </div>
        <div class="col-lg-3 col-md-6 col-sm-12 col-xs-12">
          <h3 class="footer-titel">Resources</h3>
          <ul class="footer-link">
            <li><a href="#">Payment Options</a></li>
            <li><a href="#">Fee Schedule</a></li>
            <li><a href="#">Getting Started</a></li>
            <li><a href="#">Identity Verification</a></li>
            <li><a href="#">Card Verification</a></li>
          </ul>
        </div>
        <div class="col-lg-3 col-md-6 col-sm-12 col-xs-12">
          <h3 class="footer-titel">Contact</h3>
          <ul class="address">
            <li>
              <a href="#"><i class="lni-map-marker"></i> 105 Madison Avenue - <br> Third Floor New York, NY 10016</a>
            </li>
            <li>
              <a href="#"><i class="lni-phone-handset"></i> P: +84 846 250 592</a>
            </li>
            <li>
              <a href="#"><i class="lni-envelope"></i> E: contact@uideck.com</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div id="copyright">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <div class="copyright-content">
            <p>Copyright © 2020 <a rel="nofollow" href="https://uideck.com">UIdeck</a> All Right Reserved</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</footer>
```


******************************************8


# 10. Formulários

Um Formulário HTML é um grupo de um ou mais campos/widgets em uma página web, que podem ser utilizados para coletar informações dos usuários para submetê-las a um servidor.

Formulários são também um meio relativamente seguro de compartilhar dados com o servidor, pois nos permitem enviar dados em requisições POST com proteção contra ataques maliciosos **CSRF** (Cross-Site Request Forgery - em inglês, falsificação de solicitação entre sites).

FONTE [Tutorial Django Parte 9: Trabalhando com formulários](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Forms)

## 10.1. Revisão

```html
<form action="/team_name_url/" method="post">
    <label for="team_name">Enter name: </label>
    <input id="team_name" type="text" name="name_field" value="Default name for team.">
    <input type="submit" value="OK">
</form>
```

- O  atributo `type` de um campo define que tipo de `widget` será exibido. Pode ser um campo de texto, data, imagem, etc.
- O `name` e o `id` de cada campo são utilizados para identificá-lo no JavaScript/CSS/HTML
- `value` define o valor preenchido inicialmente no campo quando ele é exibido pela primeira vez
- A tag `label` define uma legenda para o campo, onde o atributo `for` associa a a legenda ao campo `input` pelo seu identificador `id`
- O `type = 'submit'` será exibida como um botão, que ao ser pressionado, enviará os dados presentes no campo para o servidor. 
  - O método POST deve sempre ser utilizado se os dados forem resultar em uma alteração no banco de dados do servidor, pois é mais resistente a ataques de falsificação de solicitação entre sites.
  - O método GET deve ser utilizado somente para formulários que não alteram dados de usuário (um formulário de busca, por exemplo). Ele é recomendado para quando você quiser poder favoritar ou compartilhar a URL.
-  O atributo 'method' definem o método HTTP utilizado para enviar os dados e o destino para esses dados no servidor é definido em 'action'

FONTE [Tutorial Django Parte 9: Trabalhando com formulários](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Forms)

## 10.2. Fluxograma

1. Exiba o formulário padrão na primeira vez em que for solicitado pelo usuário 
2. Receba dados de uma solicitação de envio e vincule-os ao formulário. 
3. Limpe e valide os dados.
4. Se algum dado for inválido, exiba novamente o formulário, desta vez com valores preenchidos pelo usuário e mensagens de erro para os campos problemáticos.
5. Se todos os dados forem válidos, execute as ações necessárias
6. Quando todas as ações estiverem concluídas, redirecione o usuário para outra página.

## 10.3. Criando um Formulário

Primeiro precisamos criar um arquivo chamado **forms.py** que irá armazenar todos os formulários da nossa aplicação. 

- Exemplo de um formulário

```python
from django import forms

class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
```

## 10.4. Campos de formulários DJango

Para criar um formulário, precisamos ver todas as possibilidades de campos possível em [Campos de formulários](https://docs.djangoproject.com/en/dev/ref/forms/fields/).

Os principais campos de um formulários são:

- [BooleanField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#booleanfield)
- [CharField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#charfield)
- [ChoiceField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#choicefield)
- [DateField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#datefield)
- [EmailField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#emailfield)
- [BooleanField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#Booleanfield)
- [CharField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#Charfield)
- [TypedChoiceField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#typedchoicefield)
- [DateField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#datefield)
- [DateTimeField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#datetimefield)
- [DecimalField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#decimalfield)
- [DurationField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#durationfield)
- [FileField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#filefield)
- [FilePathField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#filepathfield)
- [FloatField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#Ffoatfield)
- [ImageField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#imagefield)
- [IntegerField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#integerfield)
- [GenericIPAddressField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#genericipaddressfield)
- [MultipleChoiceField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#multiplechoicefield)
- [TypedMultipleChoiceField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#typedmultiplechoicefield)
- [NullBooleanField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#nullbooleanfield)
- [RegexField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#regexfield)
- [SlugField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#slugfield)
- [TimeField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#timefield)
- [URLField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#urlfield)
- [UUIDField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#uuidfield)
- [ComboField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#combofield)
- [MultiValueField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#multivaluefield)
- [SplitDateTimeField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#splitdatetimefield)
- [ModelMultipleChoiceField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#modelmultiplechoicefield)
- [ModelChoiceField](https://docs.djangoproject.com/en/dev/ref/forms/fields/#modelchoicefield)


### 10.4.1. Os principais parâmetros dos campos

Os parâmetros mais comuns que usamos para definir os campos são:

- **label='Nome'** - Define um label para o campo que será exibido com o campo
- **label_suffix** - Por padrão, dois pontos são exibidos após o rótulo (e.g. Renewal date:). Esse argumento permite especificar um sufixo diferente contendo outros caractere(s).
- **help_text='texto de ajuda'** - Define um pequeno texto que descreve como devemos preencher o campo
- **initial='valor'** - Define um valor inicial para o campo
- **error_messages={'required': 'Please enter your name'}** - Define um dicionários para os possíveis erros do campo. Por exemplo: o campo deve ser obrigatório (required), ou que já existe algum usuário com aquele nome (unique). Lembrando que para muitos erros já existem mensagem padrões.
- **validators** - Define uma lista de funções que serão chamadas no campo quando validadas
- **disabled**: O campo é exibido, mas seu valor não pode ser editado se este for True.
- **Required** - Define que o campo é obrigatório
- **max_length, min_length** - Define o tamanho máximo e mínimo de caracteres 
- **Required** - Define que o campo é obrigatório
- **Disabled** - Define que o campo deve estar desabilitado 

Para ver mais detalhes acesse [Campos de formulários e seus argumentos](https://docs.djangoproject.com/pt-br/dev/ref/forms/fields/#core-field-arguments)

## 10.5. Widgets

Além dos campos, temos também os **widgets** que é a forma como o html é apresentado. Cada campo acima tem um widget padrão, mas podemos alterar como o campo é exibido na tela. Para ver a lista completa de widget e seus usos, acesse: [widgts](https://docs.djangoproject.com/en/dev/ref/forms/widgets/).

Exemplo

```python
from django import forms

class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
```

### 10.5.1. Lista de Widgets 

- **TextInput**
  - input_type: 'text'
  - Renders as: &lt;input type="text" ...>
- NumberInput
  - input_type: 'number'
  - Renders as: &lt;input type="number" ...>
- **EmailInput**
  - input_type: 'email'
  - Renders as: &lt;input type="email" ...>
- **URLInput**
  - input_type: 'url'
  - Renders as: &lt;input type="url" ...>
- **PasswordInput**
  - input_type: 'password'
  - Renders as: &lt;input type="password" ...>
  - Parâmetro: **render_value** - Determina se o widget terá um valor preenchido quando o formulário for reapresentado após um erro de validação (o padrão é False).
- **HiddenInput**
  - input_type: 'hidden'
  - Renders as: &lt;input type="hidden" ...>
- **DateInput, DateTimeInput, Time**
  - input_type: 'text'
  - Renders as: &lt;input type="text" ...>
  - parâmetro: **format** - O formato em que o valor inicial deste campo será exibido.
- **Textarea**
  - Renders as: &lt;textarea>...&lt;/textarea>
- **CheckboxInput**
  - input_type: 'checkbox'
  - Renders as: &lt;input type="checkbox" ...>
  - Parâmetro: **check_test** - Um chamável que obtém o valor de CheckboxInput e retorna True se a caixa de seleção deve ser marcada para esse valor.
- **Select**
  - Renders as: &lt;select>&lt;option ...>...&lt;/select>
  - Argumento - **choices** -  Este atributo é opcional quando o campo do formulário não possui um atributo de escolhas. Em caso afirmativo, ele substituirá qualquer coisa que você definir aqui quando o atributo for atualizado no campo.
- **NullBooleanSelect**
  - Selecione o widget com as opções ‘Desconhecido’, ‘Sim’ e ‘Não’
- **SelectMultiple**
Semelhante ao Select, mas permite a seleção múltipla: &lt;select multiple> ... &lt;/select>
- **RadioSelect**
Semelhante a Selecionar, mas renderizado como uma lista de botões de opção dentro de &lt;li> tags:
```html
<ul>
  <li><input type="radio" name="..."></li>
  ...
</ul>

```
Para um controle mais granular sobre a marcação gerada, você pode repetir os botões de opção no modelo. Assumindo um formulário myform com um campo Beatles que usa um RadioSelect como widget: 
```html
<fieldset>
    <legend>{{ myform.beatles.label }}</legend>
    {% for radio in myform.beatles %}
    <div class="myradio">
        {{ radio }}
    </div>
    {% endfor %}
</fieldset>
```
- **FileInput**
  - Renders as: &lt;input type="file" ...>

- **ClearableFileInput¶**
  - Renders as: <input type="file" ...> - Com uma entrada de caixa de seleção adicional para limpar o valor do campo, se o campo não for obrigatório e tiver dados iniciais. 

[Lista Completa](https://docs.djangoproject.com/en/dev/ref/forms/widgets/)

### 10.5.2. Alterando o HTML com Widgets

Ainda podemos especificar atributos HTML dentro de um widget.attr

```python
class CommentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
    url = forms.URLField()
    comment = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
```

Ou então atualizar posteriormente com 

```python
class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField()

    name.widget.attrs.update({'class': 'special'})
    comment.widget.attrs.update(size='40')
```

## 10.6. Exibindo Formulários nos Templates

Existem diversas formas de exibir um formulário, a primeira é trabalhar 100% com HTML, enquanto no outro extremo podemos inserir o formulário usando apenas um comandos Django

### 10.6.1. Formulário HTML

```Html
<p>
  <label for="id_subject">Subject:</label>
  <input id="id_subject" type="text" name="subject" maxlength="100" required>
</p>
<p>
  <label for="id_message">Message:</label>
  <textarea name="message" id="id_message" required></textarea>
</p>
<p>
  <label for="id_sender">Sender:</label>
  <input type="email" name="sender" id="id_sender" required>
</p>
<p>
  <label for="id_cc_myself">Cc myself:</label>
  <input type="checkbox" name="cc_myself" id="id_cc_myself">
</p>
```

### 10.6.2. Formulário Django-HTML

- **form.campo.id_for_label** - Contém o ID do campo
- **form.campo.errors** - Irá exibir os errors do campo caso haja algum erro ou mensagem de erro atribuída ao erro gerado.
- **form.campo** - Renderiza (exibe) o campo 

```Django 
{{ form.non_field_errors }}
<div class="fieldWrapper">
    {{ form.subject.errors }}
    <label for="{{ form.subject.id_for_label }}">Email subject:</label>
    {{ form.subject }}
</div>
<div class="fieldWrapper">
    {{ form.message.errors }}
    <label for="{{ form.message.id_for_label }}">Your message:</label>
    {{ form.message }}
</div>
<div class="fieldWrapper">
    {{ form.sender.errors }}
    <label for="{{ form.sender.id_for_label }}">Your email address:</label>
    {{ form.sender }}
</div>
<div class="fieldWrapper">
    {{ form.cc_myself.errors }}
    <label for="{{ form.cc_myself.id_for_label }}">CC yourself?</label>
    {{ form.cc_myself }}
</div>
```

### 10.6.3. Formulário Django-HTML (Menos HTML)
- **form.subject.label_tag* - contém todo o elemento `<label>`, com o atributo `for` e `name`.

```Django 
{{ form.non_field_errors }}
<div class="fieldWrapper">
  {{ form.subject.errors }}
  {{ form.subject.label_tag }}
  {{ form.subject }}
</div>
<div class="fieldWrapper">
  {{ form.message.errors }}
    {{ form.message.label_tag }}
  {{ form.message }}
</div>
<div class="fieldWrapper">
  {{ form.sender.errors }}
  {{ form.sender.label_tag }}
  {{ form.sender }}
</div>
<div class="fieldWrapper">
  {{ form.cc_myself.errors }}
  {{ form.cc_myself.label_tag }}
  {{ form.cc_myself }}
</div>
```

### 10.6.4. Formulário Django

Podemos gerar um fomulário criado, usando apenas uma linha de código.

- **{{ form.as_table }}** Vai renderizar (exibir) o formulário formatado com TAGS &lt;tr>
- **{{ form.as_p }}** Vai renderizar (exibir) o formulário formatado com TAGS &lt;p>
- **{{ form.as_ul }}** Vai renderizar (exibir) o formulário formatado com TAGS &lt;li>
- 
```Django
<form action="" method="post">
  {% csrf_token %}
  <table>
  {{ form.as_table }}
  </table>
  <input type="submit" value="Submit">
</form>
```

### 10.6.5. Mensagem de Erro


Os erros de um único campo são exibidos seguindo o código abaixo, podendo ser alterado para mudar a sua forma de exibição de forma mais personalizada.

```Django
{% if form.campo.errors %}
  <ol>
  {% for error in form.campo.errors %}
    <li><strong>{{ error|escape }}</strong></li>
  {% endfor %}
  </ol>
{% endif %}
```

### 10.6.6. Textos de Ajuda

Muitas vexes o texto de ajuda pode ser grande e conter muitos dados, como senhas que podem conter vários critérios. Para isso, podemos usar o código abaixo para exibir o erro de forma formatada.

```Django
  {% if form.campo.help_text %}
  <p class="help">{{ form.campo.help_text|safe }}</p>
  {% endif %}
```

### 10.6.7. Iterar Sobre um Formulário

Podemos fazer um loop para iterar sobre todos os campos de um formulário. Para saber mais, além de descrição das propriedades dos campos acesse [Looping over the form’s fields](https://7xwm2drhn3gdndpwco2driejom--docs-djangoproject-com.translate.goog/pt-br/dev/topics/forms/#looping-over-the-form-s-fields)

```Django
{% for field in form %}
    <div class="fieldWrapper">
        {{ field.errors }}
        {{ field.label_tag }} {{ field }}
        {% if field.help_text %}
        <p class="help">{{ field.help_text|safe }}</p>
        {% endif %}
    </div>
{% endfor %}
```

## 10.7. Validando Formulários

Podemos ainda validar os formulários com a classe e os parâmetros [validators](https://docs.djangoproject.com/en/dev/ref/validators/). 

Primeiro podemos criar uma função própria e usá-la para validar um valor de um campo do formulário, ou podemos usar uma função pronta para validar o nosso formulário. 

```python
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
```

então precisamos apenas chamar o argumento **validators** dentro de um campo, que serve tanto em campos de modelo, quanto campos de formulários.

```python
from django import forms

class MyForm(forms.Form):
    even_field = forms.IntegerField(validators=[validate_even])
```

ou então podemos usar um validador pronto como:

```python
from django.core.validators import MaxValueValidator, MinValueValidator

max_discount = models.FloatField( verbose_name=u'Maximum Discount', validators = [MinValueValidator(0.0)])
```


## 10.8. FormView

- É uma view que mostra um formulário. Caso tenha um erro da validação é exibido o formulário com os erros para se corrido. Caso o formulário passe pela validação é direcionado para uma nova URL.
- Essa view herda métodos e atributos das seguintes “views”:
  - django.views.generic.base.TemplateResponseMixin
    - **template_name** - O nome completo de um modelo a ser usado conforme definido por uma string.
  - django.views.generic.edit.BaseFormView
  - django.views.generic.edit.FormMixin
    - **initial** - Um dicionário contendo os dados iniciais do formulário.
    - **form_class** - A classe de formulário a ser instanciada.
    - **success_url** -  O URL para redirecionar quando o formulário for processado com sucesso.
    - **prefix** - O prefixo do formulário gerado.
    - **get_form_kwargs ()** -  Construa os argumentos de palavra-chave necessários para instanciar o formulário. 
    - **form_valid(form)** - Redireciona para get_success_url().
    - **get_success_url()** determine a URL para redirecionar quando o formulário for validado com sucesso. Retorna o success_url por padrão. 
    - **form_invalid(form)** - Renderiza uma resposta, fornecendo o formulário inválido como contexto. 
  - django.views.generic.edit.ProcessFormView
  - django.views.generic.base.View

### 10.8.1. Enviando os dados

Os métodos **post** e **get** podem enviar os dados dos formulário para outras Views, e possuem a seguinte sintaxe. 

```Python
def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
```

### 10.8.2. Exemplos

```python
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContatoForm

class IndexView(FormView):
  template_name = 'index.html'
  form_class = ContatoForm
  success_url = reverse_lazy('index')

  def get_context_data(self, **kwargs):
    context = super(IndexView, self).get_context_data(**kwargs)
    #trabalha a lógica do contexto
    return context

  def form_valid(self, form, *args, **kwargs):
    form.send_mail()
    messages.success(self.request, 'E-mail enviado com sucesso')
    return super(IndexView, self).form_valid(form, *args, **kwargs)

  def form_invalid(self, form, *args, **kwargs):
    messages.error(self.request, 'Erro ao enviar o e-mail')
    return super(IndexView, self).form_invalid(form, *args, **kwargs)
```


```python
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # se esta for uma solicitação POST, precisamos processar os dados do formulário
    if request.method == 'POST':
        # crie uma instância de formulário e preencha-a com os dados da solicitação:
        form = NameForm(request.POST)
        # verifique se é válido (confere crsf):
        if form.is_valid():
            # processar os dados em form.cleaned_data conforme necessário
            # ...
            # redirecionar para um novo URL:
            return HttpResponseRedirect('/thanks/')

    # Se for um GET (ou qualquer outro método), criaremos um formulário em branco
    else:
        form = NameForm()
    context = {
        'form': form,
    }
    return render(request, 'name.html', context)
```

```Python
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .forms import Formulario
from django.urls import reverse_lazy

# Create your views here.


class index(FormView):
  template_name = "index.html"
  form_class = Formulario
  success_url = reverse_lazy('success')
  initial = {'message': 'Mensagem Inicial'}

  def post(self, request, *args, **kwargs):
    form = request.POST
    if form.is_valid():
      return render(request, 'success.html', {'form': form})


class success(TemplateView):
  template_name = "success.html"
```


**********************************


# 11. Mensagens de Erro e Sucesso

Tipos de mensagens
- DEBUG - Mensagens relacionadas ao desenvolvimento que serão ignoradas (ou removidas) em uma implantação de produção
- INFO - Mensagens informativas para o usuário
- SUCCESS - Uma ação foi bem-sucedida, por ex. “Seu perfil foi atualizado com sucesso”
- WARNING - Não ocorreu uma falha, mas pode ser iminente
- ERROR - Uma ação não teve sucesso ou ocorreu alguma outra falha 

FONTE (The messages framework)[https://docs.djangoproject.com/pt-br/3.2/ref/contrib/messages/]

Para adicionar uma mensagem, use a sintaxe
```Python
from django.contrib import messages
messages.add_message(request, messages.INFO, 'Hello world.')
```
Alguns métodos de atalho fornecem uma maneira padrão de adicionar mensagens com tags comumente usadas (que geralmente são representadas como classes HTML para a mensagem):
```Python
messages.debug(request, '%s SQL statements were executed.' % count)
messages.info(request, 'Three credits remain in your account.')
messages.success(request, 'Profile details updated.')
messages.warning(request, 'Your account expires in three days.')
messages.error(request, 'Document deleted.'
```

## 11.1. Exibindo a mensagem no Template

```Django
{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
    {% endfor %}
</ul>
{% endif %}
```

Se você estiver usando o processador de contexto, seu modelo deve ser renderizado com um RequestContext. Caso contrário, certifique-se de que as mensagens estejam disponíveis para o contexto do modelo.

Mesmo se você souber que há apenas uma mensagem, você ainda deve iterar sobre a sequência de mensagens, caso contrário, o armazenamento da mensagem não será limpo para a próxima solicitação.

## 11.2. SuccessMessageMixin

Adiciona um atributo de mensagem de sucesso às classes baseadas em FormView 

- Os dados limpos do formulário estão disponíveis para interpolação de strings usando a sintaxe %(field_name)s.
- Para ModelForms, se você precisar acessar os campos do objeto salvo, substitua o método get_success_message(). 

```Python

class AuthorCreateView(SuccessMessageMixin, CreateView):
    model = Author
    success_url = '/success/'
    success_message = "%(name)s was created successfully"
```

```Python
class ComplicatedCreateView(SuccessMessageMixin, CreateView):
    model = ComplicatedModel
    success_url = '/success/'
    success_message = "%(calculated_field)s was created successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.calculated_field,
        )
```


***********************************


# 12. Modelos de Banco de Dados

Aplicativos Django acessam e gerenciam dados através de objetos Python chamados de modelos (models). Modelos definem a estrutura dos dados armazenados, incluindo os tipos de campos e possivelmente também o seu tamanho máximo, valores default, opções de listas de seleção, texto de ajuda para documentação, texto de labels para formulários, etc.

Tudo ocorre de forma independente com o banco de dados, pois tudo é abstraído, ou seja, pode escolher qualquer banco de dados, desde que devidamente configurado nas configurações. 

Algumas bibliotecas podem ser importantes:

- **PyMySQL** - Driver do servidor de conexão python-mysql
- **dj_database_url** - Responsável por configurar o banco em produção. Usado para transmitir os dados do banco de dados local para o heroku
- **psycopg2.binary** - É o responsável pelo bando PostGreeSQL

## 12.1. Configurando o MySQL

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

## 12.2. Configurando o PostGre

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

## 12.3. ORM (Object-Relational-Mapping)

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

## 12.4. Principais Campos

- **CharField** é usado para definir um tamanho fixo (médio a curto) para a string. Você deve especificar o max_length (tamanho máximo) para o dado que será armazenado.
- **TextField** é usado para grandes strings de comprimento variado. Você pode especificar um max_length (tamanho máximo) para o campo, mas isso é usado somente quando o campo é exibido em formulários (forms) (ele não é imposto no nível do banco de dados).
- **IntegerField** é um campo para armazenar números inteiros e para validar valores inseridos como números inteiros em formulários.
- **DateField** e **DateTimeField** são usados para armazenar/representar datas e informações de data/hora. Esses campos também podem declarar os parâmetros (mutuamente exclusivos) auto_now = True (para definir o campo para a data atual toda vez que o modelo é salvo), auto_now_add (para definir a data em que o primeiro modelo foi criado) e default (para definir uma data padrão que pode ser substituída pelo usuário).
- **EmailField** é usada para armazenar e validar em endereço de email.
- **FileField** e **ImageField** são usados para carregar arquivos e imagens respectivamente, (o ImageField simplesmente valida de forma adicional que o arquivo enviado é uma imagem). Eles têm parâmetros para definir como e onde os arquivos enviados são armazenados.
- **AutoField** é um tipo especial de IntegerField que é incrementada automaticamente. Uma chave primária desse tipo é adicionada de forma automática ao seu modelo, se você não especificar explicitamente um.
- **ForeignKey** é usado para especificar um relacionamento um-para-muitos com outro modelo do banco de dados (por exemplo, um carro tem um fabricante, mas um fabricante pode fazer muitos carros). O lado "um" do relacionamento é o modelo que contém a "chave" (os modelos que contêm uma "chave estrangeira" referem-se a essa "chave" e estão no lado "muitos" de tal relacionamento).
- **ManyToManyField** é usado para especificar um relacionamento muitos-para-muitos (por exemplo, um livro pode ter vários gêneros e cada gênero pode conter vários livros). Em nosso aplicativo de biblioteca, usaremos isso de maneira muito semelhante às ForeignKeys, mas elas podem ser usadas de maneiras mais complicadas para descrever as relações entre os grupos. Eles têm o parâmetro on_delete para definir o que acontece quando o registro associado é excluído (por exemplo, um valor de models.SET_NULL simplesmente definiria o valor como NULL).

###  12.4.1. Os principais parâmetros dos campos

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

## 12.5. Tipos de Relacionamentos em Models

### 12.5.1. Relacionamento 1:1 - OneToOne

O relacionamento 1-1 define que um item de uma entidade só poderá se relacionar com um item de outra entidade e o inverso também será verdade. Como exemplo podemos supor que na regra de negócio um determinado cliente pode ter apenas um único endereço, e o endereço pode estar atribuído a um único cliente.

```python
class Endereco(models.Model):
    # Definimos seus atributos

class Cliente(models.Model):
    # Definimos seus atributos
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
```

### 12.5.2. Relacionamento 1:N - ForeignKey

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

### 12.5.3. Relacionamento N:N ManyToMany

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

- ManyToMany cria uma tabela extra, entretanto,  caso queria adicionar atributos extras na coluna, será necessária ligar com um novo modelo. 

- Exemplo retirado de [Django's ManyToMany Relationship with Additional Fields](https://stackoverflow.com/questions/4443190/djangos-manytomany-relationship-with-additional-fields)
```Python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
```


-> O Exemplo completo pode ser acessado em: [Relacionamento 1-1, 1-N e N-N com Django](https://www.treinaweb.com.br/blog/relacionamento-1-1-1-n-e-n-n-com-django/)

## 12.6. Herança de modelos

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

## 12.7. Classes e métodos para os nossos modelos

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

## 12.8. Gerando os bancos de dados

Para gerar os bancos de dados precisamos executar o comando **makemigrations**. Este comando irá gerar um histórico do banco e manter a integridade entre as versões. Após os testes de integridade forem checados, devemos usar o comando **migrate** para gerar as tabelas do banco. Podemos também especificar o nome de aplicação caso necessário, ao invés de executar para todas todas. 

```python
>>python manage.py makemigrations
>>python manage.py migrate
```
## 12.9. ORM - Consultas

Podemos usar uma API para acessar os dados do nosso modelo, que contém diversas abstrações de comandos que nos permitem trabalhar com os objetos, principalmente dentro de uma view.

### 12.9.1. objects.create - Criando um objeto e salvando no banco de dados

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

### 12.9.2. objects.all() - Encontrando um ou vários objetos

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

### 12.9.3. objects.only() - Consultando apenas alguma colunas

Comando em SQL
```SQL
SELECT name, age FROM Person;
```
Comando em Django
```python
Person.objects.only('name', 'age')
```

### 12.9.4. objects.values().distinct() - Selecionado apenas os dados distintos
Consulta SQL
```SQL
SELECT DISTINCT name, age FROM Person;
```
Comando Django
```python
Person.objects.values('name', 'age').distinct()
```

### 12.9.5. Limit e Offset - Consultando um número específico de linhas

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
### 12.9.6. objects.get - Recuperando um único Objeto

O filter() sempre lhe dará um QuerySet, mesmo se um único objeto combina com a consulta - neste caso, ele será uma QuerySet que contém um único elemento.Se você sabe que somente um objeto combina com sua consulta, você pode usar o método get() em uma Manager o qual retorna o objeto diretamente:

```python
one_entry = Entry.objects.get(pk=1)
```

### 12.9.7. objects.filter - Filtrando a consulta de dados

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


#### 12.9.7.1. Filtrando pelos operadores de comparação

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

#### 12.9.7.2. Filtrando com o operador Between

Comandos SQL
```SQL
SELECT * FROM Person WHERE age BETWEEN 10 AND 20;
```

Comandos Django
```Python
Person.objects.filter(age__range=(10,20))
```

#### 12.9.7.3. Filtrando com o operador LIKE

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

#### 12.9.7.4. Filtrando com o operador IN

Comandos SQL
```SQL
WHERE id IN (1,2);
```

Comandos Django
```Python
Person.objects.filter(id__in=[1,2])
```

#### 12.9.7.5. Filtrando com o operador AND

Comandos SQL
```SQL
SELECT * FROM PERSON WHERE gender='male' AND age > 25;
```

Comandos Django
```Python
Person.objects.filter(gander='male', age__gt=25)
```

#### 12.9.7.6. Filtrando com o operador OR

Comandos SQL
```SQL
SELECT * FROM PERSON WHERE gender='male' OR age > 25;
```

Comandos Django
```Python
FROM django.db.models import Q
Person.objects.filter(Q(gander='male') | Q(age__gt=25))
```

#### 12.9.7.7. Filtrando com o operador NOT

Comandos SQL
```SQL
SELECT * FROM PERSON WHERE NOT gender='male';
```

Comandos Django
```Python
Person.objects.exclude(gander='male')
```

#### 12.9.7.8. Filtrando com o operador NULL

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

#### 12.9.7.9. Filtrando com o operador NOT NULL

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

### 12.9.8. objects.order_by - Ordenando consultas

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

### 12.9.9. UPDATE

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


### 12.9.10. DELETE

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

#### 12.9.10.1. Funções SQL - MIN, MAX, AVG, SUM E COUNT

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

### 12.9.11. GROUP BY

```SQL
SELECT gender, COUNT(*) AS count FROM Person GROUP BY gender;
```

Comando Django
```Python
Person.objects.values('gender').annotate(count=Count('gender'))
```

#### 12.9.11.1. HAVING
```SQL
SELECT gender, COUNT(*) AS count FROM Person GROUP BY gender HAVING count > 1;
```

Comando Django
```Python
Person.objects.values('gender').annotate(count=Count('gender')).values('gender', 'count').filter(count_gt=1)
```

### 12.9.12. Consultas Personalizadas

O ORM ainda nos permite consultas de SQL em estado BRUTO, para podermos realizar consultas mais complexas, ou até mesmo, se quisermos evitar ter que aprender SQL de outra forma.

```Python
Person.objects.raw('SELECT * FROM myapp_person')
Person.objects.raw('SELECT id, first_name, last_name, birth_date FROM myapp_person')
Person.objects.raw('SELECT last_name, birth_date, first_name, id FROM myapp_person')
```

#### 12.9.12.1. Passando parâmetros para consultas personalizadas

Existem cuidados que devemos tomar, e mais opções de personalizações que podem ser acessadas em 
[Passing parameters into raw()](https://docs.djangoproject.com/en/dev/topics/db/sql/#passing-parameters-into-raw)

```python
lname = 'Doe'
>>> Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])
```


#### 12.9.12.2. Referências completas de ORM Django

- [Consultas](https://docs.djangoproject.com/en/dev/topics/db/queries/)
- [QuerySet API reference](https://docs.djangoproject.com/en/dev/ref/models/querysets/)
- [Como funciona o ORM do Django](https://www.gilenofilho.com.br/como-funciona-o-orm-do-django/)
- [Performing raw SQL queries](https://docs.djangoproject.com/en/dev/topics/db/sql/)

## 12.10. Exemplo de Views e Models

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

#### 12.10.0.1. Rota produto

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
## 12.11. ModelForms

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

### 12.11.1. O Método Save

Este método `save()` aceita um argumento nomeado opcional commit, que aceita ou True ou False. Se você chamar `save()` com commit=False, então ele devolverá um objeto que ainda não foi gravado no banco de dados. Neste caso, é sua responsabilidade chamar `save()` na instância de modelo. Isso é útil se você quer fazer algum processamento customizado no objeto antes de gravá-lo, ou se você quer usar um umas das opções de gravação de modelo especializadas. commit é True por padrão.

### 12.11.2. Especificando Campos do Modelo no Formulário

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

### 12.11.3. Alterar Tipo do Campo Model-Form

Os tipos de campos padrão, Mas o ModelForm te dá a flexibilidade de mudar o campo de formulário para um determinado campo de modelo. Para alterar o tipo, basta declarar o campo novamente no formulário, parar sobrescreve-lo. 

```Python
class ArticleForm(ModelForm):
  pub_date = MyDateFormField()

  class Meta:
    model = Article
```

### 12.11.4. Herança de Formulário

Como nos formulários básicos, você pode extender e reutilizar ModelForms através da herança. Isso é útil se você precisa declarar campos ou métodos adicionais em uma classe pai para uso em alguns formulários derivados de modelos. 

### 12.11.5. Alterando Widgets 

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

### 12.11.6. Passando Valores Iniciais 

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

********************************************************

# Deploy 

Conceitos
- **Ambiente de Produção** - O ambiente de produção é o ambiente fornecido pelo computador/servidor onde você executará seu site para consumo externo
  - um ambiente de produção incluí, hardware de computador, um sistema operacional, uma linguagem em tempo de produção, um servidor web, um servidor de aplicação e um banco de dados. 
- **Infraestrutura como Serviço (IaaS)** - São ambientes remotos que fornecem hardware e rede a um determinado preço. Ou seja, deve-se escolher o hardware, Sistema operacional, o servidor web, etc. 
- **Plataforma como Serviço (PaaS)** - você não precisa se preocupar com a maior parte do seu ambiente de produção (servidor da web, servidor de aplicativos, balanceadores de carga), pois a plataforma host cuida disso para você (junto com a maior parte do que você precisa fazer para para dimensionar seu aplicativo)

## Deploy Heroku

Alguma considerações, 
    - Deve-se ter configurado corretamente os arquivos estáticos com o whitenoise ou dj-static. 
    - Deve desativar o atributo `DEGUB = False` no arquivo settings do projeto. 
    - Deve-se permiter todos os HOST `ALLOWED_HOSTS = ['*']`, e definir posteriormente apenas o HOTS do Heroku como válido. 

Fluxo 

1. Baixe o Heroku CLI
2. Faça login localmente com `heroku login`
3. Crie uma aplicação com nome aleatório com `heroku create`
4. Vinculando nosso repositório git com nosso aplicativo Heroku com `heroku git:remote -a NOMEAPP`
5. Instale o Servidor de Aplicativo `pip install gunicorn`. (Atualmente o servidor de desenvolvimento é python mange.py runserver )
6. Vamos testar nosso servidor de aplicativos. Execute o comando `gunicorn projeto.wsgi` dentro do diretório do projeto. 
7. [Crie um perfil](https://devcenter.heroku.com/articles/procfile)
   - Os aplicativos Heroku incluem um Perfil que especifica os comandos que são executados pelo aplicativo na inicialização. 
   - Dentro do diretório principal, que contém o arquivo manage.py, execute o comando `touch Procfile`. 
   - Agora teremos que escrever comandos que heroku deve executar na inicialização do aplicativo, isso inclui iniciar o servidor de aplicativos
   - `web: gunicorn tutorial.wsgi`
8. Deve-se criar um arquivo chamado `runtime.txt` na raiz do projeto com a versão do python usada. `Python 3.9.1` 
8. Devemos criar/ou atualizar o arquivo [requirements.txt](https://undefinedzack.hashnode.dev/how-to-create-a-to-do-app-in-django-with-bootstrap-and-font-awesome)
   - Este arquivo contém todos os módulos que usamos em nosso aplicativo para o bom funcionamento e sim você não precisa escrever manualmente todos os módulos que você usou, há um comando para isso. Ele calculará automaticamente quais módulos você usou com a versão.
   - `pip freeze > requirements.txt`
9. Atualize o repositório git com as últimas alterações
   1.  `git add .`
   2.  `git commit -m "adicionado gunicorn (servidor de aplicativo) com requisitos.txt e Procfile" `
10. Por fim, devemos enviar a aplicação para o HEROKU
    1.  `git push heroku master`


Erros : 
- [Collectstatic error while deploying Django app to Heroku](https://stackoverflow.com/questions/36665889/collectstatic-error-while-deploying-django-app-to-heroku)
- [How to deploy a Django app to Heroku](https://dev.to/undefinedzack/how-to-deploy-a-django-app-to-heroku-3k6i)
