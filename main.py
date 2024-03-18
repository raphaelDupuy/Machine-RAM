from machine_RAM import *

input = 'OUI'

programme = [
'JE(R0,4,4)',
'ADD(R0,1,R1)',
'ADD(R1,1,R0)',
'JUMP(-3)',
'ADD(0,1,O0)',
'ADD(0,R0,O1)',
]

ram = machine(programme, input)

print(ram)
