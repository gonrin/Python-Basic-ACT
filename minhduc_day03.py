print("+--------------MENU-----------------+")
print("|Chon C de tao hoa don              |")
print("|Chon R de xem thong tin hoa don    |")
print("|Chon T de tinh tong doanh thu      |")
print("|Chon A de tinh tong hang hoa ban ra|")
print("|Chon E de thoat                    |")
print("+-----------------------------------+")
while True:
    danhsachhoahon=[]
    x=input("=> chon chuc nang:")
    print("=> ban da chon chuc nang:",x)
    if x == 'C':
        tiep=input("tiep tuc?y/n?")
        while tiep == 'y':
            print("moi ban tao hoa don")
            hoadon={}
            banghoadon={}
            stt = input("nhap so thu tu:")
            stt_x=str(stt)
            for i in range(len(stt_x),7):
                stt_x= ' '+stt_x
            tenhanghoa= input("nhap ten hang hoa muon mua :")
            for i in range(len(tenhanghoa),16):
                tenhanghoa = tenhanghoa + ' '
            so=[]
            soluong=input("nhap so luong:")
            soluong_x=str(soluong)
            for i in range(len(soluong_x),8):
                soluong_x = ' '+soluong_x
            so.append(soluong)
            dongia= input("nhap gia cua san pham:")
            dongia_x=str(dongia)
            for i in range(len(dongia_x),13):
                dongia_x=' '+dongia_x
            tien=[]
            thanhtien=int(dongia)*int(soluong)
            thanhtien_x=str(thanhtien)
            for i in range(len(thanhtien_x),16):
                thanhtien_x=' '+thanhtien_x
            tien.append(thanhtien)
            hoadon["sohoadon"]=input("nhap so hoa don :")
            hoadon["ngaysuat"]=input("nhap ngay tao hoa don:")
            hoadon["tenkhachhang"]=input("nhap ten khach hang:")
            tiep=input("ban muon tiep tuc ko?y/n?")
    if x== 'R':
        print("                          HOA DON MUA HANG                                  ")
        print("so hoa don:",hoadon["sohoadon"])
        print("ngay xuat:",hoadon["ngaysuat"])
        print("ten khach hang:",hoadon["tenkhachhang"])
        print("_____________________________thong tin hoa don_______________________________")
        print("+----------+------------------+----------+---------------+------------------+")
        print("|   STT    |     hang hoa     | so luong |    don gia    |    thanh tien    |")
        print("+----------+------------------+----------+---------------+------------------+")
        print("| "+stt_x+"  | " +tenhanghoa+ " | "+soluong_x+" | "+dongia_x+" | "+thanhtien_x+" |")
        print("+----------+------------------+----------+---------------+------------------+")
        print("| "+stt_x+"  | " +tenhanghoa+ " | "+soluong_x+" | "+dongia_x+" | "+thanhtien_x+" |")
        print("+----------+------------------+----------+---------------+------------------+")
    if x== 'T':
        print("tong doanh thu bang")
        t_sum = 0
        tien=[]
        for num in tien:
            t_sum = t_sum + num
        print(t_sum)
    if x== 'A':
        print("so hang hoa ban ra")
        a_sum = 0
        so=[]
        for j in so:
            a_sum = a_sum + j
        print(a_sum)
    if x== 'E':
        print("^_^ bye ^_^")
        break
