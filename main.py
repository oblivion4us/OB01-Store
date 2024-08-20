class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.catalog = {}

    def add_newitem(self, item_name, price):
        self.catalog[item_name] = price
        print(f"Товар {item_name} добавлен в {self.name}")

    def delete_item(self, item_name):
        for item_name in self.catalog:
            del self.catalog[item_name]
        print(f"Товар {item_name} удален из {self.name}")

    
