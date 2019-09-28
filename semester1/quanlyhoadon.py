import os

print("+--------------MENU-----------------+")
print("|Chon THH de tao hang hoa           |")
print("|Chon XHH de xem hang hoa           |")
print("|Chon TLH de tao loai hang hoa      |")
print("|Chon XLH de xem loai hang hoa      |")
print("|Chon C de tao hoa don              |")
print("|Chon R de xem thong tin hoa don    |")
print("|Chon T de tinh tong doanh thu      |")
print("|Chon A de tinh tong hang hoa ban ra|")
print("|Chon E de thoat                    |")
print("+-----------------------------------+")

danhsachhanghoa = []
danhsachloaihanghoa = []
danhsachhoadon=[]
# danhsachhoadon = [
#     {'thue': 0.1, 'tongtien': 27500.0, 'danhsachhanghoa': [{'ten': 'Coca', 'dongia': 5000, 'thanhtien': 10000, 'stt': '1', 'soluong': 2}, {'ten': 'Pepsi', 'dongia': 3000, 'thanhtien': 15000, 'stt': '2', 'soluong': 5}], 'nguoimua': 'Cuong', 'ngayhoadon': '1', 'sohoadon': 'MS01', 'tongtientruocthue': 25000},
#     {'thue': 0.1, 'tongtien': 27500.0, 'danhsachhanghoa': [{'ten': 'Coca', 'dongia': 5000, 'thanhtien': 10000, 'stt': '1', 'soluong': 2}, {'ten': 'Pepsi', 'dongia': 3000, 'thanhtien': 15000, 'stt': '2', 'soluong': 5}], 'nguoimua': 'Cuong', 'ngayhoadon': '1', 'sohoadon': 'MS02', 'tongtientruocthue': 25000}
# ]

# hanghoaban = {
#     # "Coca": {
#     #     "tongso": 0,
#     #     "doanhthu": 0
#     # }
# }

def load_loaihanghoa_luckhoidong():
  files = os.listdir("danhmuc")
  if "loaihanghoa.csv" not in files:
     return
  
  with open('danhmuc/loaihanghoa.csv', 'r') as f:
    line = f.readline()
    while line:
        str_to_reads = line.split("#")
        #print("str_to_reads:", str_to_reads)
        if len(str_to_reads) > 1:
            loaihanghoa = {}
            loaihanghoa["id"] = str_to_reads[0]
            tenloai = str_to_reads[1]
            if tenloai.endswith('\n'):
                tenloai = tenloai[0:len(tenloai)-1]
            loaihanghoa["ten"] = tenloai
            danhsachloaihanghoa.append(loaihanghoa)
        line = f.readline()
  print("danhsachloaihanghoa:", danhsachloaihanghoa)

def load_hanghoa_luckhoidong():
  files = os.listdir("danhmuc")
  if "hanghoa.csv" not in files:
     return

  with open('danhmuc/hanghoa.csv', 'r') as f:
    line = f.readline()
    while line:
        str_to_reads = line.split("#")
        #print("str_to_reads:", str_to_reads)
        if len(str_to_reads) > 1:
            hanghoa = {}
            hanghoa["id"] = str_to_reads[0]
            hanghoa["ten"] = str_to_reads[1]
            hanghoa["giaban"] = str_to_reads[2]
            hanghoa["loaihanghoa_id"] = str_to_reads[3]
            
            if hanghoa["loaihanghoa_id"].endswith('\n'):
                hanghoa["loaihanghoa_id"] = hanghoa["loaihanghoa_id"][0:len(hanghoa["loaihanghoa_id"])-1]
            danhsachhanghoa.append(hanghoa)
        line = f.readline()
  print("danhsachhanghoa:", danhsachhanghoa)
	
load_hanghoa_luckhoidong()
	
def tao_loaihanghoa():
  data = {}
  id = input("xin moi nhap id loai hang hoa:")
  tim_id_daco = xem_loaihanghoa(id)
  if tim_id_daco is not None:
     print("Da ton tai Ma loai hang hoa nay. Xin moi ban thu hien chu nang khac")
     return

  data["id"] = id
  data["ten"] = input("xin moi nhap ten loai hang hoa:")
  danhsachloaihanghoa.append(data)
  str_to_save = data["id"] + "#" + data["ten"] + '\n'
  with open('danhmuc/loaihanghoa.csv', 'a') as f:
	    data = f.write(str_to_save)



def xem_loaihanghoa(id = None):
  if id is None:
      id = input("xin moi nhap id loai hang hoa:")
  for loai in danhsachloaihanghoa:
    if loai["id"] == id:
      print("loai hang hoa: ", loai)
      return loai


def sua_loaihanghoa(id, data):
  pass

def xoa_loaihanghoa(id):
  pass

def danhsach_loaihanghoa():
  return danhsachloaihanghoa


def tao_hanghoa():
  data = {}
  id = input("xin moi nhap id hang hoa:")
  tim_id_daco = xem_loaihanghoa(id)
  if tim_id_daco is not None:
     print("Da ton tai Ma loai hang hoa nay. Xin moi ban thu hien chu nang khac")
     return
  data["id"] = id
  data["ten"] = input("xin moi nhap ten hang hoa:")
  data["giaban"] = input("xin moi nhap gia ban:")
  loaihanghoa_id = input("xin moi nhap ma loai hang hoa:")
	
  co_hienthi_danhsachloai = False
  tim_idloai_daco = xem_loaihanghoa(loaihanghoa_id)
  
  while tim_idloai_daco is None:
     print("Danh sach loai hang hoa:")
     for loaihanghoai in danhsachloaihanghoa:
        print(loaihanghoai["id"])
     loaihanghoa_id = input("xin moi nhap ma loai hang hoa:")
     tim_idloai_daco = xem_loaihanghoa(loaihanghoa_id)
	
  
  data["loaihanghoa_id"] = loaihanghoa_id
  danhsachhanghoa.append(data)
  str_to_save = data["id"] + "#" + data["ten"] + '#' + data["giaban"] + "#" +  data["loaihanghoa_id"] + '\n'
  with open('danhmuc/hanghoa.csv', 'a') as f:
      data = f.write(str_to_save)
  


