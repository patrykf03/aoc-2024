from collections import defaultdict

with open('input') as input_file:
    rules_section, updates_section = input_file.read().split("\n\n")
    raw_rules = [list(map(int, rule.split("|"))) for rule in rules_section.splitlines()]
    update_list = [list(map(int, update.split(","))) for update in updates_section.splitlines()]

rule_dictionary = defaultdict(list)
    
for rule_source, rule_target in raw_rules:
    rule_dictionary[rule_source].append(rule_target)
    rule_dictionary[rule_source].sort()

middle_sum = 0

for current_update in update_list:
    applicable_rules = defaultdict(list)
    for page in current_update:
        if page in rule_dictionary:
            for target_page in rule_dictionary[page]:
                if target_page in current_update:
                    applicable_rules[page].append(target_page)

    is_valid_update = 1
    for rule_source in applicable_rules:
        for rule_target in applicable_rules[rule_source]:
            if current_update.index(rule_target) < current_update.index(rule_source):
                is_valid_update = 0

    if is_valid_update:
        middle_sum += current_update[len(current_update) // 2]
        print(f"Update {current_update} is valid")
    else:
        print(f"Update {current_update} is invalid")

print(f"Middle sum is {middle_sum}")
