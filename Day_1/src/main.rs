use std::io::{stdin, stdout, Write};
use std::slice::Windows;

const AVERAGE_WINDOW: usize = 3;

fn main() {
    let result: Result;
    let part_2 = is_play_part_2();
    let query = get_user_input();
    if part_2 {
        result = analyse_pt2(query);
    } else {
        result = analyse_pt1(query);
    }
    println!("Answer: {:?}", result)
}

fn analyse_pt2(query: Vec<f32>) -> Result {
    let avg = rolling_average(query, AVERAGE_WINDOW);
    return analyse_pt1(avg);
}

fn rolling_average(input: Vec<f32>, window: usize) -> Vec<f32> {
    fn average(numbers: &[f32]) -> f32 {
        numbers.iter().sum::<f32>() as f32 / numbers.len() as f32
    }

    let mut result: Vec<f32> = Vec::new();
    let window_iterator: Windows<f32> = input.windows(window);
    for item in window_iterator {
        result.push(average(item))
    }
    return result;
}

fn is_play_part_2() -> bool {
    const CHOICE_MESSAGE: &'static str = "Please Choose part '1' or '2' \n >> ";
    const RESPONSE_SUCCESS_MESSAGE: &'static str = "Running Scenario";
    let input = get_input(CHOICE_MESSAGE, RESPONSE_SUCCESS_MESSAGE);
    match input.as_str() {
        "1" => false,
        "2" => true,
        _ => panic!(
            "Did not select part 1 or 2! \n User Selected {:?}",
            input.as_str()
        ),
    }
}

fn get_input(choice_message: &str, response_success_message: &str) -> String {
    let mut input = String::new();
    print!("{}", choice_message);
    let _ = stdout().flush();
    stdin()
        .read_line(&mut input)
        .expect("Did not enter a correct string");
    println!("{} {}", response_success_message, input);
    // to remove newline at end
    input.pop();
    return input;
}

fn get_user_input() -> Vec<f32> {
    const CHOICE_MESSAGE: &'static str = "Please enter your query separated by ',' \n >> ";
    const RESPONSE_SUCCESS_MESSAGE: &'static str = "Running Analysis on";
    let query: Vec<f32> = parse_user_input(get_input(CHOICE_MESSAGE, RESPONSE_SUCCESS_MESSAGE));
    query
}

fn parse_user_input(input: String) -> Vec<f32> {
    let split = input.split(",");
    let mut final_array: Vec<f32> = Vec::new();
    for v in split {
        let number: f32 = v
            .trim()
            .parse()
            .expect("This string cannot be converted to a number");
        final_array.push(number)
    }
    final_array
}

fn analyse_pt1(mut data: Vec<f32>) -> Result {
    let mut n: f32;
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
    let increased_count: usize = increase_decrease
        .iter()
        .filter(|&n| *n == "INCREASED")
        .count();
    let decreased_count: usize = increase_decrease
        .iter()
        .filter(|&n| *n == "DECREASED")
        .count();

    println!(
        "INCREASED: {} \nDECREASED: {}",
        increased_count, decreased_count
    );

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
