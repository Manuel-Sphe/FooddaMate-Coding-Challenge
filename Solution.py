
from re import findall,sub

from typing import List

class Expression:
    def __init__(self,a1:int ,b1:int ,a2:int , b2:int):
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


      # Case 1 ax + b  = c
    def Eliminiate(self)->None:

        """
            Remove the constant factor 
        """
        if self.b1 < 0:
            print(f'Add {abs(self.b1)} to both sides')
            lft = f'{self.a1}x - {abs(self.b1)} + {abs(self.b1)} = '
            rht = f'{self.b2} + {abs(self.b1)}'
            print(lft+rht)
            print("Simplify")
            print(f'{self.a1}x = {self.b2+abs(self.b1)}')

        elif self.b1 >0:
            print(f'Subtract {self.b1} from both sides')
            lft = f'{self.a1}x + {self.b1} - {self.b1} = '
            rht = f'{self.b2} - {self.b1}'
            print(lft+rht)
            print("Simplify")
            print(f'{self.a1}x = {self.b2-self.b1}')

        

            

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

    def toString(self):
        print("Simplify")
        a1 = findall("[-+][0-9]+",self.lhs)
        a2 = findall('[-+][0-9]+',self.rhs)

        print(self.lhs.split("x"))
       
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


eq1 = Expression(7,-3,0,5)
eq1.Eliminiate()






#print(unkwon_vars)
