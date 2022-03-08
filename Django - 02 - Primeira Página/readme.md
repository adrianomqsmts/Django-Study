# Projeto Django

Em resumo, um projeto Django é um todo, que irá conter uma ou mais aplicações 

- `__init__.py` - é um arquivo em branco que instrui o Python a tratar esse diretório como um pacote Python.
- `settings.py` - Contém todas as definições do website. É onde nós registramos qualquer aplicação que criarmos, a localização de nossos arquivos estáticos, configurações de banco de dados etc. 
- `urls.py` - define os mapeamentos de URL para visualização do site. Mesmo que esse arquivo possa conter todo o código para mapeamento de URL, é mais comum delegar apenas o mapeamento para aplicativos específicos, como será visto mais adiante.
- `wsgi.py` é usado para ajudar na comunicação entre seu aplicativo Django e o web server. Você pode tratar isso como um boilerplate.
- `manage.py` - O arquivo manage.py dentro do projeto Django é responsável por permitir a execução de comandos Django dentro de um terminal como `migrations`, `makemigrations` ou `createsuperuser`

# Aplicação Django

1. Após a criação de uma nova aplicação devemos ir no PROJETO DJANGO e informar em dentro da opção de `INSTALLED_APPS` o nome da aplicação.
1. Alternativamente, podemos colocar o caminho `<aplicação>.apps.<appConfig>`
  
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core', # nova aplicação -> core.apps.CoreConfig
]
```

## Estrutura de Arquivos das Aplicações

Abaixo temos a estrutura inicial de uma aplicação Django:

- **migrations** - O pacote *migrations* é o responsável por mentar todo um histórico de versões do banco de dados.
- `admin.py` - O arquivo `admin.py` é usado para que possamos mostrar nossos dados dentro da ferramenta admin do Django, além de podermos trabalhar com todo um CRUD através da ferramenta.
- `apps.py` - O arquivo `apps.py` é responsável por definir o nome da aplicação.
- `models.py` - O arquivo `models.py` é usado para criar os modelos de dados, tendo a função de persistir os dados dentro de um banco de dados.
- `tests.py` - O arquivo `tests.py` é usado para criar funções e métodos para testar todas a aplicação Django.
- `views.py` - O arquivo `view.py` é o principal arquivo da aplicação, onde contém classes e/ou métodos que são chamados dentro do arquivo `urls.py`. Estas classes e/ou métodos irão contextualizar a requisição, podendo tratar formulários, validação de usuários ou simplesmente carregar um template para a visualização.

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

# Criar Rotas

Dado um projeto e uma aplicação, precisamos incluir, no arquivo de rota `urls.py` do **PROJETO**, uma referência para o arquivo de rotas `urls.py` que será criado dentro da nossa aplicação.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

Em seguida precisamos inserir a rota dentro do arquivo `urls.py` da **APLICAÇÃO**. Entretanto existem duas formas de fazer isso, a primeira é usando views baseadas em funções, onde precisamos apenas especificar o caminho, o nome da função dentro do arquivo `views.py` e dar um nome (apelido) para a rota.

```python
from django.urls import path
from .views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
]
```

A segunda forma é usando views baseadas em classes, que consiste na mesma ideia, mas ao invés de usar funções, iremos usar classes.

```python
from django.urls import path
from .views import IndexView	

urlpatterns = [
      path('', IndexView.as_view(), name='index'),
]
```

A fonte completa de como criar URLS pode ser acessada em [django urls path](https://docs.djangoproject.com/en/dev/ref/urls/#django.urls.path)


# Criar View

Podemos criar uma função ou classe simples, apenas para verificarmos se as rotas estão funcionado. Para isso vamos editar o arquivo `views.py` da aplicação da seguinte forma.

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá mundo!")
```

- Quem é HttpResponse? - Basicamente é um método que retorna uma resposta a uma requisição HTTP. Iremos então da maneira mais simples testar a rota que é enviar uma resposta para a requisição.

Outra forma, é redirecionar para o arquivo `index.html` que criamos dentro do diretório `templates` dentro da aplicação.

```python
from django.shortcuts import render

def index(request):
  context = {}
  return render(request, 'index.html', context)
```

A função `render` é responsável por tratar de ligar a requisição (dados enviados do browser) com o template. Ou seja, ele pega os dados da requisição (request), e envia para o template nomeado `index.html`, além de um dicionário dados de contexto (context). Os dados de contexto (context) seria uma variável para enviar dados da própria função para o arquivo `index.html`, que no momento não temos.

Por fim, podemos usar as classes, que irá herdar diversas funcionalidades e padrões prontos do Django.

```python
from django.views.generic import TemplateView

class IndexView(TemplateView):
  template_name = 'index.html'
```
