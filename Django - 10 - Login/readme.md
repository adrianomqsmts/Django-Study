# Login System

Django já tem todo um sistema pronto de autenticação que pode ser reaproveitado. Toda a implementação está dentro do módulo [`django.contrib.auth.forms`](https://docs.djangoproject.com/en/dev/ref/contrib/auth/).

Fontes:
- [Autenticação de Usuário no Django](https://django-portuguese.readthedocs.io/en/1.0/topics/auth.html#)
- [Usando o sistema de autenticação Django](https://docs.djangoproject.com/pt-br/4.0/topics/auth/default/)
- [Implementando autenticação no Django - Parte 1 ](https://www.treinaweb.com.br/blog/implementando-autenticacao-no-django-parte-1)
- [how use UpdateView change user password in the django](https://stackoverflow.com/questions/55061329/how-use-updateview-change-user-password-in-the-django)
- [Tutorial Django Parte 8: Autenticação de usuário e permissões](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Authenticationhttps://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Authentication)
- [How to disable next URL parameter while using login_required decorator in django?](https://stackoverflow.com/questions/63566841/how-to-disable-next-url-parameter-while-using-login-required-decorator-in-django)



# Model User

É um modelo de usuário embutido do Django, que possuí os seguintes campos:


- `username`: (Obrigatório). 30 caracteres ou menos.
- `first_name`: (Opcional). 30 caracteres ou menos.
- `last_name`: (Opcional). 30 caracteres ou menos.
- `email`: (Opcional). Endereço de e-mail.
- `password`: (Obrigatório). Um hash da senha, e metadados sobre a senha.
- `is_staff`: (Booleano). Determina se este usuário pode acessar o site admin.
- `is_active`: (Booleano). Determina se esta conta de usuário deve ser considerada ativa. Seta este flag para False ao invés de deletar as contas. **Isto não controla se o usuário pode ou não logar-se.**
- `is_superuser`: (Booleano). Determina que este usuário tem todas as permissões.
- `last_login`: (datetime). O último login do usuário. É setado para a data/hora atual por padrão.
- `date_joined`: (datetime). Quando a conta foi criada. É setada com a data/hora atual por padrão quando a conta é criada.

Os métodos do modelo `user` são:


- `is_authenticated()`: Sempre retorna `True`. Esta é a forma de dizer se o usuário foi autenticado. Isto não implica em quaisquer permissões, e não verifica se o usuário está ativo - ele somente indica que o usuário forneceu um nome e senha válidos.
- `get_full_name()`: Retorna o `first_name` mais o `last_name`, com um espaço entre eles.
- `set_password(raw_password): Seta a senha do usuário a partir de uma dada string.
- `check_password(raw_password): Retorna `True` se a string é a senha correta para o usuário. (Este se encarrega de tirar o hash da senha e fazer a comparação.)
- `get_group_permissions()`: Retorna uma lista de strings de permissão que o usuário tem, através de seus grupos.
- `get_all_permissions()`: Retorna uma lista de strings de permissão que o usuário possui, ambos através de permissões de grupo e usuário.
- `has_perm(perm)`:  Retorna True se o usuário tem uma permissão específica, onde perm é no formato "`<nome da aplicação>.<nome do model em minúsculo>`". Se o usuário é inativo, este método sempre retornará False.
- `has_perms(perm_list): Retorna `True` se o usuário tem cada uma das permissões especificadas, onde cada permissão está no formato "package.codename". Se o usuário estiver inativo, este método sempre retornará `False`.
- `get_and_delete_messages()`: Retorna uma lista de objetos Message da fila do usuário e deleta as mensagens da fila.
- `email_user(subject, message, from_email=None)`: Envia um e-mail para o usuário. Se `from_email` é `None`, o Django usa o `DEFAULT_FROM_EMAIL`.

## Criar novo usuário

O modelo UserManager contém o método `create_user(username, email, password=None)`  que permite criar um novo usuário.

```python
 from django.contrib.auth.models import User

user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

# Neste ponto, user é um objeto User que já foi salvo no banco de dados.
# Você pode continuar a mudar seus atributos se você quiser mudar outros
# campos.
user.is_staff = True
user.save()
```

## Mudando senhas

Para alterar uma senha, basta chamar o método `set_password()`

```python
from django.contrib.auth.models import User

u = User.objects.get(username__exact='john')
u.set_password('new password')

u.save()
```

# Login Required

No arquivo `settings.py` precisamos informar o caminho para o `LOGIN_REDIRECT_URL` que irá especificar o caminho padrão do após o login (padrão: '/accounts/profile/' ) e `LOGIN_URL` que informa a url para o login (padrão: '/accounts/login/'). 

```python
from django.contrib.auth.decorators import login_required

@login_required(login_url='/example url you want redirect/') #redirect when user is not logged in
def myview(request):
    do something
    return something #returns when user is logged in

@login_required() #redirect when user is not logged in
def myview(request):
    do something
    return something #returns when user is logged in
```

Podemos usar o `LoginRequiredMixin` para redirecionar o usuário para a área de login, caso o mesmo esteja não autenticado.


```python
from django.contrib.auth.mixins import LoginRequiredMixin

class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
```

# Sistema de Login I 

Uma forma mais simples de criar um sistema de login, é reaproveitar ao máximo as funcionalidades prontas, e neste exemplo, iremos apenas definir a rota dos templates e os templates.

```python
(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'myapp/login.html'}),
```

Arquivo `urls.py` do projeto. 

```python
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', name='login')
    path('accounts/logout/', name='logout')
    path('accounts/password_change/', name='password_change')
    path('accounts/password_change/done/', name='password_change_done')
    path('accounts/password_reset/', name='password_reset')
    path('accounts/password_reset/done/', name='password_reset_done')
    path('accounts/reset/<uidb64>/<token>/', name='password_reset_confirm')
    path('accounts/reset/done/', name='password_reset_complete')
]
```

Na raiz do projeto, podemos definir na pasta `templates` uma nova pasta denominada `registration` e então colocar templates, de mesmo nome que a rota.

- Exemplo `login.html`:

```django
{% extends "base_generic.html" %}

{% block content %}

  {% if form.errors %}
    <p>Your username and password didn't match. Please try again.</p>
  {% endif %}

  {% if next %}
    {% if user.is_authenticated %}
      <p>Your account doesn't have access to this page. To proceed,
      please login with an account that has access.</p>
    {% else %}
      <p>Please login to see this page.</p>
    {% endif %}
  {% endif %}

  <form method="post" action="{% url 'login' %}">
    {% csrf_token %}
    <table>
      <tr>
        <td>{{ form.username.label_tag }}</td>
        <td>{{ form.username }}</td>
      </tr>
      <tr>
        <td>{{ form.password.label_tag }}</td>
        <td>{{ form.password }}</td>
      </tr>
    </table>
    <input type="submit" value="login" />
    <input type="hidden" name="next" value="{{ next }}" />
  </form>

  {# Assumes you setup the password_reset view in your URLconf #}
  <p><a href="{% url 'password_reset' %}">Lost password?</a></p>

{% endblock %}

```

- Exemplo do arquivo `password_reset_form.html`:

```django
{% extends "base_generic.html" %}

{% block content %}
  <form action="" method="post">
  {% csrf_token %}
  {% if form.email.errors %}
    {{ form.email.errors }}
  {% endif %}
      <p>{{ form.email }}</p>
    <input type="submit" class="btn btn-default btn-lg" value="Reset password">
  </form>
{% endblock %}

```

Para ver o exemplo completo acesse: [Tutorial Django Parte 8: Autenticação de usuário e permissões](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Authentication)


# Sistema de Login - Class/Function Based View

Nesse contexto podemos reaproveitar o modelo `User` e os formulários prontos, que nos permitam criar, atualizar e alterar a senha dos usuários.

Algum dos formulários:
- `AdminPasswordChangeForm`: Um formulário usado na interface de administração para mudar a senha do usuário.
- `AuthenticationForm`: Um formulário para logar um usuário.
- `PasswordChangeForm`: Um formulário para permitir a um usuário mudar sua senha.
- `PasswordResetForm`: Um formulário para resetar uma senha de usuário e enviar um email com a nova senha para ele.
- `SetPasswordForm`: Um formulário que deixa um usuário mudar sua senha sem introduzir a senha antiga.
- `UserChangeForm`: Um formulário usado no admin para mudar informações de um usuário e suas permissões.
- `UserCreationForm`: Um formulário para criar um novo usuário.

## Create User

Podemos usar o formulário de criação de usuário `UserCreationForm` e o modelo `User`, em conjunto com o a view `CreateView` para criar um usuário no banco de dados.

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'create.html'
    success_url = reverse_lazy('login')
```

Alternativamente, podemos criar um novo usuário usando uma view baseada em função.

```python
def cadastrar_usuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})
```

## Login

Para realizar o login, precisamos do auxílio de duas funções: `authenticate`  e `login` que permitem autenticar o usuário no sistema e logá-lo, respectivamente.

```python
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

class LoginFormView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        username = form["username"].data
        password = form["password"].data
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super(LoginFormView, self).form_valid(form)
        else:
            return self.form_invalid(form)
```

Alternativamente podemos user uma função, ao invés das classes.

```python
def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})
```

## Logout

Para realizar o logout de um usuário, basta chamar a função `logout(user)` para deslogá-lo do sistema. 

```python
class LogoutView(View):
    # Responde apenas requisições GET
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')
```

Alternativamente podemos usar funções:

```python
def deslogar_usuario(request):
    logout(request)
    return redirect('index')
```


## Update

Para atualizar um usuário, podemos usar a view `UpdateView` em conjunto com o modelo `User` definindo quais os campos queremos permitir que o usuário atualize.

```python
class UserUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/users/login' # loginMixin
    redirect_field_name = None # loginMixin
    model = User
    template_name = 'update.html'
    success_url = reverse_lazy('index')
    fields = ['username', 'first_name', 'last_name']
    
    def get_object(self):
        return self.request.user # pega o usuário atual
```

## Alterar Senha

Para alterar senha é um pouco mais complicado usando o formulário, pois precisamos instanciar o formulário atual com o usuário atual, além de atualizar a sessão com a nova senha.

```python
class UserPasswordUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/users/login' # loginMixin
    redirect_field_name = None # loginMixin
    model = User
    template_name = 'password.html'
    success_url = reverse_lazy('index')
    
    def get_form_class(self):
        return PasswordChangeForm
        
    def get_object(self):
        return self.request.user
    
    def get(self, request, **kwargs):
        form = PasswordChangeForm(request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('index')
        else:
            return render(request, self.template_name, {'form': form})

```

Alternativamente podemos usar uma função.

```python
def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'alterar_senha.html', {'form_senha': form_senha})
```

Podemos usar o método `set_password` ao invés de usar os formulários, caso necessário.

## Remover

Podemos usar a view `DeleteView` em conjunto com o modelo `User` para remover um usuário.

```python
class UserDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/users/login' # loginMixin
    redirect_field_name = None # loginMixin
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user
```



#