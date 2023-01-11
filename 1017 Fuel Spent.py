tempo_gasto = int(input())
velocidade_media = int(input())

KM_POR_LITRO = 12

distancia = velocidade_media*tempo_gasto

gasolina_gasta = distancia/KM_POR_LITRO

print(f"{gasolina_gasta:.3f}")