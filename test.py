#1.카테고리 제시(권고)후 뽑기(랜덤)/ 2.메뉴 선택(만약에 없으면 추가할 수 있도록)->퍼센트에이지 높임
#카테고리들중 자주 선택한 카테고리 위주로 나오게끔 해서 음식 취향을 고려
#개혁안:카테고리안에서도 세분화하여서 확률을 높이면 어떨까(이후에 시도해볼 예정)
#그러려면 기능2에서 카테고리 취향 말고 음식취향도 물어봐야 할듯
#**혹시 카테고리와 카테고리의 교집합을 나타낼수는 없을까? 교집합이되는 음식은 두카테고리 모두의 취향을 올리는 걸로
import random
import time#현실감있게
#카테고리 안 제시
noodle=["라면","짜장면","짬뽕","쫄면","파스타","쌀국수","우동","스파게티","잡채","잔치국수","칼국수","볶음면","메밀국수"]
rice=["컵밥","간장계란밥","참치마요덮밥","김치볶음밥","돈까스덮밥","김밥","카레","주먹밥","오므라이스","곤드레밥","불고기덮밥","제육덮밥","치킨마요덮밥","낙지볶음밥","대패삼겹볶음밥","짜장밥","짬뽕밥","비빔밥","삼선볶음밥"]#태민
fastfood=['피자','치킨','라면','햄버거','감자튀김','토스트','크로켓']#시후
soup=["김치찌개","부대찌개","짜글이","미역국","된장찌개","만둣국","소고기뭇국","어묵국","갈비탕","감자탕","곰탕","국밥","계란국","삼계탕","육개장","닭도리탕","닭개장","설렁탕","수제비"]#태민
meat=['돈까스','대패삼겹살','돼지불고기','우삼겹 볶음','돼지고기짜글이','목살스테이크','제육볶음','수육','소불고기','오리고기','보쌈','칠면조 구이','소고기','삼겹살']#시후
seafood=["고등어구이","회","문어숙회","새우","오징어","조개구이","삼합","간장게장","양념게장","꽃게탕","초밥","굴전","고추참치","산낙지","낙지볶음","꼬막","바지락 칼국수","홍합탕","매운탕"]#태민
snackFood=["떡볶이","라면","김밥","튀김","라볶이","순대","어묵","물떡","우동","잔치국수","쫄면","소떡소떡","튀김만두","김말이튀김","돈가스","비빔국수","납작만두","새우튀김","냉면"]#태민

#카테고리안에 넣기
category=[noodle,rice,fastfood,soup,meat,snackFood,seafood]

#카테고리 총 개수 변수 설정
allnum_cate=len(category)

#카테고리 취향 리스트 preferCate설정
preferCate=[]
for i in range(1,allnum_cate+1,1):
    preferCate.append((100/allnum_cate)*i)
#메뉴 이름 붙이기 리스트 설정
name=["국수","밥","패스트푸드","국","고기","분식","해산물"]

#취향 함수 preferingCate설정
def preferingCate(n):
    if preferCate[n]<=40:#preferCate의 상한치 설정:40퍼 이하
        a=3
        preferCate[n]+=a
        for i in range(len(preferCate)):#문제점: 30 29 ...일때 29가 사라져버릴수 있음/어떻게 해결? 하나가 올라갈때 다른애들은 내려가게끔 설정->100%를 맞춤
            if i!=n:
                preferCate[i]-=a/(len(preferCate)-1)

#교집합 함수 설정: 겹치는 카테고리를 조사
def Intersection(manu_name,selected_category):#a=메뉴이름을, b=카테고리의 번호를 입력
    for i in range(allnum_cate):#카테고리 수만큼
        for ii in range(len(category[i])):#세부 카테고리의 길이만큼
            if i!=selected_category and manu_name in category[i]:#내가 고른 카테고리가 아니라면 그리고 해당 카테고리안에 같은 이름의 메뉴가 있다면 
                    preferingCate(i)

