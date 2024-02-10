from IN_OUT import IN_OUT
from Card import Card
from Read_file import Read_file
from Save_file import Save_file

class View:
    def __init__(self, acc):
        self.IO = IN_OUT
        self.car = Card(acc)
        self.item = Read_file()
        self.save = Save_file(acc)
        self.chooce = ""
        self.chooc = ""
        self.man_menu = """
    1. View items
    2. View card
    3. Title price
    4. Clear Card
    5. Clear Element
    6. Save in file
    7. Exit
    Enter your choece : """ 
        self.second_menu = """
    1. add Item
    2. return to main menu
    3. view card
    Enter your choece : """ 
   
    def display_main_manu(self):

        while True:
            self.chooce = self.IO.get_message(self.man_menu)

            if self.chooce == '1':
                self.IO.set_message("_"*50)
                self.item.print_list()
                
                self.IO.set_message("_"*50)

                self.chooc = self.IO.get_message(self.second_menu)
                if self.chooc == '1':
                    self.IO.set_message("_"*50)
                    num = int(self.IO.get_message("Enter Number of chooce: "))
                    quantity = int(self.IO.get_message("Enter the quantity: "))
                    self.add_item_in_card(num, quantity)

                elif self.chooc == '2':continue
                elif self.chooc == '3': 
                    self.car.view_card
                    continue
            
            elif self.chooce == '2':
                self.car.view_card()
                continue

            elif self.chooce == '3':
                self.car.title_price()
            
            elif self.chooce == '4': self.car.Clear_element(all=True)

            elif self.chooce == '5': 
                self.car.view_card()
                num = int(self.IO.get_message("Enter the number of Element: "))
                new_list = self.car.card.items()
                for i, (phone, _) in enumerate(new_list, 1):
                    if i == num:
                        self.car.Clear_element(phone=phone)
                        break
            elif self.chooce == '6': 
                self.save.save_card(self.car.card)
                self.IO.set_message("Thank for you Good lock...")
                break

            elif self.chooce == '7':
                break
    
    def add_item_in_card(self,num, quantity):
        new_list = self.item.Items_list.items()

        for i, (phone, pq) in enumerate(new_list, 1):

            if i == num:
                price = list(pq.items())
                old_quantity = list(pq.items())
                new_quantity = int(list(old_quantity)[1][1]) - quantity

                if int(list(old_quantity)[1][1]) >= new_quantity:
                    self.car.card[phone] = {'Price': int(list(price[0])[1])*quantity, 'Quantity': quantity}
                    self.IO.set_message("Added to cart")
                else: self.IO.set_message("The item is not have this quantity")


