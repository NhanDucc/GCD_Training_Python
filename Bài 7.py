import random

mon_phai = {
    "Hệ Kim": ["Thiếu Lâm", "Thiên Vương"],
    "Hệ Mộc": ["Đường Môn", "Ngũ Độ"],
    "Hệ Thủy": ["Nga Mi", "Thúy Yên"],
    "Hệ Hỏa": ["Cái Bang", "Thiên Nhẫn"],
    "Hệ Thổ": ["Võ Đang", "Côn Lôn"]
}

sat_thuong_co_ban = {
    "Thiếu Lâm": {"Sát thương": 43, "Hệ ngũ hành": "Hệ Kim"},
    "Thiên Vương": {"Sát thương": 40, "Hệ ngũ hành": "Hệ Kim"},
    "Đường Môn": {"Sát thương": 48, "Hệ ngũ hành": "Hệ Mộc"},
    "Ngũ Độ": {"Sát thương": 47, "Hệ ngũ hành": "Hệ Mộc"},
    "Nga Mi": {"Sát thương": 45, "Hệ ngũ hành": "Hệ Thủy"},
    "Thúy Yên": {"Sát thương": 49, "Hệ ngũ hành": "Hệ Thủy"},
    "Cái Bang": {"Sát thương": 44, "Hệ ngũ hành": "Hệ Hỏa"},
    "Thiên Nhẫn": {"Sát thương": 42, "Hệ ngũ hành": "Hệ Hỏa"},
    "Võ Đang": {"Sát thương": 42, "Hệ ngũ hành": "Hệ Thổ"},
    "Côn Lôn": {"Sát thương": 45, "Hệ ngũ hành": "Hệ Thổ"}
}

he_khac_che = {
    "Hệ Hoả": {"Hệ Kim": 0.2},
    "Hệ Kim": {"Hệ Mộc": 0.25},
    "Hệ Mộc": {"Hệ Thổ": 0.2},
    "Hệ Thổ": {"Hệ Thuỷ": 0.1},
    "Hệ Thuỷ": {"Hệ Hoả": 0.15}
}

def tao_nhan_vat():
    print("Danh sách nhân vật:")
    for i, nhan_vat in enumerate(sat_thuong_co_ban.keys(), start=1):
        print(f"{i}. {nhan_vat}")

    lua_chon_nhan_vat = int(input("Chọn nhân vật: "))
    while lua_chon_nhan_vat not in range(1, 11):
        lua_chon_nhan_vat = int(input("Lựa chọn không hợp lệ. Chọn lại nhân vật: "))

    nhan_vat = list(sat_thuong_co_ban.keys())[lua_chon_nhan_vat - 1]
    ten_nhan_vat = input("Nhập tên nhân vật của bạn: ")

    return {
        "Tên": ten_nhan_vat,
        "Nhân vật": nhan_vat,
        "Cấp độ": 1,
        "Sát thương cơ bản": sat_thuong_co_ban[nhan_vat]["Sát thương"],
        "Hệ ngũ hành": sat_thuong_co_ban[nhan_vat]["Hệ ngũ hành"],
        "Kinh nghiệm": 0,
        "Số lượng quái nhỏ": 0
    }

def tao_quai(so_luong_quai_nho):
    if so_luong_quai_nho >= 10:
        ngu_hanh = random.choice(list(mon_phai.keys()))
        cap_do = random.randint(7, 10)
        sat_thuong = 42
    else:
        ngu_hanh = random.choice(list(mon_phai.keys()))
        cap_do = random.randint(1, 6)
        sat_thuong = 38

    return {
        "Hệ ngũ hành": ngu_hanh,
        "Cấp độ": cap_do,
        "Sát thương cơ bản": sat_thuong
    }

def cap_nhat_kinh_nghiem(nhan_vat, quai):
    if quai["Cấp độ"] >= 7:
        nhan_vat["Kinh nghiệm"] += 2
    else:
        nhan_vat["Kinh nghiệm"] += 1

    if nhan_vat["Kinh nghiệm"] >= 10:
        nhan_vat["Cấp độ"] += 1
        nhan_vat["Kinh nghiệm"] = 0
        nhan_vat["Số lượng quái nhỏ"] = 0

