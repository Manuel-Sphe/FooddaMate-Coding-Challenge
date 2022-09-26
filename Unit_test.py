import unittest
from Expession import Expression
from Equation import Equation
import Solution

class TestStringMethods(unittest.TestCase):

    def test_expand(self):
        ex = Expression('2(2x+3)+2(3x-3)',"40")
        self.assertEqual(ex.Expand(["+2(2x+3)","+2(3x-3)"]), ['+4x+6','+6x-6'])

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

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
