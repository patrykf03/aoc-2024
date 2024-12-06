from collections import defaultdict

# Read file into lists
with open('input') as input_file:
    rules_section, updates_section = input_file.read().split("\n\n")
    raw_rules = [list(map(int, rule.split("|"))) for rule in rules_section.splitlines()]
    update_list = [list(map(int, update.split(","))) for update in updates_section.splitlines()]

# empty dictionary
rule_dictionary = defaultdict(list)

# populate dictionary where key is the page that has to be leftmost and the values are the pages that need to appear after
for rule_source, rule_target in raw_rules:
    # add the value to the right key
    rule_dictionary[rule_source].append(rule_target)

# wrong middle sum
wrong_sum, correct_sum = 0, 0

for current_update in update_list:
    # make an empty dictionary of rules that will apply to this update 
    applicable_rules = defaultdict(list)
    for page in current_update:
        # 1. check if we need the entire key
        if page in rule_dictionary:
            # 2. iteratively check if the values are in the update
            for target_page in rule_dictionary[page]:
                if target_page in current_update:
                    applicable_rules[page].append(target_page)

    # validate the update by checking if all rules are followed
    is_valid_update = 1
    for rule_source in applicable_rules:
        for rule_target in applicable_rules[rule_source]:
            if current_update.index(rule_target) < current_update.index(rule_source):
                is_valid_update = 0
                
    if is_valid_update: 
        # if valid, add the middle value to the correct sum
        middle = current_update[len(current_update) // 2]
        correct_sum += middle
    else:
        # if invalid, find the key that has exactly half the values and add the key to the wrong sum
        for rule_source in applicable_rules:
            if (len(applicable_rules[rule_source]) == len(current_update) // 2):
                wrong_sum += rule_source

print(f"Part 1: {correct_sum}")
print(f"Part 2: {wrong_sum}")