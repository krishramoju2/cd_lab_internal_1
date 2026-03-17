def check_acceptance(tokens):
   table = {
       'E':  {'id': ['T', "E'"], '(': ['T', "E'"]},
       "E'": {'+': ['+', 'T', "E'"], ')': [], '$': []},
       'T':  {'id': ['F', "T'"], '(': ['F', "T'"]},
       "T'": {'+': [], '*': ['*', 'F', "T'"], ')': [], '$': []},
       'F':  {'id': ['id'], '(': ['(', 'E', ')']}
   }
   stack = ['$', 'E']
   tokens.append('$')
   i = 0
   while stack:
       top = stack.pop()
       current = tokens[i]
       if top == current:
           i += 1
       elif top in table:
           if current in table[top]:
               for symbol in reversed(table[top][current]):
                   stack.append(symbol)
           else:
               return False # Rejected: No table entry
       else:
           return False # Rejected: Terminal mismatch     
   return i == len(tokens)
print(check_acceptance(['id', '+', 'id']))
print(check_acceptance(['id', '*','+' 'id']))
