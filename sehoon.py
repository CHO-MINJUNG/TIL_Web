x = int(input('x 입력 ::: '))
y = int(input('y 입력 ::: '))
if x>0 and y>0:
    print("1사분면입니다.")
elif x<0 and y>0:
    print('2사분면입니다.')
elif x>0 and y<0:
    print('4사분면입니다.')
elif x<0 and y<0:
    print('3사분면입니다.')