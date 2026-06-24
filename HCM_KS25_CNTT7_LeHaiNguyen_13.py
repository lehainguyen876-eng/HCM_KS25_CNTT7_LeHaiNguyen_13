class InventoryItem:
    def __init__(self, id, name, category, quantity, unit_price, storage_fee):
        self.id = id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.unit_price = unit_price
        self.storage_fee = storage_fee
        self.total_inventory_value = 0.0
        self.inventory_type = ""

        self.calculate_total_value()
        self.classify_stock_status()

    def calculate_total_value(self):
        self.total_inventory_value = self.quantity * self.unit_price + self.storage_fee

    def classify_stock_status(self):
        if self.total_inventory_value < 5000000:
            self.inventory_type = "Thấp"
        elif self.total_inventory_value < 20000000:
            self.inventory_type = "Trung Bình"
        elif self.total_inventory_value < 50000000:
            self.inventory_type = "Cao"
        else:
            self.inventory_type = "Rất cao"

class InventoryManager:
    def __init__(self):
        self.products = []

    def add_item(self):
        id = input("Nhập mã hàng hóa: ").strip()
        if not id:
            print("Mã hàng hóa không được để trống")
            return

        duplicate = False
        for prod in self.products:
            if prod.id == id:
                duplicate = True
                break
        if duplicate:
            print("Mã hàng hóa đã tồn tại trong kho")
            return

        name = input("Nhập tên hàng hóa: ").strip()
        if not name:
            print("Tên hàng hóa không được để trống")
            return

        category = input("Nhập danh mục hàng hóa: ").strip()
        if not category:
            print("Danh mục không được để trống")
            return

        try:
            unit_price = float(input("Nhập giá nhập: "))
            if unit_price < 0:
                print("Đơn giá phải >= 0")
                return

            quantity = int(input("Nhập số lượng tồn kho: "))
            if not (0 <= quantity <= 100000):
                print("Số lượng tồn kho phải là số nguyên từ 0 đến 100000")
                return

            storage_fee = float(input("Nhập chi phí lưu kho: "))
            if storage_fee < 0:
                print("Chi phí lưu kho phải >= 0")
                return
        except ValueError:
            print("Dữ liệu nhập vào không hợp lệ")
            return

        new_item = InventoryItem(id, name, category, quantity, unit_price, storage_fee)
        self.products.append(new_item)
        print("Nhập hàng hóa mới vào kho thành công")

    def show_all(self):
        if not self.products:
            print("Kho hàng hiện tại đang trống")
            return
        print("-" * 145)
        print(f"{'Mã hàng hóa':<12} | {'Tên hàng hóa':<25} | {'Danh mục':<15} | {'Số lượng':<10} | {'Đơn giá nhập':<15} | {'Chi phí kho':<15} | {'Tổng giá trị':<18} | {'Phân loại tồn kho'}")
        print("-" * 145)
        for prod in self.products:
            print(f"{prod.id:<12} | {prod.name:<25} | {prod.category:<15} | {prod.quantity:<10} | {prod.unit_price:<15,.1f} | {prod.storage_fee:<15,.1f} | {prod.total_inventory_value:<18,.1f} | {prod.inventory_type}")
        print("-" * 145)

    def update_item(self):
        id = input("Nhập mã hàng hóa cần cập nhật: ").strip()
        
        found_product = ""
        for prod in self.products:
            if prod.id == id:
                found_product = prod
                break

        if found_product != "":
            try:
                unit_price = float(input("Nhập giá nhập mới: "))
                if unit_price < 0:
                    print("Đơn giá phải >= 0")
                    return

                quantity = int(input("Nhập số lượng mới: "))
                if not (0 <= quantity <= 100000):
                    print("Số lượng tồn kho phải là số nguyên từ 0 đến 100000")
                    return

                storage_fee = float(input("Nhập chi phí lưu kho mới: "))
                if storage_fee < 0:
                    print("Chi phí lưu kho phải >= 0")
                    return
            except ValueError:
                print("Dữ liệu nhập vào phải là số hợp lệ")
                return

            found_product.unit_price = unit_price
            found_product.quantity = quantity
            found_product.storage_fee = storage_fee

            found_product.calculate_total_value()
            found_product.classify_stock_status()
            print("Cập nhật thông tin sản phẩm thành công")
        else:
            print("Không tìm thấy mã hàng hóa phù hợp")

    def delete_item(self):
        id = input("Nhập mã hàng hóa cần xóa khỏi kho: ").strip()
        
        found_product = ""
        for prod in self.products:
            if prod.id == id:
                found_product = prod
                break

        if found_product != "":
            confirm = input("Bạn có chắc muốn xóa hàng hóa này khỏi hệ thống không? (Y/N): ").strip().lower()
            if confirm == "y":
                self.products.remove(found_product)
                print("Đã xóa hàng hóa khỏi hệ thống thành công")
            else:
                print("Đã hủy bỏ thao tác xóa")
        else:
            print("Không tìm thấy mã hàng hóa phù hợp")
        
    def search_product(self):
        keyword = input("Nhập tên hàng hóa cần tìm: ").strip().lower()
        results = []
        for prod in self.products:
            if keyword in prod.name.lower():
                results.append(prod)

        if not results:
            print("Không tìm thấy hàng hóa phù hợp")
            return

        print("-" * 145)
        print(f"{'Mã hàng hóa':<12} | {'Tên hàng hóa':<25} | {'Danh mục':<15} | {'Số lượng':<10} | {'Đơn giá nhập':<15} | {'Chi phí kho':<15} | {'Tổng giá trị':<18} | {'Phân loại tồn kho'}")
        print("-" * 145)
        for prod in results:
            print(f"{prod.id:<12} | {prod.name:<25} | {prod.category:<15} | {prod.quantity:<10} | {prod.unit_price:<15,.1f} | {prod.storage_fee:<15,.1f} | {prod.total_inventory_value:<18,.1f} | {prod.inventory_type}")
        print("-" * 145)


def menu():
    print("""
================ MENU ================
1. Hiển thị danh sách hàng hóa
2. Thêm hàng hóa mới
3. Cập nhật hàng hóa
4. Xóa hàng hóa
5. Tìm kiếm hàng hóa
6. Thoát
=====================================
""")

def main():
    manager = InventoryManager()
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn (1-6): ").strip()

        match choice:
            case "1":
                manager.show_all()
            case "2":
                manager.add_item()
            case "3":
                manager.update_item()
            case "4":
                manager.delete_item()
            case "5":
                manager.search_product()
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản hàng hóa")
                break
            case _:
                print("Lựa chọn không hợp lệ Vui lòng nhập từ 1 đến 6")


if __name__ == "__main__":
    main()