password=input("Enter Password=")

lower_case= [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

upper_case= [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers=["0","1","2","3","4","5","6","7","8","9"]

special_characters=  [
    ':', '?', '!', '\'', '^', '\"', '#', '$', '%', '&', '(', ')', '*', '+', 
    ',', '-', '.', '/', ';', '<', '=', '>', '@', '[', '\\', ']', '_', '`', 
    '{', '|', '}', '~'
]

dontsecure = [
    'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl',
    'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv',
    'uvw', 'vwx', 'wxy', 'xyz'
]

numberss=['123','234','345','456','567','678','789','321','432','543','654','765','876','987']

if len(password)<=5:
    print("Your password is short")
counter=0

for i in lower_case:
    for j in password:
        if i==j:
            counter=counter+1

if counter==0:
    print("Insecure Password(Use lower case )")

counter=0
for k in upper_case:
    for j in password:
        if k==j:
            counter=counter+1

if counter==0:
    print("Insecure Password(Use Upper Case )")

counter=0
for l in numbers:
    for k in password:
        if l==k:
            counter=counter+1

if counter==0:
    print("Insecure Password(Use numbers)")
counter=0
for i in special_characters:
    for k in password:
        if i==k:
            counter=counter+1

if counter==0:
    print("Insecure Password(Use speacial characters)")

counter=0

for k in range(0,len(dontsecure)):
    for j in range(0,len(password)):
        if dontsecure[k]==password[j:j+3]:
            counter=counter+1

if counter!=0:
    print("Insecure Password(Avoid sequential letters)")

counter=0

for k in range(0,len(numberss)):
    for j in range(0,len(password)):
        if numberss[k]==password[j:j+3]:
            counter=counter+1
if counter!=0:
    print("Insecure Password (Avoid sequential numbers)")