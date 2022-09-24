from hashlib import new
from re import findall,sub, search
from typing import List

class Expression:
    #init method or costructor 
    def __init__(self,lhs:str, rhs:str):
        self.lhs = lhs 
        self.rhs = rhs

    def Grouping(self)->None:
        print("Grouping!!!")
        
        unkwon_vars_left = findall(r"[-+]?[0-9]*x",self.lhs) # find list with pattern
        unkwon_vars_right = findall(r"[-+]?[0-9]*x",self.rhs)

        consts_lelf =  sub(r"[-+]?[0-9]*x","",self.lhs) # replace 
        consts_right = sub(r"[-+]?[0-9]*x","",self.rhs) # replace 

        self.modify(unkwon_vars_left)
        print(unkwon_vars_left)

        self.modify(unkwon_vars_right)

        # after the modify we call expan if there are brackets

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

    
    # Setters
    def setLeft(self,newVal:str)->None:
        self.lhs = newVal

    def setRight(self,newVal:str)->None:
        self.rhs = newVal

    # Getters 
    def getLeft(self)->str:
        return self.lhs

    def getRight(self)->str:
        return self.rhs


    def toString(self)->None:
        print("Simplify")
        print(self.getLeft()+" = "+self.getRight())

        
    def modify(self,arr:List[str])->List[str]:
        """
         This method handle the case where there an +x and -x
        """
        for i,val in enumerate(arr):
            if val=="+x" or val=="x":
                arr[i] = "+1x"
            elif val=="-x":
                arr[i]="-1x"
        return arr


class Equation:
    def __init__(self,exp:Expression, a1:int ,b1:int ,a2:int , b2:int):
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
        self.exp = exp



    # Case 1 ax + b  = c
    def Eliminiate(self)->None:

        """
            Remove the constant factor 
        """
        if self.b1 < 0:
            print(f'Add {abs(self.b1)} to both sides')
            lft = f'{self.exp.getLeft()}+ {abs(self.b1)} = '
            rht = f'{self.exp.getRight()} + {abs(self.b1)}'
            print(lft+rht)
            print("Simplify")
            print(f'{self.a1}x = {self.b2+abs(self.b1)}')

        elif self.b1 >0:
            print(f'Subtract {self.b1} from both sides')
            lft = f'{self.exp.getLeft()} - {self.b1}'
            rht = f'{self.exp.getRight()} - {self.b1}'

            print(lft+" = "+rht)
            

            
            if self.a2>0:

                lft = f'{self.a1}x'
                if (self.b2-self.b1>0):
                    rht = f'{self.a2}x + {self.b2-self.b1}'
                elif (self.b2-self.b1):
                    rht = f'{self.a2}x {self.b2- self.b1}'

                else:
                    rht = f'{self.a2}x'
                self.exp.setLeft(lft)
                self.exp.setRight(rht)

                self.set_b2(self.b2-self.b1)
                self.set_a1(self.a2-self.b1)
                print(f"Subtract {self.a2}x from both sides")
                print(f'{self.exp.getLeft()} - {self.a2}x = {self.exp.getRight()} - {self.a2}x')
                print('Simplify')
                print(f'{self.a1}x = {self.b2}')
                print(f'divide both sides by {self.a1}')
                print(f'x = {self.b2}/{self.a1}')

                
            elif self.a2<0:
                print(f'Add {self.a2}x to both sides')
                print("Simplify")
                print(f'{self.exp.getLeft()}')
    
    def set_a1(self, new_b:int)->None:
        self.a1 = new_b

    def set_b2(self, new_b:int):
        self.b2 = new_b
    
        
expression = Expression("7x-3+2(x+4)","4x-3+5")


#equ = Equation(expression,7,1,4,2)

#qu.Eliminiate()

exp = "2(44x+3)+6=24-4x-339(3x-2)"
var = findall(r'[-+]?[0-9]+\(.+?\)',exp)

print(var)

#a1x+b1 = a2x + b2 

   
def Expand(exp:List[str])->List[str]:
    print("Expand")
    for index,item in enumerate(exp):
        lst = search(r'[-+]?[0-9]+',item) #get the x coffients
        lst = lst.group()

        # the costanst if any 
        x_coeff = search(r'[-+]?[0-9]+x',item)
        x_coeff=x_coeff.group().replace('x','')

        # get the constant 
        try:
            const = item[item.index('x')+1:item.index(')')]
            ans1 = eval(const)
            
            ans = eval(lst)*eval(x_coeff)

         
            if ans1>0:
                if eval(lst)>0:
                    exp[index] = f'{ans}x+{ans1*eval(lst)}' 
                elif eval(lst) <0:
                    exp[index] = f'{ans}x{ans1*eval(lst)}'
            elif ans1<0:
                if eval(lst)>0:
                    exp[index] = f'{ans}x{ans1*eval(lst)}' 
                elif eval(lst) <0:
                    exp[index] = f'{ans}x+{ans1*eval(lst)}'

           

        except ValueError:
            pass
    print(exp)
    return exp

lst = Expand(var)


    







#print(unkwon_vars)
