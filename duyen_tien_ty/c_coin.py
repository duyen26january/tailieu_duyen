import subprocess
import decimal
import ccxt
import pandas as pd
def duyen2601():
    api_key="cjkP5LELert09RlTLz5St3wOqaytum6YHqQMLy82nc2JLB4svyuFARb7xa4fF1aZ"
    secret_key="x03QoF8nq2R4lfKfotooblP5l8ypSeUkHIs5JeCnX2jx1RvCYLzCisXnSv4lnyDa"
kos = float(input("X="))  # Khởi tạo x bằng 1 (điểm dừng)
def main():
    x=kos
    x_values = []
    while (abs(1-x)>1e-8):
        y = (11 - 5 * x) / 6
        x_values.append(x)
        x = y  # Gán x = y để tiếp tục lặp
        duyen2601()
    return x_values
getlink=[]
if __name__ == "__main__":
    j=1
    while(j<900000):
        result = main()
        for i, x_val in enumerate(result):
            coin=str(f"{x_val:.36f}")
            coin_block=float(coin[9:38])
            getlink.append(coin_block)
        j=j+1
        coin=getlink[-1]
        x=coin_block
print( coin)

 ## đã hoàn thành xong một block, các dòng dưới sẻ tạo block tiếp theo, tiếp tục gán coin cho x
file1=open('coin.txt','r+')
for k,coin in enumerate(result):
    file1.write('<data!!!>')
    file1.write(str(getlink[k]))
    file1.write('<!!!data>')
file1.close()

