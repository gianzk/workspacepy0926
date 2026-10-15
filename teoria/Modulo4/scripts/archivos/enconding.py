
# lectura sin encoding
# with open('textto_español.txt', mode='r') as f:
#     content = f.read()

# }lectura con encoding
with open('textto_español.txt', mode='r', encoding='utf-8') as f:
    content = f.read()

print(content)