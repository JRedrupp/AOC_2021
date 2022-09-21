use std::io::{stdin, stdout, Write};

fn main() {
    let query = get_user_input();
    let result: Result = analyse(query);
    println!("Answer: {:?}", result)
}

fn get_user_input() -> Vec<i32> {
    let mut input = String::new();

    print!("Please enter your query separated by ',' \n >> ");
    let _ = stdout().flush();
    stdin().read_line(&mut input).expect("Did not enter a correct string");
    println!("Running Analysis on {}", input);
    let query: Vec<i32> = parse_user_input(input);
    query
}

fn parse_user_input(input: String) -> Vec<i32> {
    let split = input.split(",");
    let mut final_array: Vec<i32> = Vec::new();
    for v in split {
        let number: i32 = v
            .trim()
            .parse()
            .expect("This string cannot be converted to a number");
        final_array.push(number)
    }
    final_array
}


fn analyse(mut data: Vec<i32>) -> Result {
    let mut n: i32;
    let mut increase_decrease: Vec<String> = Vec::new();
    n = data.remove(0);
    for val in data {
        if val < n {
            increase_decrease.push("DECREASED".to_string())
        } else if val > n {
            increase_decrease.push("INCREASED".to_string())
        }
        n = val
    }
    println!("Increased/Decreased List: {:?}", increase_decrease);
    let increased_count: usize = increase_decrease.iter().filter(|&n| *n == "INCREASED").count();
    let decreased_count: usize = increase_decrease.iter().filter(|&n| *n == "DECREASED").count();

    println!("INCREASED: {} \nDECREASED: {}", increased_count, decreased_count);

    return if increased_count < decreased_count {
        Result::DECREASED
    } else if increased_count > decreased_count {
        Result::INCREASED
    } else {
        Result::CONSTANT
    };
}

#[derive(Debug)]
enum Result {
    INCREASED,
    DECREASED,
    CONSTANT,
}

