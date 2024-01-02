tien_gui = int(input("Nhap so tien muon gui: "))
ki_han = int(input("Nhap so ki han muon gui: "))
ky_han = 0
lai = 3/100
s = 0
for i in range (1, ki_han+1):
    ky_han += 1
    tien_gui = tien_gui + lai * tien_gui
    print(f"So tien se co sau ky han {ky_han} la: {tien_gui}")