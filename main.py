from machine_RAM import *

input = [1,1]

programme = [
'ADD(0,1,O0)',
'ADD(I1,I1,O1)',
]

ram = Machine(programme, input)

ram.calcule()
