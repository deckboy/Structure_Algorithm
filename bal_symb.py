import stacks

def match_symb(symb_str):
    symb_pairs = {
        '(' : ')',
        '[' : ']',
        '{' : '}',
        '<' : '>'
    }
    
    openers = symb_pairs.keys()
    my_stack = stacks.Stack()
    
    index = 0
    
    while index<len(symb_str):
        symb = symb_str[index]
        
        if symb in openers:
            my_stack.push(symb)
            
        else:
            if my_stack.is_empty():
                return False
                
            else:
                top_item = my_stack.pop()
                if symb != symb_pairs[top_item]:
                    return False
        index +=1
        
    if my_stack.is_empty():
        return True

print(match_symb('({[]})'))
print(match_symb('({([{}]]})'))