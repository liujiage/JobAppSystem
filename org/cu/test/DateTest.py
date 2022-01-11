import time
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print(time.strftime("%m/%d/%y", time.localtime()))


if __name__ == '__main__':
    unittest.main()
