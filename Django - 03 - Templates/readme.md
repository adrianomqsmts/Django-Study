# Templates

Um template Django é um documento de texto ou uma string Python marcada usando a linguagem de template Django. Algumas construções são reconhecidas e interpretadas pelo mecanismo de template. Os principais são variáveis ​​e tags. Um modelo é renderizado com um contexto. A renderização substitui variáveis ​​por seus valores, que são pesquisados ​​no contexto, e executa tags. Todo o resto é produzido como está.

#  Variáveis

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

# 9.2. TAGS
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


## 9.2.1. comment

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

## 9.2.2. csrf_token

Essa tag é usada para proteção contra CSRF, conforme descrito na documentação para [Cross Site Request Forgeries]([https://link](https://7xwm2drhn3gdndpwco2driejom--docs-djangoproject-com.translate.goog/en/3.1/ref/csrf/)) .

## 9.2.3. cycle

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


## 9.2.4. debug

Produz uma carga completa de informações de depuração, incluindo o contexto atual e os módulos importados.

## 9.2.5. filter

Filtra o conteúdo do bloco por meio de um ou mais filtros. Vários filtros podem ser especificados com canais e filtros podem ter argumentos, assim como na sintaxe de variável. Observe que o bloco inclui todo o texto entre as tags `filter` e `endfilter`.

```django
{% filter force_escape|lower %}
    This text will be HTML-escaped, and will appear in all lowercase.
{% endfilter %}
```

## 9.2.6. firstof

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

## 9.2.7. for

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

## 9.2.8. for… empty

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

## 9.2.9. if

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

## 9.2.10. Operadores booleanos

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


## 9.2.11. lorem

Exibe texto latino 'lorem ipsum' de forma aleatória. Isso é útil para fornecer dados de amostra em modelos. A sintaxe é `{% lorem [count] [method] [random] %}`, onde:

- count - Um número (ou variável) contendo o número de parágrafos ou palavras a serem gerados (o padrão é 1).
- method - Quer por palavras, para HTML parágrafos ou para blocos de parágrafo de texto simples (o padrão é b).
- random - A palavra random, que se dada, não usa o parágrafo comum (“Lorem ipsum dolor sit amet…”) ao gerar texto.

exemplos 

- {% lorem %} produzirá o parágrafo comum “lorem ipsum”.
- {% lorem 3 p %}irá gerar o parágrafo “lorem ipsum” comum e dois parágrafos aleatórios, cada um envolvido em tags P HTML .
- {% lorem 2 w random %} irá produzir duas palavras latinas aleatórias.

## 9.2.12. now 

Exibe a data e/ou hora atual, usando um formato de acordo com a string fornecida. Essa string pode conter caracteres especificadores de formato, conforme descrito na seção de filtro date.

```django 
It is {% now "jS F Y H:i" %}
```

para ver mais opções acesse [now]([https://link](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#now))


## 9.2.13. regroup

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

## 9.2.14. resetcycle

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

## 9.2.15. spaceless

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

## 9.2.16. url

Retorna uma referência de caminho absoluto (um URL sem o nome de domínio) correspondendo a uma determinada visualização e parâmetros opcionais. Quaisquer caracteres especiais no caminho resultante serão codificados usando `iri_to_uri()`.

```django
{% url 'some-url-name' v1 v2 %}
```
O primeiro argumento é um nome de padrão de URL . Pode ser um literal entre aspas ou qualquer outra variável de contexto. Argumentos adicionais são opcionais e devem ser valores separados por espaço que serão usados ​​como argumentos no URL. 


### 9.2.16.1. url interagindo com o path

```python
path('client/<int:id>/', app_views.client, name='app-views-client')
```

```django
{% url 'app-views-client' client.id %}
```

### 9.2.16.2. url com apelidos

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

## 9.2.17. verbatim

Impede o mecanismo de template de renderizar o conteúdo desta tag de bloco. 

```django
{% verbatim myblock %}
    Avoid template rendering via the {% verbatim %}{% endverbatim %} block.
{% endverbatim myblock %}
```

## 9.2.18. widthratio

Para criar gráficos de barras e outros, esta tag calcula a proporção de um determinado valor a um valor máximo e, em seguida, aplica essa proporção a uma constante. - Referência completa : [widthratio](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#widthratio)

## 9.2.19. width
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

## 9.2.20. load 

Carrega um conjunto de tags de modelo personalizado. Por exemplo, o modelo a seguir carregaria todas as tags e filtros registrados `somelibrary` localizados no pacote package.`otherlibrary`:

```django
{% load somelibrary package.otherlibrary %}
```

Você também pode carregar seletivamente filtros ou tags individuais de uma biblioteca, usando o argumento `foo`. Neste exemplo, as tags/filtros do modelo nomeados `foo` e `bar` serão carregados de somelibrary:

```django 
{% load foo bar from somelibrary %}
```

## 9.2.21. include

Carrega um modelo e o renderiza com o contexto atual. Esta é uma forma de 'incluir' outros modelos em um modelo. O nome do modelo pode ser uma variável ou uma string codificada (entre aspas), entre aspas simples ou duplas. Este exemplo inclui o conteúdo do modelo 'foo/bar.html':

```django
{% include "foo/bar.html" %}
```

Você pode passar contexto adicional para o modelo usando argumentos de palavra-chave:

```django
{% include "name_snippet.html" with person="Jane" greeting="Hello" %}
```

## 9.3. Filtros

Filtros transformam os valores de variáveis ​​e argumentos de tag. Eles se parecem com isto:

``` Django
{{ django|title }}
```

## 9.3.1. add 

Adiciona o argumento ao valor: Se value for 4, a saída será 6.

```django 
{{ value|add:"2" }}
```

## 9.3.2. addslashes

Adiciona barras antes das aspas. Útil para sequências de escape em CSV, por exemplo: Se value for "I'm using Django", a saída será ."I\'m using Django"

```django
{{ value|addslashes }}
```

## 9.3.3. capfirst

Capitaliza o primeiro caractere do valor. Se o primeiro caractere não for uma letra, este filtro não terá efeito: Se value for "django", a saída será "Django".

```django
{{ value|capfirst }}
```

## 9.3.4. center

Centraliza o valor em um campo de uma determinada largura: Se value for "Django", a saída será : `"     Django    "`

```django
"{{ value|center:"15" }}"
```

## 9.3.5. cut
Remove todos os valores de arg da string fornecida. Se value for "String with spaces", a saída será "Stringwithspaces"

```django 
{{ value|cut:" " }}
```

## 9.3.6. date

Formata uma data de acordo com o formato fornecido. Se value for um datetime, a saída será a string .'Wed 09 Jan 2008'. Para ver a lista completa de personalização de datas acesse [Date]([https://link](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date))

```django 
{{ value|date:"D d M Y" }}
```

## 9.3.7. Deafult

Se o valor for avaliado como False, usa o padrão fornecido. Caso contrário, usa o valor. Se value for "" (a string vazia), a saída será nothing.

```python
{{ value|default:"nothing" }}
```

## 9.3.8. default_if_none

Se (e somente se) o valor for `None`, usa o padrão fornecido. Caso contrário, usa o valor. Observe que, se uma string vazia for fornecida, o valor padrão não será usado. Se value for None, a saída será nothing.

```django
{{ value|default_if_none:"nothing" }}
```

## 9.3.9. dictsort

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
  
## 9.3.10. dictsortreversed

Pega uma lista de dicionários e retorna essa lista classificada em ordem reversa pela chave fornecida no argumento. Isso funciona exatamente da mesma forma que o filtro acima, mas o valor retornado estará na ordem inversa.

## 9.3.11. divisibleby

Retorna True se o valor for divisível pelo argumento. Se value for 21, a saída seria True.

```django
{{ value|divisibleby:"3" }}
```

## 9.3.12. escape

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

## 9.3.13. escapejs

Caracteres de escape para uso em strings JavaScript. Isso não torna a string segura para uso em literais de modelo HTML ou JavaScript, mas protege você de erros de sintaxe ao usar modelos para gerar JavaScript/JSON.

```django
{{ value|escapejs }}
```


## 9.3.14. filesizeformat

Formatos o valor como um tamanho de arquivo 'legível' (ie , , , etc.).'13 KB''4.1 MB''102 bytes'. Se value for 123456789, a saída seria .117.7 MB

```django 
{{ value|filesizeformat }}
```

## 9.3.15. first

Retorna o primeiro item de uma lista. Se value for a lista `['a', 'b', 'c']`, a saída será 'a'.

```django 
{{ value|first }}
```

## 9.3.16. floatformat

Quando usado sem um argumento, arredonda um número de ponto flutuante para uma casa decimal - mas apenas se houver uma parte decimal a ser exibida. Por exemplo: Se value for 34.23234 a saída será 34.2, se 34.00000 será 34, se 34.26000 será 34.3.

```django
{{ value|floatformat }}
```

Se usado com um argumento de número inteiro, `floatformat` arredonda um número para essa quantidade de casas decimais. Por exemplo: Se value for 34.23234 a saída será 34.232, se 34.00000 será 34.000, se 34.26000 será 34.260.

```django
{{ value|floatformat:3 }}
```

- Para ver mais possibilidades de formatação, acesse [floatformat](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#floatformat)

## 9.3.17. get_digit

ado um número inteiro, retorna o dígito solicitado, onde 1 é o dígito mais à direita, 2 é o segundo dígito mais à direita, etc. Retorna o valor original para entrada inválida (se a entrada ou argumento não for um inteiro, ou se argumento é menor que 1). Caso contrário, a saída é sempre um número inteiro. 

```django
{{ value|get_digit:"2" }}
```

Se value for 123456789, a saída será 8.

## 9.3.18. iriencode

Converte um IRI (Identificador de Recurso Internacionalizado) em uma string adequada para inclusão em uma URL. Isso é necessário se você estiver tentando usar strings contendo caracteres não ASCII em um URL. É seguro usar este filtro em uma string que já passou pelo `urlencodefiltro.` Se value for `"?test=1&me=2"`, a saída será `"?test=1&amp;me=2"`.

```django
{{ value|iriencode }}
```

## 9.3.19. join

Junta uma lista com uma string.  Se value for a lista `['a', 'b', 'c']`, a saída será a string `"a // b // c"`.

```python
{{ value|join:" // " }}
```

## 9.3.20. json_script

Produz com segurança um objeto Python como JSON, envolvido em uma \<\script\> tag, pronto para uso com JavaScript.
[json_script](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#json-script)

## 9.3.21. last

Retorna o último item de uma lista. Se value for a lista `['a', 'b', 'c', 'd']`, a saída será a string `"d"`.

``` django
{{ value|last }}
```

## 9.3.22. length

Retorna o comprimento do valor. Isso funciona para strings e listas. Se value for `['a', 'b', 'c', 'd']` ou `"abcd"`, a saída será `4`. O filtro retorna 0para uma variável indefinida.

```django
{{ value|length }}
```


## 9.3.23. length_is

Retorna `True` se o comprimento do valor for o argumento ou `False` caso contrário. Se value for `['a', 'b', 'c', 'd']` ou `"abcd"`, a saída será `True`.

```django
{{ value|length_is:"4" }}
```

## 9.3.24. linebreaks

Substitui quebras de linha em texto simples por HTML apropriado; uma única nova linha torna-se uma quebra de linha HTML ( \<br>) e uma nova linha seguida por uma linha em branco torna-se uma quebra de parágrafo (\<p>). Se value for Joel\nis a slug, a saída será \<p>Joel\<br>is a slug\</p>.

```django
{{ value|linebreaks }}
```

## 9.3.25. linebreaksbr

Converte todas as novas linhas em um pedaço de texto simples em quebras de linha HTML (\<br>). Se value for Joel\nis a slug, a saída será Joel\<br>is a slug.

```python
{{ value|linebreaksbr }}
```

## 9.3.26. linenumbers

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

## 9.3.27. force_escape

Aplica escape de HTML a uma string (consulte o filtro escape para obter detalhes). Este filtro é aplicado imediatamente e retorna uma nova string com escape. Isso é útil nos raros casos em que você precisa de vários escapes ou deseja aplicar outros filtros aos resultados de escape. Normalmente, você deseja usar o filtro escape. Por exemplo, se você deseja capturar os elementos \<p> HTML criados pelo `linebreaksfiltro`:

```django
{% autoescape off %}
    {{ body|linebreaks|force_escape }}
{% endautoescape %}
```

## 9.3.28. ljust

Alinha à esquerda o valor em um campo de uma determinada largura. Se value for Django, a saída será `"Django    "`.

```django
"{{ value|ljust:"10" }}"
```

## 9.3.29. lower

Converte uma string em letras minúsculas.Se value for `Totally LOVING this Album!`, a saída será `totally loving this album!`

```django
{{ value|lower }}
```

## 9.3.30. make_list

Retorna o valor transformado em uma lista. Para uma string, é uma lista de caracteres. Para um inteiro, o argumento é convertido em uma string antes de criar uma lista. Se value for a string `"Joel"`, a saída seria a lista `['J', 'o', 'e', 'l']` . Se value for `123`, a saída será a lista `['1', '2', '3']`.

```django 
{{ value|make_list }}
```

## 9.3.31. phone2numeric

Converte um número de telefone (possivelmente contendo letras) em seu equivalente numérico. A entrada não precisa ser um número de telefone válido. Isso irá facilmente converter qualquer string. Se value for 800-COLLECT, a saída será 800-2655328.

```django 
{{ value|phone2numeric }}
```

## 9.3.32. pluralize

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

## 9.3.33. random

Retorna um item aleatório da lista fornecida. Se value for a lista `['a', 'b', 'c', 'd']`, a saída pode ser `"b"`.

```django
{{ value|random }}
```

## 9.3.34. rjust

Alinha à direita o valor em um campo de uma determinada largura. Se value for `Django`, a saída será `"    Django"`.

```django
"{{ value|rjust:"10" }}"
```

## 9.3.35. safe

Marca uma string como não exigindo mais escape de HTML antes da saída. Quando o escape automático está desativado, este filtro não tem efeito. Se você estiver encadeando filtros, um filtro aplicado depois safe pode tornar o conteúdo inseguro novamente. Por exemplo, o código a seguir imprime a variável como está, sem escape:

```django
{{ var|safe|escape }}
```

## 9.3.36. safeseq

Entendi nada. Desculpa! [safeseq](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#safeseq)


## 9.3.37. slice

Retorna uma parte da lista.  Se some_list for `['a', 'b', 'c']`, a saída será `['a', 'b']`.

```django 
{{ some_list|slice:":2" }}
```

## 9.3.38. slugify

Converte para ASCII. Converte espaços em hifens. Remove caracteres que não são alfanuméricos, sublinhados ou hifens. Converte em minúsculas. Também remove os espaços em branco à esquerda e à direita. Se value for "Joel is a slug", a saída será "joel-is-a-slug".

```django 
{{ value|slugify }}
```

## 9.3.39. stringformat

Formata a variável de acordo com o argumento, um especificador de formatação de string. Este especificador usa a sintaxe de Formatação de String no estilo `printf`, com a exceção de que o “%” inicial é descartado. Se value for 10, a saída será 1.000000E+01.

```django
{{ value|stringformat:"E" }}
```

## 9.3.40. striptags

Faz todos os esforços possíveis para remover todas as tags HTML. Se value for "\<b>Joel\</b> \<button>is\</button> a \<span>slug\</span>", a saída será "Joel is a slug".

```django
{{ value|striptags }}
```

## 9.3.41. time
Formata uma hora de acordo com o formato fornecido. O formato fornecido pode ser o predefinido TIME_FORMAT ou um formato personalizado, igual ao filtro date. Observe que o formato predefinido depende da localidade. Se value for equivalente a datetime.datetime.now(), a saída será a string "01:23".

```django
{{ value|time:"H:i" }}
```

[time](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#time)

## 9.3.42. timesince

Formata uma data como a hora desde essa data (por exemplo, “4 dias, 6 horas”). Recebe um argumento opcional que é uma variável contendo a data a ser usada como ponto de comparação (sem o argumento, o ponto de comparação é agora ). Por exemplo, se blog_date for uma instância de data representando meia-noite em 1 de junho de 2006 e comment_date for uma instância de data para 08:00 em 1 de junho de 2006, o seguinte retornaria “8 horas”:

```django 
{{ blog_date|timesince:comment_date }}
```

## 9.3.43. timeuntil 

Semelhante a timesince, exceto que mede o tempo de agora até a data ou datetime fornecida. Por exemplo, se hoje é 1 de junho de 2006 e conference_date é uma instância de data que contém 29 de junho de 2006, então retornará “4 semanas”.{{ conference_date|timeuntil }} . ecebe um argumento opcional que é uma variável contendo a data a ser usada como ponto de comparação (em vez de agora ). Se from_date contiver 22 de junho de 2006, o seguinte retornará “1 semana”:

## 9.3.44. title

Converte uma string em caixa de título, fazendo com que as palavras comecem com um caractere maiúsculo e os caracteres restantes com minúsculas. Esta tag não faz nenhum esforço para manter “palavras triviais” em minúsculas. Se value for "my FIRST post", a saída será "My First Post".

```django
{{ value|title }}
```

## 9.3.45. truncatechars

Trunca uma string se for maior que o número especificado de caracteres. As strings truncadas terminarão com um caractere de reticências traduzível (“…”). Se value for "Joel is a slug", a saída será "Joel i…".

```django
{{ value|truncatechars:7 }}
```

## 9.3.46. truncatechars_html

Semelhante a truncatechars, exceto que reconhece tags HTML. Quaisquer tags que são abertas na string e não fechadas antes do ponto de truncamento são fechadas imediatamente após o truncamento. Se value for "\<p>Joel is a slug\</p>", a saída será "\<p>Joel i…\</p>". As novas linhas no conteúdo HTML serão preservadas.

## 9.3.47. truncatewords

Trunca uma string após um certo número de palavras. Se value for "Joel is a slug", a saída será "Joel is …".

```django 
{{ value|truncatewords:2 }}
```

## 9.3.48. truncatewords_html

emelhante a truncatewords, exceto que reconhece tags HTML. Todas as tags que são abertas na string e não fechadas antes do ponto de truncamento são fechadas imediatamente após o truncamento. Isso é menos eficiente do que truncatewords, portanto, só deve ser usado quando estiver recebendo texto HTML. Se value for "\<p>Joel is a slug\</p>", a saída será "\<p>Joel is …\</p>".

## 9.3.49. unordered_list

Pega recursivamente uma lista auto-aninhada e retorna uma lista HTML não ordenada - SEM abrir e fechar as tags \<ul>.  Para ler sobre acesse : 
[unordered_list](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#unordered-list)

## 9.3.50. upper

Converte uma string em maiúsculas. Se value for "Joel is a slug", a saída será "JOEL IS A SLUG".

```django 
{{ value|upper }}
```

## 9.3.51. urlencode

Escapa um valor para uso em um URL. Se value for "https://www.example.org/foo?a=b&c=d", a saída será "https%3A//www.example.org/foo%3Fa%3Db%26c%3Dd"

```django
{{ value|urlencode }}
```

Um argumento opcional contendo os caracteres que não devem ser escapados pode ser fornecido. Se não for fornecido, o caractere '/' será considerado seguro. Uma string vazia pode ser fornecida quando todos os caracteres devem ser escapados. Por exemplo:

```django
{{ value|urlencode:"" }}
```

Se value for "https://www.example.org/", a saída será "https%3A%2F%2Fwww.example.org%2F".

## 9.3.52. urlize

Converte URLs e endereços de e-mail em texto em links clicáveis. Os links podem ter pontuação final (pontos, vírgulas, parênteses próximos) e pontuação inicial (parênteses de abertura) e urlizeainda farão a coisa certa. Se value for "Check out www.djangoproject.com", a saída será ."Check out \<a href="http://www.djangoproject.com" rel="nofollow">www.djangoproject.com\</a>"

```django
{{ value|urlize }}
```

## 9.3.53. urlizetrunc

Converte URLs e endereços de e-mail em links clicáveis ​​assim como urlize , mas trunca URLs mais longos do que o limite de caracteres fornecido. Se value for "Check out www.djangoproject.com", a saída seria 'Check out \<a href="http://www.djangoproject.com" rel="nofollow">www.djangoproj…\</a>'

```django 
{{ value|urlizetrunc:15 }}
```

## 9.3.54. wordcount

Retorna o número de palavras. Se value for `"Joel is a slug"`, a saída será `4`.

```django 
{{ value|wordcount }}
```

## 9.3.55. wordwrap

Encapsula palavras no comprimento de linha especificado.

```django
{{ value|wordwrap:5 }}
```

Se value for Joel is a slug, a saída seria:

Joel
is a
slug

## 9.3.56. yesno

Mapas valores para True, Falsee (opcionalmente) None, para as cadeias de “sim”, “não”, “talvez”, ou um mapeamento personalizado passada como uma lista separada por vírgulas, e retorna uma dessas cadeias de acordo com o valor: Se valor for True, a saída será yeah; se for Flase, será no; se for None, será maybe... Por padrão se não por passado parâmetro, será apenas yes e no.


```django
{{ value|yesno:"yeah,no,maybe" }}
```

****************************

- Também é possível criar tags e filtros personalizados. Para isto acesse: [Writing custom template tags](https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/#howto-writing-custom-template-tags)


# 4. Henraça de templates

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

## 9.4.1. Dicas para usar a herança
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


# 9.6. Arquivos Estáticos

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

## Configuração dos Arquivos Estáticos

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

## Estutura de Pastas e Arquivos

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

## Exemplo com Passagem de Context0


## Urls Projeto

```Django
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
] 
```

## View da Aplicação
``` Django
from django.shortcuts import render

def index(request):
  context =	{} 
  return render(request, 'index.html', context)
```

## Url da Aplicação
``` Django
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]  
```

## View da Aplicação
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

## Arquivo Index

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

### Saída

**Marca Ford**

Lista de Cores
  - RED
  - WHITE
  - BLUE



## Exemplo Com Herança, Arquivos Estáticos e Inclusão de Arquivos

## Settings Projeto RESUMIDO

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

## Urls Projeto

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

## Url da Aplicação
``` Django
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]  
```

## View da Aplicação
``` Django
from django.shortcuts import render

def index(request):
  context =	{} 
  return render(request, 'index.html', context)
```

## Template Base

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

## Template index.html

- O arquivo index herda todas os arquivos carregados, o menu e as imagens do template BASE, abstraindo e simplificando o código
  - `{% extends 'base.html' %}`
- Além disso o arquivo diz logo em seguida que irá carregar arquivos estátricos.
  - `{% load static %}`
- Dentro do Bloco, **de mesmo nome** da base, iremos especificar o conteúdo que será inserido, na mesma posição original do arquivo base. 
  - `{% block content %} ... {% endblock content %}`
- Dentro do bloco iremos incluir arquivos HTML que contém diversos conteúdos, na ordem em que devem aparecer, 
  - `{% include 'footer.html' %}`

## Arquivo Footer

- Contém o carregamento de arquivos estáticos
  - `{% load static %}`
- Contém todo o código HTML responsável pela formatação do rodapé da pégina. 


### HTMLs

#### Base

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

#### Index

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
