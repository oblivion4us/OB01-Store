class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.catalog = {}

    def add_newitem(self, item_name, price):
        self.catalog[item_name] = price
        print(f"Товар {item_name} добавлен в {self.name}")

    def delete_item(self, item_name):
        if item_name in self.catalog:
            del self.catalog[item_name]
        print(f"Товар {item_name} удален из {self.name}")

    def check_price(self, item_name):
        return self.catalog.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.catalog:
            self.catalog[item_name] = new_price
            print(f"Для товара {item_name} обновлена в  {self.name}")
        else:
            print(None)

store1 = Store("Spar", "Ленина 51")
store2 = Store("Дешево", "Карташева 25")
store3 = Store("Авоська", "Черняховского 2")

store1.add_newitem("Кола", 80)
store1.add_newitem("Пельмени", 200)
store1.add_newitem("Сыр", 70)

store1.delete_item("Сыр")
print(store1.check_price("Кола"))
store1.update_price("Пельмени", 220)




