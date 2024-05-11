class Account:
    def __init__(self, acc_no, acc_passwd):
        self.acc_no = acc_no
        self.__acc_passwd = acc_passwd  # private member

    def reset_password(self):
        print(self.__acc_passwd)


account1 = Account("1", "john@010")
print(account1.acc_no, account1.reset_password())
