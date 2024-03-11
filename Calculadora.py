class Calculadora:
    def suma(self, num):
        ans = num[0]
        for x in num[1:]:
            ans+=x
        return ans
    
    def resta(self, num):
        ans = num[0]
        for x in num[1:]:
            ans-=x
        return ans
    
    def mult(self, num):
        ans = num[0]
        for x in num[1:]:
            ans*=x
        return ans
    
    def div(self, num):
        ans = num[0]
        for x in num[1:]:
            if x == 0:
                print("No se puede realizar la division")
                return 
            ans/=x
        return ans    
    
    def solicitarNums(self):
        nums = []
        cant = int(input("Cuantos ingrese cuantos numeros desea operar: "))
        for x in range(cant):
            nums.append(int(input(f"Num {x+1}: ")))
        return nums