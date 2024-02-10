from Read_file import Read_file
from IN_OUT import IN_OUT

class Card:
    def __init__(self, acc):
        self.item = Read_file()
        self.IO = IN_OUT
        self.nam = acc
        self.title = 0
        self.card = {}
    
    def view_card(self):
        for i, (phone, pq) in enumerate(self.card.items(), 1):
            self.IO.set_message(f"{i}.{phone} {pq}")

    def title_price(self):
        for _,it in self.card.items():
            price = list(it.items())
            price = int(list(price[0])[1])
            self.title += price
        self.IO.set_message(f"The Title of price is {self.title}")
    
    def Clear_elements(self):
        self.card.clear()

    def Clear_element(self, all=False, phone=""):
        if all:
            self.Clear_elements()
        else:
            self.card.pop(phone)
    