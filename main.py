from machine_RAM import *

input = [2,1,4]

programme = [
'ADD(0,I1,R0)',
'JUMP(2)',
'ADD(0,0,R1)',
'ADD(0,0,R1)',
'JL(R0,I2,1)',
'JUMP(2)',
'ADD(R0,1,R0)',
'JUMP(-2)',
'ADD(0,1,O0)',
'ADD(R0,0,O1)',
]

ram = Machine(programme, input)

ram.calcule()
