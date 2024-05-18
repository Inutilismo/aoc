from collections import defaultdict


with open("day3/input.txt", "r") as f:
    input = f.read().splitlines()

part_numbers = []

symbols_matrix = defaultdict(bool)
part_numbers_matrix = defaultdict(bool)

adjs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

for line_index in range(len(input)):
    chars = list(input[line_index])

    for char_index in range(len(chars)):
        if not chars[char_index].isalnum() and chars[char_index] != ".":
            symbols_matrix[(line_index, char_index)] = True

for line_index in range(len(input)):
    chars = list(input[line_index])

    for char_index in range(len(chars)):
        is_part_number = False
        char = chars[char_index]

        if char.isnumeric() and not part_numbers_matrix[(line_index, char_index)]:
            number = char

            for adj in adjs:
                if symbols_matrix[(line_index + adj[0], char_index + adj[1])]:
                    is_part_number = True
                    part_numbers_matrix[(line_index, char_index)] = True

            if is_part_number:
                aux_index = char_index - 1
                while aux_index >= 0 and chars[aux_index].isnumeric():
                    number = chars[aux_index] + number
                    part_numbers_matrix[(line_index, aux_index)] = True 
                    aux_index -= 1

                aux_index = char_index + 1
                while aux_index < len(chars) and chars[aux_index].isnumeric(): 
                    number = number + (chars[aux_index])
                    part_numbers_matrix[(line_index, aux_index)] = True
                    aux_index += 1
                part_numbers.append(int(number))

print(sum(part_numbers))
