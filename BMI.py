name= input('Bạn tên gì?')
print(f"Xin chào {name}! Sau đây {name} hãy nhập thông tin để biết chỉ số BMI của {name} nhé!")

#Tính chỉ số MBI
chieu_cao_cm = input(f"Nhập chiều cao của {name} (cm):")
can_nang_kg = input(f"Nhập cân nặng của {name} (kg):")

#Chuyển đổi chuỗi thành số
chieu_cao_m = float(chieu_cao_cm)/100 #Đổi cm sang m
can_nang = float(can_nang_kg)

#Tính BMI
bmi = can_nang / (chieu_cao_m * chieu_cao_m)

print(f"Chỉ số BMI của {name}n là: {bmi:2f}")

#Đánh giá BMi ở mức nào
if bmi < 18.5:
    print(f"-> {name} đang ở mức Gầy, cần nạp TÀ TƯA GẤP.")
elif bmi < 25:
    print(f"→ {name} đang ở mức BÌNH THƯỜNG. Chưa đủ WOW. Nạp thêm TÀ TƯA đi")
elif bmi < 30:
    print(f"→ {name} đang ở mức THỪA CÂN. NGƯNG UỐNG TÀ TƯA GẤP")
else:
    print(f"→ {name} đang ở mức BÉO PHÌ. VƯỢT MỨC PICKlEBALL RỒI ĐÓ")
