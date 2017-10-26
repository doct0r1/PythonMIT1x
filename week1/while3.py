iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1  # for starting from 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
