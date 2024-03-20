"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    while True :
        n = int(input("양의 정수를 입력해주세요. "))
        if n > 0 :
            break
        print("X")  

    sum = 0
    for i in range(0,n+1) :
        sum += i
    print(sum)


    return


if __name__ == '__main__':
    main()
