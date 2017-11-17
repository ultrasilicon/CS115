'''
Created on April 13, 2016
Last modified on April 13, 2016

@author: Brian Borowski

CS115 - Quadratic Equation Test Script
'''
import unittest
from quadratic import QuadraticEquation

class Test(unittest.TestCase):

    def test01(self):
        try:
            QuadraticEquation(0, 0, 0)
            self.fail('The constructor should have raised a ValueError when a is 0.')
        except ValueError as error:
            self.assertEqual(str(error), 'Coefficient \'a\' cannot be 0 in a quadratic equation.')

    def test02(self):
        qe = QuadraticEquation(1.0, 1.0, 1.0)
        self.assertAlmostEqual(qe.a, 1.0)
        self.assertAlmostEqual(qe.b, 1.0)
        self.assertAlmostEqual(qe.c, 1.0)
        self.assertEqual(str(qe), 'x^2 + x + 1.0 = 0')
        self.assertAlmostEqual(qe.discriminant(), -3.0)
        self.assertEqual(qe.root1(), None)
        self.assertEqual(qe.root2(), None)

    def test03(self):
        qe = QuadraticEquation(9.0, -1, 81.0)
        self.assertAlmostEqual(qe.a, 9.0)
        self.assertAlmostEqual(qe.b, -1.0)
        self.assertAlmostEqual(qe.c, 81.0)
        self.assertEqual(str(qe), '9.0x^2 - x + 81.0 = 0')
        self.assertAlmostEqual(qe.discriminant(), -2915.0)
        self.assertEqual(qe.root1(), None)
        self.assertEqual(qe.root2(), None)

    def test04(self):
        qe = QuadraticEquation(1.0, 2.0, 0.0)
        self.assertAlmostEqual(qe.a, 1.0)
        self.assertAlmostEqual(qe.b, 2.0)
        self.assertAlmostEqual(qe.c, 0.0)
        self.assertEqual(str(qe), 'x^2 + 2.0x = 0')
        self.assertAlmostEqual(qe.discriminant(), 4.0)
        self.assertEqual(qe.root1(), 0.0)
        self.assertEqual(qe.root2(), -2.0)

    def test05(self):
        qe = QuadraticEquation(1.0, 0.0, -25)
        self.assertAlmostEqual(qe.a, 1.0)
        self.assertAlmostEqual(qe.b, 0.0)
        self.assertAlmostEqual(qe.c, -25.0)
        self.assertEqual(str(qe), 'x^2 - 25.0 = 0')
        self.assertAlmostEqual(qe.discriminant(), 100.0)
        self.assertEqual(qe.root1(), 5.0)
        self.assertEqual(qe.root2(), -5.0)

    def test06(self):
        qe = QuadraticEquation(1.0, -5.0, 6)
        self.assertAlmostEqual(qe.a, 1.0)
        self.assertAlmostEqual(qe.b, -5.0)
        self.assertAlmostEqual(qe.c, 6)
        self.assertEqual(str(qe), 'x^2 - 5.0x + 6.0 = 0')
        self.assertAlmostEqual(qe.discriminant(), 1.0)
        self.assertEqual(qe.root1(), 3.0)
        self.assertEqual(qe.root2(), 2.0)

    def test07(self):
        qe = QuadraticEquation(-1.0, -5.0, -6)
        self.assertAlmostEqual(qe.a, -1.0)
        self.assertAlmostEqual(qe.b, -5.0)
        self.assertAlmostEqual(qe.c, -6.0)
        self.assertEqual(str(qe), '-x^2 - 5.0x - 6.0 = 0')
        self.assertAlmostEqual(qe.discriminant(), 1.0)
        self.assertEqual(qe.root1(), -3.0)
        self.assertEqual(qe.root2(), -2.0)

    def test08(self):
        qe = QuadraticEquation(1, 0, 0)
        self.assertAlmostEqual(qe.a, 1.0)
        self.assertAlmostEqual(qe.b, 0.0)
        self.assertAlmostEqual(qe.c, 0.0)
        self.assertEqual(str(qe), 'x^2 = 0')
        self.assertAlmostEqual(qe.discriminant(), 0.0)
        self.assertEqual(qe.root1(), 0.0)
        self.assertEqual(qe.root2(), 0.0)

    def test09(self):
        qe = QuadraticEquation(1.3, 2.3, 5.6)
        self.assertAlmostEqual(qe.a, 1.3)
        self.assertAlmostEqual(qe.b, 2.3)
        self.assertAlmostEqual(qe.c, 5.6)
        self.assertEqual(str(qe), '1.3x^2 + 2.3x + 5.6 = 0')
        self.assertAlmostEqual(qe.discriminant(), -23.83)
        self.assertEqual(qe.root1(), None)
        self.assertEqual(qe.root2(), None)

    def test10(self):
        qe = QuadraticEquation(0.25, 4, 8)
        self.assertAlmostEqual(qe.a, 0.25)
        self.assertAlmostEqual(qe.b, 4)
        self.assertAlmostEqual(qe.c, 8)
        self.assertEqual(str(qe), '0.25x^2 + 4.0x + 8.0 = 0')
        self.assertAlmostEqual(qe.discriminant(), 8.0)
        self.assertAlmostEqual(qe.root1(), -2.3431457505076194)
        self.assertAlmostEqual(qe.root2(), -13.65685424949238)

if __name__ == '__main__':
    unittest.main()
