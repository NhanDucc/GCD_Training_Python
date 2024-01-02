ngay = int(input("Nhap ngay cua the ki 21: "))
thang = int(input("Nhap thang cua the ki 21: "))
nam = int(input("Nhap nam cua the ki 21: "))

if 2000 < nam < 2101:
    if 0 < thang < 13:
        if thang in range (1,8) and thang % 2 != 0:
            if 0 < ngay < 32:
                print("Co ton tai")
            else:
                print("Khong ton tai")  
        if thang == 2:
                if (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0:
                    if 0 < ngay <= 29:
                        print("Co ton tai")
                    else:
                        print("Khong ton tai")
                else:
                    if 0 < ngay <= 28:
                        print("Co ton tai")
                    else:
                        print("Khong ton tai")                
        if thang in range (1,8) and thang % 2 == 0 and thang != 2:
            if 0 < ngay < 31:
                print("Co ton tai")
            else:
                print("Khong ton tai")
        if thang in range (8,13) and thang % 2 != 0:
            if 0 < ngay < 31:
                print("Co ton tai")
            else:
                print("Khong ton tai")
        if thang in range (8,13) and thang % 2 == 0:
            if 0 < ngay < 32:
                print("Co ton tai")
            else:
                print("Khong ton tai")
    else:
        print("Khong ton tai")   
else:
    print("Khong ton tai")
