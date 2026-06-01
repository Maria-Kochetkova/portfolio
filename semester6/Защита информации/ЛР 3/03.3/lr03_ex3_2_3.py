import unittest

def extended_gcd(a, b):
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return "GCD <> 1"
    else:
        return x % m

class TestModInverse(unittest.TestCase):
    def test_1(self):
        self.assertEqual(mod_inverse(3, 11), 4)
        self.assertEqual(mod_inverse(5, 12), 5)

    def test_2(self):
        self.assertEqual(mod_inverse(2, 4), "GCD <> 1")
        self.assertEqual(mod_inverse(6, 9), "GCD <> 1")

    def test_3(self):
        self.assertEqual(mod_inverse(3425673427763, 231846), 49037)
        self.assertEqual(mod_inverse(6532329827346, 324784327), 172932012)

if __name__ == "__main__":
    # a = 123456789
    # m = 91827364564
    # print(mod_inverse(a, m))

    unittest.main()

