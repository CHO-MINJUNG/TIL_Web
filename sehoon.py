loop_value = int(input('loop value ::: '))
value = int(input('배수 value ::: '))
sum = 0
while True:
    sum+=value
    if sum>loop_value:
        break
    print(sum)