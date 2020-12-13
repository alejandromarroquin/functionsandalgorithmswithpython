import time
objetivo=int(input('Ingresa un número: '))
epsilon=0.01
paso=epsilon**2
respuesta=0.0
num=0
start = time.time()
while abs(respuesta**2-objetivo)>=epsilon and respuesta<=objetivo:
    print(respuesta**2-objetivo, respuesta)
    respuesta+=paso
    num+=1
end = time.time()
print(f'Para resolver hizo {num} iteraciones y se demoro {end - start} segundos')
if abs(respuesta**2-objetivo)>=epsilon:
    print(f'No se encontro la raíz cuadrada del objetivo')
else:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')