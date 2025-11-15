###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    code = ord(char) + 1
    enc = chr(code)
    encrypted_text += enc


print(plain_text)
print(encrypted_text)