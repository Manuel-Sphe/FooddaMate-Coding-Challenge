from re import findall,sub, search
from typing import List

class Expression:
    #init method or costructor 
    def __init__(self,lhs:str, rhs:str):
        self.lhs = lhs 
        self.rhs = rhs

    def Grouping(self)->str:
        

        # for case where there's a positive leading constant on either side append the '+'
        if self.modify_const(self.lhs) != None:
                self.setLeft(self.modify_const(self.lhs))
        if self.modify_const(self.rhs) != None:
                self.setRight(self.modify_const(self.rhs))

       
        if self.hasParethesis(self.lhs):

            # remove all brackets on the left 
            print('Distribute - left ')
            print(self.lhs, end=" = ")
            var = findall(r'[-+]?[0-9]+\(.+?\)',self.lhs)
            var2= findall(r'[-+]?[0-9]+\(.+?\)',self.lhs)

            lst = self.Expand(var)

            for i in range(len(lst)):
                self.lhs=self.lhs.replace(var2[i],lst[i])
                self.setLeft(self.lhs)
            print(self.lhs)
        
        print() 

        if self.hasParethesis(self.rhs):
            #remove the right
            print('Disribute - right')
            print(self.rhs, end=" = ")
            var = findall(r'[-+]?[0-9]+\(.+?\)',self.rhs)
            var2= findall(r'[-+]?[0-9]+\(.+?\)',self.rhs)

            lst = self.Expand(var)

            for i in range(len(lst)):
                self.rhs=self.rhs.replace(var2[i],lst[i])
                self.setRight(self.rhs)
            print(self.rhs)

        print()
        print(self.lhs,self.rhs, sep=' = ')


        unkwon_vars_left = findall(r"[-+]?[0-9]*x",self.lhs) # find list with pattern
        unkwon_vars_right = findall(r"[-+]?[0-9]*x",self.rhs)

        consts_lelf =  sub(r"[-+]?[0-9]*x","",self.lhs) # replace 
     
        consts_right = sub(r"[-+]?[0-9]*x","",self.rhs) # replace 


        self.modify(unkwon_vars_left)
        self.modify(unkwon_vars_right)

        # after the modify we call expan if there are brackets

        left_coef = "".join(unkwon_vars_left)
        right_coef = "".join(unkwon_vars_right)

        print(right_coef)
        
        print(left_coef+" "+consts_lelf+ " = "+right_coef+" "+consts_right)
 
        try:
            # e.g 3x+2x-3x = 10x+4
            if consts_lelf == "":
                self.setLeft(str(eval(left_coef.replace("x","")))+"x")
                
            else:
                self.setLeft(str(eval(left_coef.replace("x","")))+"x"+self.digits_toString(consts_lelf))
            if consts_right =="":
                self.setRight(str(eval(right_coef.replace("x","")))+"x")
            else:
                self.setRight(str(eval(right_coef.replace("x","")))+"x"+self.digits_toString(consts_right))
            
            
                
        except SyntaxError:
            pass
    
        self.toString()

        return self.getLeft()+"="+self.getRight()

    def digits_toString(self,value:str)->str:
        try:
            if eval(value)>=0:
                return "+"+str(eval(value))
            return str(eval(value))
        except TypeError:
            pass
        

    
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

    def modify_const(self,side:str):
        try:
            if eval(side[0])>0 and side.index('x')!=-1:
                side = "+"+side 
                return side
            return side
        except SyntaxError:
            pass
        except NameError:
            pass
        except ValueError:
            pass

    def hasParethesis(self,expression:str)->bool:
        print("The value to test",expression)
        try:
         
            if expression.index(')')!=-1 and expression.index('(')!=-1:
                return True
        except ValueError:
            return False
        except AttributeError:
            pass

    def getSign(self,string:str)->int:
        for index,item in enumerate(string):
            if item =='-' or item =='+' and index>0:
                return index

    def Expand(self,exp:List[str])->List[str]:
        
        for index,item in enumerate(exp):
            
            lst = search(r'[-+]?[0-9]+',item) #get the x coffients
            lst = lst.group()

           
            # the costanst if any 

            x_coeff = search(r'[-+]?[0-9]*x',item) 
            x_coeff=x_coeff.group()

            # the case when is () has no leading number
            if x_coeff=="-x":
                x_coeff ="-1x"

            elif x_coeff=="x":
                x_coeff="+1x"


            x_coeff=x_coeff.replace('x','')
            # get the constant 
            try:
                
                
                try:
                    const = item[item.index('x')+1:item.index(')')]
                    ans1 = eval(const)
                except SyntaxError:
                    const = item[item.index('(')+1:self.getSign(item)]
                    ans1 = eval(const)
          

                ans = eval(lst)*eval(x_coeff)
                if ans >0 :
                    ans ="+"+str(ans)
                
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
        return exp
