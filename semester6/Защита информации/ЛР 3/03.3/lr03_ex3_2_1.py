# import unittest

def mod_exp(a, x, m):
    if m == 1:
        return 0
    elif x < 0:
        return "not"
    elif x == 0:
        return 1

    res = 1
    a = a % m
    c = a

    n = bin(x)[3:]
    while len(n) > 0:
        c = (c * c) % m

        if n[0] == '1':
            c = (c * a) % m
        n = n[1:]
    res = c

    return res

# class TestModExp(unittest.TestCase):
#     def test_1(self):
#         self.assertEqual(mod_exp(2332, -1633, 1342), "not")
#
#     def test_2(self):
#         self.assertEqual(mod_exp(5, 0, 7), 1)
#         self.assertEqual(mod_exp(0, 100, 10), 0)
#         self.assertEqual(mod_exp(10, -10, 1), 0)
#
#     def test_3(self):
#         self.assertEqual(mod_exp(147843136, 8512446241, 673634), 483170)
#         self.assertEqual(mod_exp(12343254849737832783, 2456348436238727843278, 14567483923672334287), 2891686914374584124)

if __name__ == "__main__":
    a = 5
    b = 0
    m = 7
    print(mod_exp(a, b, m))

    # unittest.main()
