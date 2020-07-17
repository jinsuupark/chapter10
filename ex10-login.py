
users={
    "go":"g1234",
    "hong":"h1234",
    "kim":"k1234",
    "na":"n1234",
    "al":"a1234"
}
# def login():
#     id = input("ID를 입력하세요: ")
#     if users.get(id) == None:
#         print(id + "는 존재하지않습니다")
#     else:
#         for cnt in range(3):
#             password = input("비밀번호를 입력하세요")
#             if cnt == 2:
#                 print("3회 실패하였습니다.")
#                 break
#
#             if users.get(id) == password:
#                 print("로그인에 성공했습니다 반갑습니다 " + id + " 님")
#                 break
#             else:
#                 print("비밀번호가 틀렸습니다")
#
#
# def main():
#     login()
#
#
# main()

def get_user_info():
    id = input("ID를 입력하세요")
    password = input("패스워드 입력")
    return id,password

def check_login(id,password):
    if id not in users:
        print(f"{id}는 존재하지 않는 ID입니다")
        return False
    elif users.get(id) ==password:
        return True
    else:
        print("비밀번호가 틀렸습니다.")
        return False

def print_result(result,user_id):
    if result:
        print(f"로그인에 성공했습니다. 반갑습니다.{user_id}님")
    else:
        print("로그인에 실패했습니다. \n 다음기회에..")

def main():

    result = False #로그인 결과 상태 저장 디폴트 False

    for i in range(3):  #최대 3회 시도
        user_id,password = get_user_info() #user ID, Password 입력
        result  =check_login(user_id,password) #로그인 검사
        if result: #로그인 성공시 탈출
            break
    print_result(result,user_id) #결과 출력

main()


