class MenuItem:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def update(self, name=None, price=None, stock=None):
        if name:
            self.name = name
        if price is not None:
            self.price = price
        if stock is not None:
            self.stock = stock

    def __str__(self):
        return f"{self.name} - Rp {self.price} - Stok: {self.stock}"

class FoodOrderingSystem:
    def __init__(self):
        self.menu = []
        self.cart = []
        self.order_history = []

    def add_menu_item(self, name, price, stock):
        item_id = len(self.menu) + 1
        new_item = MenuItem(item_id, name, price, stock)
        self.menu.append(new_item)
        print(f"Menu item '{name}' berhasil ditambahkan!")

    def remove_menu_item(self, item_id):
        item = next((item for item in self.menu if item.id == item_id), None)
        if item:
            self.menu.remove(item)
            print(f"Menu item '{item.name}' berhasil dihapus!")
        else:
            print("Item tidak ditemukan!")

    def edit_menu_item(self, item_id):
        item = next((item for item in self.menu if item.id == item_id), None)
        if item:
            print(f"Editing item: {item}")
            name = input("Nama baru (kosongkan untuk tetap sama): ")
            price = input("Harga baru (kosongkan untuk tetap sama): ")
            stock = input("Stok baru (kosongkan untuk tetap sama): ")
            item.update(
                name=name if name else None,
                price=float(price) if price else None,
                stock=int(stock) if stock else None
            )
            print(f"Menu item '{item.name}' berhasil diupdate!")
        else:
            print("Item tidak ditemukan!")

    def show_menu(self):
        print("Menu:")
        for item in self.menu:
            print(f"{item.id}. {item}")

    def add_to_cart(self, item_id, quantity):
        item = next((item for item in self.menu if item.id == item_id), None)
        if item and item.stock >= quantity:
            self.cart.append({'item': item, 'quantity': quantity})
            item.stock -= quantity
            print(f"'{item.name}' x{quantity} telah ditambahkan ke keranjang.")
        else:
            print("Stok tidak cukup atau item tidak ditemukan!")

    def remove_from_cart(self, item_id):
        cart_item = next((cart_item for cart_item in self.cart if cart_item['item'].id == item_id), None)
        if cart_item:
            self.cart.remove(cart_item)
            print(f"Item '{cart_item['item'].name}' telah dihapus dari keranjang.")
        else:
            print("Item tidak ditemukan di keranjang!")

    def calculate_total(self, discount=0):
        total = sum(item['item'].price * item['quantity'] for item in self.cart)
        total_after_discount = total * (1 - discount / 100)
        return total_after_discount

    def checkout(self, discount=0):
        total = self.calculate_total(discount)
        print(f"Total harga (setelah diskon {discount}%): Rp {total}")
        payment = float(input("Masukkan jumlah pembayaran: "))
        if payment >= total:
            change = payment - total
            self.order_history.append({'cart': self.cart, 'total': total, 'payment': payment, 'change': change})
            print(f"Pembayaran berhasil! Kembalian: Rp {change}")
            self.cart = []  # Kosongkan keranjang setelah checkout
        else:
            print("Pembayaran kurang, silakan coba lagi.")

    def show_order_history(self):
        print("Riwayat Pemesanan:")
        for order in self.order_history:
            print(f"Pembayaran: Rp {order['payment']} - Total: Rp {order['total']} - Kembalian: Rp {order['change']}")
            print("Detail pesanan:")
            for item in order['cart']:
                print(f"{item['item'].name} x{item['quantity']} - Rp {item['item'].price * item['quantity']}")

def main():
    system = FoodOrderingSystem()

    while True:
        print("\n1. Kelola Menu")
        print("2. Lihat Menu")
        print("3. Keranjang Belanja")
        print("4. Checkout")
        print("5. Riwayat Pemesanan")
        print("6. Keluar")

        choice = input("Pilih opsi: ")

        if choice == '1':
            print("\n1. Tambah Menu")
            print("2. Hapus Menu")
            print("3. Edit Menu")
            menu_choice = input("Pilih opsi menu: ")

            if menu_choice == '1':
                name = input("Nama makanan: ")
                price = float(input("Harga makanan: "))
                stock = int(input("Stok makanan: "))
                system.add_menu_item(name, price, stock)

            elif menu_choice == '2':
                system.show_menu()
                item_id = int(input("Masukkan ID item yang ingin dihapus: "))
                system.remove_menu_item(item_id)

            elif menu_choice == '3':
                system.show_menu()
                item_id = int(input("Masukkan ID item yang ingin diedit: "))
                system.edit_menu_item(item_id)

        elif choice == '2':
            system.show_menu()

        elif choice == '3':
            system.show_menu()
            item_id = int(input("Masukkan ID item yang ingin ditambahkan ke keranjang: "))
            quantity = int(input("Jumlah item: "))
            system.add_to_cart(item_id, quantity)

        elif choice == '4':
            discount = float(input("Masukkan diskon (%): "))
            system.checkout(discount)

        elif choice == '5':
            system.show_order_history()

        elif choice == '6':
            print("Terima kasih telah menggunakan aplikasi pemesanan makanan.")
            break
        else:
            print("Opsi tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
