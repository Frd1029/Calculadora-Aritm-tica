class Calculadora:
    def suma(self, *num):
        ans = num[0]
        for x in num[1:]:
            ans+=x
        return ans
    
    def resta(self, *num):
        ans = num[0]
        for x in num[1:]:
            ans-=x
        return ans
    
    def mult(self, *num):
        ans = num[0]
        for x in num[1:]:
            ans*=x
        return ans
    