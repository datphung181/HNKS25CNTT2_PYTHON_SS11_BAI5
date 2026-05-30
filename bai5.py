'''
- Input
    lựa chọn menu
    id sản phẩm 
    số lg
    mã giảm giá
- output
    dữ liệu đã chuẩn hóa
    thông báo thành công hc lỗi
- các hàm cần dùng: remove, get, strip, upper, isdigit, 
- Pseudocode 
- in menu
- nhận lựa chọn 
- 1: hiện ra bảng
- 2: nhập id, ktra id có tồn tại k, có cho mua, không thì báo lỗi
- 3: nhập id, ktra id có tồn tại k, có check tiếp số lg nhậpp với lịch sử bán, nếu hợp lệ mới cho đổi cho đôi, không thì báo lỗi
- 4: nhập id, ktra id có tồn tại k, có thì check inout hợp lệ k nếu có thì cập nhật
- 5: nhập id, ktra id có tồn tại k, có cho nhập, không thì báo lỗi
- 6: thoát

'''


product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5,
        "returned": 1,
        "discount": 0
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3,
        "returned": 0,
        "discount": 10
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7,
        "returned": 1,
        "discount": 15
    }
]

while True:
    choice = input('''
===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====
1. Hiển thị danh sách sản phẩm
2. Bán sản phẩm cho khách hàng
3. Xử lý đổi trả sản phẩm
4. Áp dụng giảm giá cho sản phẩm
5. Nhập thêm hàng vào kho cửa hàng
6. Thoát chương trình

Mời bạn nhập lựa chọn: '''
    ).strip()
    
    if choice.isdigit():
        choice = int(choice)
    else:
        print("Hãy nhập 1 số dương 1-6")
        continue
    
    match choice:
        case 1:
            if not product_list:
                print("Danh sách sản phẩm hiện đang trống.")
                continue
            print("Danh sách sản phẩm hiện tại:")
            for index, product in enumerate(product_list,start=1):
                if product.get("quantity") == 0:
                    status = "Hết hàng"
                elif product.get("quantity") <=5:
                    status = "Sắp hết hàng"
                else:
                    status = "Còn hàng"
                    
                print(f"{index}. Mã SP: {product.get("product_id")} | Tên: {product.get("product_name")} | Giá: {product.get("price")} | Tồn kho: {product.get("quantity")} | Đã bán: {product.get("sold")} | Đổi trả: {product.get("returned")} | Giảm giá: {product.get("discount")}% | Trạng thái: {status}")
                
        case 2:
            id_input = input("Nhập mã sản phẩm khách muốn mua:").strip().upper()
            is_found = False
            
            for product in product_list:
                if id_input == product.get("product_id"):
                    is_found = True
                    
                    quantity_input = input("Nhập số lượng khách mua: ")
                    if not quantity_input.isdigit() or int(quantity_input) <= 0:
                        print("Số lượng mua không hợp lệ")
                    else:
                        quantity_input = int(quantity_input)
                        if quantity_input > product.get("quantity"):
                            print("Số lượng trong kho không đủ để bán")
                        else:
                            product["quantity"] -= quantity_input
                            product["sold"] += quantity_input
                            total_money = (product.get("price") * (100 - product.get("discount"))/ 100) * quantity_input
                            print(f"Bạn đã mua {quantity_input} {product.get("product_name")}. Tổng tiền: {total_money}")
                    break
                
            if not is_found:
                print("Không tìm thấy mã sản phẩm")
                
        case 3:
            id_input = input("Nhập mã sản phẩm khách muốn đổi/trả: ").strip().upper()
            is_found = False
            
            for product in product_list:
                if id_input == product.get("product_id"):
                    is_found = True
                    
                    quantity_input = input("Nhập số lượng đổi/trả: ")
                    if not quantity_input.isdigit() or int(quantity_input) <= 0:
                        print("Số lượng đổi/trả không hợp lệ")
                    else:
                        quantity_input = int(quantity_input)
                        if quantity_input > product.get("sold"):
                            print("Số lượng đổi/trả không được vượt quá số lượng đã bán")
                        else:
                            product["quantity"] += quantity_input
                            product["sold"] -= quantity_input
                            product["returned"] += quantity_input
                            
                            print(f"Bạn đã trả {quantity_input} {product.get("product_name")}")
                    break
                
            if not is_found:
                print("Không tìm thấy sản phẩm cần đổi trả")
            
        case 4:
            id_input = input("Nhập mã sản phẩm cần áp dụng giảm giá: ").strip().upper()
            is_found = False
            
            for product in product_list:
                if id_input == product.get("product_id"):
                    is_found = True
                    
                    discount_input = input("Nhập phần trăm giảm giá: ")
                    if not discount_input.isdigit():
                        print("Phần trăm giảm giá không hợp lệ")
                    else:
                        discount_input = int(discount_input)
                        if discount_input > 70 or discount_input <= 0:
                            print(f"Không thể cập nhật giảm giá > 70{'%'} hc < 0%")
                        else:
                            product["discount"] = discount_input
                            
                            print(f"Bạn đã chỉnh mã giảm giá của {product.get("product_name")} thành {discount_input}% ")
                    break
                
            if not is_found:
                print("Không tìm thấy mã sản phẩm")
                
        case 5:
            id_input = input("Nhập mã sản phẩm khách muốn thêm:").strip().upper()
            is_found = False   
                      
            for product in product_list:
                if id_input == product.get("product_id"):
                    is_found = True
                    
                    quantity_input = input("Nhập số lượng nhập thêm: ")
                    if not quantity_input.isdigit() or int(quantity_input) <= 0:
                        print("Nhập kho không hợp lệ")
                    else:
                        quantity_input = int(quantity_input)
                        product["quantity"] += quantity_input
                        print(f"Bạn đã nhập {quantity_input} {product.get("product_name")}.")
                    break
                
            if not is_found:
                print("Không tìm thấy mã sản phẩm")
                
        case 6: 
            print("Thoát chương trình.Sau đó dừng chương trình.")
            
        case _:
            print("Lỗi cú pháp, vui lòng nhập lại!!!")
            
