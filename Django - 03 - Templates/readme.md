# 1. Projeto

Este projeto teve como estudo usar um template base e usar a herança de templates, permitindo separar uma única página em vários arquivos modulares. Além de usar arquivos estáticos.

- [1. Projeto](#1-projeto)
- [2. Templates](#2-templates)
- [3. Variáveis](#3-variáveis)
- [4. Herança de templates](#4-herança-de-templates)
  - [4.1. Dicas para usar a herança](#41-dicas-para-usar-a-herança)
- [5. Arquivos Estáticos](#5-arquivos-estáticos)
  - [5.1. Configuração dos Arquivos Estáticos](#51-configuração-dos-arquivos-estáticos)
  - [5.2. Estutura de Pastas e Arquivos](#52-estutura-de-pastas-e-arquivos)
  - [5.3. Exemplo com Passagem de Contexto](#53-exemplo-com-passagem-de-contexto)
  - [5.4. Urls Projeto](#54-urls-projeto)
  - [5.5. View da Aplicação](#55-view-da-aplicação)
  - [5.6. Url da Aplicação](#56-url-da-aplicação)
  - [5.7. View da Aplicação](#57-view-da-aplicação)
  - [5.8. Arquivo Index](#58-arquivo-index)
    - [5.8.1. Saída](#581-saída)
  - [5.9. Exemplo Com Herança, Arquivos Estáticos e Inclusão de Arquivos](#59-exemplo-com-herança-arquivos-estáticos-e-inclusão-de-arquivos)
  - [5.10. Settings do Projeto](#510-settings-do-projeto)
  - [5.11. Urls Projeto](#511-urls-projeto)
  - [5.12. Url da Aplicação](#512-url-da-aplicação)
  - [5.13. View da Aplicação](#513-view-da-aplicação)
  - [5.14. Template Base](#514-template-base)
  - [5.15. Template index.html](#515-template-indexhtml)
  - [5.16. Arquivo Footer](#516-arquivo-footer)
    - [5.16.1. HTMLs](#5161-htmls)
      - [5.16.1.1. Base](#51611-base)
      - [5.16.1.2. Index](#51612-index)
      - [5.16.1.3. footer](#51613-footer)
- [6. TAGS](#6-tags)
  - [6.1. comment](#61-comment)
  - [6.2. csrf_token](#62-csrf_token)
  - [6.3. cycle](#63-cycle)
  - [6.4. debug](#64-debug)
  - [6.5. filter](#65-filter)
  - [6.6. firstof](#66-firstof)
  - [6.7. for](#67-for)
  - [6.8. for … empty](#68-for--empty)
  - [6.9. if](#69-if)
  - [6.10. Operadores booleanos](#610-operadores-booleanos)
  - [6.11. lorem](#611-lorem)
  - [6.12. now](#612-now)
  - [6.13. regroup](#613-regroup)
  - [6.14. url](#614-url)
    - [6.14.1. url interagindo com o path](#6141-url-interagindo-com-o-path)
    - [6.14.2. url com apelidos](#6142-url-com-apelidos)
  - [6.15. with](#615-with)
  - [6.16. load](#616-load)
  - [6.17. include](#617-include)
- [7. Filtros](#7-filtros)
  - [7.1. add](#71-add)
  - [7.2. addslashes](#72-addslashes)
  - [7.3. capfirst](#73-capfirst)
  - [7.4. center](#74-center)
  - [7.5. cut](#75-cut)
  - [7.6. date](#76-date)
  - [7.7. Deafult](#77-deafult)
  - [7.8. default_if_none](#78-default_if_none)
  - [7.9. dictsort](#79-dictsort)
  - [7.10. divisibleby](#710-divisibleby)
  - [7.11. escape](#711-escape)
  - [7.12. first](#712-first)
  - [7.13. floatformat](#713-floatformat)
  - [7.14. join](#714-join)
  - [7.15. last](#715-last)
  - [7.16. length](#716-length)
  - [7.17. linebreaks](#717-linebreaks)
  - [7.18. linebreaksbr](#718-linebreaksbr)
  - [7.19. linenumbers](#719-linenumbers)
  - [7.20. force_escape](#720-force_escape)
  - [7.21. lower](#721-lower)
  - [7.22. make_list](#722-make_list)
  - [7.23. pluralize](#723-pluralize)
  - [7.24. random](#724-random)
  - [7.25. safe](#725-safe)
  - [7.26. slice](#726-slice)
  - [7.27. slugify](#727-slugify)
  - [7.28. striptags](#728-striptags)
  - [7.29. time](#729-time)
  - [7.30. timesince](#730-timesince)
  - [7.31. title](#731-title)
  - [7.32. truncatewords](#732-truncatewords)
  - [7.33. upper](#733-upper)
  - [7.34. wordcount](#734-wordcount)
  - [7.35. wordwrap](#735-wordwrap)
  - [7.36. yesno](#736-yesno)

# 2. Templates

Um template Django é um documento de texto ou uma string Python marcada usando a linguagem de template Django. Algumas construções são reconhecidas e interpretadas pelo mecanismo de template. Os principais são variáveis ​​e tags. Um modelo é renderizado com um contexto. A renderização substitui variáveis ​​por seus valores, que são pesquisados ​​no contexto, e executa tags. Todo o resto é produzido como está.


#  3. Variáveis

Uma variável produz um valor do contexto, que é um objeto do tipo dicionário que mapeia chaves para valores. As variáveis ​​são circundadas por `{{ e }}` (chaves duplas) assim:

```Django
My first name is {{ first_name }}. My last name is {{ last_name }}.
```

Se os valores passados pelo contexto forem `{'first_name': 'John', 'last_name': 'Doe'}`, então o resultado seria: 

```html
My first name is John. My last name is Doe.
```

As pesquisas de dicionário, de atributo e de índice de lista são implementadas com uma notação de ponto:

```Django
{{ my_dict.key }}
{{ my_object.attribute }}
{{ my_list.0 }}
```

# 4. Herança de templates

A parte mais poderosa - e portanto a mais complexa - do mecanismo de template do Django é a herança de template. A herança do modelo permite que você crie um modelo básico de “esqueleto” que contém todos os elementos comuns do seu site e define os blocos que os modelos filhos podem substituir.


Para criar o modelo base, iremos criar um esqueleto que irá conter todo que é comum em todo as as páginas que a herdarem, como links de bibliotecas, menus, barras laterais, rodapé, etc. 

Exemplo de um arquivo `base.html`

```Django
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

Usando as TAGS `{% block <name> %}{% endblock %}`, podemos sobrescrever o que estiver contido dento deles usando o nome que a atribuímos no arquivo que herdar o documento base.  Exemplo de documento que herda de base. Para herdar, usamos a tag `extends`

```Django
{% extends "base.html" %}

{% block title %}My amazing blog{% endblock %}

{% block content %}
{% for entry in blog_entries %}
    <h2>{{ entry.title }}</h2>
    <p>{{ entry.body }}</p>
{% endfor %}
{% endblock %}
```

## 4.1. Dicas para usar a herança

- Se você usar em um modelo, `{% extends %}` deve ser a primeira tag de modelo nesse modelo. A herança do modelo não funcionará, caso contrário.
-  Mais tags `{% block %}` em seus modelos básicos são melhores. Lembre-se de que os modelos filhos não precisam definir todos os blocos pais, portanto, você pode preencher padrões razoáveis ​​em vários blocos e, em seguida, definir apenas aqueles de que precisa mais tarde. É melhor ter mais ganchos do que menos ganchos.
-  Se você estiver duplicando conteúdo em vários modelos, provavelmente significa que você deve mover esse conteúdo para um `{% block %}` em um modelo pai.
-  Se você precisar obter o conteúdo do bloco do template pai, a variável `{{ block.super }}{{ block.super }}` fará o truque. Isso é útil se você deseja adicionar ao conteúdo de um bloco pai em vez de substituí-lo completamente. Os dados inseridos usando não serão escapados automaticamente, uma vez que já foram escapados, se necessário, no modelo pai.
-  Usando o mesmo nome de modelo do qual você está herdando, pode ser usado para herdar um modelo ao mesmo tempo em que o substitui. Combinado com `{% extends %}{{ block.super }}`, esta pode ser uma maneira poderosa de fazer pequenas personalizações. Consulte Estendendo um modelo substituído em Como substituir modelos para obter um exemplo completo.
-  Variáveis ​​criadas fora de usando a sintaxe da tag template não podem ser usadas dentro do bloco. Por exemplo, este modelo não renderiza nada:
  
```Django
{% block %}as{% translate "Title" as title %}
{% block content %}{{ title }}{% endblock %}
```

Para facilitar a leitura extra, você pode opcionalmente dar um nome à sua tag. Por exemplo:

```Django
    {% block content %}
    ...
    {% endblock content %}
```

- Em modelos maiores, essa técnica ajuda a ver quais tags `{% block %}` estão sendo fechadas. Finalmente, observe que você não pode definir várias blocktags com o mesmo nome no mesmo modelo. Essa limitação existe porque uma tag de bloco funciona em “ambas” direções. Ou seja, uma tag de bloco não fornece apenas uma lacuna a ser preenchida - ela também define o conteúdo que preenche a lacuna no pai . Se houvesse duas blocktags com nomes semelhantes em um modelo, o pai desse modelo não saberia qual dos conteúdos dos blocos usar.


# 5. Arquivos Estáticos

Para usar os arquivos estáticos dentro de um template, primeiro devemos configurar corretamente o arquivo `settings.py` especificando o caminho dos arquivos estáticos. Em seguida devemos ter um diretório chamado   `static` com os arquivos dentro da aplicação. Em seguida, em todos os templates, nas primeiras linhas devemos especificar que iremos usar arquivos estáticos, carregando ele com a tag `{% load static %}`.

```Django
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

## 5.1. Configuração dos Arquivos Estáticos

- Em testes podemos instalar a biblioteca
- `whitenoise` - Responsável por cuidar dos arquivos estáticos, como o JavaScript e CSS
- Em produção devemos instalar a biblioteca 
  - `dj-static` - Responsável por exibir arquivos estáticos e dinâmicos de forma mais segura, substituindo o whitenoise.
- Para incluir imagens, devemos usar?
  -  `django-stdimage` - Trabalha com imagens dentro da aplicação (imagens de um produto, por exemplo)
- Devemos alterar as aplicações permitidas dentro do arquivo `settings.py` para permitir as novas aplicações, como o `stdimage` e o `bootstrap4`. 

- Caso seja usado o `whitenoise`, devemos **inserir o middleware na segunda linha**. com a seguinte sintaxe: `'whitenoise.middleware.WhiteNoiseMiddleware'`. 
- Para permitir os templates, precisamos criar um diretório na aplicação chamado `templates`, e dentro da linha de configuração `TEMPLATES`, na opção `DIR` devemos especificar o diretório: `DIR['templates']`.
- Devemos também informar o diretório dos nosso arquivos estáticos como visto nas configurações acima. 
  
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

- Nos arquivos `*.html` precismos informar que os mesmos irão trabalhar com arquivos estáticos. Para isso, bastamos usar a sintaxe abaixo

```Django
{% load static %}
<link rel="stylesheet" href="{% static 'css/estilos.css' %}">
```

- O comando abaixo é responsável por coletar todos os arquivos estáticos ao longo das aplicações e a reúnem de forma central dentro do Projeto. 

```shell
python manage.py collectstatic
```

- Podemos também especificar os caminhos de mídias que foram especificados dentro do arquivo `settings.py`, para que o projeto faça o roteamento correto dos arquivos (caso seja necessário no projeto arquivos de mídias).

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

## 5.2. Estutura de Pastas e Arquivos

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

## 5.3. Exemplo com Passagem de Contexto


## 5.4. Urls Projeto

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
] 
```

## 5.5. View da Aplicação

```python
from django.shortcuts import render

def index(request):
  context =	{} 
  return render(request, 'index.html', context)
```

## 5.6. Url da Aplicação

```python
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]  
```

## 5.7. View da Aplicação

```python
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

## 5.8. Arquivo Index

```Django
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

### 5.8.1. Saída

**Marca Ford**

Lista de Cores
  - RED
  - WHITE
  - BLUE


## 5.9. Exemplo Com Herança, Arquivos Estáticos e Inclusão de Arquivos

## 5.10. Settings do Projeto

```python
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

## 5.11. Urls Projeto

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

## 5.12. Url da Aplicação

```python
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]  
```

## 5.13. View da Aplicação

```python
from django.shortcuts import render

def index(request):
  context =	{} 
  return render(request, 'index.html', context)
```

## 5.14. Template Base

- Contém uma TAG especificando que o arquivo precisará usar arquivos estáticos
  -  `{% load static %}`
- Contém o carregamento de todos os arquivos estáticos de personalização como CSS, Fonts, JavaScript e outros.
  - `<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">`
  - `<script src="{% static 'js/jquery-min.js' %}"></script>`
  - `<link rel="stylesheet" href=" {% static 'fonts/line-icons.css' %}">`
- Contém um bloco onde irá ser carregado um conteúdo
  - `{% block content %} {% endblock content %}` 
- Contém uma TAG para carregar uma Imagem e uma TAG que irá redirecionar a página para a URL com o nome de 'index'
  - `<a href="{% url 'index' %}" class="navbar-brand"><img src=" {% static 'img/logo.png' %}" alt=""></a>`

## 5.15. Template index.html

- O arquivo index herda todas os arquivos carregados, o menu e as imagens do template BASE, abstraindo e simplificando o código
  - `{% extends 'base.html' %}`
- Além disso o arquivo diz logo em seguida que irá carregar arquivos estátricos.
  - `{% load static %}`
- Dentro do Bloco, **de mesmo nome** da base, iremos especificar o conteúdo que será inserido, na mesma posição original do arquivo base. 
  - `{% block content %} ... {% endblock content %}`
- Dentro do bloco iremos incluir arquivos HTML que contém diversos conteúdos, na ordem em que devem aparecer, 
  - `{% include 'footer.html' %}`

## 5.16. Arquivo Footer

- Contém o carregamento de arquivos estáticos
  - `{% load static %}`
- Contém todo o código HTML responsável pela formatação do rodapé da página. 


### 5.16.1. HTMLs

#### 5.16.1.1. Base

```Django
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

#### 5.16.1.2. Index

```python
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

#### 5.16.1.3. footer

```python
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

# 6. TAGS

As tags fornecem lógica arbitrária no processo de renderização. Esta definição é deliberadamente vaga. Por exemplo, uma tag pode produzir conteúdo, servir como uma estrutura de controle, por exemplo, uma instrução `if` ou um loop `for`, obter conteúdo de um banco de dados ou até mesmo permitir o acesso a outras tags de modelo.

As tags são circundadas por `{% e %}` (chave e porcentagem?) assim:

```python
{% csrf_token %}
```

As tags aceitam parâmetros como:

```python
{% cycle 'odd' 'even' %}
{% url 'produto/' produto.id %}
```

Algumas tags exigem tags de início e fim:

```python
{% if user.is_authenticated %} Hello, {{ user.username }}.{% endif %}
```


## 6.1. comment

Ignora tudo entre as tags. Uma nota opcional pode ser inserida na primeira tag. Por exemplo, isso é útil ao comentar o código para documentar porque o código foi desativado. `{% comment %}{% endcomment %}`

```Django
<p>Rendered text with {{ pub_date|date:"c" }}</p>
{% comment "Optional note" %}
    <p>Commented out text with {{ create_date|date:"c" }}</p>
{% endcomment %}
```

Para criar um comentário de uma linha em um modelo, use a sintaxe de comentário: `{# #}`.

```django
{# greeting #}hello
```

## 6.2. csrf_token

Essa tag é usada para proteção contra CSRF, conforme descrito na documentação para [Cross Site Request Forgeries]([https://link](https://7xwm2drhn3gdndpwco2driejom--docs-djangoproject-com.translate.goog/en/3.1/ref/csrf/)) .

## 6.3. cycle

Produz um de seus argumentos cada vez que essa tag é encontrada. O primeiro argumento é produzido no primeiro encontro, o segundo argumento no segundo encontro e assim por diante. Depois que todos os argumentos são exauridos, a tag passa para o primeiro argumento e o produz novamente.

Esta tag é particularmente útil em um loop:

```python
{% for o in some_list %}
    <tr class="{% cycle 'row1' 'row2' %}">
        ...
    </tr>
{% endfor %}
```
A primeira iteração produz HTML que se refere à classe row1, a segunda a row2, a terceira a row1novamente e assim por diante para cada iteração do loop. Você também pode usar variáveis.


## 6.4. debug

Produz uma carga completa de informações de depuração, incluindo o contexto atual e os módulos importados.

## 6.5. filter

Filtra o conteúdo do bloco por meio de um ou mais filtros. Vários filtros podem ser especificados com canais e filtros podem ter argumentos, assim como na sintaxe de variável. Observe que o bloco inclui todo o texto entre as tags `filter` e `endfilter`.

```Django
{% filter force_escape|lower %}
    This text will be HTML-escaped, and will appear in all lowercase.
{% endfilter %}
```

## 6.6. firstof

Produz a primeira variável de argumento que não é 'falsa' (ou seja, existe, não está vazia, não é um valor booleano falso e não é um valor numérico zero). Não produz nada se todas as variáveis ​​passadas forem 'falsas'.

```Django
{% firstof var1 var2 var3 %}
```

Isso é equivalente a:

```Django
{% if var1 %}
    {{ var1 }}
{% elif var2 %}
    {{ var2 }}
{% elif var3 %}
    {{ var3 }}
{% endif %}
```

## 6.7. for

Faz um loop em cada item em uma matriz, tornando o item disponível em uma variável de contexto. Por exemplo, para exibir uma lista de atletas fornecida em `athlete_list`:

```Django
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

## 6.8. for … empty

A tag `for` pode receber uma cláusula opcional cujo texto é exibido se a matriz fornecida estiver vazia ou não puder ser encontrada: `{% empty %}`

```Django
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% empty %}
    <li>Sorry, no athletes in this list.</li>
{% endfor %}
</ul>
```

## 6.9. if

A tag avalia uma variável e se essa variável for 'verdadeira' (ou seja, existe, não está vazia e não é um valor booleano falso), o conteúdo do bloco é gerado: `{% if %}`

```Django
{% if athlete_list %}
    Number of athletes: {{ athlete_list|length }}
{% elif athlete_in_locker_room_list %}
    Athletes should be out of the locker room soon!
{% else %}
    No athletes.
{% endif %}
```

## 6.10. Operadores booleanos

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


## 6.11. lorem

Exibe texto latino 'lorem ipsum' de forma aleatória. Isso é útil para fornecer dados de amostra em modelos. A sintaxe é `{% lorem [count] [method] [random] %}`, onde:

- `count` - Um número (ou variável) contendo o número de parágrafos ou palavras a serem gerados (o padrão é 1).
- `method` - Quer por palavras, para HTML parágrafos ou para blocos de parágrafo de texto simples (o padrão é b).
- `random` - A palavra random, que se dada, não usa o parágrafo comum (“Lorem ipsum dolor sit amet…”) ao gerar texto.

Exemplos? 

- `{% lorem %}` produzirá o parágrafo comum “lorem ipsum”.
- `{% lorem 3 p %}` irá gerar o parágrafo “lorem ipsum” comum e dois parágrafos aleatórios, cada um envolvido em tags P HTML .
- `{% lorem 2 w random %}` irá produzir duas palavras latinas aleatórias.

## 6.12. now 

Exibe a data e/ou hora atual, usando um formato de acordo com a string fornecida. Essa string pode conter caracteres especificadores de formato, conforme descrito na seção de filtro date.

```Django
It is {% now "jS F Y H:i" %}
```

para ver mais opções acesse [now](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#now)

## 6.13. regroup

Reagrupa uma lista de objetos semelhantes por um atributo comum. Você pode usar a tag para agrupar a lista de cidades por país. O seguinte snippet de código de modelo faria isso: `{% regroup %}`. Para ver o exemplo completo acesse: [regroup](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#regroup)

```Django
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
## 6.14. url

Retorna uma referência de caminho absoluto (um URL sem o nome de domínio) correspondendo a uma determinada visualização e parâmetros opcionais. Quaisquer caracteres especiais no caminho resultante serão codificados usando `iri_to_uri()`.

```Django
{% url 'some-url-name' v1 v2 %}
```

O primeiro argumento é um nome de padrão de URL. Pode ser um literal entre aspas ou qualquer outra variável de contexto. Argumentos adicionais são opcionais e devem ser valores separados por espaço que serão usados ​​como argumentos no URL. 


### 6.14.1. url interagindo com o path

```python
path('client/<int:id>/', app_views.client, name='app-views-client')
```

```Django
{% url 'app-views-client' client.id %}
```

### 6.14.2. url com apelidos

Se quiser recuperar um URL sem exibi-lo, você pode usar uma chamada um pouco diferente:

```Django
{% url 'some-url-name' arg arg2 as the_url %}
<a href="{{ the_url }}">I'm linking to {{ the_url }}</a>
```

Essa sintaxe não causará erro se a visualização estiver ausente. Na prática, você usará isso para vincular a visualizações que são opcionais: `{% url ... as var %}`

```Django
{% url 'some-url-name' as the_url %}
{% if the_url %}
  <a href="{{ the_url }}">Link to optional stuff</a>
{% endif %}
```

## 6.15. with

Armazena em cache uma variável complexa com um nome mais simples. Isso é útil ao acessar um método 'caro' (por exemplo, um que acessa o banco de dados) várias vezes.

```Django
{% with total=business.employees.count %}
    {{ total }} employee{{ total|pluralize }}
{% endwith %}
```

A variável preenchida (no exemplo acima, total) está disponível apenas entre as tags `{% with %}{% endwith %}`. Você pode atribuir mais de uma variável de contexto:

```Django
{% with alpha=1 beta=2 %}
    ...
{% endwith %}
```

## 6.16. load 

Carrega um conjunto de tags de modelo personalizado. Por exemplo, o modelo a seguir carregaria todas as tags e filtros registrados `somelibrary` localizados no pacote package.`otherlibrary`:

```Django
{% load somelibrary package.otherlibrary %}
```

Você também pode carregar seletivamente filtros ou tags individuais de uma biblioteca, usando o argumento `foo`. Neste exemplo, as tags/filtros do modelo nomeados `foo` e `bar` serão carregados de `somelibrary`:

```Django 
{% load foo bar from somelibrary %}
```

## 6.17. include

Carrega um modelo e o renderiza com o contexto atual. Esta é uma forma de 'incluir' outros modelos em um modelo. O nome do modelo pode ser uma variável ou uma string codificada (entre aspas), entre aspas simples ou duplas. Este exemplo inclui o conteúdo do modelo `foo/bar.html`:

```Django
{% include "foo/bar.html" %}
```

Você pode passar contexto adicional para o modelo usando argumentos de palavra-chave:

```Django
{% include "name_snippet.html" with person="Jane" greeting="Hello" %}
```

# 7. Filtros

Filtros transformam os valores de variáveis ​​e argumentos de tag. Eles se parecem com isto:

```Django
{{ django|<filter>}}
```

## 7.1. add 

Adiciona o argumento ao valor: Exemplo: Se value for 4, a saída será 6.

```Django 
{{ value|add:"2" }}
```

## 7.2. addslashes

Adiciona barras antes das aspas. Útil para sequências de escape em CSV, por exemplo: Se value for "I'm using Django", a saída será: "I\'m using Django"

```Django
{{ value|addslashes }}
```

## 7.3. capfirst

Capitaliza o primeiro caractere do valor. Se o primeiro caractere não for uma letra, este filtro não terá efeito: Se value for "django", a saída será "Django".

```Django
{{ value|capfirst }}
```

## 7.4. center

Centraliza o valor em um campo de uma determinada largura: Se value for "Django", a saída será : `"     Django    "`

```Django
"{{ value|center:"15" }}"
```

## 7.5. cut
Remove todos os valores de arg da string fornecida. Se value for `String with spaces`, a saída será `Stringwithspaces`

```Django 
{{ value|cut:" " }}
```

## 7.6. date

Formata uma data de acordo com o formato fornecido. Se value for um `datetime`, a saída será a string `Wed 09 Jan 2008`. Para ver a lista completa de personalização de datas acesse [Date](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date)

```Django 
{{ value|date:"D d M Y" }}
```

## 7.7. Deafult

Se o valor for avaliado como `False,` usa o padrão fornecido. Caso contrário, usa o valor. Se value for `""` (a string vazia), a saída será `nothing`.

```Django
{{ value|default:"nothing" }}
```

## 7.8. default_if_none

Se (e somente se) o valor for `None`, usa o padrão fornecido. Caso contrário, usa o valor. Observe que, se uma string vazia for fornecida, o valor padrão não será usado. Se value for `None`, a saída será `nothing`.

```Django
{{ value|default_if_none:"nothing" }}
```

## 7.9. dictsort

Pega uma lista de dicionários e retorna essa lista classificada pela chave fornecida no argumento.  Se value for `[{'name': 'zed', 'age': 19}, {'name': 'amy', 'age': 22}, {'name': 'joe', 'age': 31},]` a saída será `[{'name': 'amy', 'age': 22}, {'name': 'joe', 'age': 31}, {'name': 'zed', 'age': 19},]`

```Django
{{ value|dictsort:"name" }}
```

Uutro exemplo :

```Django
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

Então a saída seria:

* Alice (Lewis)
* 1984 (George)
* Timequake (Kurt)
  

## 7.10. divisibleby

Retorna `True` se o valor for divisível pelo argumento. Se `value` for `21`, a saída seria `True`.

```Django
{{ value|divisibleby:"3" }}
```

## 7.11. escape

Escapa do HTML de uma string. Especificamente, ele faz essas substituições:

- `<` é convertido para `&lt;`
- `>` é convertido para `&gt;`
- `'` (aspas simples) é convertido para `&#x27;`
- `"` (aspas duplas) é convertido para `&quot;`
- `&` é convertido para `&amp;`


## 7.12. first

Retorna o primeiro item de uma lista. Se value for a lista `['a', 'b', 'c']`, a saída será 'a'.

```Django 
{{ value|first }}
```

## 7.13. floatformat

Quando usado sem um argumento, arredonda um número de ponto flutuante para uma casa decimal - mas apenas se houver uma parte decimal a ser exibida. Por exemplo: Se `value` for `34.23234` a saída será `34.2`, se `34.00000` será `34`, se `34.26000` será `34.3`.

```Django
{{ value|floatformat }}
```

Se usado com um argumento de número inteiro, `floatformat` arredonda um número para essa quantidade de casas decimais. Por exemplo: Se `value` for `34.23234` a saída será `34.232`, se `34.00000` será `34.000`, se `34.26000` será `34.260`.

```Django
{{ value|floatformat:3 }}
```

- Para ver mais possibilidades de formatação, acesse [floatformat](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#floatformat)


## 7.14. join

Junta uma lista com uma string.  Se value for a lista `['a', 'b', 'c']`, a saída será a string `"a // b // c"`.

```Django
{{ value|join:" // " }}
```

## 7.15. last

Retorna o último item de uma lista. Se value for a lista `['a', 'b', 'c', 'd']`, a saída será a string `"d"`.

```Django
{{ value|last }}
```

## 7.16. length

Retorna o comprimento do valor. Isso funciona para strings e listas. Se value for `['a', 'b', 'c', 'd']` ou `"abcd"`, a saída será `4`. O filtro retorna 0para uma variável indefinida.

```Django
{{ value|length }}
```

## 7.17. linebreaks

Substitui quebras de linha em texto simples por HTML apropriado; uma única nova linha torna-se uma quebra de linha HTML (`<br>`) e uma nova linha seguida por uma linha em branco torna-se uma quebra de parágrafo (`<p>`). Se value for `Joel\nis is a slug`, a saída será `<p>Joel<br>is a slug</p>`.

```Django
{{ value|linebreaks }}
```

## 7.18. linebreaksbr

Converte todas as novas linhas em um pedaço de texto simples em quebras de linha HTML (`<br>`). Se value for `Joel\nis a slug`, a saída será: `Joel`<br>`is a slug`.

```Django
{{ value|linebreaksbr }}
```

## 7.19. linenumbers

Exibe texto com números de linha.

```Django
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

## 7.20. force_escape

Aplica escape de HTML a uma string (consulte o filtro escape para obter detalhes). Este filtro é aplicado imediatamente e retorna uma nova string com escape. Isso é útil nos raros casos em que você precisa de vários escapes ou deseja aplicar outros filtros aos resultados de escape. Normalmente, você deseja usar o filtro escape. Por exemplo, se você deseja capturar os elementos `<p>` HTML criados pelo `linebreaksfiltro`:

```Django
{% autoescape off %}
    {{ body|linebreaks|force_escape }}
{% endautoescape %}
```

## 7.21. lower

Converte uma string em letras minúsculas.Se value for `Totally LOVING this Album!`, a saída será `totally loving this album!`

```Django
{{ value|lower }}
```

## 7.22. make_list

Retorna o valor transformado em uma lista. Para uma string, é uma lista de caracteres. Para um inteiro, o argumento é convertido em uma string antes de criar uma lista. Se value for a string `"Joel"`, a saída seria a lista `['J', 'o', 'e', 'l']` . Se value for `123`, a saída será a lista `['1', '2', '3']`.

```Django 
{{ value|make_list }}
```

## 7.23. pluralize

Retorna um plural sufixo se o valor não é 1, '1' ou um objeto de comprimento 1. Por padrão, este sufixo é 's'. 
Se `num_messages` for `1`, a saída será `You have 1 message`. Se `num_messages` for `2` a saída será `You have 2 messages`.

```Django
You have {{ num_messages }} message{{ num_messages|pluralize }}.
```

Podemos alterar o sufixo caso necessário 

```Django
You have {{ num_walruses }} walrus{{ num_walruses|pluralize:"es" }}.
```

Para palavras que não são pluralizadas por sufixo simples, você pode especificar um sufixo no singular e no plural, separados por vírgula

```Django 
You have {{ num_cherries }} cherr{{ num_cherries|pluralize:"y,ies" }}.
```

## 7.24. random

Retorna um item aleatório da lista fornecida. Se value for a lista `['a', 'b', 'c', 'd']`, a saída pode ser `"b"`.

```Django
{{ value|random }}
```

## 7.25. safe

Marca uma string como não exigindo mais escape de HTML antes da saída. Quando o escape automático está desativado, este filtro não tem efeito. Se você estiver encadeando filtros, um filtro aplicado depois safe pode tornar o conteúdo inseguro novamente. Por exemplo, o código a seguir imprime a variável como está, sem escape:

```Django
{{ var|safe|escape }}
```

## 7.26. slice

Retorna uma parte da lista.  Se some_list for `['a', 'b', 'c']`, a saída será `['a', 'b']`.

```Django 
{{ some_list|slice:":2" }}
```

## 7.27. slugify

Converte para ASCII. Converte espaços em hifens. Remove caracteres que não são alfanuméricos, sublinhados ou hifens. Converte em minúsculas. Também remove os espaços em branco à esquerda e à direita. Se value for `Joel is a slug`, a saída será `joel-is-a-slug`.

```Django 
{{ value|slugify }}
```

## 7.28. striptags

Faz todos os esforços possíveis para remover todas as tags HTML. Se value for `<b>Joel</b> <button>is</button> a <span>slug</span>`, a saída será `Joel is a slug`.

```Django
{{ value|striptags }}
```

## 7.29. time
Formata uma hora de acordo com o formato fornecido. O formato fornecido pode ser o predefinido TIME_FORMAT ou um formato personalizado, igual ao filtro date. Observe que o formato predefinido depende da localidade. Se value for equivalente a `datetime.datetime.now()`, a saída será a string "01:23".

```Django
{{ value|time:"H:i" }}
```

[time](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#time)

## 7.30. timesince

Formata uma data como a hora desde essa data (por exemplo, “4 dias, 6 horas”). Recebe um argumento opcional que é uma variável contendo a data a ser usada como ponto de comparação (sem o argumento, o ponto de comparação é agora ). Por exemplo, se `blog_date` for uma instância de data representando meia-noite em `1 de junho de 2006` e `comment_date` for uma instância de data para `08:00 em 1 de junho de 2006`, o seguinte retornaria `8 horas`:

```Django 
{{ blog_date|timesince:comment_date }}
```

## 7.31. title

Converte uma string em caixa de título, fazendo com que as palavras comecem com um caractere maiúsculo e os caracteres restantes com minúsculas. Esta tag não faz nenhum esforço para manter “palavras triviais” em minúsculas. Se value for "my FIRST post", a saída será "My First Post".

```Django
{{ value|title }}
```

## 7.32. truncatewords

Trunca uma string após um certo número de palavras. Se `value` for `Joel is a slug`, a saída será `Joel is …`.

```Django 
{{ value|truncatewords:2 }}
```

## 7.33. upper

Converte uma string em maiúsculas. Se value for "Joel is a slug", a saída será "JOEL IS A SLUG".

```Django 
{{ value|upper }}
```


## 7.34. wordcount

Retorna o número de palavras. Se value for `"Joel is a slug"`, a saída será `4`.

```Django 
{{ value|wordcount }}
```

## 7.35. wordwrap

Encapsula palavras no comprimento de linha especificado.

```Django
{{ value|wordwrap:5 }}
```

Se value for Joel is a slug, a saída seria:

```
Joel
is a
slug
```

## 7.36. yesno

Mapas valores para `True`, `False` (opcionalmente) `None`, para as cadeias de “sim”, “não”, “talvez”, ou um mapeamento personalizado passada como uma lista separada por vírgulas, e retorna uma dessas cadeias de acordo com o valor: Se valor for `True`, a saída será `yeah`; se for `Flase`, será `no`; se for `None`, será `maybe`... Por padrão se não por passado parâmetro, será apenas `yes` e `no`.


```python
{{ value|yesno:"yeah,no,maybe" }}
```

****************************

- Também é possível criar tags e filtros personalizados. Para isto acesse: [Writing custom template tags](https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/#howto-writing-custom-template-tags)