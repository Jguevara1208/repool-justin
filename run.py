import os
from static import command_list, invalid_key, generate_sum_string, generate_get_string, _get_current, set_requires

stack = [{}]

def _set(split_cmd, cmd):
    key, value = None, None
    current = _get_current(stack)

    if len(split_cmd) < 3:
        print(f'You gave me: {cmd}\n')
        print(set_requires)
        new_set_cmd = input('please enter the command again: ')
        _validate_cmd(new_set_cmd)
    else:
        key = split_cmd[1]
        value = ' '.join(split_cmd[2::])

    current[key] = value
    _continue()



def _get(key):
    current = _get_current(stack)
    if key not in current:
        print(invalid_key)
        _continue()
    else:
        curr_len = len(current[key]) + 44
        print(generate_get_string(curr_len, current[key]))
        _continue()



def _sum():
    current = _get_current(stack)
    sum = 0

    for key in current:
        if current[key].isdigit():
            sum += int(current[key])
    sum_len = len(str(sum)) + 44

    print(generate_sum_string(sum_len, sum))
    _continue()



def _begin():
    inTransaction = isinstance(stack[-1], list)
    current = _get_current(stack)
    copy = { key: val for key, val in current.items()}

    if inTransaction:
        stack[-1].append(copy)
    else:
        stack.append([copy])

    _continue()



def _commit():
    inTransaction = isinstance(stack[-1], list)
    if inTransaction:
        temp = stack[-1].pop()
        stack.pop()
        stack.append(temp)
    else:
        print('Nothing to commit')
    _continue()



def _rollback():
    if len(stack) > 1:
        stack.pop()
    else:
        print('Error: Not in a transaction')
    _continue()



def _current():
    print(_get_current(stack))
    _continue()



def _stack():
    print(stack)
    _continue()



def _end():
    print('Thank you for your time.')



functionMap = {
    'get': _get,
    'set': _set,
    'sum': _sum,
    'begin': _begin,
    'commit': _commit,
    'rollback': _rollback,
    'stack': _stack,
    'current': _current,
    'end': _end
}



def _validate_cmd(cmd): 
    os.system('cls' if os.name == 'nt' else 'clear')
    if len(cmd) == 0: _continue()

    split_cmd = cmd.split()
    command = split_cmd[0]

    if len(split_cmd) == 0 or command.lower() not in functionMap:
        print(f'\n            {command} is not a valid command\n')
        _continue()
    elif command.lower() == 'set':
        _set(split_cmd, cmd) 
    elif command.lower() == 'get':
        key = ' '.join(split_cmd[1::])
        _get(key)
    else:
        functionMap[command]()



def _continue():
    current = _get_current(stack)
    print(command_list)
    print('   Current keys in your dictionary: ' + ', '.join([key for key in current]) + '\n')
    res = input('   Please type one of the commands.\n\n    ')
    _validate_cmd(res)



_continue()
