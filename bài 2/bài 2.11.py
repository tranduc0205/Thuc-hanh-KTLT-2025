import re 
mk = []
items = [x for x in input("nhập mật khẩu: ").split(',')]

for p in items :
    if len(p)<6 or len(p)>12:
        continue
    
    if not re. search("[a-z]",p):
        continue
    elif not re. search("[0-9]",p):
        continue
    elif not re. search("[A-Z]",p):
        continue
    elif not re. search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    
    mk.append(p)
    print(",".join(mk))
    print("sv:tran nguyen viet duc")
    print("235752020710013")


    