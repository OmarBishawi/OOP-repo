class store:
    def __init__(self,name):
        self.name = name 
        self.products = []
    def add_product(self,new_product):
        self.products.append(new_product)
    def sell_product(self,id):
        if id>= 0 and id <len(self.products):
            sold_product = self.products.pop(id)
            sold_product.print_info()
        else:
            print("invalid product ID")

    def inflation(self,percent_increase):
        for products in self.products:
            product.update_price(percent_increase, is_increased=True)
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, is_increased=False)


class product:
    def __init__(self,name,price,category):
        self.name=name 
        self.price= price
        self.category=category

    def update_price(self,percent_change,is_increased):
        if is_increased :
            self.price *= (1 + percent_change /100)
        else :
            self.price *=(1 - percent_change / 100)

    def print_info(self):
        print("product name :",self.name)
        print("category:",self.category)
        print("price :",self.price)


store = store("alocado")
product1=product("laptop",1000,"electronics")

store.products.append(product1)
product1.update_price(10,True)
print (product1.price)
product1.update_price(5,False)
print(product1.price)
product1.print_info()
store.add_product(product1)