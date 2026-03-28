while 1:
    try:
        str1 = input() # input은 "Hello\n"라고 읽는다.
        print(str1) # print가 개행(\n) 추가 못하게 -> end = ""
    except EOFError:
        break