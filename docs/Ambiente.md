# O seu ambiente de trabalho
Abaixo encontram-se dicas de como preparar um ambiente para realizar 
as tarefas de programação deste módulo.

## Crie o ambiente de programação

1. Atom
Editor de texto que facilita a criação do scripts. Possui 
extensões que podem ser habilidades para incrementar o 
suporte ao desenvolvimento de programas. Acesso feito [aqui](https://atom.io)

2. IDE PyCharm.
Ambiente integrado de programação dedicado aos projetos escrito em python. Possui um ambiente
bem mais completo com apoio a validação do código, controle de versão (git, github e subversion),
console python e autocomplete. O PyCharm vem em diferentes versões, a sugestão
é usar a community edition que está disponível [aqui](https://www.jetbrains.com/pycharm/download)

4. Python

Instalação do python deve ocorre para a versão mais atualizada, python3. Abaixo encontra-se link para tutoriais de instalação:

* [Windows](https://python.org.br/instalacao-windows/)
* [Linux](https://python.org.br/instalacao-linux/)
* [Mac](https://python.org.br/instalacao-mac/)


# Atualizando o *pip*

Com o python instalado, o seu computador também deve ter instalado o gerenciador de pacotes do python, O *pip*. Garanta que ele esteja atualizado, para isso execute o seguinte comando:

```bash
$ pip3 install --upgrade pip
Collecting pip
[...]
Successfully installed pip-22.1
```

# Instalando o ambiente virtual (*virtualenv*)

Isole o ambiente que será usado para construir os seus scripts. O isolamento evita que ocorra o conflito de versões de 
bibliotecas impactando o projeto em curso ou outros projetos que já desenvolvido. Em cada ambiente será instalado 
exatamente as libs com as versões adequadas ao projeto.

Para a instalação do ambiente virtual execute o seguinte comando:

```bash
$ pip3 install --user --upgrade virtualenv
Collecting virtualenv
[...]
Successfully installed virtualenv
```
Crie um ambiente Python virtual isolado executando o seguinte comando:

```bash
$ cd $T_PATH
$ virtualenv env
created virtual environment CPython3.7.4.final.0-64 in 2167ms
```
Ative o seu ambiente executando o seguinte comando:

```bash
$ cd $T_PATH
$ source env/bin/activate
```
O ambiente está pronto para a instalação de novos pacotes sem quaisquer efeitos colaterais ou gerar conflitos com outros 
projetos.

Para desativar o ambiente, execute o seguinte comando:

```bash
$ deactivate
```
