1. Criando e Adicionando
  * [Criar um novo post](#criar-um-novo-post)
  * [Atualizando o site](#atualizando-o-site)
  * [Adicionar materiais](#materiais)


Criar um novo Post
------------------

Para criar um novo post, noticias, artigos, eventos, rode o comando:

	make post NAME='NOME DO SEU POST'

Ele irá criar um novo arquivo `nome-do-seu-post.md` na pasta `content` e abrirá seu editor favorito com um conteúdo pré-adicionado.  Você
só precisará adicionar o restante do conteúdo.


* Obs: Deve adicionar a categoria do post.*
Exemplos:

**category: Eventos**

**category: Proximos Eventos**

* Para ter uma descrição mais curta na página inicial ou página de eventos adicione a tag ***sumary***, com um resumo do post
* Pode se adicionar tag para os posts, adicionando ***tags***:
	ex: tags: eventos, django_girls, python 

Após terminar o post, renderize-o com o comando:

	pelican content

Se tudo deu certo, seu novo post já estará disponível na página.

* Quando o post estiver pronto pode adicioná-lo ao github:
	
	git commit -am "Adicionado post NOME DE SEU POST"
	git push origin nome_branch

Criar uma nova Página
---------------------

Para criar uma nova página, rode o comando:

	make page NAME='NOME PAGINA'

Ele irá criar um novo arquivo `nome-pagina.md` na pasta `content/pages` e abrirá seu editor favorito com um conteúdo pré-adicionado.  Você só precisará adicionar o restante do conteúdo.

Após terminar de editar a página, renderize-a com o comando:

	pelican content

Se tudo deu certo, sua página já estará disponível em `/slug-pagina/`. A página aparecerá no menu automaticamente.

* Quando o post estiver pronto pode adicioná-lo ao github:
	
	git commit -am "Adicionado post NOME DE SEU POST"
	git push origin nome_branch


Para adicionar links na página Materiais
---------------------

No arquivo: pelicanconf.py

* adicionar uma tupla no MATERIAIS_LINKS:
	ex: ('Nome do curso', link, tema),

Rode o comando:

	pelican content

* Quando estiver pronto pode adicioná-lo ao github:
	
	git commit -am "Adicionado post NOME DA Alteração"
	git push origin nome_branch

Para adicionar links da barra social:
---------------------

No arquivo: pelicanconf.py

* Para adicionar um link para um site:
	* adicionar uma tupla no LINKS:
		ex: ('Nome site', link),

* Para adicionar links para redes social do Pyladies Caxias:
	* adicionar uma tupla no SOCIAL:
			ex: ('nome_do_icone', 'Titulo', 'link'),

* Para adicionar links para site de eventos Python:
	* adicionar uma tupla no EVENTOS:
			ex: ('Titulo do link', 'link'),

Rode o comando:

	pelican content

* Quando estiver pronto pode adicioná-lo ao github:
	
	git commit -am "Adicionado post NOME DA Alteração"
	git push origin nome_branch


Atualizando o site
------------------

Para atualizar o site rode o comando abaixo.

    make github

Ele vai compilar os html, e dar o push na brach gh-pages do github.

* Obs: Ainda é necessário dar o commit das atualizações na sua branch