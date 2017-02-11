'''
Algoritmo


El algoritmo funciona pidiéndole al computador la hora de la máquina.
Luego lo que se hace es convertir la hora en un string, posteriormente se toman
los números que están después del número decimal que son los que cambian más rápidamente
entonces se obtiemen números aleatorios.
'''

import time as tm

x=str(tm.time()).split(".")[1]

print ('Random number: ',x)
