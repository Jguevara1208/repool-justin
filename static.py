command_list = '''
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
               The commands are as follows:
    _________________________________________________
    |        Command        |        Command        |
    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
    |  - SET <Key> <Value>  |   - GET: GET <Key>    |
    |  - SUM                |   - BEGIN             |
    |  - COMMIT             |   - ROLLBACK          |
    |  - CURRENT            |   - END               |
    |  - STACK              |                       |
    |                       |                       |
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
   '''

invalid_key = '''
    _______________________________
    |                             |
    |   That key does not exist   |
    |                             |
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾'''

set_requires = 'set requires at least three arguments seperated by spaces: SET <Key> <Value> \n'

def generate_get_string(curr_len, value):
    return f'''
    {'_' * curr_len}
    {'|'+ ' ' * (curr_len - 2) + '|'}
    |    The value you are looking for is: {value}    |
    {'|'+ ' ' * (curr_len - 2) + '|'}
    {'‾' * curr_len}
        '''


def generate_sum_string(sum_len, sum):
    return f'''
    {'_'* (sum_len + 1)}
    {'|'+ ' ' * (sum_len - 1) + '|'}
    |  The sum of your current dictionary is: {sum}  |
    {'|'+ ' ' * (sum_len - 1) + '|'}
    {'‾'* (sum_len + 1)}'''

def _get_current(stack):
    return stack[-1][-1] if isinstance(stack[-1], list) else stack[-1]