def random_manu(Q_procate):#카테고리속메뉴 추천/
    indexCate=int(Q_procate)
    random.shuffle(category[indexCate-1])
    result=category[indexCate-1][0:3]
    rec=input(f"제가 추천하는 메뉴는 1.{result[0]},2.{result[1]},3.{result[2]}에요 뭘 고르실래요?(번호입력)")
    rec=int(rec)-1
    print(f"{result[rec]}를 고르셨습니다. 이용해주셔서 감사합니다.")

def function1():#랜덤뽑기함수/function1
    print("랜덤 뽑기에 오신것을 환영합니다.")
    time.sleep(0.2)
    print("카테고리: 1.국수 2.밥 3.패스트푸드 4.국 5.고기 6.분식 7.해산물")
    while True:#오류 발생시 멈춤이 나타나지 않도록 설계
        Q_procate=input("혹시 먹고싶은 카테고리가 있나요?(번호제시 or 아니오 를 입력)")
        if Q_procate.isdigit():
            Q_procate = int(Q_procate)
            break
        elif Q_procate=="아니오":
            break
        elif Q_procate!="아니오":
            print("숫자 또는 아니오를 입력해주세요.")
            continue
    if Q_procate!="아니오": #카테고리고르기/O
        random_manu(Q_procate)
    else:#카테고리고르기/X

        print("그렇다면 제가 카테고리를 추천드리겠습니다.")
        time.sleep(0.3)
        randNum=list(range(1,101))
        choNum_Inran=random.choice(randNum)
        for i in range(len(preferCate)):
            if i!=0 and preferCate[i-1]<choNum_Inran<=preferCate[i]:
                reccate=i
            elif i==0 and choNum_Inran<=preferCate[0]:
                reccate=0
        reccateName=name[reccate-1]
        print(f"제가 추천드리는 카테고리는 \"{reccateName}\"이에요!")
        time.sleep(0.3)
        print("이 카테고리로 추천드릴게요")
        random_manu(reccate)

def function2():#메뉴선택함수/function2
    print("카테고리: 1.국수 2.밥 3.패스트푸드 4.국 5.고기 6.분식 7.해산물")
    while True:
        Q_procate=input("카테고리를 골라주세요(숫자 입력):")
        if Q_procate.isdigit() and 1<=int(Q_procate)<=7:#문자열숫자/?
            break
        else:
            print("카테고리를 제대로 입력해주세요")
            
    Q_procate=int(Q_procate)-1
    print("알겠습니다.");time.sleep(0.3)
    reccateName = name[Q_procate]
    while True:
        Q_manu=input(f"{reccateName}-{category[Q_procate]}\n이중 어떤 음식을 먹고 싶나요?(음식명 적기)")
        if Q_manu in category[Q_procate]:
            break
        else:
            print("제대로 입력해주세요!\n")
            continue
    print(f"{Q_manu}선택 완료");time.sleep(0.1)
    Q_preferCate=input("당신의 취향을 반영한겁니까?(예/아니오)")
    if Q_preferCate=="예":
        preferingCate(Q_procate)
        if turnonInter==1:
            Intersection(Q_manu,Q_procate)
    else:
        print("알겠습니다")
count=1
print("교집합 기능을 사용하여 당신의 취향을 더욱더 반영할 수 있습니다.");time.sleep(0.2)
Q_Intersection=input(" 기능을 사용하시겠습니까(예/아니오):")
if Q_Intersection=="예":
    turnonInter=1
while True:
    print(f"--------{count}번째이용--------")
    print("기능 1.음식 랜덤 뽑기, 2.원하는 메뉴 선택");time.sleep(0.2)
    Q_function=input("어떤 기능을 이용하시겠어요?(1 or 2)(이용X원할시 bye입력)")

    if Q_function=="1":
        function1()
    elif Q_function=="2":
        function2()
    elif Q_function=="bye":
        print("Bye!")
        break
    print(preferCate)
    count+=1
