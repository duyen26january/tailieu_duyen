use std::io;

fn main() {
    println!("Nhập hệ số a, b, c của phương trình bậc hai:");

    let mut a = String::new();
    io::stdin().read_line(&mut a).expect("Failed to read line");
    let a: f64 = a.trim().parse().expect("Please type a number!");

    let mut b = String::new();
    io::stdin().read_line(&mut b).expect("Failed to read line");
    let b: f64 = b.trim().parse().expect("Please type a number!");

    let mut c = String::new();
    io::stdin().read_line(&mut c).expect("Failed to read line");
    let c: f64 = c.trim().parse().expect("Please type a number!");

    let delta = b.powi(2) - 4.0 * a * c;

    if delta > 0.0 {
        let x1 = (-b + delta.sqrt()) / (2.0 * a);
        let x2 = (-b - delta.sqrt()) / (2.0 * a);
        println!("Phương trình có hai nghiệm phân biệt: x1 = {}, x2 = {}", x1, x2);
    } else if delta == 0.0 {
        let x = -b / (2.0 * a);
        println!("Phương trình có nghiệm kép: x = {}", x);
    } else {
        println!("Phương trình vô nghiệm");
    }
}