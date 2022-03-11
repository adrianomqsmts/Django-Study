# Login System

Django já tem todo um sistema pronto de autenticação que pode ser reaproveitado. Toda a implementação está dentro do módulo [`django.contrib.auth.forms`](https://docs.djangoproject.com/en/dev/ref/contrib/auth/).


# Model User

É um modelo de usuário embutido do Django, que possuí os seguintes campos:


- username: (Obrigatório). 30 caracteres ou menos.
- first_name: (Opcional). 30 caracteres ou menos.
- last_name: (Opcional). 30 caracteres ou menos.
- email: (Opcional). Endereço de e-mail.
- password: (Obrigatório). Um hash da senha, e metadados sobre a senha.
- is_staff: (Booleano). Determina se este usuário pode acessar o site admin.
- is_active: (Booleano). Determina se esta conta de usuário deve ser considerada ativa. Seta este flag para False ao invés de deletar as contas. **Isto não controla se o usuário pode ou não logar-se.**
- is_superuser: (Booleano). Determina que este usuário tem todas as permissões.
- last_login: (datetime). O último login do usuário. É setado para a data/hora atual por padrão.
- date_joined: (datetime). Quando a conta foi criada. É setada com a data/hora atual por padrão quando a conta é criada.

Os métodos do modelo `user` são:


- is_authenticated(): Sempre retorna `True`. Esta é a forma de dizer se o usuário foi autenticado. Isto não implica em quaisquer permissões, e não verifica se o usuário está ativo - ele somente indica que o usuário forneceu um nome e senha válidos.
- get_full_name(): Retorna o `first_name` mais o `last_name`, com um espaço entre eles.
- set_password(raw_password): Seta a senha do usuário a partir de uma dada string.
- check_password(raw_password): Retorna `True` se a string é a senha correta para o usuário. (Este se encarrega de tirar o hash da senha e fazer a comparação.)
- get_group_permissions(): Retorna uma lista de strings de permissão que o usuário tem, através de seus grupos.
- get_all_permissions(): Retorna uma lista de strings de permissão que o usuário possui, ambos através de permissões de grupo e usuário.
- has_perm(perm):  Retorna True se o usuário tem uma permissão específica, onde perm é no formato "<nome da aplicação>.<nome do model em minúsculo>". Se o usuário é inativo, este método sempre retornará False.
- has_perms(perm_list): Retorna True se o usuário tem cada uma das permissões especificadas, onde cada permissão está no formato "package.codename". Se o usuário estiver inativo, este método sempre retornará False.
- get_and_delete_messages(): Retorna uma lista de objetos Message da fila do usuário e deleta as mensagens da fila.
- email_user(subject, message, from_email=None): Envia um e-mail para o usuário. Se from_email é None, o Django usa o DEFAULT_FROM_EMAIL.

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


# Sistema de Login - Function Based View

## Create User

O Django tem um formulário pronto para a criação de usuário, chamado `UserCreationForm`


