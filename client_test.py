import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):

    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        # Adding assertions for each quote to check the output of getDataPoint
        self.assertEqual(getDataPoint(quotes[0]), ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2))
        self.assertEqual(getDataPoint(quotes[1]), ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        # Adding assertions for each quote to check the output of getDataPoint
        self.assertEqual(getDataPoint(quotes[0]), ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2))
        self.assertEqual(getDataPoint(quotes[1]), ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2))

    def test_getRatio(self):
        # Testing getRatio with valid prices
        price_a = 120.48
        price_b = 121.68
        expected_ratio = price_a / price_b
        self.assertEqual(getRatio(price_a, price_b), expected_ratio)

    def test_getRatio_divideByZero(self):
        # Testing getRatio where price_b is zero
        price_a = 120.48
        price_b = 0
        self.assertEqual(getRatio(price_a, price_b), float('inf'))

    def test_getRatio_zeroNumerator(self):
        # Testing getRatio where price_a is zero
        price_a = 0
        price_b = 121.68
        expected_ratio = 0 / price_b
        self.assertEqual(getRatio(price_a, price_b), expected_ratio)


if __name__ == '__main__':
    unittest.main()
