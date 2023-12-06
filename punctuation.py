str_text = "This is @ Tejas's <Code>...!"

punctuation = '''!#%^&*()@$<,>>??:;"'""{}[]\|~.`'''

for els in str_text :
    if els in punctuation:
        str_text = str_text.replace(els,"")

print(str_text)