
from re import findall,sub

from typing import List

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
        

       
        self.setLeft(str(eval(left_coef.replace("x","")))+"x"+self.digits_toString(consts_lelf))
        self.setRight(str(eval(right_coef.replace("x","")))+"x"+self.digits_toString(consts_right))
    
        self.toString()

    def digits_toString(self,val:str)->str:
        if eval(val)>=0:
            return "+"+str(eval(val))
        return str(eval(val))
    
    def setLeft(self,newVal:str)->None:
        self.lhs = newVal

    def setRight(self,newVal:str)->None:
        self.rhs = newVal

    def toString(self):
        print("Simplify")
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
eq = "7x-3 +5x + 2x -x+7+3-4-9+10-25x  = 3x - 5 +2x+3"

eq = eq.replace(" ","")

sides = eq.split("=")

lhs ,rhs= sides[0], sides[1]

object = Equation(lhs,rhs)

object.Grouping()





#print(unkwon_vars)