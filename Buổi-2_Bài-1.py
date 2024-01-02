tien_muon = int(input("Nhap tien can muon: "))
lai = 10/100
tien_no = tien_muon - 120
nam = 1
while tien_no > 0:
    nam += 1
    tien_no = tien_no - 120 + lai * tien_no

print(f"So nam can tra la: {nam}")
