def solve_equation():
    x_values = []
    x = 1.0  # Khởi tạo x bằng 1 (điểm dừng)
    
    while x >= 1:
        y = (11 - 5 * x) / 6
        x_values.append(x)
        x = y  # Gán x = y để tiếp tục lặp
    
    return x_values

if __name__ == "__main__":
    result = solve_equation()
    print("Các giá trị x tại các thời điểm:")
    for i, x_val in enumerate(result):
        print(f"Thời điểm {i+1}: x = {x_val:.6f}")
