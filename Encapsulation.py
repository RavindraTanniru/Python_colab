class BankAccount:
    def __init__(self, balance):
        self.public_balance = balance        # Public variable
        self._protected_balance = balance    # Protected variable (convention only)
        self.__private_balance = balance     # Private variable (name mangling)

    # Public method
    def deposit(self, amount):
        if amount > 0:
            self.__private_balance += amount

    # Protected method
    def _apply_interest(self):
        self.__private_balance *= 1.05   # 5% interest

    # Private method
    def __deduct_fee(self):
        self.__private_balance -= 10

    # Getter method (safe access to private data)
    def get_balance(self):
        return self.__private_balance


# Object creation
acc = BankAccount(1000)
print(acc.public_balance)        # ✅ Accessible everywhere
print(acc._protected_balance)    # ⚠️ Accessible, but should be treated as internal use
# print(acc.__private_balance)   # ❌ Direct access not allowed

acc.deposit(500)
print(acc.get_balance())         # ✅ Safe access: 1500

