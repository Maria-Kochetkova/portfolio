# import unittest

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

# class TestGCD(unittest.TestCase):
#     def test_1(self):
#         self.assertEqual(gcd(0, 7), 7)
#         self.assertEqual(gcd(0, 0), 0)
#         self.assertEqual(gcd(1, 1), 1)
#
#     def test_2(self):
#         self.assertEqual(gcd(-14, 21), 7)
#         self.assertEqual(gcd(14, -21), 7)
#         self.assertEqual(gcd(-14, -21), 7)
#
#     def test_3(self):
#         self.assertEqual(gcd(14, 14), 14)
#         self.assertEqual(gcd(-7, -7), 7)
#
#     def test_4(self):
#         self.assertEqual(gcd(123456789, 987654321), 9)


if __name__ == "__main__":
    a = 467045676745674556774458358390
    b = 64626327832578457652645267
    print(gcd(a, b))

    # unittest.main()
