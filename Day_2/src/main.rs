use std::fs;
use std::str::FromStr;

const FILE_PATH: &str = "input.txt";

fn main() {
    let directions = fs::read_to_string(FILE_PATH).expect("Should have been able to read the file");
    println!("Analysing file {}", FILE_PATH);
    let mut position = Position {
        depth: 0,
        forward: 0,
        aim: 0,
    };
    let direction_vec = directions.split("\n");
    for turn in direction_vec{
        if turn.is_empty(){continue}
        let turn_duo = turn.split(" ").collect::<Vec<&str>>();
        println!("turn duo => {:?}", turn_duo);
        let dir: Direction = Direction::from_str(turn_duo[0]).expect("Could not parse Direction");
        let dist:i32 = i32::from_str(turn_duo[1]).expect("Could not parse distance");
        position.move_position(dir, dist)
    }

    println!("Final Position: {:?}", position);
    println!("Z * X: {:?}", position.mult_pos())


}

#[derive(Debug)]
enum Direction {
    Forward,
    Down,
    Up,
}

impl std::str::FromStr for Direction {

    type Err = ();

    fn from_str(input: &str) -> Result<Direction, Self::Err> {
        match input {
            "forward"  => Ok(Direction::Forward),
            "down"  => Ok(Direction::Down),
            "up"  => Ok(Direction::Up),
            _      => Err(()),
        }
    }
}

#[derive(Debug)]
#[derive(Copy, Clone)]
struct Position {
    depth: i32,
    forward: i32,
    aim: i32,
}

impl  Position {

    fn move_position(&mut self, direction: Direction, distance: i32){
        match  direction {
            Direction::Forward => {
                self.forward += distance;
                self.depth += self.aim * distance
            }
            Direction::Up => {
                self.aim -= distance
            }
            Direction::Down => {
                self.aim += distance
            }
        }
        println!("Moved {:?} by {}. Current Position => {:?}", direction, distance, self)
    }

    fn mult_pos(self) -> i32 {
        return self.depth * self.forward
    }

}