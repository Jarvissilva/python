fizzubuzz = []
for i in range(1,33):
    if i%3 == 0 and i%5==0:
        fizzubuzz.append("fizzbuzz")
        continue
    elif i%3 == 0:
        fizzubuzz.append("fizz")
        continue
    elif i%5==0:
        fizzubuzz.append("buzz")
        continue
    fizzubuzz.append(i)
    
print(fizzubuzz)