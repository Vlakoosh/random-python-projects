input_image = [
    ['   ','   ','   ','   ','   ','   ','   ','   '],
    ['   ','   ','###','###','   ','   ','   ','   '],
    ['   ','###','###','###','###','   ','   ','   '],
    ['   ','###','###','###','###','###','   ','   '],
    ['   ','   ','###','###','###','###','###','   '],
    ['   ','###','###','###','###','###','   ','   '],
    ['   ','###','###','###','###','   ','   ','   '],
    ['   ','   ','###','###','   ','   ','   ','   '],
    ['   ','   ','   ','   ','   ','   ','   ','   ']]


result = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
for j in range(len(input_image)):
    for i in range(len(input_image[0])):
        result[i-1].append(input_image[j][i-1])

for j in range(len(result)):
    for i in range(len(result[0])):
        print(result[j][i], end="")
    print("\n")