use std::fs;

const FILE_PATH: &str = "input.txt";
//const FILE_PATH: &str = "test.txt";

fn main() {
    let file = fs::read_to_string(FILE_PATH).expect("Should have been able to read the file");
    println!("Analysing file {}", FILE_PATH);
    let report = ReportStream::from_str(file.as_str());
    println!("Analysing report {:?}", report);

    println!("Calculating o2");
    let o2: usize = report.clone().calculate_o2();
    println!("o2 is  => {}", o2);

    println!("Calculating co2");
    let co2: usize = report.clone().calculate_co2();
    println!("co2 is  => {}", co2);

    println!("Answer is {}", o2*co2);

    println!("Answer is {}", o2*co2 == 6124992);

}

#[derive(Debug, Clone)]
struct ReportStream {
    data : Vec<String>,
    bit_len: usize
}

impl ReportStream {
    fn from_str(file_string: &str) -> Self {
        let mut data : Vec<String> = Vec::new();
        let split = file_string.split("\n");
        for s in split{
            let temp_str = s.to_string();
            if temp_str.is_empty(){
                continue
            }
            data.push(temp_str);
        }
        let bit_len: usize = data[0].len();

        return Self { data, bit_len }

    }

    fn calculate_o2(mut self) -> usize{

        for i in 0..self.bit_len {
            if self.data.len() == 1{
                break
            }
            let mut b_0 = 0;
            let mut b_1 = 0;
            for byte in &self.data{
                let bit = byte.chars().nth(i).unwrap().to_string();
                match bit.as_str() {
                    "0" => b_0 += 1,
                    "1" => b_1 += 1,
                    _ => {}
                }
            }
            if b_1 >= b_0{
                self.remove_bit_n_in_pos("1", i)
            } else {
                self.remove_bit_n_in_pos("0", i)
            }
        }

        let final_val = &self.data[0];

        return isize::from_str_radix(final_val, 2).unwrap() as usize
    }

    fn calculate_co2(mut self) -> usize{
        for i in 0..self.bit_len {
            if self.data.len() == 1{
                break
            }
            let mut b_0 = 0;
            let mut b_1 = 0;
            for byte in &self.data{
                let bit = byte.chars().nth(i).unwrap().to_string();
                match bit.as_str() {
                    "0" => b_0 += 1,
                    "1" => b_1 += 1,
                    _ => {}
                }
            }
            if b_0 > b_1{
                self.remove_bit_n_in_pos("1", i)
            } else {
                self.remove_bit_n_in_pos("0", i)
            }
        }

        let final_val = &self.data[0];

        return isize::from_str_radix(final_val, 2).unwrap() as usize
    }

    fn remove_bit_n_in_pos(&mut self, bit_to_keep: &str, x_pos: usize) {
        let mut ind_to_del = Vec::new();
        for vec_pos in self.data.iter().enumerate(){
            if vec_pos.1.chars().nth(x_pos).unwrap().to_string().as_str() != bit_to_keep{
                ind_to_del.push(vec_pos.0)
            }
        }
        ind_to_del.reverse();
        for i in ind_to_del{
            self.data.remove(i);
        }
    }
}


