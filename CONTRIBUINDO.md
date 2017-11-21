Para fazer a manutenção use a branch **dev**.

```
git checkout dev
```

1. Criando e Adicionando
  * [Eventos](#criar-um-novo-evento)
  * [Criar um novo post](#criar-um-novo-post)
  * [Criar uma nova página](#criar-uma-nova-página)
  * [Adicionar materiais](#materiais)
  * [Adicionar links na barra social](#barra-social)
  * [Atualizando o site](#atualizando-o-site)


Criar um novo Post
------------------

Para criar um novo post, noticias, artigos, eventos, rode o comando:

	```
    make post NAME="NOME DO SEU POST"
    ```

Ele irá criar um novo arquivo **nome-do-seu-post.md** na pasta **content** e abrirá seu editor favorito com um conteúdo pré-adicionado.  Você só precisará adicionar o restante do conteúdo.

* Para ter uma descrição mais curta na página inicial ou página de eventos adicione a tag ***sumary***, com um resumo do post
* Pode se adicionar tag para os posts, adicionando ***tags***:
	ex: tags: eventos, django_girls, python

Após terminar o post, renderize-o com o comando:
    ```
	pelican content
    ```

Se tudo deu certo, seu novo post já estará disponível na página.

* Quando o post estiver pronto pode adicioná-lo ao github:
    ```
	git commit -am "Adicionado post NOME DE SEU POST"
	git push origin nome_branch
    ```

Eventos
------------------

Os eventos criados pelo meetup aparecerão direto na página de eventos, caso precise criar uma paǵina de evento que não está no meetup segue os passos abaixo:

Para criar um novo evento (congressos, seminários) Ex: Python Brasil:

	```
    make event NAME="NAME EVENTO"
    ```

Ele irá criar um novo arquivo **nome-do-seu-evento.rst** na pasta **content** e abrirá seu editor favorito com um conteúdo pré-adicionado.  Você só precisará adicionar o restante do conteúdo.

* Ex:
    ```
    :slug: novo-evento

    :event-start: 2017-09-8 9:00
    :event-duration: 3h
    :event-end:  2017-09-10 12:00
    :location: Local do Evento
    :summary: Descrição do Evento
    ```

Após terminar o post, renderize-o com o comando:

	```
    pelican content
    ```

Se tudo deu certo, seu novo post já estará disponível na página. O evento aparecerá na página de Eventos e na home.

* Quando o post estiver pronto pode adicioná-lo ao github:

    ```
	git commit -am "Adicionado post NOME DE SEU POST"
	git push origin nome_branch
    ```

Criar uma nova Página
---------------------

Para criar uma nova página, rode o comando:

    ```
    make page NAME='NOME PAGINA'
    ```

Ele irá criar um novo arquivo **nome-pagina.md** na pasta **content/pages** e abrirá seu editor favorito com um conteúdo pré-adicionado.  Você só precisará adicionar o restante do conteúdo.

Após terminar de editar a página, renderize-a com o comando:
    ```
	pelican content
    ```

Se tudo deu certo, sua página já estará disponível em **/slug-pagina/**. A página aparecerá no menu automaticamente.

* Quando o post estiver pronto pode adicioná-lo ao github:
    ```
	git commit -am "Adicionado post NOME DE SEU POST"
	git push origin nome_branch
    ```

Materiais
---------------------

Para adicionar links na página Materiais:

No arquivo: pelicanconf.py

* adicionar uma tupla no MATERIAIS_LINKS:
	ex: ('Nome do curso', link, tema),

Rode o comando:
    ```
	pelican content
    ```

* Quando estiver pronto pode adicioná-lo ao github:
    ```
	git commit -am "Adicionado post NOME DA Alteração"
	git push origin nome_branch
    ```


Barra Social
---------------------

Para adicionar links da barra social:

No arquivo: pelicanconf.py

* Para adicionar um link para um site:
	* adicionar uma tupla no LINKS:
		ex: ('Nome site', link),

* Para adicionar links para redes social do PyLadies Caxias do Sul:
	* adicionar uma tupla no SOCIAL:
			ex: ('nome_do_icone', 'Titulo', 'link'),

* Para adicionar links para site de eventos Python:
	* adicionar uma tupla no EVENTOS:
			ex: ('Titulo do link', 'link'),

Rode o comando:
    ```
	pelican content
    ```

* Quando estiver pronto pode adicioná-lo ao github:
    ```
	git commit -am "Adicionado post NOME DA Alteração"
	git push origin nome_branch
    ```


Atualizando o site
------------------

Para atualizar o site rode o comando abaixo.
    ```
    make github
    ```

Ele vai compilar os html, e dar o push na brach master do github.

* Obs: Ainda é necessário dar o commit das atualizações na **branch dev**
