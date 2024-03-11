from Calculadora import Calculadora

class Main:
    clc = Calculadora()
    num = clc.solicitarNums()
    ope = int(input("Que operación desea realizar:\n1-Suma.\t2-Resta. 3-Multiplicación. 4-División\n"))

    operaciones = {
        1: clc.suma(num),
        2: clc.resta(num),
        3: clc.mult(num),
        4: clc.div(num)
    }

    if ope in operaciones:
        print("Respuesta: ", operaciones[ope])
    else:
        print("¡La operación no existe!")
