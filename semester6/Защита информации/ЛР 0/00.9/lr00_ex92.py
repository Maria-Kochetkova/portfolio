# import unittest

def Rem_inside(n, m, b):
    return n**m % b

def Rem(n, m, b):
    if m == 0:
        result = 1
    elif b == 0 or b < 0:
        result = "not"
    elif m % 2 == 0 and b > 0:
        result = Rem_inside(n**2 % b, m / 2, b)
    else:
        result = n * Rem_inside(n**2 % b, (m - 1) / 2, b) % b
    return result


# class Tests(unittest.TestCase):
#     def test_1(self):
#         self.assertEqual(Rem(0, 17, 3), 0)
#
#     def test_2(self):
#         self.assertEqual(Rem(5, 0, 2), 1)
#
#     def test_3(self):
#         self.assertEqual(Rem(7, 5, 0), "not")
#
#     def test_4(self):
#         self.assertEqual(Rem(3, 2, -5), "not")
#
#     def test_5(self):
#         self.assertEqual(Rem(9, 2, 4), 1)
#
#     def test_6(self):
#         self.assertEqual(Rem(9, 3, 4), 9)

if __name__ == "__main__":
    n = 9
    m = 3
    b = 4
    print(Rem(n, m, b))

    # unittest.main()
