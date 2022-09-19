
from re import findall,sub

from typing import List

class Expression:
    def __init__(self,a1:float ,a2:float ,b1:float , b2:float):
        """
            ax+b is an expression
            a1x + b1 = a2x + b2
            (a1-a2)x = b2-b1 - perfomr a swap
            x = (b2-b1)/(a1-a2)
        """
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2

        def swap(self)->None:
            pass

class Equation:
    #init method or costructor 
    def __init__(self,lhs:str, rhs:str):
        self.lhs = lhs 
        self.rhs = rhs

    def Grouping(self)->None:
        print("Grouping!!!")
        
        unkwon_vars_left = findall("[-+]?[0-9]*x",self.lhs) # find list with pattern
        unkwon_vars_right = findall("[-+]?[0-9]*x",self.rhs)

        consts_lelf =  sub("[-+]?[0-9]*x","",self.lhs) # replace 
        consts_right = sub("[-+]?[0-9]*x","",self.rhs) # replace 

        self.modify(unkwon_vars_left)
        self.modify(unkwon_vars_right)

        left_coef = "".join(unkwon_vars_left)
        right_coef = "".join(unkwon_vars_right)
        
        print(left_coef+" "+consts_lelf+ " = "+right_coef+" "+consts_right)
        
        try:
            self.setLeft(str(eval(left_coef.replace("x","")))+"x"+self.digits_toString(consts_lelf))
            self.setRight(str(eval(right_coef.replace("x","")))+"x"+self.digits_toString(consts_right))
        except SyntaxError:
            pass
    
        self.toString()

    def digits_toString(self,val:str)->str:
        if eval(val)>=0:
            return "+"+str(eval(val))
        return str(eval(val))
    
    def setLeft(self,newVal:str)->None:
        self.lhs = newVal

    def setRight(self,newVal:str)->None:
        self.rhs = newVal

    def toString(self)->None:
        print("Simplify")
        a1 = findall("[-+][0-9]+",self.lhs)
        a2 = findall('[-+][0-9]+',self.rhs)
       
       
        print(self.lhs+" = "+self.rhs)

        
       

    def modify(self,arr:List[str])->List[str]:
        """
         This method handle the case where there an +x and -x
        """
        for i,val in enumerate(arr):
            if val=="+x":
                arr[i] = "+1x"
            elif val=="-x":
                arr[i]="-1x"
        return arr





#eq = input("Enter a linear equation:\n")
eq = "7x-3=5"

eq = eq.replace(" ","")

sides = eq.split("=")

lhs ,rhs= sides[0], sides[1]

object = Equation(lhs,rhs)

object.Grouping()





#print(unkwon_vars)
