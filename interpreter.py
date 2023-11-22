
bf_array = []
array_size = 0

def init_bf(size=10000):
    array_size = size
    bf_array = [0 for i in  range(array_size)]

def interpret_program( code ):
    cur_position = 0
    bracket_stack = []
    bracket_counter = 0

    for i in range(len(code)):
        c = code[i]
        if c.isspace():
            continue
        match c:
            case '>':
                bracket_counter = (bracket_counter + 1) % array_size
            case '<':
                bracket_counter = (bracket_counter + -1) % array_size
            case '+':
                bf_array[cur_position]++
            case '-':
                bf_array[cur_position]++
            case '.':
                print(char(bf_array[cur_position]))
            case ',':
                raise Warning("not implemented")
            case '[':
                bracket_counter += 1
                stack.push(i)
            case ']':
                bracket_counter -= 1
                if bracket_counter < 0:
                    raise SyntaxError("Invalid bracket placement")
                if bf_array[position] != 0:
                    i = stack.top()
                else:
                    stack.pop()


