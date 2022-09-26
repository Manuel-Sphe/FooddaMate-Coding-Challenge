
from Expession import Expression
from Equation import Equation


def Solve(text:str):

    #text = input("Enter Equation to solve\n")
    text = text.replace(' ','')

    ls = text.split('=')
    print(ls)

    expression = Expression(ls[0],ls[1])
    
    equ = expression.Grouping()
    
    print(equ)

    matrix = [0 for i in range(4)]

    #left 
    try:
        if equ[equ.index('x')+1:equ.index('=')]:
            matrix[1]=eval(equ[equ.index('x')+1:equ.index('=')])

        if equ[:equ.index('x')]:
            matrix[0] = eval(equ[:equ.index('x')])

        equ = equ[equ.index("=")+1:]
    
        #right
        if equ[equ.index('x')+1:]:
            matrix[3]=eval(equ[equ.index('x')+1:])

        if equ[:equ.index('x')]:
            matrix[2] = eval(equ[:equ.index('x')])
    except ValueError:
        matrix[3] = eval(equ)
        pass
    except SyntaxError:
        print('special case',equ)
        if equ=="x":
            matrix[2] = 1

        if equ =='-x':
            matrix[2] = -1
        pass

    #print(matrix)
    equ =Equation(expression,matrix[0],matrix[1],matrix[2],matrix[3])
    return equ.Eliminiate()

def main():
    text = input("Enter Equation to solve\n")
    text = text.replace(" ","")
    Solve(text)
if __name__ =="__main__":
    main()




