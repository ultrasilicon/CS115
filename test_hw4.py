"""
 I pledge my honor that I have abided by the Stevens Honor System
 
 By Tim Zheng 
 04 Oct 2017
"""

import unittest
import hw4


class Test(unittest.TestCase):
    def test01(self):
        self.assertEqual(hw4.pascal_row(0), [1])

    def test02(self):
        self.assertEqual(hw4.pascal_row(1), [1,1])

    def test03(self):
        self.assertEqual(hw4.pascal_row(5), [1, 5, 10, 10, 5, 1])

    def test04(self):
        self.assertEqual(hw4.pascal_row(2), [1, 2, 1])

    def test05(self):
        self.assertEqual(hw4.pascal_row(10), [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1])

    def test06(self):
        self.assertEqual(hw4.pascal_triangle(0), [[1]])

    def test07(self):
        self.assertEqual(hw4.pascal_triangle(1), [[1], [1, 1]])

    def test08(self):
        self.assertEqual(hw4.pascal_triangle(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])

    def test09(self):
        self.assertEqual(hw4.pascal_triangle(2), [[1], [1, 1], [1, 2, 1]])

    def test10(self):
        self.assertEqual(hw4.pascal_triangle(3), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])


if __name__ == "__main__":
    unittest.main()
