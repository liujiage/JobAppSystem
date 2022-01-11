import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        map = dict()
        map["123"] = "v1"
        map["456"] = "v2"
        print(map.values())
        for v in map.values():
            print(v)

    def test_str(self):
        s = "like '%%%s%%'" % "jiage"
        print(s)
