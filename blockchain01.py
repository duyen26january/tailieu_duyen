import subprocess
import decimal
import hashlib
from datetime import datetime

# Lấy thời gian hiện tại
now = datetime.now()
# Chỉ lấy giờ và phút
current_hour_minute = now.strftime("%H:%M")
print("Giờ và phút hiện tại:", current_hour_minute)
def hash256(data):
    return hashlib.sha256(data.encode()).hexdigest()
lever2="nguyễn hữu duyến"
lever3="__"
kos = float(input("X="))
def coin_main(lever1,lever2,lever3,datetime_object):
    lever2=str(j)+"!"+str(input("Nhap vao du lieu ban muon=="))
    #nên nhớ ở dòng này lever2 có thể được cấu trúc thành lever2_1 và lever2_3 của hàm coin_main2
    #coin_main() sẻ có cấu trúc là 1.000000000...xxxxxxx,lever2,lever3 
    #thế nên lever2 cũng có thể có cấu trúc là 1.0000000000..xxxxxx nhưng số chử số không luôn ít hơn lever1, ở hàm của lever2 có thể là hàm để chạy các hợp đồng thông minh
    #và có thể mở rộng tối đa layer(n-3) với n là số số không liên tiếp hay nói rất khác so với sơ đồ Miekey mà các diển đàn nói
    lever3=hash256(hash256(lever1)+hash256(lever2)+hash256(lever3))
    if(lever2)==("1"+"!"+"BEGIN"):
           ls=(input("BEGIN+ls+lever3  ::>"))
           dadd=open('duyen.txt','a+')
           dadd.write('BEGIN:  '+str(ls)+str(lever3))
           dadd.close()
    if(lever2)==("1"+"!"+"END"):
            ls=(input("END+ls+lever3  ::>"))
            dadd=open('duyen.txt','a+')
            dadd.write('END:  '+str(ls)+str(lever3))
            dadd.close()
    if(lever2)==("1"+"!"+"RUN"):
            ls=(input("RUN+ls+lever3  ::>"))
            dadd=open('duyen.txt','a+')
            dadd.write('RUN   '+str(ls)+str(lever3))
            dadd.close()
    if(lever2)==("1"+"!"+"python3"):
            ls=(input("CMD____________ls_______________lever3 ::>"))
            pycoc=open('duyen.py','a+')
            pycoc.write(str(ls)+'\n')
            pycoc.write('##'+str(lever3)+'\n')
            pycoc.close()
            subprocess.run(['python3 duyen.py'], capture_output=True, text=True, shell=True, check=True)
    if(lever2)==("1"+"!"+"JS"):
            ls=(input("JS____________ls_______________lever3 ::>"))
            JSCODE=open('duyen.js','a+')
            JSCODE.write(str(ls)+'\n')
            JSCODE.write('//'+str(lever3)+'\n')
            JSCODE.close()
            subprocess.run(['node duyen.js'], capture_output=True, text=True, shell=True, check=True)
    return (lever1,lever2,lever3,current_hour_minute)  # Khởi tạo x bằng 1 (điểm dừng)
## Với thuật toán này ta có thể mở tối đa 14 lớp layer cho 16 chuổi số 0 liên tiếp nhau.
## Nếu coi mỗi lớp chịu trách nhiệm chạy một hệ biên dịch thì có thể hỗ trợ tối đa 14 ngôn ngữ lập trình
def main():
    x=kos
    x_values = []
    while (abs(1-x)>1e-8):
        y = (11 - 5 * x) / 6
        #giá trị không nhất thiết phải là (11-5*x/6) mà là có dạng ((2a+1)-ax)/(a+1) với a là số nguyên dương
        #số (abs(1-x)))>1e-n với n là số nguyên dương có thể lớn tùy theo các layer của blockchain có muốn chứa nhiêù blockchain khác hay không và tùy theo nhu cấu về tính khả thi 
        #của hệ thống máy tính node có thể mở rộng thường số a và số n là số lớn nhưng tôi chỉ đưa ra ví dụ đơn giản....
        x_values.append(x)
        x = y  # Gán x = y để tiếp tục lặp
        print(coin_main(str(x),lever2,lever3,current_hour_minute))
    return x_values
getlink=[]
if __name__ == "__main__":
    j=1
    while(j<2000):
        result = main()
        for i, x_val in enumerate(result):
            coin=str(f"{x_val:.36f}")
            coin_block=float(coin[9:38])
            getlink.append(coin_block)
        j=j+1
        coin=getlink[-1]
        x=coin_block
        print(coin_block)
        if (j==2000):
            break


 ## đã hoàn thành xong một block, các dòng dưới sẻ tạo block tiếp theo, tiếp tục gán coin cho x


