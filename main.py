def get_data() -> list:
    file: str = input("data: ") + ".txt"

    with open(file) as f:
        return f.read().split('\n')

def parse_data(data: list) -> list:
    temp: list = []

    for i in data:
        if i:
            game = i.split()
            r: list = []
            g: list = []
            b: list = []
        
            # get color count
            for k,v in enumerate(game):
                if 'red' in v:
                    r.append(int(game[k-1]))
                elif 'green' in v:
                    g.append(int(game[k-1]))
                elif 'blue' in v:
                    b.append(int(game[k-1]))

            temp.append((int(game[1][:-1]),[max(r), max(g), max(b)]))

    return temp

def calc_data(data: list, cubes: list) -> int:
    sum_of_games: int = 0

    # compare cubes to pulls in games
    for k,v in enumerate(data):
        red = v[1][0] <= cubes[0]
        green = v[1][1] <= cubes[1] 
        blue = v[1][2] <= cubes[2]
            
        if red and green and blue:
                sum_of_games += v[0]
    
    return sum_of_games

def calc_power(data: list) -> int:
    sum_of_power: int = 0
    
    for v in data:
        sum_of_power += v[1][0]*v[1][1]*v[1][2]

    return sum_of_power

def part1() -> None:
    data = parse_data(get_data())
    c_data = calc_data(data, [12,13,14])
    print(c_data)

def part2() -> None:
    data = parse_data(get_data())
    data_power = calc_power(data)
    print(data_power)

part2()
