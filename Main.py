from Calculadora import Calculadora

class Main:
    clc = Calculadora()
    num = clc.solicitarNums()
    print("suma: ",clc.suma(num)) #4
    print("resta: ",clc.resta(num)) #4
    print("multiplicación: ",clc.mult(num)) #2,4
    print("División: ",clc.div(num)) #-1.25
