from Expession import Expression
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
    