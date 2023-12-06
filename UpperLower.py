str_text = "Tejas plays Chess"

lower=0
upper=0

for i in str_text:
    if i.islower():
        lower+=1
    elif i.isupper():
        upper+=1

print(f"lower case count = {lower}")
print(f"Upper case count = {upper}")