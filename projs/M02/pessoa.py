class Pessoa(object):
    def __init__(self, nome, idade, peso, altura):
        self._name = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def imc(self, variacao=0.1):
        cal =  self.peso/(self.altura*self.altura)
        return cal - cal*variacao


class Funcionario(Pessoa):
    def __init__(self, matricula, nome, idade, peso, altura):
        super().__init__(nome, idade, peso, altura)
        self.matricula = matricula

    def imc(self):
        return (self.peso-0.1) / (self.altura * self.altura)

def usa():
    p = Pessoa('Maria', idade=25, peso=67.0, altura=1.7)
    print("pessoa: %s" % p.nome)

    diretor = Funcionario(matricula="674567",nome="João", idade=30, peso=85, altura=1.5)
    print("diretor: %s" % diretor.nome)

    print("IMC do diretor: %f" % diretor.imc())
    print("IMC da pessoa: %f" % p.imc(variacao=0.0))

if __name__ == "__main__":
    usa()