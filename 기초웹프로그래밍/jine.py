print("자판기 관리 프로그램, 관리자: 박진이, 202020817")
print("======================기능======================")
print('1: 음료추가 2: 음료삭제 3: 자판기이용 4: 종료')
print('============================================')
음료목록=[]

while(True):
    fun= int(input('기능 선택 :'))
    if fun ==4: 
        print("자판기 관리 프로그램 종료")
        break
    if fun ==1 :
        print("음료 목록:", 음료목록)
        음료=input("추가할 음료는? : ")
        음료목록.append(음료)
        print("음료 목록:", 음료목록)
    if fun==2:
        print("음료 목록:", 음료목록)
        삭제음료=input("삭제할 음료는? : ")
        음료목록.remove(삭제음료)
        print("음료 목록:", 음료목록)
    if fun==3:
        money=int(input("동전을 넣으세요(500원이상): "))
        while(True):
            print("(현재 금액: "+str(money)+"원) 음료 목록:",음료목록)
            num = int(input("음료를 선택하세요(순서대로 1,2,3... 입력, 거스름돈 받기: 0):"))
            if num==0:
                print("거스름돈은 "+str(money)+"원 입니다.")
                break
            money = money - 500
            print(음료목록[num-1]+"가 나왔습니다")
    print("-------------------------------")    