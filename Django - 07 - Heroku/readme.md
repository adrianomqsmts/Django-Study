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
