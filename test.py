import re

psw = 'Pranay@11'

reg =  r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'

pat = re.compile(reg)

mat = re.search(pat,psw)

if mat:
    print("Valid Password")
else:
    print("Invalid Password")