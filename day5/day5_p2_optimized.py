from collections import defaultdict


# Read file into lists
with open('test') as input_file:
    rules_section, updates_section = input_file.read().split("\n\n")
    raw_rules = [rule.split("|") for rule in rules_section.splitlines()]
    update_list = [update.split(",") for update in updates_section.splitlines()]

# empty dictionary
rule_dictionary = defaultdict(set)

# populate dictionary where key is the page that has to be leftmost and the values are the pages that need to appear after
for rule_source, rule_target in raw_rules:
    # add the value to the right key
    rule_dictionary[rule_source].add(rule_target)

wrong_sum, correct_sum = 0, 0

for current_update in update_list:
    
    applicable_rules = defaultdict(list)
    for page in current_update:
        # 1. check if we need the entire key
        if page in rule_dictionary:
            # 2. iteratively check if the values are in the update
            for target_page in rule_dictionary[page]:
                if target_page in current_update:
                    applicable_rules[page].append(target_page)


    correct_order = [x[0] for x in sorted(applicable_rules.items(), key=lambda x: len(x[1]), reverse=True)]

    # check if order is correct
    # yes this is a hack cos its technically missing the last digit but idfc it works
    if correct_order == current_update[:-1]:
        correct_sum += int(correct_order[len(current_update) // 2])
    else:
        wrong_sum += int(correct_order[len(current_update) // 2])

print(f"Part 1: {correct_sum}")
print(f"Part 2: {wrong_sum}")