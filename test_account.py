from account import *


class Test:
    def setup_method(self):
        self.a1 = Account('John')
        self.a2 = Account('Juan')

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init(self):
        assert self.a1.get_name() == 'John'
        assert self.a1.get_balance() == 0
        assert self.a2.get_name() == 'Juan'
        assert self.a2.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(50) is True
        assert self.a1.get_balance() == 50

        assert self.a1.deposit(-50) is False
        assert self.a1.get_balance() == 50

        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 50

        assert self.a2.deposit(100.50) is True
        assert self.a2.get_balance() == 100.50

        assert self.a2.deposit(-80) is False
        assert self.a2.get_balance() == 100.50

        assert self.a2.deposit(0) is False
        assert self.a2.get_balance() == 100.50

    def test_withdraw(self):
        assert self.a1.deposit(50) is True  # Setup for some cases to be true
        assert self.a1.get_balance() == 50

        assert self.a2.deposit(100.50) is True
        assert self.a2.get_balance() == 100.50

        assert self.a1.withdraw(25) is True
        assert self.a1.get_balance() == 25

        assert self.a1.withdraw(-5) is False
        assert self.a1.get_balance() == 25

        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == 25

        assert self.a1.withdraw(65) is False
        assert self.a1.get_balance() == 25

        assert self.a2.withdraw(10.50) is True
        assert self.a2.get_balance() == 90

        assert self.a2.withdraw(-18) is False
        assert self.a2.get_balance() == 90

        assert self.a2.withdraw(0) is False
        assert self.a2.get_balance() == 90

        assert self.a2.withdraw(140) is False
        assert self.a2.get_balance() == 90
