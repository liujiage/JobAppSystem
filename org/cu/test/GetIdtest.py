import unittest

from org.cu.common.ToolsCommon import getId


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print(getId("test-"))


if __name__ == '__main__':
    unittest.main()
