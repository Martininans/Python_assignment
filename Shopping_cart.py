class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class ShoppingCart:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.products = [None] * self.INITIAL_CAPACITY
        self.quantities = [0] * self.INITIAL_CAPACITY
        self.size = 0

    def resize_arrays(self):
        new_capacity = len(self.products) * 2
        new_products = [None] * new_capacity
        new_quantities = [0] * new_capacity
        for i in range(self.size):
            new_products[i] = self.products[i]
            new_quantities[i] = self.quantities[i]
        self.products = new_products
        self.quantities = new_quantities

    def add_product(self, product, quantity):
        if self.size >= len(self.products):
            self.resize_arrays()
        self.products[self.size] = product
        self.quantities[self.size] = quantity
        self.size += 1

    def calculate_total(self):
        total = 0
        for i in range(self.size):
            total += self.products[i].get_price() * self.quantities[i]
        return total

    def display_invoice(self):
        print("Invoice:")
        total = self.calculate_total()
        discount = 0.1 * total if total > 100 else 0
        vat = 0.075 * total
        total_with_discount = total - discount
        total_with_vat = total_with_discount + vat

        for i in range(self.size):
            print(f"{self.products[i].get_name()}: {self.quantities[i]} x ${self.products[i].get_price():.2f}")
        print(f"Total: ${total:.2f}")
        print(f"Discount (if applicable): ${discount:.2f}")
        print(f"VAT (7.5%): ${vat:.2f}")
        print(f"Total with VAT: ${total_with_vat:.2f}")


def main():
    print("Enter the name and price of the product:")
    name = input()
    price = float(input())

    print("Enter the quantity:")
    quantity = int(input())

    product = Product(name, price)
    cart = ShoppingCart()
    cart.add_product(product, quantity)

    cart.display_invoice()


if __name__ == "__main__":
    main()
