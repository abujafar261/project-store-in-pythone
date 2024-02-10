from IN_OUT import IN_OUT

class Read_file:
    def __init__(self):
        self.IO = IN_OUT
        self.file = "C:\\Users\\abuja\\Desktop\\python project\\Items.txt"
        self.Items_list = {}
        
    def print_list(self):
        with open(self.file, 'r') as f:
            self.Items = f.readlines()
    
  
        for item in self.Items:
                items = item.split(",")
                self.Items_list[items[0]] = {items[1]: items[2], items[3]: items[4]}
            
        for i, (phone, pq) in enumerate(self.Items_list.items(), 1):
                    price = list(pq.items())
                    self.IO.set_message(f"{i}. {phone}: {list(price[0])[1]}")
