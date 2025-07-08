text = "Hello! My Name Is Santoshi"
vowel_count=0
space_count=0
symbol_count=0
consonants_count=0
vowels="aeiouAEIOU"
space=' '
symbol='!@#$%^&*'
for char in text:
    if char in vowels:
        vowel_count += 1
    elif char in space:
        space_count += 1
    elif char in symbol:
        symbol_count += 1    
    else:
        consonants_count +=1  

print("the number of vowels count is : ",vowel_count)
print("the number of space count is : ",space_count)
print("the number of symbol count is : ",symbol_count) 
print("the number of consonants count is : ",consonants_count) 