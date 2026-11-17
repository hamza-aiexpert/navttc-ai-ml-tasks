# Task 27 - User defined exception handling in Python

# 1. Simple custom exception
class NegativeNumberError(Exception):
    """Raised when a negative number is supplied."""
    pass

def square_root(n):
    if n < 0:
        raise NegativeNumberError("cannot take the square root of a negative number")
    return n ** 0.5

try:
    print(square_root(16))
    print(square_root(-4))
except NegativeNumberError as e:
    print("Caught NegativeNumberError:", e)

# 2. Custom exception with extra data
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Balance {balance} is less than requested amount {amount}")

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

acct = BankAccount(1000)
for amt in (300, 900):
    try:
        print("Withdrew", amt, "-> balance", acct.withdraw(amt))
    except InsufficientFundsError as e:
        print("Error:", e, "| short by", e.amount - e.balance)

# 3. Exception hierarchy
class ValidationError(Exception):
    pass
class AgeError(ValidationError):
    pass
class EmailError(ValidationError):
    pass

def validate(age, email):
    if not 0 < age < 120:
        raise AgeError(f"invalid age {age}")
    if "@" not in email:
        raise EmailError(f"invalid email {email!r}")
    return True

for a, e in [(25, "ali@example.com"), (150, "x@y.com"), (30, "nomail")]:
    try:
        print("valid:", validate(a, e))
    except AgeError as err:
        print("AgeError ->", err)
    except ValidationError as err:      # catches EmailError via the base class
        print("ValidationError ->", type(err).__name__, err)

# 4. Re-raising and exception chaining
try:
    try:
        int("xyz")
    except ValueError as e:
        raise ValidationError("could not parse input") from e
except ValidationError as e:
    print("Chained:", e, "| caused by:", repr(e.__cause__))
