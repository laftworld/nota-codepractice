# word counter를 만들기
# from IPython import embed

def wordCounter(word:str)->int:
    """
    글자수 세는 프로그램

    input: str type의 word
    output: int type의 글자 수
    """

    cnt = 0

    a = word.split()
    cnt = len(a)
    return cnt

def data()->str:
    """
    파일로 부터 입력을 받는 부분.
    input: 없음
    output: 파일로 부터 읽어 들인 문자열

    TODO: 파일 이름 선택할 수 있도록 optparser 추가하기
    """
    d = './data.txt' 
    with open(d, 'r', encoding='utf-8') as f:
        result = f.read()
        # print(result)
    result = ' '.join(result)

    return result

def main():
    choice = input("Choose from file: 1 \n Choose from user input: 2 \n: ")
    if choice == '1':
        word = data()
    elif choice == '2':
        word = input("What do you want: ")
    else:
        pass
    cnt = wordCounter(word)
    print("The number of words in given input is :", cnt)
    
if __name__ == '__main__':
    main()


