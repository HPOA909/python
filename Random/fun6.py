string1 = "*******MtSAC CIS Business Division********"
string2 = "Having fun."
string3 = string1.lstrip()
print(string1.lstrip("*")+string2)
print(string1.rstrip("*")+string2)
print(string1.strip("*")+string2)

txt = "50"

x = txt.zfill(4)

print(x)