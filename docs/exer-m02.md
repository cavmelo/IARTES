# Sobre ser guiado por teste
1. Elabore um programa que realize a leitura de uma data e um número de telefone, e armazene os valores lidos
em um dicionário que tem a seguinte estrutura:
```json
{
   "data":"dd/mm/aaaa",
   "telefone":"(92)999879876"
}
```
2. A data
considere uma data válida aquela que apresenta as seguintes características:
    1. dia > 0 e dia <= 31
    2. mes > 0 e mes <=12
    3. ano > 0

A data tem ainda as seguintes características especiais:

1. Os meses de Janeiro, Março, Abril, Maio, Junho, Agosto, Outubro, Dezembro tem 31 dias.

2. O mês de fevereiro tem 28 ou 29 dias (ano bissexto);

3. Os demais meses possuem 30 dias

# O caso do ano Bissexto
Para caracterizar se um dado ano é bissexto e portanto o mês de fevereiro terá 29 dias use as seguintes considerações:
1. Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá para a etapa 5.
2. Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário, vá para a etapa 4.
3. Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário, vá para a etapa 5.
4. O ano é bissexto (tem 366 dias).
5. O ano não é um ano bissexto (tem 365 dias).

# Usando Strings

Melhor abordagem neste estágio é usar o tipo de dado string (__str__). A string permite que você faça a leitura com os separadores e depois individualize os elementos. Por exemplo:
```Python
data = input()

dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[6:])
```
