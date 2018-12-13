import unittest

from city_functions import city_country


class CityTestCase(unittest.TestCase):
    """城市和国家的测试用例"""

    def test_city_country(self):
        """处理 Guangxi,China 这样的输入"""
        ret = city_country('guangxi', 'china')
        self.assertEqual(ret, 'Guangxi,China')


if __name__ == '__main__':
    unittest.main()
