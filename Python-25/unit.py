
import unittest
from bank import BankAccount
from shoppingCart import ShoppingCart


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.person1 = BankAccount("John", 2000)

    def test_get_balance(self):
       self.assertEqual(self.person1.get_balance(), 2000)

    def test_deposit(self):
        self.person1.deposit(500)
        self.assertEqual(self.person1.get_balance(), 2500)

        # with self.assertRaises(ValueError) as context:
        #     self.person1.balance()
        #
        # self.assertEqual(str(context.exception), "Balance cannot be less than 0.")

    def test_withdraw(self):
        self.person1.withdraw(500)
        self.assertEqual(self.person1.get_balance(), 1500)



class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.shoppingCart1 = ShoppingCart()

    def test_is_empty(self):
        self.assertEqual(self.shoppingCart1.is_empty(), True)

    def test_add_item(self):
        self.shoppingCart1.add_item("apple", 500, 20)
        self.assertEqual(self.shoppingCart1.items, [{'name': "apple", 'price': 500, 'quantity':  20}])

    def test_remove_item(self):
        self.shoppingCart1.remove_item("apple")
        self.assertEqual(self.shoppingCart1.items, [])

    def test_total_price(self):
        self.shoppingCart1.add_item("apple", 500, 20)
        self.assertEqual(self.shoppingCart1.total_price(), 10000)