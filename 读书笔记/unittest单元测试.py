"""
unittest单元测试 - 

Author: kayotin
Date 2024/2/14
"""

import unittest


class TestAddition(unittest.TestCase):
    def test_add(self):
        # 测试相等
        # self.assertEqual(2 + 3, 6)
        # 测试是否为True
        self.assertTrue(2+3 == 6)


if __name__ == "__main__":
    unittest.main()
