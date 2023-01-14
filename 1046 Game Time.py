hora1, hora2 = map(int, input().split())

if hora1 == hora2:
    duracao = 24
elif hora1 > hora2:
    duracao = 24-abs(hora1-hora2)
else:
    duracao = abs(hora2-hora1)
    
print(f"O JOGO DUROU {duracao} HORA(S)")