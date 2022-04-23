## Instalação do projeto na máquina local:

### Requisitos na máquina local:

* Instalação do PostgreSQL: https://www.postgresql.org/

  * site oficial do PostgreSQL: https://www.postgresql.org/
  * vídeo passo a passo da instalação: https://www.youtube.com/watch?v=His77sqWfGU

* Instalação do Python (a partir da versão 3.9 ):

  * site oficial do python: https://www.python.org/
  * vídeo passo a passo da instalação: https://www.youtube.com/watch?v=pDBnCDuL-dc

* Instalação do Git:

  * site oficial do Git: https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git

  * vídeo passo a passo da instalação: https://www.youtube.com/watch?v=ONztz-yh4jY

    

### Clonando projeto para máquina local:

* Criar repositório onde será mantido o projeto. Ex.: C:\Users\seunome\desenv\badmintonbd
* No git bash, executar o comando: **git clone https://github.com/csdamo/badminton_scout.git**
* 

### Criando ambiente virtual de desenvolvimento:

* No prompt de comando, executar o comando: **pip install virtualenv** 

* Pelo prompt, vá até o diretório do projeto e execute o comando: **virtualenv venv** - ele criará uma pasta dentro do repositório com o nome "venv"

* Agora, é possível ativar o ambiente virtual de desenvolvimento: ainda no prompt de comando (dentro do repositório do projeto) execute o comando: **venv/Scripts/activate** (Windows) ou **source venv/bin/activate** (Linux) 

* Para você saber se o ambiente virtual foi ativadi, perceba se antes do caminho do seu diretório, aparece o nome do ambiente entre parênteses. Ex.: (venv) C:\Users\seunome\desenv\badmintonbd>

  

### Iniciando a configuração do projeto Django

* Dentro do ambiente virtual, rodar o comando **pip install -r requirements.txt** para instalar os pacotes na versão correta para o projeto 

* Baixar o arquivo **settings.py** do projeto, no diretório das configurações do projeto (pasta com o nome settings) - o arquivo settings não ficará junto com o projeto no GitHub pois possui a senha do banco de dados

  

### Configurando o banco de dados

- Criar banco de dados no Postgres : **create --**> **database –**-> **nome_do_banco** (Esse processo pode ser feito com o PGAdmin do Postgres)
- Configurar o banco de dados no settings.py - dentro do arquivo settings nas configurações de banco de dados, colocar as seguintes informações: 

DATABASES = { 
  						'default': { 
   										 'ENGINE': 'django.db.backends.postgresql_psycopg2', 
   										 'NAME': 'nomedobanco', 
   										 'USER': 'usuariopostgres', 
    										'PASSWORD': 'senhadobanco', 
    										'HOST': '127.0.0.1', 
   										 'PORT': '5432', # posta padrão do Postgres 
  										} 
						} 



### Criação das tabelas no banco de dados: 

- Dentro do diretório do projeto, com o ambiente virtual ativado rodar o comando de criação das tabelas do banco de dados: **python manage.py migrate**  - além das tabelas necessárias para o nosso projeto, serão criadas as tabelas próprias do Django

  

### Criar o usuário "root" do projeto 

- Ainda com o ambiente virtual ativo, rodar o comando: **python manage.py createsuperuser** 

- Informar usuário (pode usar admin como padrão), e-mail e senha 

  

### Subindo o servidor:

- No prompt de comando, com o ambiente virtual ativado, executar o comando: **python manage.py runserver** 
- Acessar o endereço http://127.0.0.1:8000/ no navegador para verificar o projeto rodando 
- Aceaar o admin do projeto através do endereço endereço http://127.0.0.1:8000/admin 
- Fazer o login com os dados cadastrados no superuser



