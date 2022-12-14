import unittest
from Expession import Expression
from Equation import Equation
import Solution

class TestStringMethods(unittest.TestCase):

    def test_modify(self):
        ex  = Expression('','')
        self.assertEqual(ex.modify(['+x','3x']),['+1x','3x'])
        self.assertEqual(ex.modify(['-x','6x','+x']),['-1x','6x','+1x'])

    def test_modifyConst(self):
        ex = Expression('','')
        self.assertEqual(ex.modify_const('4+x'),'+4+x')
        
    def test_expand(self):
        ex = Expression('2(2x+3)+2(3x-3)',"40")
        self.assertEqual(ex.Expand(["+2(2x+3)","+2(3x-3)"]), ['+4x+6','+6x-6'])

    def test_getSign(self):
        ex = Expression('2x+3','3x-1')
        self.assertTrue(ex.getSign(ex.getLeft())==2)

        
    def test_hasParentessis(self):
        ex = Expression('2(x+3)','4x+3')
        self.assertTrue(ex.hasParethesis(ex.getLeft()))
        self.assertFalse(ex.hasParethesis(ex.getRight()))


    def test_parethesis(self):
        ex = Expression('7x-5','2')
        self.assertTrue(ex.hasParethesis('2(2-x)'))
        self.assertFalse(ex.hasParethesis(ex.getLeft()))
        self.assertEqual(ex.getLeft(),'7x-5')


    def test_solve(self):
        s = '7x-5=2'
        sp = Solution.Solve(s)
        self.assertEqual(sp, 'x=1.00')
        self.assertEqual(s.split('='),['7x-5','2'])

        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
