carro1 = { 'modelo' : 'Corsa' , 'ano' : 2007 }
carro2 = { 'modelo' : 'Belina' , 'ano' : 1986 }
carro3 = { 'modelo' : 'Monza' , 'ano' : 1995 }

print( carro1 )

carro1[ 'modelo'] = 'Corsa Classic'
print( carro1 )

frota = carro1, carro2

print("------------------------------------------")
print( frota )
print(frota[1])
carro2['modelo'] = "Del Rey"
# frota[0] = carro3
print( frota )

print("------------------------------------------")
for chave, valor in  carro3.items() :
    print( chave , ": " , valor)
    

