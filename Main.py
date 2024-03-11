from Calculadora import Calculadora

class Main:
    clc = Calculadora()
    print("suma: ",clc.suma(2,-3,5)) #4
    print("resta: ",clc.resta(3,2, -3)) #4
    print("multiplicación: ",clc.mult(3,2,0.4)) #2,4
    print("División: ",clc.div(10, -2, 4)) #-1.25
