SUCCESS = 1
FAILED = 0
cursor = 0
string = ""

def current_char():
    if cursor < len(string):
        return string[cursor]
    return '\0'

# Grammar rule: E -> T E'
def E():
    global cursor
    print(f"{string[cursor:]: <16} E -> T E'")
    if T():
        if Edash():
            return SUCCESS
        else:
            return FAILED
    else:
        return FAILED

# Grammar rule: E' -> + T E' | $
def Edash():
    global cursor
    if current_char() == '+':
        print(f"{string[cursor:]: <16} E' -> + T E'")
        cursor += 1
        if T():
            if Edash():
                return SUCCESS
            else:
                return FAILED
        else:
            return FAILED
    else:
        print(f"{string[cursor:]: <16} E' -> $")
        return SUCCESS

# Grammar rule: T -> F T'
def T():
    global cursor
    print(f"{string[cursor:]: <16} T -> F T'")
    if F():
        if Tdash():
            return SUCCESS
        else:
            return FAILED
    else:
        return FAILED

# Grammar rule: T' -> * F T' | $
def Tdash():
    global cursor
    if current_char() == '*':
        print(f"{string[cursor:]: <16} T' -> * F T'")
        cursor += 1
        if F():
            if Tdash():
                return SUCCESS
            else:
                return FAILED
        else:
            return FAILED
    else:
        print(f"{string[cursor:]: <16} T' -> $")
        return SUCCESS

# Grammar rule: F -> ( E ) | i
def F():
    global cursor
    if current_char() == '(':
        print(f"{string[cursor:]: <16} F -> ( E )")
        cursor += 1
        if E():
            if current_char() == ')':
                cursor += 1
                return SUCCESS
            else:
                return FAILED
        else:
            return FAILED
    elif current_char() == 'i':
        print(f"{string[cursor:]: <16} F -> i")
        cursor += 1
        return SUCCESS
    else:
        return FAILED

if __name__ == "__main__":
    string = input("Enter the string: ")
    cursor = 0
    print("\nInput           Action")
    print("---------------------------------")
    
    # Start parsing from E
    if E() and cursor == len(string):
        print("---------------------------------")
        print("String is successfully parsed")
    else:
        print("---------------------------------")
        print("Error in parsing String")
