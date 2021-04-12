import unittest

class PaymentTest(unittest.TestCase):
    def test_paymentindollar(self):
        print("this is payment in dollar test")
        self.assertTrue(True)

    def test_paymentintaka(self):
        print("this is payment in taka test")
        self.assertTrue(True)



if __name__ == "__main__":
    unittest.main()