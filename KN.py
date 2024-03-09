class Phone:
    def __init__(self, brand, model, price, quantity_in_stock):
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def display(self):
        return f"{self.brand:<10} {self.model:<20} - Giá: {self.price:<15}VND - Còn hàng: {self.quantity_in_stock:<5}"

    def sell(self, quantity_sold):
        if quantity_sold <= 0:
            print("số lượng không hợp lệ.")
        elif quantity_sold > self.quantity_in_stock:
            print("không đủ hàng trong kho.")
        else:
            self.quantity_in_stock -= quantity_sold
            print(f"đã bán {quantity_sold} chiếc {self.brand} {self.model}.")

class Store:
    def __init__(self):
        self.phones = []

    def add_phone(self, phone):
        for existing_phone in self.phones:
            if existing_phone.brand == phone.brand and existing_phone.model == phone.model:
                existing_phone.quantity_in_stock += phone.quantity_in_stock
                return
        self.phones.append(phone)

    def list_phones(self):
        if not self.phones:
            print("không có trong kho.")
            return

        print("danh sách điện thoại:")
        for phone in self.phones:
            print(phone.display())

    def find_phone_by_brand(self, brand):
        matching_phones = [phone for phone in self.phones if phone.brand == brand]
        if matching_phones:
            print(f"danh sách điện thoại của hãng {brand}:")
            for phone in matching_phones:
                print(phone.display())
        else:
            print(f"không tìm thấy điện thoại của hãng {brand} trong kho.")

    def sell_phone(self):
        if not self.phones:
            print("không có điện thoại trong kho.")
            return

        brand = input("nhập hãng điện thoại cần bán: ")
        matching_phones = [phone for phone in self.phones if phone.brand == brand]
        if matching_phones:
            print("danh sách điện thoại cần bán:")
            for phone in matching_phones:
                print(phone.display())

            phone_index = int(input("chọn số điện thoại để bán (1, 2, ...): ")) - 1

            if 0 <= phone_index < len(matching_phones):
                quantity_sold = int(input("nhập số lượng cần bán: "))
                matching_phones[phone_index].sell(quantity_sold)
            else:
                print("lựa chọn không hợp lệ.")
        else:
            print(f"hông tìm thấy điện thoại của hãng {brand} trong kho.")

def main():
    store = Store()

    while True:
        print("\nQuản Lý Bán Điện Thoại")
        print("1. Thêm điện thoại vào kho")
        print("2. Liệt kê danh sách điện thoại")
        print("3. Bán điện thoại theo hãng")
        print("4. Tìm kiếm điện thoại theo hãng")
        print("5. Thoát")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            brand = input("Nhập hãng điện thoại: ")
            model = input("Nhập model điện thoại: ")
            price = float(input("Nhập giá điện thoại: "))
            quantity = int(input("Nhập số lượng trong kho: "))
            phone = Phone(brand, model, price, quantity)
            store.add_phone(phone)

        elif choice == "2":
            store.list_phones()

        elif choice == "3":
            store.sell_phone()

        elif choice == "4":
            brand = input("Nhập hãng điện thoại cần tìm: ")
            store.find_phone_by_brand(brand)

        elif choice == "5":
            print("Out !")
            break

        else:
            print("Lựa chọn không hợp lệ. thử lại.")

if __name__ == "__main__":
    main()
