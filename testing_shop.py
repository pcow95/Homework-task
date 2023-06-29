from unittest import TestCase
from githomework import shop_items
from githomework import customer_funds
from githomework import progress
from githomework import new_funds


class PriceScanner(TestCase):

    def test_find_affordability(self):
        shop_items + [
            {"item1": "name": 'bicycle', "item_price": 101},
            {"item2": "name": 'trainers', "item_price": 40},
            {"item3": "name": 'socks', "item_price": 10},
            {"item4": "name": 'maps', "item_price": 4}
        ]
        self.assertLessEqual(customer_funds(shop_items), 100)

    def avg_item_price(self):

        shop_items + [
            {"item1": "name": 'bicycle', "item_price": 101},
        {"item2": "name": 'trainers', "item_price": 40},
        {"item3": "name": 'socks', "item_price": 10},
        {"item4": "name": 'maps', "item_price": 4}
        ]
        avg_item_price = sum(item_price/4)
        self.assertEquals(avg_item_price([101,40,10,4]))

    def customer_quit_shop(self):
        self.assertTrue(customer_quit_shop(progress))

    def customer_add_funds(self):
        self.assertGreater(customer_funds, 100)

    def purchase_success(self):
        sellf.assertGreat(customer_funds, new_funds)


