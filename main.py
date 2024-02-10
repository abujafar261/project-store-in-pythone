from Account import Account
from View import View


def main():
    print("Add Account ...")
    name = input("Enter your name: ")
    phone = input("Enter your phoen: ")
    address = input("Enter your address: ")

    account = Account(name, phone, address)

    v = View(account)
    v.display_main_manu()

if __name__ == '__main__':
    main()