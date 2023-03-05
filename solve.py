game_link = 'https://hyperjumps.quantamagazine.org/'

sequence_length = 8
sequence_numbers = [3, 5, 3, 6, 2, 7, 4, 1]


def print_pattern(seq, last_num=9):
    for n in seq:
        print(n, end=" -> ")
    print(last_num)


def generate_all_starting_pair(sequence_numbers):
    starting_numbers = set()
    for i in range(len(sequence_numbers)):
        for j in range(len(sequence_numbers)):
            if i != j:
                starting_numbers.add(
                    (sequence_numbers[i], sequence_numbers[j]))
    return starting_numbers


def remove_element(num, arr):
    try:
        arr.remove(num)
        return True, arr
    except:
        return False, arr


def next_possible_number(a, b):
    outcomes = set()
    if a <= 0 or b <= 0:
        return outcomes
    outcomes = set(((a+b) % 10, (a*b) % 10))
    if (a-b) > 0:
        outcomes.add((a-b) % 10)
    if a % b == 0:
        outcomes.add(int((a/b)) % 10)
    return outcomes


def is_correct_pattern(a, b, obj=9):
    return 9 in next_possible_number(a, b)


def next_possible_picks(ans_seq):
    outcomes = set()
    ans_seq_length = len(ans_seq)
    if ans_seq_length > 2:
        outcomes.update(next_possible_number(
            ans_seq[ans_seq_length-3] * 10 + ans_seq[ans_seq_length-2], ans_seq[ans_seq_length-1]))
    outcomes.update(next_possible_number(
        ans_seq[ans_seq_length-2], ans_seq[ans_seq_length-1]))
    return outcomes


def print_if_correct_sequence(ans_seq):
    ans_seq_length = len(ans_seq)
    if ans_seq_length == sequence_length and sequence_length == 2:
        if is_correct_pattern(ans_seq[ans_seq_length-2], ans_seq[ans_seq_length-1]):
            print_pattern(ans_seq)
    elif ans_seq_length == sequence_length and sequence_length > 2:
        if is_correct_pattern(ans_seq[ans_seq_length-3] * 10 + ans_seq[ans_seq_length-2], ans_seq[ans_seq_length-1]):
            print_pattern(ans_seq)


def generate_solution(ans_seq, remaining_nums):
    if len(ans_seq) == sequence_length:
        print_if_correct_sequence(ans_seq)
    elif len(ans_seq) <= sequence_length:
        possible_numbers = next_possible_picks(ans_seq)
        for num in possible_numbers:
            success,  next_remaining_nums = remove_element(
                num, remaining_nums.copy())
            if success:
                next_ans_seq = ans_seq.copy()
                next_ans_seq.append(num)
                generate_solution(next_ans_seq, next_remaining_nums)


starting_numbers = generate_all_starting_pair(sequence_numbers)

for starting_pair in starting_numbers:
    ans_seq = []
    x, y = starting_pair
    _, remaining_nums = remove_element(x, sequence_numbers.copy())
    _, remaining_nums = remove_element(y, remaining_nums)
    ans_seq.extend([x, y])
    generate_solution(ans_seq, remaining_nums)
