![PyLadies](content/images/icones/logo.jpg)

# site
Projeto colaborativo do site PyLadies Caxias do Sul - Rio grande do Sul.

A página foi desenvolvida utilizando a biblioteca de geração de sites estáticos [Pelican](http://docs.getpelican.com/).


## Instalando e rodando
```
$ git clone git@github.com:PyladiesCaxias/PyladiesCaxias.github.io.git
```
Entre na pasta do repositório e crie um ambiente virtual (virtualenv). Se você não sabe como criar uma virtualenv, é altamente recomendado que leia o [tutorial DjangoGirls](http://tutorial.djangogirls.org/pt/django_installation/). Ative a virtualenv.

```
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

Criando um virtualenv:
```
cd <repo-path>
virtualenv -p python3 venv
```


Ativando o ambiente (**sempre** faça isto antes de qualquer ação):  
```
cd <repo-path>
source venv/bin/activate
```

Instalando as dependências do projeto:  
```
cd <repo-path>
source venv/bin/activate
pip install -r requirements.txt
```

Acesse a branch de desenvolvimento:

```
git checkout dev
```

Gerando a estrutura do projeto:  
```
pelican content
```

## Executando o projeto local

```
cd <repo-path>/output
python -m pelican.server
```

## Estrutura do projeto
```
├── content
│   ├── home.md
│   └── images
│       └── logo.jpg
├── develop_server.sh
├── fabfile.py
├── LICENSE
├── Makefile
├── output
│   ├── archives.html
│   ├── authors.html
│   ├── categories.html
│   ├── index.html
│   ├── tags.html
│   └── theme
│       ├── css
│       │   ├── main.css
│       │   ├── pygment.css
│       │   ├── reset.css
│       │   ├── typogrify.css
│       │   └── wide.css
│       └── images
│           └── icons
│               ├── aboutme.png
│               ├── bitbucket.png
│               ├── delicious.png
│               ├── facebook.png
│               ├── github.png
│               ├── gitorious.png
│               ├── gittip.png
│               ├── google-groups.png
│               ├── google-plus.png
│               ├── hackernews.png
│               ├── lastfm.png
│               ├── linkedin.png
│               ├── reddit.png
│               ├── rss.png
│               ├── slideshare.png
│               ├── speakerdeck.png
│               ├── stackoverflow.png
│               ├── twitter.png
│               ├── vimeo.png
│               └── youtube.png
├── pelicanconf.py
├── publishconf.py
└── requirements.txt

```

Contribuindo
------------

Para contribuir com o projeto veja o guia de
[Contribuição](https://github.com/PyladiesCaxias/PyladiesCaxias.github.io/blob/master/CONTRIBUINDO.md).

Links Úteis
-----------

* Documentação Pelican - http://docs.getpelican.com/en/3.6.3/
* Virtualenv - http://docs.python-guide.org/en/latest/dev/virtualenvs/
