# 1. Formulários

Um Formulário HTML é um grupo de um ou mais campos/widgets em uma página web, que podem ser utilizados para coletar informações dos usuários para submetê-las a um servidor.

Formulários são também um meio relativamente seguro de compartilhar dados com o servidor, pois nos permitem enviar dados em requisições POST com proteção contra ataques maliciosos **CSRF** (Cross-Site Request Forgery - em inglês, falsificação de solicitação entre sites).

FONTE [Tutorial Django Parte 9: Trabalhando com formulários](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Forms)

- [1. Formulários](#1-formulários)
  - [1.1. Revisão HTML](#11-revisão-html)
- [2. Fluxograma](#2-fluxograma)
- [3. Criando um Formulário](#3-criando-um-formulário)
  - [3.1. Campos de formulários Django](#31-campos-de-formulários-django)
  - [3.2. Os principais parâmetros dos campos](#32-os-principais-parâmetros-dos-campos)
  - [3.3. Widgets](#33-widgets)
    - [3.3.1. Lista de Widgets](#331-lista-de-widgets)
  - [3.4. Alterando o HTML](#34-alterando-o-html)
- [4. Exibindo Formulários nos Templates](#4-exibindo-formulários-nos-templates)
  - [4.1. Formulário HTML](#41-formulário-html)
  - [4.2. Formulário Django-HTML](#42-formulário-django-html)
  - [4.3. Formulário Django-HTML (Menos HTML)](#43-formulário-django-html-menos-html)
  - [4.4. Formulário Django](#44-formulário-django)
  - [4.5. Mensagem de Erro](#45-mensagem-de-erro)
  - [4.6. Textos de Ajuda](#46-textos-de-ajuda)
  - [4.7. Iterar Sobre um Formulário](#47-iterar-sobre-um-formulário)
- [5. FormView](#5-formview)
    - [5.0.1. Enviando os dados](#501-enviando-os-dados)
    - [5.0.2. Exemplos](#502-exemplos)
- [6. Mensagens de Erro e Sucesso](#6-mensagens-de-erro-e-sucesso)
  - [6.1. Exibindo a mensagem no Template](#61-exibindo-a-mensagem-no-template)
  - [6.2. SuccessMessageMixin](#62-successmessagemixin)

## 1.1. Revisão HTML

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
  - O método `POST` deve sempre ser utilizado se os dados forem resultar em uma alteração no banco de dados do servidor, pois é mais resistente a ataques de falsificação de solicitação entre sites.
  - O método `GET` deve ser utilizado somente para formulários que não alteram dados de usuário (um formulário de busca, por exemplo). Ele é recomendado para quando você quiser poder favoritar ou compartilhar a URL.
-  O atributo `method` definem o método HTTP utilizado para enviar os dados e o destino para esses dados no servidor é definido em `action`

FONTE [Tutorial Django Parte 9: Trabalhando com formulários](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Forms)

# 2. Fluxograma

1. Exiba o formulário padrão na primeira vez em que for solicitado pelo usuário 
2. Receba dados de uma solicitação de envio e vincule-os ao formulário. 
3. Limpe e valide os dados.
4. Se algum dado for inválido, exiba novamente o formulário, desta vez com valores preenchidos pelo usuário e mensagens de erro para os campos problemáticos.
5. Se todos os dados forem válidos, execute as ações necessárias
6. Quando todas as ações estiverem concluídas, redirecione o usuário para outra página.

# 3. Criando um Formulário

Primeiro precisamos criar um arquivo chamado `forms.py` que irá armazenar todos os formulários da nossa aplicação. 

- Exemplo de um formulário

```python
from django import forms

class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
```

## 3.1. Campos de formulários Django

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


## 3.2. Os principais parâmetros dos campos

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

## 3.3. Widgets

Além dos campos, temos também os **widgets** que é a forma como o html é apresentado. Cada campo acima tem um widget padrão, mas podemos alterar como o campo é exibido na tela. Para ver a lista completa de widget e seus usos, acesse: [widgts](https://docs.djangoproject.com/en/dev/ref/forms/widgets/).

Exemplo

```python
from django import forms

class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
```

### 3.3.1. Lista de Widgets 

- `TextInput`
  - `input_type: 'text'`
  - Renders as: `<input type="text" ...>`
- NumberInput
  - input_type: 'number'
  - Renders as: <input type="number" ...>
- `EmailInput`
  - input_type: 'email'
  - Renders as: <input type="email" ...>
- `URLInput`
  - input_type: 'url'
  - Renders as: `<input type="url" ...>`
- `PasswordInput`
  - `input_type: 'password'`
  - Renders as: `<input type="password" ...>`
  - Parâmetro: `render_value` - Determina se o widget terá um valor preenchido quando o formulário for reapresentado após um erro de validação (o padrão é False).
- `HiddenInput`
  - `input_type: 'hidden'`
  - Renders as: `<input type="hidden" ...>`
- `DateInput, DateTimeInput, Time`
  - `input_type: 'text'`
  - Renders as: `<input type="text" ...>`
  - parâmetro: `format` - O formato em que o valor inicial deste campo será exibido.
- `Textarea`
  - Renders as: `<textarea>...</textarea>`
- `CheckboxInput`
  -` input_type: 'checkbox'`
  - Renders as: `<input type="checkbox" ...>`
  - Parâmetro: `check_test` - Obtém o valor de CheckboxInput e retorna True se a caixa de seleção deve ser marcada para esse valor.
- `Select`
  - Renders as: `<select><option ...>...</select>`
  - Argumento - `choices` -  Este atributo é opcional quando o campo do formulário não possui um atributo de escolhas. Em caso afirmativo, ele substituirá qualquer coisa que você definir aqui quando o atributo for atualizado no campo.
- `NullBooleanSelect`
  - Selecione o widget com as opções ‘Desconhecido’, ‘Sim’ e ‘Não’
- `SelectMultiple`
Semelhante ao Select, mas permite a seleção múltipla: `<select multiple> ... </select>`
- `RadioSelect`
Semelhante a Selecionar, mas renderizado como uma lista de botões de opção dentro de `<li>` tags:

```html
<ul>
  <li><input type="radio" name="..."></li>
  ...
</ul>

```

Para um controle maior sobre a marcação gerada, você pode repetir os botões de opção no modelo. Assumindo um formulário `myform` com um campo `city` que usa um `RadioSelect` como widget: 

```html
<fieldset>
    <legend>{{ myform.city.label }}</legend>
    {% for radio in myform.city %}
    <div class="myradio">
        {{ radio }}
    </div>
    {% endfor %}
</fieldset>
```

- `FileInput`
  - Renders as: `<input type="file" ...>`

- `ClearableFileInput`
  - Renders as: `<input type="file" ...>` - Com uma entrada de caixa de seleção adicional para limpar o valor do campo, se o campo não for obrigatório e tiver dados iniciais. 

[Lista Completa](https://docs.djangoproject.com/en/dev/ref/forms/widgets/)

## 3.4. Alterando o HTML

Ainda podemos especificar atributos HTML dentro de um `widget.attr`

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

# 4. Exibindo Formulários nos Templates

Existem diversas formas de exibir um formulário, a primeira é trabalhar 100% com HTML, enquanto no outro extremo podemos inserir o formulário usando apenas um comandos Django

## 4.1. Formulário HTML

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

## 4.2. Formulário Django-HTML

- `form.campo.id_for_label` - Contém o ID do campo
- `form.campo.errors` - Irá exibir os `errors` do campo caso haja algum erro ou mensagem de erro atribuída ao erro gerado.
- `form.campo` - Renderiza (exibe) o campo 

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

## 4.3. Formulário Django-HTML (Menos HTML)
- `form.subject.label_tag` - contém todo o elemento `<label>`, com o atributo `for` e `name`.

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

## 4.4. Formulário Django

Podemos gerar um fomulário criado, usando apenas uma linha de código.

- `{{ form.as_table }}` Vai renderizar (exibir) o formulário formatado com TAGS `<tr>`.
- `{{ form.as_p }}` Vai renderizar (exibir) o formulário formatado com TAGS `<p>`.
- `{{ form.as_ul }}` Vai renderizar (exibir) o formulário formatado com TAGS `<li>`.
  
```Django
<form action="" method="post">
  {% csrf_token %}
  <table>
  {{ form.as_table }}
  </table>
  <input type="submit" value="Submit">
</form>
```

## 4.5. Mensagem de Erro

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

## 4.6. Textos de Ajuda

Muitas vexes o texto de ajuda pode ser grande e conter muitos dados, como senhas que podem conter vários critérios. Para isso, podemos usar o código abaixo para exibir o erro de forma formatada.

```Django
  {% if form.campo.help_text %}
  <p class="help">{{ form.campo.help_text|safe }}</p>
  {% endif %}
```

## 4.7. Iterar Sobre um Formulário

Podemos fazer um loop para iterar sobre todos os campos de um formulário. Para saber mais, além de descrição das propriedades dos campos acesse [Looping over the form’s fields](https://stackoverflow.com/questions/19123715/django-for-loop-to-iterate-form-fields)

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

# 5. FormView

- É uma view que mostra um formulário. Caso tenha um erro da validação é exibido o formulário com os erros para se corrido. Caso o formulário passe pela validação é direcionado para uma nova URL.
- Essa view herda métodos e atributos das seguintes `views`:
  - `django.views.generic.base.TemplateResponseMixin`
    - `template_name` - O nome completo de um modelo a ser usado conforme definido por uma string.
  - `django.views.generic.edit.BaseFormView`
  - `django.views.generic.edit.FormMixin`
    - `initial` - Um dicionário contendo os dados iniciais do formulário.
    - `form_class` - A classe de formulário a ser instanciada.
    - `success_url` -  O URL para redirecionar quando o formulário for processado com sucesso.
    - `prefix` - O prefixo do formulário gerado.
    - `get_form_kwargs ()` -  Construa os argumentos de palavra-chave necessários para instanciar o formulário. 
    - `form_valid(form)` - Redireciona para `get_success_url()`.
    - `get_success_url()` determine a URL para redirecionar quando o formulário for validado com sucesso. Retorna o `success_url` por padrão. 
    - `form_invalid(form)` - Renderiza uma resposta, fornecendo o formulário inválido como contexto. 
  - `django.views.generic.edit.ProcessFormView`
  - `django.views.generic.base.View`

### 5.0.1. Enviando os dados

Os métodos `post` e `get` podem enviar os dados dos formulário para outras Views, e possuem a seguinte sintaxe. 

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

### 5.0.2. Exemplos

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

# 6. Mensagens de Erro e Sucesso

Tipos de mensagens
- `DEBUG` - Mensagens relacionadas ao desenvolvimento que serão ignoradas (ou removidas) em uma implantação de produção
- `INFO` - Mensagens informativas para o usuário
- `SUCCESS` - Uma ação foi bem-sucedida, por ex. “Seu perfil foi atualizado com sucesso”
- `WARNING` - Não ocorreu uma falha, mas pode ser iminente
- `ERROR` - Uma ação não teve sucesso ou ocorreu alguma outra falha 

FONTE (The messages framework)[https://docs.djangoproject.com/pt-br/3.2/ref/contrib/messages/]

Para adicionar uma mensagem, use a sintaxe:

```Python
from django.contrib import messages
messages.add_message(request, messages.INFO, 'Hello world.')
```

- Alguns métodos de atalho fornecem uma maneira padrão de adicionar mensagens com tags comumente usadas (que geralmente são representadas como classes HTML para a mensagem):

```Python
messages.debug(request, '%s SQL statements were executed.' % count)
messages.info(request, 'Three credits remain in your account.')
messages.success(request, 'Profile details updated.')
messages.warning(request, 'Your account expires in three days.')
messages.error(request, 'Document deleted.')
```

## 6.1. Exibindo a mensagem no Template

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

## 6.2. SuccessMessageMixin

Adiciona um atributo de mensagem de sucesso às classes baseadas em FormView 

- Os dados limpos do formulário estão disponíveis para interpolação de strings usando a sintaxe `%(field_name)`s.
- Para ModelForms, se você precisar acessar os campos do objeto salvo, substitua o método `get_success_message()`. 

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
  



