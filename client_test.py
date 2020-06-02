import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))
  

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

    

    
    """ ------------ Add more unit tests ------------ REGARDING getRatio function"""
  def test_getRatio_priceb_zero(self):
    price_a=112.2
    price_b=0
    self.assertIsNone(getRatio(price_a, price_b))

  def test_getRatio_pricea_zero(self):
    price_a=0
    price_b=223.3
    self.assertEqual(getRatio(price_a, price_b),0)

  def test_getRatio_greaterThan_1(self):
    price_a=117.38
    price_b=116.505
    self.assertGreater(getRatio(price_a, price_b),1)

  def test_getRatio_lessThan_1(self):
    price_a=114.25
    price_b=115.525
    self.assertLess(getRatio(price_a, price_b),1)


  def test_getRatio_exactly_1(self):
    price_a=223.3
    price_b=223.3
    self.assertEqual(getRatio(price_a, price_b),1)
  

if __name__ == '__main__':
    unittest.main()
