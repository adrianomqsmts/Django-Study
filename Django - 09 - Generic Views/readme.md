
# 11. Criando Rotas

Como criar urls dinâmicas e com expressões regulares acesse [URL dispatcher]([https://link](https://docs.djangoproject.com/en/dev/topics/http/urls/))

- Para capturar valores de um URL devemos usar colchetes angulares (`<>`) .
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
- Uma solicitação para a url  `/articles/2003/03/building-a-django-site/` corresponderia ao padrão final. Django chamaria a função `views.article_detail(request, year=2003, month=3, slug="building-a-django-site")`.

## 11.1. Conversores de Caminhos

Os seguintes conversores de caminho estão disponíveis por padrão:

- `str` - Corresponde a qualquer string não vazia, excluindo o separador de caminho `'/'`. Este é o padrão se um conversor não estiver incluído na expressão.
- `int` - Corresponde a zero ou qualquer inteiro positivo. Retorna um `int`.
- `slug` - Corresponde a qualquer `string slug` consistindo em letras ou números ASCII, mais o hífen e os caracteres de sublinhado. Por exemplo `building-your-1st-django-site`.
- `uuid` - Corresponde a um UUID formatado. Para evitar que vários URLs sejam mapeados para a mesma página, devem ser incluídos travessões e as letras devem ser minúsculas. Por exemplo `075194d3-6885-417e-a8a8-6c931e272f00`. Retorna uma UUIDinstância.
- `path` - Corresponde a qualquer string não vazia, incluindo o separador de caminho '`/`'. Isso permite que você compare com um caminho de URL completo em vez de um segmento de um caminho de URL como com str.

[Registrando conversores de caminho personalizado](https://docs.djangoproject.com/en/3.1/topics/http/urls/#registering-custom-path-converters)

### 11.1.1. Usando Expressões regulares
Se a sintaxe de caminhos e conversores não for suficiente para definir seus padrões de URL, você também pode usar expressões regulares. Para fazer isso, use `re_path()` em vez de `path()`.

Em expressões regulares Python, a sintaxe para grupos nomeados de expressão regular é (`? P <nome> padrão`), onde nome é o nome do grupo e padrão é algum padrão a ser correspondido.

- `^` - Início do url
- `$` - Fim do url
- `\` - Escape para valores interpretados
- `|` - Ou
- `+` - 1 ou mais ocorrências
- `?` - 0 ou 1 ocorrência
- `{n}` - n ocorrências
- `{n,m}` - Entre n e m ocorrências
- `[] `(Agrupamento de caracteres
- `(?P ___)` - Capture a ocorrência que corresponde a regexp `___` e atribua-a ao nom
- `.` - Qualquer caractere
- `\d+` - Um ou mais dígitos. Observe o escape, sem correspondências de escape `d+` literalmente
- `\D+` - Um ou mais não dígitos. Note escape, sem correspondências de escape `D+` literalmente
- `[a-zA-Z0-9_]+` - Um ou mais caracteres de palavra, letra minúscula, número ou sublinhado
- `\w+` - Um ou mais caracteres de palavra, equivalente a `[a-zA-Z0-9_]`) Nota de escape, sem correspondências de escape `w+` literalmente
- `[-@\w]+` - Um ou mais caracteres de palavra, traço ou arroba. Não observe nenhum escape, `\w` pois está entre colchetes (ou seja, um agrupamento).

| Expressão regular de url           | Descrição                                                                            | URLs de exemplo                                                            |
| ---------------------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| re_path(r'^$',.....)               | String vazia (página inicial)                                                        | http://127.0.0.1/                                                          |
| re_path(r'^stores/',.....)         | Quaisquer caracteres finais                                                          | http://127.0.0.1/stores/ ou http://127.0.0.1/stores/long+string+with+12345 |
| re_path(r'^about/contact/$',.....) | Exato, sem caracteres finais                                                         | http://127.0.0.1/about/contact/                                            |
| re_path(r'^stores/\d+/',....       | Número                                                                               | http://127.0.0.1/stores/2/                                                 |
| re_path(r'^drinks/\D+/',.....)     | Sem dígitos                                                                          | http://127.0.0.1/drinks/mocha/                                             |
| re_path(r'^drinks/mocha            | espresso/',.....)                                                                    | Opções de palavra, quaisquer caracteres finais                             | http://127.0.0.1/drinks/mocha/ ou http://127.0.0.1/drinks/mochaccino/ ou http://127.0.0.1/drinks/espresso/ |
| re_path(r'^drinks/mocha$           | espresso/$',.....)                                                                   | Opções de palavras exatas, sem caracteres finais                           | http://127.0.0.1/drinks/mocha/ ou http://127.0.0.1/drinks/espresso/                                        |
| re_path(r'^stores/\w+/',.....)     | Caracteres de palavras (qualquer letra minúscula ou maiúscula, número ou sublinhado) | http://127.0.0.1/stores/sandiego/ ou http://127.0.0.1/stores/1/            |
| re_path(r'^stores/[-\w]+/',.....)  | Caracteres de palavra ou traço                                                       | http://127.0.0.1/san-diego/                                                |
| re_path(r'^state/[A-Z]{2}/',.....) | Duas letras maiúsculas                                                               | http://127.0.0.1/CA/                                                       |


Aqui está o URLconf de exemplo anterior, reescrito usando expressões regulares

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


***********************

# 12. Generic Views - Visões Genéricas

As views genéricas surgem para simplificar o trabalho repetitivo de criação das views, ou seja, elas contém diversos métodos prontos que nem precisamos naos preocupar em ter que escreve-los como validação de formulários. 

## 12.1. Base Views

As três classes a seguir fornecem muitas das funcionalidades necessárias para criar visualizações do Django. Você pode pensar nelas como visualizações pai, que podem ser usadas por si mesmas ou herdadas. Eles podem não fornecer todos os recursos necessários para projetos; nesse caso, há Mixins e visualizações baseadas em classes genéricas.

### 12.1.1. View 

A visão de base baseada na classe mestre. Todas as outras visualizações baseadas em classe herdam desta classe base. Não é estritamente uma visualização genérica e, portanto, também pode ser importada django.views.

A lista de nomes de métodos HTTP que esta visualização aceitará por padrão são: `['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']`

Exemplo:
```python
from django.http import HttpResponse
from django.views import View

class MyView(View):
    # Responde apenas requisições GET
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')
```

```python
from django.urls import path
from myapp.views import MyView

urlpatterns = [
    path('mine/', MyView.as_view(), name='my-view'),
]
```

### 12.1.2. TemplateView

Quando você precisa apenas renderizar uma página para o usuário essa com certeza é a melhor Class Based View (CBV) para o caso. Você pode editar o contexto que o template recebe sobrescrevendo a função `get_context_data()`. Importante ressaltar que o TemplateView conta com o Mixin `ContextMixin` que irá pegar automaticamente os argumentos da URL que serviu a View.

Exemplo

```python
from django.views.generic.base import TemplateView
from articles.models import Article

class HomePageView(TemplateView):

    template_name = "article.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context
```

``` python
from django.urls import path
from myapp.views import HomePageView

urlpatterns = [
    path('article/<int:value>', HomePageView.as_view(), name='article'),
]
```

- No exemplo acima, a variável `context` contém os `latest_articles` e o `value` armazenados. 
- Podemos ainda adicionar `extra_context` durante a url
  
```python
from django.views.generic import TemplateView
TemplateView.as_view(extra_context={'title': 'Custom Title'})
```

### 12.1.3. Redirect View

Redireciona para um determinado URL.

O URL fornecido pode conter formatação de string no estilo dicionário-de-strings. Os parâmetros capturados na URL do RedirectView serão repassados para a URL que o usuário está sendo redirecionado.

Atributos
- `url` - O URL para o qual será redirecionado, como uma string um valor vazio para gerar um erro HTTP 410 (desaparecido).
- `pattern_name` - O nome do padrão de URL para o qual redirecionar. A reversão será feita usando os mesmos argumentos e kwargs que são passados ​​para esta visão.
- `permanent` - Se o redirecionamento deve ser permanente. A única diferença aqui é o código de status HTTP retornado. Se `True`, então o redirecionamento usará o código de status 301. Se `False`, então o redirecionamento usará o código de status 302. Por padrão, permanent é `False`.
- `query_string` - Se deve passar a string de consulta GET para o novo local. Se `True`, então a string de consulta é anexada ao URL. Se `False`, então a string de consulta é descartada. Por padrão, `query_string` é `False`.
Métodos
- `get_redirect_url(*args , **kwargs)` -  Constrói o URL de destino para redirecionamento. Os argumentos args e kwargs são argumentos posicionais e/ou de palavra-chave capturados do padrão de URL, respectivamente.

Exemplo: 

```python
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from articles.models import Article

class ArticleCounterRedirectView(RedirectView):

    permanent = False
    query_string = True
    pattern_name = 'article-detail'

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        article.update_counter()
        return super().get_redirect_url(*args, **kwargs)
```

```python
from django.urls import path
from django.views.generic.base import RedirectView
from article.views import ArticleCounterRedirectView, ArticleDetail

urlpatterns = [
    path('counter/<int:pk>/', ArticleCounterRedirectView.as_view(), name='article-counter'),
    path('details/<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
    path('go-to-django/', RedirectView.as_view(url='https://djangoproject.com'), name='go-to-django'),
]
```

## 12.2. Display Views

As duas views abaixo foram desenvolvidas para exibir informações. Tipicamente essas views são as mais usadas na maioria dos projetos.

### 12.2.1. DetailView

Esta CBV é usada para renderizar um template contendo em seu contexto um objeto obtido pelo parâmetro enviado na URL. Contextualizando seria passado algo como um produto e o seu id para ser detalhado dentro do template.

É importante notar o fluxo de execução das views genéricas. O fluxo básico de execução dessa classe quando recebe uma requisição é. (LEMBRANDO que todas as funções já estão implementadas, mas caso seja necessário sobrescrever alguma, devemos entender o seu contexto):

1. `dispatch()`
   - verifica se a classe tem um método com o nome do verbo HTTP usado na requisição. Caso não haja, um http.HttpResponseNotAllowed é retornado
2. `http_method_not_allowed()`
3. `get_template_names()`
   - retorna uma lista de templates que devem ser usados para renderizar a resposta. Caso o primeiro template da lista não seja encontrado o Django tenta o segundo e assim por diante.. 
4. `get_slug_field()`
   - Esta função deve retornar o nome do campo que será usado para fazer a busca pelo objeto. Por default o Django procura pelo campo slug.
5. `get_queryset()`
  - retornar um queryset que será usado para buscar um objeto. `get_queryset()` é chamado pela implementação default do método `get_object()`, se o `get_object()` for sobrescrito a chamada ao `get_queryset()` pode não ser realizada.
6. `get_object()`
   - É o responsável por retornar o objeto que será enviado para o template. Normalmente essa função não precisa ser sobrescrita.
7. `get_context_object_name()`
  - Depois de obter o objeto que será enviado para o template é necessário saber qual será o nome desse objeto no contexto do template, isso é feito pela função `get_context_object_name()`, por default o nome do objeto no template será o nome do Model.
8. `get_context_data()`
    - Função que captura o contexto para os templates
9.  `get()`
    - Obtém o objeto e coloca no contexto,
10. `render_to_response()`
    -  Renderiza o template.

Exemplo

Views.py
```python 
from django.views.generic.detail import DetailView
from django.utils import timezone
from articles.models import Article

class ArticleDetailView(DetailView):
    slug_field = 'titulo'
    model = Article
    context_object_name = 'meu_artigo'
    template_name = 'detalhe_artigo.html'

    get_queryset(self):
        return self.model.filter(user=self.request.user)
```

Urls.py

```python
from django.conf.urls import url
from article.views import ArticleDetailView

urlpatterns = [
    url(r'^(?P<titulo>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
]
```

detalhe_artigo.html

```Django
<h1>{{ meu_artigo.titulo }}</h1>
<p>{{ meu_artigo.conteudo }}</p>
<p>Reporter: {{ meu_artigo.user.name }}</p>
<p>Published: {{ meu_artigo.data_publicacao|date }}</p>
```


Outro exemplo na mesma lógica

```python
from django.utils import timezone
from django.views.generic.detail import DetailView
from articles.models import Article

class ArticleDetailView(DetailView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
```

```python
from django.urls import path
from article.views import ArticleDetailView

urlpatterns = [
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
]
```

```Django
<h1>{{ object.headline }}</h1>
<p>{{ object.content }}</p>
<p>Reporter: {{ object.reporter }}</p>
<p>Published: {{ object.pub_date|date }}</p>
<p>Date: {{ now|date }}</p>
```

### 12.2.2. ListView

Uma página que representa uma lista de objetos. Enquanto essa view está executando a variável `self.object_list` vai conter a lista de objetos que a view está utilizando. Também possui o mesmo fluxo que as demais views.

views.py

```python
from django.views.generic.list import ListView
from django.utils import timezone
from articles.models import Artigo

class ArticleListView(ListView):

    model = Artigo
    queryset = Artigo.objects.filter(status='publicado')
    template_name = 'artigo_list.html'

    # OU ENTÃO
    #def get_queryset(self, **kwargs):
    #    return Artigo.objects.filter(status='publicado')  
```

artigo_list.html

```Django
<h1>Articles</h1>
<ul>
{% for article in object_list %}
    <li>{{ article.pub_date|date }} - {{ article.headline }}</li>
{% empty %}
    <li>No articles yet.</li>
{% endfor %}
</ul>  
```

Outro exemplo 

```python
from django.utils import timezone
from django.views.generic.list import ListView
from articles.models import Article

class ArticleListView(ListView):

    model = Article
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
```

```python
from django.urls import path
from article.views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
]
```

```Django
<h1>Articles</h1>
<ul>
{% for article in object_list %}
    <li>{{ article.pub_date|date }} - {{ article.headline }}</li>
{% empty %}
    <li>No articles yet.</li>
{% endfor %}
</ul>
```

## 12.3. Editing Views

As views descritas abaixo contém o comportamento básico para edição de conteúdo. 

### 12.3.1. FormView

Uma view que mostra um formulário. Se houver erro, mostra o formulário novamente contendo os erros de validação. Em caso de sucesso redireciona o usuário para uma nova URL.

- `form_valid()`: Chamada quando o formulário é validado com sucesso
- `form_invalid()`: Chamada quando o formulário contém erros
- `get_sucess_url()`: Chamada quando o formulário é validado com sucesso e retorna a url para qual o usuário deve ser redirecionado

forms.py

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
```

views.py
```python
from myapp.forms import ContactForm
from django.views.generic.edit import FormView

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)
```

contact.html

```Django
<form action="" method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Send message" />
</form>
```

### 12.3.2. CreateView
Uma visão que exibe um formulário para a criação de um objeto, exibindo novamente o formulário com erros de validação (se houver) e salvando o objeto. Trabalham bem com MODELOS!

- O atributo fields determina quais campos do model devem estar presentes no formulário. É obrigatório especificar o atributo fields ou então o atributo form_class, nunca os dois ao mesmo tempo, pois isso geraria uma exceção `ImproperlyConfigured`.

urls.py

```python
from django.urls import path
from .views import AddPostCreateView

urlpatterns = [
    path('add_post/', AddPostCreateView.as_view(), name='add_post'),
]
```

Models.py

```python
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='title')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    header_image = models.ImageField(
        null=True, blank=True, upload_to="images/")
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="coding")
    likes = models.ManyToManyField(User, related_name='blogpost')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})
```

views.py Se formos usar um formulário personalizado, devemos omitir quais campos serão usados na criação em fields.

```python
class AddPostCreateView(CreateView):
    model = Post
    #form_class = PostForm
    template_name = "add_post.html"
    fields = '__all__'
```

add_post.html

```Django
{% extends 'base.html' %}
{% block title %}ADD Post{% endblock title %}
{% block content %}
<h1>Add Post</h1>
<br />
<hr />
<br />
<div class="form-group">
  <form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.media }}
    {{ form.as_p }}
    <button type="submit" class="btn btn-secondary">Post</button>
  </form>
</div>
<script>
  var name = "{{ user.id }}";
  document.getElementById("elder").value =  name;
</script>
{% endblock content %}
```

Outro exemplo

```python
from django.views.generic.edit import CreateView
from myapp.models import Author

class AuthorCreate(CreateView):
    model = Author
    fields = ['name']
```

```Django
<form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save">
</form>
```


### 12.3.3. UpdateView

Uma visão que exibe um formulário para editar um objeto existente, exibindo novamente o formulário com erros de validação (se houver) e salvando as alterações no objeto. Isso usa um formulário gerado automaticamente a partir da classe de modelo do objeto (a menos que uma classe de formulário seja especificada manualmente).

- `template_name_suffix` 
    - A UpdateView exibida para uma solicitação GET usa um `template_name_suffixde ` '`_form`'. Por exemplo, alterar este atributo para '`_update_form`' atualizando os objetos para modelo do Author faria com que o padrão do `template_name` fosse '`myapp/author_update_form.html`'.
- `object`
  - Ao usar UpdateView você tem acesso ao `self.object`, que é o objeto que está sendo atualizado.


```python
from django.views.generic.edit import UpdateView
from myapp.models import Author

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']
    template_name_suffix = '_update_form'
```

```Django 
<form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Update">
</form>
```

### 12.3.4. DeleteView

Uma visualização que exibe uma página de confirmação e exclui um objeto existente. O objeto fornecido só será excluído se o método de solicitação for POST. Se essa visualização for obtida por meio de GET, ela exibirá uma página de confirmação que deve conter um formulário que efetua um POST no mesmo URL.

```python
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from myapp.models import Author

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')
```

```Django
<form method="post">{% csrf_token %}
    <p>Are you sure you want to delete "{{ object }}"?</p>
    <input type="submit" value="Confirm">
</form>
```


Um exemplo mais completo

```python
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from myapp.models import Author

class AuthorCreate(CreateView):
    model = Author
    fields = ['name']

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')
```

urls.py

```python
from django.conf.urls import url
from myapp.views import AuthorCreate, AuthorUpdate, AuthorDelete

urlpatterns = [
    # ...
    url(r'author/add/$', AuthorCreate.as_view(), name='author_add'),
    url(r'author/(?P<pk>[0-9]+)/$', AuthorUpdate.as_view(), name='author_update'),
    url(r'author/(?P<pk>[0-9]+)/delete/$', AuthorDelete.as_view(), name='author_delete'),
]
```

## 12.4. Date Views

Date-based generic views são views com a função de exibir páginas com dados filtrados por datas, por exemplo: posts em um blog, notícias, consultas ao médico, etc.

### 12.4.1. ArchiveIndexView

Uma página de índice de nível superior mostrando os objetos “mais recentes”, por data. Objetos com uma data futura não são incluídos, a menos que você defina `allow_future` como `True`.

- O nome default do `context_object_name` é `latest`.
- O sufixo `_archive` no nome do template.
- Além da lista de objetos o contexto também contem a variável `date_list` contendo todos os anos que tem objetos em ordem decrescente. Isso pode ser alterado para mês ou dia usando o atributo `date_list_period`. Isso se aplica a todas as Data-based generic views.
- `date_list`: Um objeto QuerySet que contém todos os anos que possuem objetos disponíveis de acordo com queryset, representados como datetime.datetime, em ordem decrescente.

urls.py

```python
from django.urls import path
from django.views.generic.dates import ArchiveIndexView
from myapp.models import Article

urlpatterns = [
    path('archive/',
         ArchiveIndexView.as_view(model=Article, date_field="pub_date"),
         name="article_archive"),
]
```

```Django
<ul>
    {% for article in latest %}
        <li>{{ article.pub_date }}: {{ article.title }}</li>
    {% endfor %}
</ul>
```

### 12.4.2. YearArchiveView

Uma página de arquivo anual mostrando todos os meses disponíveis em um determinado ano. Objetos com uma data futura não são exibidos, a menos que você defina `allow_future` como `True`.

- `make_object_list`
  - Um booleano que especifica se é necessário recuperar a lista completa de objetos deste ano e passá-los para o modelo. Se `True`, a lista de objetos será disponibilizada para o contexto. Se `False`, o Nonequeryset será usado como a lista de objetos. Por padrão, é `False`
- `get_make_object_list()` 
  - Determine se uma lista de objetos será retornada como parte do contexto. Retorna `make_object_list` por padrão.
- `date_list`
  - Um QuerySet que contém todos os meses que têm objetos disponíveis de acordo com queryset, representados como datetime.datetime, em ordem crescente.
- `year`
  - Um date que representa o ano determinado.
- `next_year`
  - Um date que representa o primeiro dia do próximo ano, de acordo com `allow_emptye` `allow_future`.
- `previous_year`
  - Um date que representa o primeiro dia do ano anterior, de acordo com `allow_emptye` `allow_future`.
- Usa um padrão `template_name_suffix` de `_archive_year`

```python
from django.views.generic.dates import YearArchiveView
from myapp.models import Article

class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True
```

```python
from django.urls import path
from myapp.views import ArticleYearArchiveView

urlpatterns = [
    path('<int:year>/',
         ArticleYearArchiveView.as_view(),
         name="article_year_archive"),
]
```

```Django
<ul>
    {% for date in date_list %}
        <li>{{ date|date }}</li>
    {% endfor %}
</ul>

<div>
    <h1>All Articles for {{ year|date:"Y" }}</h1>
    {% for obj in object_list %}
        <p>
            {{ obj.title }} - {{ obj.pub_date|date:"F j, Y" }}
        </p>
    {% endfor %}
</div>
```

### 12.4.3. Outras DateViews

Existem também outras que seguem a mesma lógica de implementação com os mesmos atributos e métodos como:
- [MonthArchiveView](https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-date-based/#montharchiveview)
  - Uma página de arquivo mensal mostrando todos os objetos em um determinado mês.
- [WeekArchiveView](https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-date-based/#weekarchiveview)
  - Uma página de arquivo semanal mostrando todos os objetos em um determinado mês.
- [DayArchiveView](https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-date-based/#dayarchiveview)
  - Uma página de arquivo do dia mostrando todos os objetos em um determinado dia.
- [TodayArchiveView](https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-date-based/#todayarchiveview)
  - Uma página de arquivo do dia mostrando todos os objetos de hoje . É exatamente igual a django.views.generic.dates.DayArchiveView, exceto que a data de hoje é usada em vez dos argumentos year/ month/ day.
- [DateDetailView](https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-date-based/#datedetailview)
  - Uma página que representa um objeto individual. Se o objeto tiver um valor de data no futuro, a visualização lançará um erro 404 por padrão, a menos que você defina allow_futurecomo True.

Fontes : [class-based-views-django](http://pythonclub.com.br/class-based-views-django.html)
*******************************************









