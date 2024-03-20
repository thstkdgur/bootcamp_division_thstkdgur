"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    Alphabet = input("알파벳 하나를 입력해주세요. ")
    Vowels = {"a","e","i","o","u"}
    if Alphabet in Vowels :
        print("O")
    else :
        print("X")

    return


if __name__ == '__main__':
    main()
