with open('day2/input.txt', 'r') as f:
    input = f.read().splitlines()

bag = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

true_id_sum = 0
final_power_sum = 0

for game in input:
    game_id = int("".join([number for number in game.split(":")[0] if number.isnumeric()]))

    possible = True
    minimun_bag = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    power_sum = 0

    for set in game.split(":")[1].split(";"):
        for cube in set.split(","):
            number_of_cubes = int("".join([number for number in cube if number.isnumeric()]))
            color = [color for color in bag if color in cube][0]
            
            if minimun_bag[color] < number_of_cubes:
                minimun_bag[color] = number_of_cubes
            
            if number_of_cubes > bag[color]:
                possible = False

    game_power_sum = 1
    for color, number_of_cubes in minimun_bag.items():
        game_power_sum *= number_of_cubes

    final_power_sum += game_power_sum
        
    if possible:
        true_id_sum += int(game_id)

print("possible game ids sum: ", true_id_sum)
print("games power sum: ", final_power_sum)
    