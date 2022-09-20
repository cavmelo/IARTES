# Aula sobre Conceitos básicos

1. Escreva um script python que define duas variáveis do tipo inteiro (__int__)
e atribui um valor positivo para elas. Imprima as duas variáveis.
2. Seja x = 2 + 4j, descubra qual é tipo associado a essa variável pelo interpretador.
3. Experimente a inicialização de variáveis como segue:
   1. urnas = {}
   2. sessao = {"escola municipal", 103}

   descubra qual é o tipo da variável __urnas__ e da variável __sessao__. Explique se necessário
a razão dos tipos serem distintos.
4. Nas definições de nomes de variáveis abaixo quais têm nomes válidos e quais são invalidos
    1. ola = "mundo"
    2. _ola = "mundo"
    3. _1_ola = "mundo"
    4. 1_ola = "mundo"
    5. ola_1 = "mundo"
    6. meu mundo = "ola"

aponte as razões para os nomes inválidos, indicando o item e a razão da violação
das regras de nomeação de variável.

5. No seguinte comando de atribuição 
   1. casa, senha = "minha", "ola"
   2. casa, senha = "minha"
   3. casa = "minha"

Quais foram as atribuições que funcionaram e quais não funcionaram? Explique a razão dos problemas.
   
6. Considere as seguintes operações matemáticas, e indique o resultado de cada uma:
   1. (10 - 6)**2
   2. 10 - 6**2
   3. 10 - 3 // 2
   4. 10 - 3 / 2

7. Qual a importância de se criar ambiente virtuais para o desenvolvimentos de projetos usando Python?

8. Descubra e responda qual versão do python está instalado no seu ambiente de desenvolvimento. Que comando você usou 
para obter essa informação?

9. Uma tupla é um tipo imutável, portanto qualquer variável desse tipo pode ser alterada desde que os seus elementos 
sejam individualizados, como no código abaixo:

   __comprado = ("carro", "GM", "20K")__

   __comprado[1] = "Ford"__

   você concorda com essa afirmação? justifique sua resposta.


10. Considere o código abaixo:

      __numero = input()__
      
      print(numero*3)
   
      se o valor 3(três) for informado como entrada e armazenado na variável número.

11. Revise o código disponibilizado em src/primeiro.py. Em seguida altere o programa
para que ele se torne generalista, i.e., aceite qualquer quantidade de notas que cada
aluno pode ter. 