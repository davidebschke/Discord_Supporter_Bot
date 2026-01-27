import unittest
from main import getGreeting

class MyTestCase(unittest.TestCase):
    def test_getGreeting(self):
        self.assertEqual(getGreeting(), "Hello World!")

   if __name__ == '__main__':
        unittest.main()
