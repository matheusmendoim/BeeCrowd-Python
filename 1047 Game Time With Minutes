initial_hour, initial_minute, final_hour, final_minute = map(int, input().split())

initial_time = (initial_hour*60)+initial_minute
final_time = (final_hour*60)+final_minute

time = final_time-initial_time

if time <= 0:
    time += (24*60)
    
duration_hour = time//60
duration_minute = time%60

print(f"O JOGO DUROU {duration_hour} HORA(s) E {duration_minute} MINUTO(S)")