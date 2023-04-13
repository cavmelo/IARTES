# Projeto Final

## Usando conceitos de POO no contexto de TDD

A implementação deve seguir a metodologia TDD. Para isso, apresente no seu relatório
uma lista de requisitos para cada classe da hierarquia. Essa lista precisa ser 
suficientemente fechada para que a equipe de teste consiga desenvolver o conjunto 
de testes, e esse oriente a implementação.

## Relatório do Projeto RH

1. Introdução.
Este documento apresenta o planejamento das atividades de testes contendo a hierarquia de Classes do sistema  Recursos humanos (RH) de uma escola o qual será utilizado como base para as atividades de testes, a fim de obter experiência prática em implementação dos conceitos de POO no contexto de TDD. Desta forma, as classes criadas foram utilizando o conceito de POO e aplicação de casos de Teste usando a biblioteca Pytest.



![classes_projeto](https://user-images.githubusercontent.com/7781570/193377406-10c5ebbe-72b6-4197-aa4b-da6db64a2bdd.png)


2. Lista de Resquisitos para cada classe
   - Criar uma classe abstrata para que sirva como contrato para as demais classes do negócio. Exemplo.: classe Pessoa.

   - Classe Funcionário: deverá receber nome, data de nascimento, telefone, matricula, departamento e data de admissão

   - Classe Professor: herda da classe Funcionário e deverá conter os atributos carga horária, titulo e area de atuação.

   - Técnico: herda da classe Funcionário e deverá conter os atributos cargo, chefia, qualificação

3.  A hierarquia. 

No paradigma orientado à objetos, uma classe é a representação do mundo real. A classe Pessoa é a nossa classe Principal e é do tipo abstrata.

class Pessoa(ABC):

    def __init__(self, nome, data_nascimento, telefone):

        self.nome = nome

        self.data_nascimento = data_nascimento

        self.telefone = telefone

Em python utilizamos classes abstradas para criar contratos, esse tipo de classe não pode ser instanciada. O módulo ABC fornece a base para definir classes abstradas. Um método se torna abstrato quando decorado com @abstractmethod.

o método ( __init__ ), define o construtor da classe, ou seja, definimos como uma nova pessoa será criada em nosso programa.


Os Getters e setters são usados em muitas linguagens de programação orientada a objetos para garantir o princípio do encapsulamento de dados. 

@abstractmethod
    def set_nome(self):
        pass

    @abstractmethod
    def set_data_nascimento(self):
        pass

    @abstractmethod
    def set_telefone(self):
        pass

    @abstractmethod
    def get_nome(self):
        pass

    @abstractmethod
    def get_data_nascimento(self):
        pass

    @abstractmethod
    def get_telefone(self):
        pass


A classe Funcionario

class Funcionario(Pessoa):

    def __init__(self, nome, data_nascimento, telefone,
                 matricula, departamento, data_admissao):

        super().__init__(nome, data_nascimento, telefone)

        self.matricula = matricula

        self.departamento = departamento

        self.data_admissao = data_admissao


A classe Funcionario herda apenas da classe Pessoa sendo chamada de herança simples. E deriva suas classes: Professor e Técnico

A classe Professor herda da classe Funcionario.


class Professor(Funcionario):

    def __init__(self, nome, data_nascimento, telefone, matricula, departamento, data_admissao,
                 carga_horaria, titulo, area_de_atuacao):

        super().__init__(nome, data_nascimento, telefone, matricula, departamento, data_admissao)

        self.carga_horaria = carga_horaria

        self.titulo = titulo

        self.area_de_atuacao = area_de_atuacao

O Polimorfismo é a capacidade de um objeto poder ser referenciado de várias formas, e podemos visualizar sua implementação desse conceito com o uso dos mesmo
metodos na classe Funcionário sendo implementado na classe Professor.


A classe Técnico herda da classe Funcionario.

class Tecnico(Funcionario):

    def __init__(self, nome, data_nascimento, telefone, matricula, departamento, data_admissao,
                 cargo, chefia, qualificacao):

        super().__init__(nome, data_nascimento, telefone, matricula, departamento, data_admissao)

        self.cargo = cargo

        self.chefia = chefia

        self.qualificacao = qualificacao


4. Relatório de cobertura do código.

Essa implementação foi guiada por chamadas recorrentes à coverage. Veja como chamar a coverage com o conjunto de diretivas adequadas:

coverage run --source=. -m pytest tests.py

coverage report --show-missing

- A primeira execução contém uma cobertura de código 59%

![coverage_im1_50](https://user-images.githubusercontent.com/7781570/193372318-b979e213-5cb6-46c7-944a-4c10e4ccc524.png)

Foi verificado se cada classe retorna o esperado, confome o Métodos da Classe Pessoa, juntos com as demais classes:

Caso de teste do Método da Classe:

-  Validação dos gets e sets: nome, data de nascimento, etc.

<hr>
- A execução que contém uma cobertura de 80% do código.


![img_1.png](https://github.com/EwertonMaia/imgtrabalho/blob/main/80%25teste.jpeg?raw=true)

Chegamos a uma cobertura de 82%, quando foi implementado na classe Professor os teste de `calcular salário de professor`

-[ ] Caso de teste do Método da Classe:

   Validação dos gets e sets: `salario,carga_horaria, titulo.
 (A princípio queríamos implementar uma sobrecarga de método (salario) mas o Python não suporta, o polimorfismo ocorre nas classes filhas de Funcionário)
<hr>
- A execução que contém uma cobertura de 94% do código.


![img_1.png](https://github.com/EwertonMaia/imgtrabalho/blob/main/94%25teste.jpeg?raw=true)

Chegamos a uma cobertura de 94%, quando foi implementado na classe Técnico os teste de `calcular salário de técnico`

-[ ] Caso de teste do Método da Classe:

   Validação dos gets e sets: `salario,chefia, qualificação, etc.`




5. Conclusões.

   Podemos perceber que é fundamental a execução de um estudo para refinar os requisitos de um projeto, definir bem os atributos implementados nas classes e saber o que se quer testar no código. é importante também gerar uma lista de teste.

   Nossa dificultade foi empregar os conceitos de forma organizada, pois cada um dos integrantes tem ideias próprias.
   
   Agradecemos ao Prof Cesar, pelos ensinamoe e orientação na disciplina.