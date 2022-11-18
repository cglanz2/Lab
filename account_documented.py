class Account:
    def __init__(self, name):
        """
        Creating two private variables for account name
        and account balance
        :param name:
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> float:
        """
        Function for depositing positive nonzero numbers
        into the account balance
        :param amount:
        :return:
        """
        if amount > 0:
            self.__account_balance = self.__account_balance + amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> float:
        """
        Function for withdrawing positive nonzero number
        from the account balance. Will not allow withdraw
        amounts larger than the account balance
        :param amount:
        :return:
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance = self.__account_balance - amount
            return True

    def get_balance(self):
        """
        Returns the account balance
        :return:
        """
        return self.__account_balance

    def get_name(self):
        """
        Returns the account name
        :return:
        """
        return self.__account_name
