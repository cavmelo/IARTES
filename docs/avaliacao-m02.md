# Sobre TDD, PyTest, e Coverage
Neste trabalho, dois validadores serão desenvolvidos a partir dos conceitos e técnicas 
apresentados até então no curso. Especificamente, os validadores serão projetados usando
a técnica de Desenvolvimento Dirigido por Teste (TDD), e implementados em Python de forma 
incremental. Para isso considere os passos a seguir.

## Os Validadores
O endereço de correio eletrônico (__email__) e cadastro de pessoa física (__CPF__) são informações bastante utilizadas
para coletar informações sobre pessoas. Essas duas informações apresentam padrões que por definição
precisam ser respeitados, durante a coleta da informação. 

### email, o que validar
Todo email válido precisa apresentar o símbolo especial @. Esse caracter divide o email em duas
partes: o identificador e o domínio em que o endereço está hospedado. Sua primeira tarefa e pesquisar
quais são as regras usadas para validar essas duas partes. De posse dessa informação, implemente em python:
1. Casos de teste;
2. Script de validação.

### o CPF, o que validar
Todo CPF para ser válido precisa apresentar também duas partes. Essas partes são separadas por um caracter - (traço), 
sendo a segunda parte conhecida como dígito verificador. A sua primeira tarefa é pesquisar quais
são as regras usadas para validar um CPF, o que inclui a definição do dígito Verificador. De posse desse conhecimento,
implemente em python:
1. Casos de teste;
2. Script de validação

O processo de desenvolvimento desses dois validadores precisa ter o amparo nos casos de testes elaborados, portanto quanto mais abrangentes
forem os casos, mais robusta será a sua implementação. 

## Metodologia

A seguir, apresentam-se as linhas gerais de como o trabalho deverá ser realizado. Duas ferramentas essenciais para realização
desta tarefa são: __pytest__ e __coverage__. Dessa forma, antes de mais nada, realize a instalação dos mesmos. 

```shell
pip install pytest
```
```shell
pip install coverage
```

O passo seguinte é a implementação de duas classes com os casos de teste de cada validador. Essas classes podem ser implementadas
em um mesmo arquivo __.py__. É preciso respeita as regras de atribuição de nomes às classes, isto é, todas precisam iniciar
seus nomes com a palavra __Test__, seguido de um nome que faça referência ao validador, i.e., Email e Cpf. 

Crie uma pasta __TDD__ para armazenar as classes e os testes. 

Veja a seguir um exemplo de como as classes __DEVEM__ ser nomeadas, bem como os seus métodos.

```python
import validador as val
class TestTelefone(object):
    def test_ddd_invalido(self):
        v = val.Validador()
        telefone = '(9)999664444'
        assert v.validar_telefone(telefone) == False
```
Observe que tanto o nome da classe quanto o nome do método iniciam com a palavra __test__. O detalhe importante é que a classe é nomeada
com __T__ maiúsculo.

Após definido e implementado os casos de teste, deve-se proceder à implementação dos validadores de email e cpf. Crie os seus validadores
realizando a extensão das operações já implementadas no script __validador.py__.

Essa implementação deve ser guiada por chamadas recorrentes à __coverage__. Veja como chamar a __coverage__ com o conjunto de diretivas
adequadas.

```shell
coverage run --source=. -m pytest tests.py 
```


Para obter as estatísticas de cobertura de código, veja abaixo como chamar a __coverage__.
```
 coverage report --show-missing 
 ```