def he_so_tang_sat_thuong(nhan_vat_1, nhan_vat_2):
    sat_thuong_hien_tai_1 = nhan_vat_1["Sát thương cơ bản"]
    sat_thuong_hien_tai_2 = nhan_vat_2["Sát thương cơ bản"]
    he_ngu_hanh_nv_1 = nhan_vat_1["Hệ ngũ hành"]
    he_ngu_hanh_nv_2 = nhan_vat_2["Hệ ngũ hành"]
    
    if he_ngu_hanh_nv_1 == "Hệ Hoả" and he_ngu_hanh_nv_2 == "Hệ Kim":
        sat_thuong_hien_tai_1 *= 1.2
    elif he_ngu_hanh_nv_1 == "Hệ Kim" and he_ngu_hanh_nv_2 == "Hệ Mộc":
        sat_thuong_hien_tai_1 *= 1.25
    elif he_ngu_hanh_nv_1 == "Hệ Mộc" and he_ngu_hanh_nv_2 == "Hệ Thổ":
        sat_thuong_hien_tai_1 *= 1.2
    elif he_ngu_hanh_nv_1 == "Hệ Thổ" and he_ngu_hanh_nv_2 == "Hệ Thủy":
        sat_thuong_hien_tai_1 *= 1.1
    elif he_ngu_hanh_nv_1 == "Hệ Thủy" and he_ngu_hanh_nv_2 == "Hệ Hoả":
        sat_thuong_hien_tai_1 *= 1.15
    
    if he_ngu_hanh_nv_2 == "Hệ Hoả" and he_ngu_hanh_nv_1 == "Hệ Kim":
        sat_thuong_hien_tai_2 *= 1.2
    elif he_ngu_hanh_nv_2 == "Hệ Kim" and he_ngu_hanh_nv_1 == "Hệ Mộc":
        sat_thuong_hien_tai_2 *= 1.25
    elif he_ngu_hanh_nv_2 == "Hệ Mộc" and he_ngu_hanh_nv_1 == "Hệ Thổ":
        sat_thuong_hien_tai_2 *= 1.2
    elif he_ngu_hanh_nv_2 == "Hệ Thổ" and he_ngu_hanh_nv_1 == "Hệ Thủy":
        sat_thuong_hien_tai_2 *= 1.1
    elif he_ngu_hanh_nv_2 == "Hệ Thủy" and he_ngu_hanh_nv_1 == "Hệ Hoả":
        sat_thuong_hien_tai_2 *= 1.15
    
    return sat_thuong_hien_tai_1, sat_thuong_hien_tai_2

def tinh_sat_thuong(nhan_vat, quai):
    sat_thuong_hien_tai_1, sat_thuong_hien_tai_2 = he_so_tang_sat_thuong(nhan_vat, quai)
    sat_thuong_theo_cap_1 = nhan_vat["Cấp độ"] * 0.1 * nhan_vat["Sát thương cơ bản"]
    sat_thuong_theo_cap_2 = quai["Cấp độ"] * 0.1 * quai["Sát thương cơ bản"]
    sat_thuong_hien_tai_1 += sat_thuong_theo_cap_1
    sat_thuong_hien_tai_2 += sat_thuong_theo_cap_2

    return sat_thuong_hien_tai_1, sat_thuong_hien_tai_2

def combat(nhan_vat, quai):
    sat_thuong_hien_tai_nhan_vat = tinh_sat_thuong(nhan_vat, quai)
    sat_thuong_hien_tai_quai = tinh_sat_thuong(quai, nhan_vat)
    return sat_thuong_hien_tai_nhan_vat >= sat_thuong_hien_tai_quai

def giao_chien_cuoi_cung(nhan_vat_1, nhan_vat_2):
    sat_thuong_hien_tai_1 = tinh_sat_thuong(nhan_vat_1, nhan_vat_2)
    sat_thuong_hien_tai_2 = tinh_sat_thuong(nhan_vat_2, nhan_vat_1)

    if sat_thuong_hien_tai_1 > sat_thuong_hien_tai_2:
        print(f"{nhan_vat_1['Tên']} đã đánh bại {nhan_vat_2['Tên']}!")
    elif sat_thuong_hien_tai_1 < sat_thuong_hien_tai_2:
        print(f"{nhan_vat_2['Tên']} đã đánh bại {nhan_vat_1['Tên']}!")
    else:
        print("Hai người chơi có cùng sát thương. Đây là trận hòa!")

print("Người chơi 1:")
nhan_vat_1 = tao_nhan_vat()

print("\nNgười chơi 2:")
nhan_vat_2 = tao_nhan_vat()

print("\nThông tin nhân vật thứ nhất: ")
for key, value in nhan_vat_1.items():
    print(f"{key}: {value}")

print("\nThông tin nhân vật thứ hai: ")
for key, value in nhan_vat_2.items():
    print(f"{key}: {value}")

so_luong_quai_nho_1 = 0
so_luong_quai_nho_2 = 0

while True:
    quai_1 = tao_quai(so_luong_quai_nho_1)
    if combat(nhan_vat_1, quai_1):
        so_luong_quai_nho_1 += 1

    quai_2 = tao_quai(so_luong_quai_nho_2)
    if combat(nhan_vat_2, quai_2):
        so_luong_quai_nho_2 += 1

    if so_luong_quai_nho_1 >= 10:
        quai_to_1 = tao_quai(so_luong_quai_nho_1)
        if combat(nhan_vat_1, quai_to_1):
            print("Người chơi 1 đã đánh bại quái to!")
            break

    if so_luong_quai_nho_2 >= 10:
        quai_to_2 = tao_quai(so_luong_quai_nho_2)
        if combat(nhan_vat_2, quai_to_2):
            print("Người chơi 2 đã đánh bại quái to!")
            break

    if so_luong_quai_nho_2 >= 10:
        quai_to_2 = tao_quai(so_luong_quai_nho_2)
        if combat(nhan_vat_2, quai_to_2):
            print("Người chơi 2 đã đánh bại quái to!")
            break
        
print("\nCuộc giao chiến cuối cùng:")
giao_chien_cuoi_cung(nhan_vat_1, nhan_vat_2)