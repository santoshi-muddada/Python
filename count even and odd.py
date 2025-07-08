numbers = [24,31,54,61,70,83,95,68]

even_count = 0
odd_count = 0

for num in numbers :
    if num % 2 == 0:
       even_count += 1
    else:
        odd_count += 1
print("even number count is :",even_count)        
print("odd number count is :",odd_count)