def xem_hanghoa(id = None):
  if id is None:
      id = input("xin moi nhap id hang hoa:")
  for hanghoa in danhsachhanghoa:
    if hanghoa["id"] == id:
      print(hanghoa)
      return hanghoa


hanghoaban = {}


load_loaihanghoa_luckhoidong()

while True:
    x=input("=> chon chuc nang:")
    print("=> ban da chon chuc nang:",x)
    if x.upper() == 'TLH':
      tao_loaihanghoa()
    if x.upper() == 'XLH':
      xem_loaihanghoa()
    if x.upper() == 'THH':
      tao_hanghoa()
    if x.upper() == 'XHH':
      xem_hanghoa()
    if x.upper() == 'C':
        print("moi ban tao hoa don")
        hoadon={}
        hoadon["sohoadon"] = input("nhap so hoa don:")
        hoadon["ngayhoadon"]= input("nhap ngay hoa don :")
        hoadon["nguoimua"]= input("nhap nguoi mua hang :")
        hoadon["tongtientruocthue"] = 0
        hoadon["thue"] = 0.1
        hoadon["tongtien"] = 0
        hoadon["danhsachhanghoa"] = []

        nhaphanghoa = input("=> Ban co muon nhap hang hoa khong (y/n): ")
        while nhaphanghoa.upper() == 'Y':
            hanghoa = {}
            hanghoa["stt"] = input("nhap so thu tu: ")
            hanghoa["ten"] = input("nhap ten hang hoa: ")
            soluong = input("nhap so luong: ")
            hanghoa["soluong"] = int(soluong)
            hanghoa["dongia"] = int(input("nhap don gia:"))
            hanghoa["thanhtien"] = hanghoa["soluong"] * hanghoa["dongia"]
            
            if hanghoa["ten"] in hanghoaban:
                hanghoaban[hanghoa["ten"]]["tongso"] = hanghoaban[hanghoa["ten"]]["tongso"] + hanghoa["soluong"]
                hanghoaban[hanghoa["ten"]]["doanhthu"] = hanghoaban[hanghoa["ten"]]["doanhthu"] + hanghoa["thanhtien"]
            else:
                hanghoaban[hanghoa["ten"]] = {
                    "tongso": hanghoa["soluong"],
                    "doanhthu": hanghoa["thanhtien"]
                }

            hoadon["danhsachhanghoa"].append(hanghoa)

            hoadon["tongtientruocthue"] = hoadon["tongtientruocthue"] + hanghoa["thanhtien"]

            nhaphanghoa = input("=> Ban co muon nhap hang hoa khong (y/n): ")
        
        hoadon["tongtien"] = hoadon["tongtientruocthue"] + hoadon["tongtientruocthue"]*hoadon["thue"]
        danhsachhoadon.append(hoadon)
        print("Kiemtra:", danhsachhoadon)

    if x.upper() == 'R':
        timthay = False
        while timthay is False:
            sohoadon_canxem = input("nhap so hoa don can xem:")
            for hoadon in danhsachhoadon:
                if hoadon["sohoadon"] == sohoadon_canxem:
                    timthay = True
                    #Hoa don se in o day
                    print("                          HOA DON MUA HANG                                  ")
                    print("so hoa don:",hoadon["sohoadon"])
                    print("ngay xuat:",hoadon["ngayhoadon"])
                    print("ten khach hang:",hoadon["nguoimua"])
                    print("_____________________________thong tin hoa don_______________________________")
                    print("+----------+------------------+----------+---------------+------------------+")
                    print("|   STT    |     hang hoa     | so luong |    don gia    |    thanh tien    |")
                    print("+----------+------------------+----------+---------------+------------------+")
                    
                    for hanghoa in hoadon["danhsachhanghoa"]:
                        print("In dong hang hoa o day")
                        #print("| "+stt_x+"  | " +tenhanghoa+ " | "+soluong_x+" | "+dongia_x+" | "+thanhtien_x+" |")
                    print("+----------+------------------+----------+---------------+------------------+")
                    #end of Hoa don se in o day
                    break
    if x.upper() == 'T':
        tongdoanhthu = 0
        for hoadon in danhsachhoadon:
            tongdoanhthu = tongdoanhthu + hoadon["tongtien"]
        print("Tong doanh thu la: ", tongdoanhthu)

    if x.upper() == 'A':
        tongsohanghoa = 0
        doanhsoban = 0

        tenhanghoa = input("nhap ten hang hoa can xem:")
        for hoadon in danhsachhoadon:
            for hanghoa in hoadon["danhsachhanghoa"]:
                if hanghoa["ten"] == tenhanghoa:
                    tongsohanghoa = tongsohanghoa + hanghoa["soluong"]
                    doanhsoban = doanhsoban + hanghoa["thanhtien"]
                    break
        print("Tong so hang hoa: ", tongsohanghoa)
        print("Doanh so ban: ", doanhsoban)
    
    if x.upper() == 'E':
        print("Tam biet! Hen gap lai")
        break
        
            

