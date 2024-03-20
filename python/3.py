"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    while True :
        time = int(input("시간을 입력해주세요(0~23)"))
        if 0 <= time <= 23 :
            break
        print("다시 입력해주세요")

    if time < 12 :
        print("am")
            
    else :
        print("pm")

    return


if __name__ == '__main__':
    main()
