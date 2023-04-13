from profissionalAdministrador import ProfissionalAdministrador
from profissionalContador import ProfissionalContador
from profisionalEngenheiro import ProfissionalEngenheiro

listaProfissonalAdministrador = []
listaProfissionalContador = []
listaProfissionalEngenheiro = []

profissionalAdministrador1 = ProfissionalAdministrador (154790, 'Ana Júlia', 26, 78745012306, 999652648)
profissionalAdministrador2 = ProfissionalAdministrador (202010, 'João', 31, 15478965214, 991474560)
profissionalAdministrador3 = ProfissionalAdministrador (202020, 'Junior', 30, 15478965214, 991474560)

listaProfissonalAdministrador.append(profissionalAdministrador1)
listaProfissonalAdministrador.append(profissionalAdministrador2)
listaProfissonalAdministrador.append(profissionalAdministrador3)

ProfissionalContador1 = ProfissionalContador (61432144, 'Joaquim', 50, 12345678912, 32415050) 
ProfissionalContador2 = ProfissionalContador (20017463, 'Francielle', 25, 12345678998, 32428080)
ProfissionalContador3 = ProfissionalContador (20017222, 'Raimundo', 10, 12345678998, 32428080)

listaProfissionalContador.append(ProfissionalContador1)
listaProfissionalContador.append(ProfissionalContador2)
listaProfissionalContador.append(ProfissionalContador3)

ProfissionalEngenheiro1 = ProfissionalEngenheiro (61432144, 'Joaquim', 50, 12345678912, 32415050) 
ProfissionalEngenheiro2 = ProfissionalEngenheiro (20017463, 'Francielle', 25, 12345678998, 32428080)
ProfissionalEngenheiro3 = ProfissionalEngenheiro (20017222, 'Raimundo', 10, 12345678998, 32428080)

listaProfissionalEngenheiro.append(ProfissionalEngenheiro1)
listaProfissionalEngenheiro.append(ProfissionalEngenheiro2)
listaProfissionalEngenheiro.append(ProfissionalEngenheiro3)

print('~'*40)
print('Lista de Administradores:')
for administrador in listaProfissonalAdministrador:
  print('CRA: {} | Nome: {} | Idade: {}'.format(administrador.get_cra(), administrador.get_nome(), administrador.get_idade()))
  print('CPF: {} | Telefone: {}'.format(administrador.get_cpf(), administrador.get_telefone().get_telefone()), end='\n\n')
print('~'*40)

print('Lista de Contadores:')
for contador in listaProfissionalContador:
  print('CRC: {} | Nome: {} | Idade: {}'.format(contador.get_crc(), contador.get_nome(), contador.get_idade()))
  print('CPF: {} | Telefone: {}'.format(contador.get_cpf(), contador.get_telefone().get_telefone()), end='\n\n')
print('~'*40)

print('Lista de Engenheiros:')
for engenheiro in listaProfissionalEngenheiro:
  print('CREA: {} | Nome: {} | Idade: {}'.format(engenheiro.get_crea(), engenheiro.get_nome(), engenheiro.get_idade()))
  print('CPF: {} | Telefone: {}'.format(engenheiro.get_cpf(), engenheiro.get_telefone().get_telefone()), end='\n\n')
print('~'*40)