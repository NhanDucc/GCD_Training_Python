nam_sinh = int(input("Nhap nam sinh cua ban: "))
nam_nay = int(input("Nam nay la nam: "))
if nam_sinh<nam_nay:
    tuoi = nam_nay-nam_sinh
    print(f"Nam nay ban {tuoi} tuoi")
else:
    print("Khong hop ly, vui long nhap lai")