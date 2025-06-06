import decimal
def solve_equation(x):
    # Khởi tạo giá trị y ban đầu
    y = (11 - 5 * x) / 6
    
    # Lặp lại cho đến khi x gần đạt đến 1.00000000000xxx
    while abs(x - 1.0) > 1e-33:
        x = y
        y = (11 - 5 * x) / 6
        k=x
        print(k)
    return y

# Đặt giá trị ban đầu của x
x_initial = int(input())

# Giải bài toán
result_y = solve_equation(x_initial)

print(f"Giá trị của y khi x tiến gần đến 1.00000000000xxx là: {result_y:.15f}")
if(result_y<1):
    z=1-result_y
    print(z)
