import sys
sys.path.append('.')

workflows_raw, parts_raw = open('19/input.txt').read().split('\n\n')

parts = [{category.split('=')[0]: int(category.split('=')[1]) for category in part[1:-1].split(',')} for part in parts_raw.splitlines()]
workflows = {workflow.split('{')[0]: [elem for elem in workflow.split('{')[1][:-1].split(',')] for workflow in workflows_raw.splitlines()} 

def get_workflow(part, workflow):
    if workflow in ['A', 'R']: return workflow
    for elem in workflows[workflow]:
        if '>' not in elem and '<' not in elem: return get_workflow(part, elem)
        if eval(f'{part[elem[0]]}{elem.split(':')[0][1:]}'):
            return get_workflow(part, elem.split(':')[1])
        
total = 0
for part in parts:
    if get_workflow(part, 'in') == 'A':
        total += sum(list(part.values()))
        
print(total)