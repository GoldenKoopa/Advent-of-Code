import sys
sys.path.append('.')

with open('12/input.txt', 'r') as file:
    contents = file.read().splitlines()
    
contents = [(elem.split()[0], eval(elem.split()[1])) for elem in contents]

def get_configurations(pattern, lengths):
    qmark_indices = [i for i in range(len(pattern)) if pattern[i] == '?']
    qmark_count = len(qmark_indices)
    options = 1 << qmark_count
    total_needed_spring_count = sum(lengths) - pattern.count('#')
    total = 0
    for i in range(options):
        option = str(bin(i)).rjust(qmark_count, '0')
        if option.count('1') != total_needed_spring_count: continue
        new_pattern = list(pattern)
        for j in range(qmark_count):
            new_pattern[qmark_indices[j]] = '#' if option[len(option) - j - 1] == '1' else '.'
        
        if check_for_valid(new_pattern, lengths):
            total += 1
    
    return total



def check_for_valid(pattern, lengths):
    spring_count = 0
    pattern_lengths = []
    
    for i in range(len(pattern)):
        if pattern[i] == '#':
            spring_count += 1
        
        if pattern[i] == '.' and spring_count > 0:
            pattern_lengths.append(spring_count)
            spring_count = 0
    
    if spring_count != 0:
        pattern_lengths.append(spring_count)
    
    if len(lengths) != len(pattern_lengths):
        return False
    
    for i in range(len(pattern_lengths)):
        if lengths[i] != pattern_lengths[i]:
            return False
    
    return True
        

total = 0
for line, lengths in contents:
    configs = get_configurations(line, lengths)
    total += configs
    
    
print(total)
  