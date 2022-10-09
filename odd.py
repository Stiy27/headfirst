from datetime import datetime
import time
import random

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for i in range(5):
    
    #Capitura o minuto atual e armazena na variável
    right_this_minute = datetime.today().minute
    
    #Verifica se o minuto atual está na lista odds
    if right_this_minute in odds:
        print("This minute seens a little odd.")
    else:
        print("Not an odd minute.")
        
    #Pausa o looop (for) por um número aleatório de segundos
    # - time.sleep(random.randint(1, 60)) - #
    wait_time = random.randint(1,60)
    time.sleep(wait_time)