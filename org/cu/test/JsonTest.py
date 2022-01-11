import json
import unittest

from org.cu.entity.Apply import Apply



class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = Apply()
        a.createDate = "01/01/21"
        a.applyId = 1
        print(a.toJSON())

    def test_2(self):
        print("do some thing1.....")

    def test_3(self):
        print("do some thing2.....")

    def test_4(self):
        print("do some thing2.....")

if __name__ == '__main__':
    unittest.main()
