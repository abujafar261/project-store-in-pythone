class Save_file:
    def __init__(self, account):
        self.path = "C:\\Users\\abuja\\Desktop\\python project\\card.txt"  
        self.name = account
        self.cards ={}

    def save_card(self, add_card):
        with open(self.path, 'w') as f:
            self.cards = {self.name.name : add_card}
            f.writelines(f"{self.cards}")
