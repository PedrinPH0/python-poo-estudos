from modelos.carro import Carro
from modelos.moto import Moto

carro_suv = Carro('Ford', 'Territory', 6)
carro_hb20 = Carro('Hyundai', 'Sense', 4)
carro_polo = Carro('Volkswagen', 'Track', 4)
moto_rx1 = Moto('Subaru', 'Trilha', 'Casual')
moto_bmx = Moto('Yahama', 'Rua', 'Esportiva')
moto_50tinha = Moto('Toyota', 'Caseira', 'Casual')

'''
print(carro_suv)
print(carro_hb20)
print(carro_polo)
print(moto_rx1)
print(moto_bmx)
print(moto_50tinha)
'''

Carro.listar_veiculos()
print('')
Moto.listar_veiculos()