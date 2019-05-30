import numpy as np

def calc_dist(edit_distance_matrix, i, j, input1_list, input2_list):
    # Calculate distance
    if (input1_list[i - 1] == input2_list[j - 1]):
        delta = 0
    else:
        delta = 1

    return min(edit_distance_matrix[i - 1, j - 1] + delta, edit_distance_matrix[i, j - 1] + 1,
               edit_distance_matrix[i - 1, j] + 1)


def calcEditDist(input1, input2):
    input1_list = list(input1)
    input2_list = list(input2)

    # Make edit distance matrix
    edit_distance_matrix = np.zeros((len(input1_list) + 1, len(input2_list) + 1))

    # Init edit distance matrix
    for i in range(len(input1_list) + 1):
        edit_distance_matrix[i, 0] = i

    for j in range(len(input2_list) + 1):
        edit_distance_matrix[0, j] = j

    # Impute edit distance matrix
    for i in range(1, len(input1_list) + 1):
        for j in range(1, len(input2_list) + 1):
            edit_distance_matrix[i, j] = calc_dist(edit_distance_matrix, i, j, input1_list, input2_list)

    return edit_distance_matrix[len(input1_list), len(input2_list)]


def userInput():


    BASE_CODE, CHOSUNG, VOWEL = 44032, 588, 28
    # 초성 리스트
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    # 모음 리스트
    VOWEL_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ','ㅣ']

    # 종성 리스트
    JONGSUNG_LIST = ['λ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    input1_1 = input()
    input1_2 = input()
    input1_1list = list(input1_1)
    input1_2list = list(input1_2)
    word1=""
    word2=""
    for unit in input1_1list:
        char_code = ord(unit) - BASE_CODE
        char1 = int(char_code / CHOSUNG)
        a = CHOSUNG_LIST[char1]
        char2 = int((char_code - (CHOSUNG * char1)) / VOWEL)
        b = VOWEL_LIST[char2]
        char3 = int((char_code - (CHOSUNG * char1) - (VOWEL * char2)))
        c = JONGSUNG_LIST[char3]
        temp1 = a+b+c
        word1 = word1 + temp1

    for unit in input1_2list:
        char_code = ord(unit) - BASE_CODE
        char1_1 = int(char_code / CHOSUNG)
        d = CHOSUNG_LIST[char1_1]
        char1_2 = int((char_code - (CHOSUNG * char1_1)) / VOWEL)
        e = VOWEL_LIST[char1_2]
        char1_3 = int((char_code - (CHOSUNG * char1_1) - (VOWEL * char1_2)))
        f = JONGSUNG_LIST[char1_3]
        temp2 = d+e+f
        word2 = word2 + temp2

    result1 = calcEditDist(word1, word2)

    input2_1 = input()
    input2_2 = input()
    input2_1list = list(input2_1)
    input2_2list = list(input2_2)

    word3=""
    word4=""
    for unit in input2_1list:
        char_code = ord(unit) - BASE_CODE
        char1 = int(char_code / CHOSUNG)
        a = CHOSUNG_LIST[char1]
        char2 = int((char_code - (CHOSUNG * char1)) / VOWEL)
        b = VOWEL_LIST[char2]
        char3 = int((char_code - (CHOSUNG * char1) - (VOWEL * char2)))
        c = JONGSUNG_LIST[char3]
        temp3 = a + b + c
        word3 = word3 + temp3

    for unit in input2_2list:
        char_code = ord(unit) - BASE_CODE
        char1_1 = int(char_code / CHOSUNG)
        d = CHOSUNG_LIST[char1_1]
        char1_2 = int((char_code - (CHOSUNG * char1_1)) / VOWEL)
        e = VOWEL_LIST[char1_2]
        char1_3 = int((char_code - (CHOSUNG * char1_1) - (VOWEL * char1_2)))
        f = JONGSUNG_LIST[char1_3]
        temp4 = d + e + f
        word4 = word4 + temp4

    result2 = calcEditDist(word3, word4)


    printResult(result1, result2, input1_1, input1_2, input2_1, input2_2)

def case1():
    input1_1 = "가까이"
    input1_2 = "가까히"
    BASE_CODE, CHOSUNG, VOWEL = 44032, 588, 28
    # 초성 리스트
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    # 모음 리스트
    VOWEL_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ','ㅣ']

    # 종성 리스트
    JONGSUNG_LIST = ['λ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ','ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    input1_1list = list(input1_1)
    input1_2list = list(input1_2)

    word1=""
    word2=""
    for unit in input1_1list:
        char_code = ord(unit) - BASE_CODE
        char1 = int(char_code / CHOSUNG)
        a = CHOSUNG_LIST[char1]
        char2 = int((char_code - (CHOSUNG * char1)) / VOWEL)
        b = VOWEL_LIST[char2]
        char3 = int((char_code - (CHOSUNG * char1) - (VOWEL * char2)))
        c = JONGSUNG_LIST[char3]
        temp1 = a + b + c
        word1 = word1 + temp1

    for unit in input1_2list:
        char_code = ord(unit) - BASE_CODE
        char1_1 = int(char_code / CHOSUNG)
        d = CHOSUNG_LIST[char1_1]
        char1_2 = int((char_code - (CHOSUNG * char1_1)) / VOWEL)
        e = VOWEL_LIST[char1_2]
        char1_3 = int((char_code - (CHOSUNG * char1_1) - (VOWEL * char1_2)))
        f = JONGSUNG_LIST[char1_3]
        temp2 = d + e + f
        word2 = word2 + temp2

    result1 = calcEditDist(word1, word2)

    input2_1 = "가까이"
    input2_2 = "가랑이"
    input2_1list = list(input2_1)
    input2_2list = list(input2_2)

    word3=""
    word4=""
    for unit in input2_1list:
        char_code = ord(unit) - BASE_CODE
        char1 = int(char_code / CHOSUNG)
        a = CHOSUNG_LIST[char1]
        char2 = int((char_code - (CHOSUNG * char1)) / VOWEL)
        b = VOWEL_LIST[char2]
        char3 = int((char_code - (CHOSUNG * char1) - (VOWEL * char2)))
        c = JONGSUNG_LIST[char3]
        temp3 = a + b + c
        word3 = word3 + temp3

    for unit in input2_2list:
        char_code = ord(unit) - BASE_CODE
        char1_1 = int(char_code / CHOSUNG)
        d = CHOSUNG_LIST[char1_1]
        char1_2 = int((char_code - (CHOSUNG * char1_1)) / VOWEL)
        e = VOWEL_LIST[char1_2]
        char1_3 = int((char_code - (CHOSUNG * char1_1) - (VOWEL * char1_2)))
        f = JONGSUNG_LIST[char1_3]
        temp4 = d + e + f
        word4 = word4 + temp4
    result2 = calcEditDist(word3, word4)

    printResult(result1, result2, input1_1, input1_2, input2_1, input2_2)


def case2():

    input1_1 = "가랑이"
    input1_2 = "가랭이"

    BASE_CODE, CHOSUNG, VOWEL = 44032, 588, 28
    # 초성 리스트
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    # 모음 리스트
    VOWEL_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ','ㅣ']

    # 종성 리스트
    JONGSUNG_LIST = ['λ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ','ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    input1_1list = list(input1_1)
    input1_2list = list(input1_2)

    word1=""
    word2=""
    for unit in input1_1list:
        char_code = ord(unit) - BASE_CODE
        char1 = int(char_code / CHOSUNG)
        a = CHOSUNG_LIST[char1]
        char2 = int((char_code - (CHOSUNG * char1)) / VOWEL)
        b = VOWEL_LIST[char2]
        char3 = int((char_code - (CHOSUNG * char1) - (VOWEL * char2)))
        c = JONGSUNG_LIST[char3]
        temp1 = a + b + c
        word1 = word1 + temp1

    for unit in input1_2list:
        char_code = ord(unit) - BASE_CODE
        char1_1 = int(char_code / CHOSUNG)
        d = CHOSUNG_LIST[char1_1]
        char1_2 = int((char_code - (CHOSUNG * char1_1)) / VOWEL)
        e = VOWEL_LIST[char1_2]
        char1_3 = int((char_code - (CHOSUNG * char1_1) - (VOWEL * char1_2)))
        f = JONGSUNG_LIST[char1_3]
        temp2 = d + e + f
        word2 = word2 + temp2

    result1 = calcEditDist(word1, word2)

    input2_1 = "가랑이"
    input2_2 = "가랑잎"
    input2_1list = list(input2_1)
    input2_2list = list(input2_2)

    word3=""
    word4=""
    for unit in input2_1list:
        char_code = ord(unit) - BASE_CODE
        char1 = int(char_code / CHOSUNG)
        a = CHOSUNG_LIST[char1]
        char2 = int((char_code - (CHOSUNG * char1)) / VOWEL)
        b = VOWEL_LIST[char2]
        char3 = int((char_code - (CHOSUNG * char1) - (VOWEL * char2)))
        c = JONGSUNG_LIST[char3]
        temp3 = a + b + c
        word3 = word3 + temp3

    for unit in input2_2list:
        char_code = ord(unit) - BASE_CODE
        char1_1 = int(char_code / CHOSUNG)
        d = CHOSUNG_LIST[char1_1]
        char1_2 = int((char_code - (CHOSUNG * char1_1)) / VOWEL)
        e = VOWEL_LIST[char1_2]
        char1_3 = int((char_code - (CHOSUNG * char1_1) - (VOWEL * char1_2)))
        f = JONGSUNG_LIST[char1_3]
        temp4 = d + e + f
        word4 = word4 + temp4
    result2 = calcEditDist(word3, word4)

    printResult(result1, result2, input1_1, input1_2, input2_1, input2_2)


def case3():
    input1_1 = "가려지다"
    input1_2 = "그려지다"
    BASE_CODE, CHOSUNG, VOWEL = 44032, 588, 28
    # 초성 리스트
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    # 모음 리스트
    VOWEL_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ','ㅣ']

    # 종성 리스트
    JONGSUNG_LIST = ['λ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ','ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    input1_1list = list(input1_1)
    input1_2list = list(input1_2)

    word1=""
    word2=""
    for unit in input1_1list:
        char_code = ord(unit) - BASE_CODE
        char1 = int(char_code / CHOSUNG)
        a = CHOSUNG_LIST[char1]
        char2 = int((char_code - (CHOSUNG * char1)) / VOWEL)
        b = VOWEL_LIST[char2]
        char3 = int((char_code - (CHOSUNG * char1) - (VOWEL * char2)))
        c = JONGSUNG_LIST[char3]
        temp1 = a + b + c
        word1 = word1 + temp1

    for unit in input1_2list:
        char_code = ord(unit) - BASE_CODE
        char1_1 = int(char_code / CHOSUNG)
        d = CHOSUNG_LIST[char1_1]
        char1_2 = int((char_code - (CHOSUNG * char1_1)) / VOWEL)
        e = VOWEL_LIST[char1_2]
        char1_3 = int((char_code - (CHOSUNG * char1_1) - (VOWEL * char1_2)))
        f = JONGSUNG_LIST[char1_3]
        temp2 = d + e + f
        word2 = word2 + temp2

    result1 = calcEditDist(word1, word2)

    input2_1 = "가려지다"
    input2_2 = "가리워지다"
    input2_1list = list(input2_1)
    input2_2list = list(input2_2)

    word3=""
    word4=""
    for unit in input2_1list:
        char_code = ord(unit) - BASE_CODE
        char1 = int(char_code / CHOSUNG)
        a = CHOSUNG_LIST[char1]
        char2 = int((char_code - (CHOSUNG * char1)) / VOWEL)
        b = VOWEL_LIST[char2]
        char3 = int((char_code - (CHOSUNG * char1) - (VOWEL * char2)))
        c = JONGSUNG_LIST[char3]
        temp3 = a + b + c
        word3 = word3 + temp3

    for unit in input2_2list:
        char_code = ord(unit) - BASE_CODE
        char1_1 = int(char_code / CHOSUNG)
        d = CHOSUNG_LIST[char1_1]
        char1_2 = int((char_code - (CHOSUNG * char1_1)) / VOWEL)
        e = VOWEL_LIST[char1_2]
        char1_3 = int((char_code - (CHOSUNG * char1_1) - (VOWEL * char1_2)))
        f = JONGSUNG_LIST[char1_3]
        temp4 = d + e + f
        word4 = word4 + temp4
    result2 = calcEditDist(word3, word4)

    printResult(result1, result2, input1_1, input1_2, input2_1, input2_2)


def case4():
    input1_1 = "가만히"
    input1_2 = "가만이"
    BASE_CODE, CHOSUNG, VOWEL = 44032, 588, 28
    # 초성 리스트
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    # 모음 리스트
    VOWEL_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ','ㅣ']

    # 종성 리스트
    JONGSUNG_LIST = ['λ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ','ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    input1_1list = list(input1_1)
    input1_2list = list(input1_2)

    word1=""
    word2=""
    for unit in input1_1list:
        char_code = ord(unit) - BASE_CODE
        char1 = int(char_code / CHOSUNG)
        a = CHOSUNG_LIST[char1]
        char2 = int((char_code - (CHOSUNG * char1)) / VOWEL)
        b = VOWEL_LIST[char2]
        char3 = int((char_code - (CHOSUNG * char1) - (VOWEL * char2)))
        c = JONGSUNG_LIST[char3]
        temp1 = a + b + c
        word1 = word1 + temp1

    for unit in input1_2list:
        char_code = ord(unit) - BASE_CODE
        char1_1 = int(char_code / CHOSUNG)
        d = CHOSUNG_LIST[char1_1]
        char1_2 = int((char_code - (CHOSUNG * char1_1)) / VOWEL)
        e = VOWEL_LIST[char1_2]
        char1_3 = int((char_code - (CHOSUNG * char1_1) - (VOWEL * char1_2)))
        f = JONGSUNG_LIST[char1_3]
        temp2 = d + e + f
        word2 = word2 + temp2

    result1 = calcEditDist(word1, word2)

    input2_1 = "가만히"
    input2_2 = "가마니"
    input2_1list = list(input2_1)
    input2_2list = list(input2_2)

    word3=""
    word4=""
    for unit in input2_1list:
        char_code = ord(unit) - BASE_CODE
        char1 = int(char_code / CHOSUNG)
        a = CHOSUNG_LIST[char1]
        char2 = int((char_code - (CHOSUNG * char1)) / VOWEL)
        b = VOWEL_LIST[char2]
        char3 = int((char_code - (CHOSUNG * char1) - (VOWEL * char2)))
        c = JONGSUNG_LIST[char3]
        temp3 = a + b + c
        word3 = word3 + temp3

    for unit in input2_2list:
        char_code = ord(unit) - BASE_CODE
        char1_1 = int(char_code / CHOSUNG)
        d = CHOSUNG_LIST[char1_1]
        char1_2 = int((char_code - (CHOSUNG * char1_1)) / VOWEL)
        e = VOWEL_LIST[char1_2]
        char1_3 = int((char_code - (CHOSUNG * char1_1) - (VOWEL * char1_2)))
        f = JONGSUNG_LIST[char1_3]
        temp4 = d + e + f
        word4 = word4 + temp4
    result2 = calcEditDist(word3, word4)

    printResult(result1, result2, input1_1, input1_2, input2_1, input2_2)


def case5():
    input1_1 = "희치희치"
    input1_2 = "희칠희칠"
    BASE_CODE, CHOSUNG, VOWEL = 44032, 588, 28
    # 초성 리스트
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    # 모음 리스트
    VOWEL_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ','ㅣ']

    # 종성 리스트
    JONGSUNG_LIST = ['λ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ','ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    input1_1list = list(input1_1)
    input1_2list = list(input1_2)

    word1=""
    word2=""
    for unit in input1_1list:
        char_code = ord(unit) - BASE_CODE
        char1 = int(char_code / CHOSUNG)
        a = CHOSUNG_LIST[char1]
        char2 = int((char_code - (CHOSUNG * char1)) / VOWEL)
        b = VOWEL_LIST[char2]
        char3 = int((char_code - (CHOSUNG * char1) - (VOWEL * char2)))
        c = JONGSUNG_LIST[char3]
        temp1 = a + b + c
        word1 = word1 + temp1

    for unit in input1_2list:
        char_code = ord(unit) - BASE_CODE
        char1_1 = int(char_code / CHOSUNG)
        d = CHOSUNG_LIST[char1_1]
        char1_2 = int((char_code - (CHOSUNG * char1_1)) / VOWEL)
        e = VOWEL_LIST[char1_2]
        char1_3 = int((char_code - (CHOSUNG * char1_1) - (VOWEL * char1_2)))
        f = JONGSUNG_LIST[char1_3]
        temp2 = d + e + f
        word2 = word2 + temp2

    result1 = calcEditDist(word1, word2)

    input2_1 = "희치희치"
    input2_2 = "히끗히끗"
    input2_1list = list(input2_1)
    input2_2list = list(input2_2)

    word3=""
    word4=""
    for unit in input2_1list:
        char_code = ord(unit) - BASE_CODE
        char1 = int(char_code / CHOSUNG)
        a = CHOSUNG_LIST[char1]
        char2 = int((char_code - (CHOSUNG * char1)) / VOWEL)
        b = VOWEL_LIST[char2]
        char3 = int((char_code - (CHOSUNG * char1) - (VOWEL * char2)))
        c = JONGSUNG_LIST[char3]
        temp3 = a + b + c
        word3 = word3 + temp3

    for unit in input2_2list:
        char_code = ord(unit) - BASE_CODE
        char1_1 = int(char_code / CHOSUNG)
        d = CHOSUNG_LIST[char1_1]
        char1_2 = int((char_code - (CHOSUNG * char1_1)) / VOWEL)
        e = VOWEL_LIST[char1_2]
        char1_3 = int((char_code - (CHOSUNG * char1_1) - (VOWEL * char1_2)))
        f = JONGSUNG_LIST[char1_3]
        temp4 = d + e + f
        word4 = word4 + temp4
    result2 = calcEditDist(word3, word4)

    printResult(result1, result2, input1_1, input1_2, input2_1, input2_2)

def case6():
    input1_1 = "성균관대학교"
    input1_2 = "성균관대핵교"
    BASE_CODE, CHOSUNG, VOWEL = 44032, 588, 28
    # 초성 리스트
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    # 모음 리스트
    VOWEL_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ','ㅣ']

    # 종성 리스트
    JONGSUNG_LIST = ['λ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ','ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    input1_1list = list(input1_1)
    input1_2list = list(input1_2)

    word1=""
    word2=""
    for unit in input1_1list:
        char_code = ord(unit) - BASE_CODE
        char1 = int(char_code / CHOSUNG)
        a = CHOSUNG_LIST[char1]
        char2 = int((char_code - (CHOSUNG * char1)) / VOWEL)
        b = VOWEL_LIST[char2]
        char3 = int((char_code - (CHOSUNG * char1) - (VOWEL * char2)))
        c = JONGSUNG_LIST[char3]
        temp1 = a + b + c
        word1 = word1 + temp1

    for unit in input1_2list:
        char_code = ord(unit) - BASE_CODE
        char1_1 = int(char_code / CHOSUNG)
        d = CHOSUNG_LIST[char1_1]
        char1_2 = int((char_code - (CHOSUNG * char1_1)) / VOWEL)
        e = VOWEL_LIST[char1_2]
        char1_3 = int((char_code - (CHOSUNG * char1_1) - (VOWEL * char1_2)))
        f = JONGSUNG_LIST[char1_3]
        temp2 = d + e + f
        word2 = word2 + temp2

    result1 = calcEditDist(word1, word2)

    input2_1 = "성균관대학교"
    input2_2 = "생균관대핵교"
    input2_1list = list(input2_1)
    input2_2list = list(input2_2)

    word3=""
    word4=""
    for unit in input2_1list:
        char_code = ord(unit) - BASE_CODE
        char1 = int(char_code / CHOSUNG)
        a = CHOSUNG_LIST[char1]
        char2 = int((char_code - (CHOSUNG * char1)) / VOWEL)
        b = VOWEL_LIST[char2]
        char3 = int((char_code - (CHOSUNG * char1) - (VOWEL * char2)))
        c = JONGSUNG_LIST[char3]
        temp3 = a + b + c
        word3 = word3 + temp3

    for unit in input2_2list:
        char_code = ord(unit) - BASE_CODE
        char1_1 = int(char_code / CHOSUNG)
        d = CHOSUNG_LIST[char1_1]
        char1_2 = int((char_code - (CHOSUNG * char1_1)) / VOWEL)
        e = VOWEL_LIST[char1_2]
        char1_3 = int((char_code - (CHOSUNG * char1_1) - (VOWEL * char1_2)))
        f = JONGSUNG_LIST[char1_3]
        temp4 = d + e + f
        word4 = word4 + temp4
    result2 = calcEditDist(word3, word4)

    printResult(result1, result2, input1_1, input1_2, input2_1, input2_2)


def case7():
    input1_1 = "룰루랄라"
    input1_2 = "랄라룰루"
    BASE_CODE, CHOSUNG, VOWEL = 44032, 588, 28
    # 초성 리스트
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    # 모음 리스트
    VOWEL_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ','ㅣ']

    # 종성 리스트
    JONGSUNG_LIST = ['λ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ','ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    input1_1list = list(input1_1)
    input1_2list = list(input1_2)

    word1=""
    word2=""
    for unit in input1_1list:
        char_code = ord(unit) - BASE_CODE
        char1 = int(char_code / CHOSUNG)
        a = CHOSUNG_LIST[char1]
        char2 = int((char_code - (CHOSUNG * char1)) / VOWEL)
        b = VOWEL_LIST[char2]
        char3 = int((char_code - (CHOSUNG * char1) - (VOWEL * char2)))
        c = JONGSUNG_LIST[char3]
        temp1 = a + b + c
        word1 = word1 + temp1

    for unit in input1_2list:
        char_code = ord(unit) - BASE_CODE
        char1_1 = int(char_code / CHOSUNG)
        d = CHOSUNG_LIST[char1_1]
        char1_2 = int((char_code - (CHOSUNG * char1_1)) / VOWEL)
        e = VOWEL_LIST[char1_2]
        char1_3 = int((char_code - (CHOSUNG * char1_1) - (VOWEL * char1_2)))
        f = JONGSUNG_LIST[char1_3]
        temp2 = d + e + f
        word2 = word2 + temp2

    result1 = calcEditDist(word1, word2)

    input2_1 = "룰루랄라"
    input2_2 = "눈누난나"
    input2_1list = list(input2_1)
    input2_2list = list(input2_2)

    word3=""
    word4=""
    for unit in input2_1list:
        char_code = ord(unit) - BASE_CODE
        char1 = int(char_code / CHOSUNG)
        a = CHOSUNG_LIST[char1]
        char2 = int((char_code - (CHOSUNG * char1)) / VOWEL)
        b = VOWEL_LIST[char2]
        char3 = int((char_code - (CHOSUNG * char1) - (VOWEL * char2)))
        c = JONGSUNG_LIST[char3]
        temp3 = a + b + c
        word3 = word3 + temp3

    for unit in input2_2list:
        char_code = ord(unit) - BASE_CODE
        char1_1 = int(char_code / CHOSUNG)
        d = CHOSUNG_LIST[char1_1]
        char1_2 = int((char_code - (CHOSUNG * char1_1)) / VOWEL)
        e = VOWEL_LIST[char1_2]
        char1_3 = int((char_code - (CHOSUNG * char1_1) - (VOWEL * char1_2)))
        f = JONGSUNG_LIST[char1_3]
        temp4 = d + e + f
        word4 = word4 + temp4
    result2 = calcEditDist(word3, word4)

    printResult(result1, result2, input1_1, input1_2, input2_1, input2_2)

def case8():
    input1_1 = "철저히"
    input1_2 = "철저이"
    BASE_CODE, CHOSUNG, VOWEL = 44032, 588, 28
    # 초성 리스트
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    # 모음 리스트
    VOWEL_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ','ㅣ']

    # 종성 리스트
    JONGSUNG_LIST = ['λ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ','ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    input1_1list = list(input1_1)
    input1_2list = list(input1_2)

    word1=""
    word2=""
    for unit in input1_1list:
        char_code = ord(unit) - BASE_CODE
        char1 = int(char_code / CHOSUNG)
        a = CHOSUNG_LIST[char1]
        char2 = int((char_code - (CHOSUNG * char1)) / VOWEL)
        b = VOWEL_LIST[char2]
        char3 = int((char_code - (CHOSUNG * char1) - (VOWEL * char2)))
        c = JONGSUNG_LIST[char3]
        temp1 = a + b + c
        word1 = word1 + temp1

    for unit in input1_2list:
        char_code = ord(unit) - BASE_CODE
        char1_1 = int(char_code / CHOSUNG)
        d = CHOSUNG_LIST[char1_1]
        char1_2 = int((char_code - (CHOSUNG * char1_1)) / VOWEL)
        e = VOWEL_LIST[char1_2]
        char1_3 = int((char_code - (CHOSUNG * char1_1) - (VOWEL * char1_2)))
        f = JONGSUNG_LIST[char1_3]
        temp2 = d + e + f
        word2 = word2 + temp2

    result1 = calcEditDist(word1, word2)

    input2_1 = "철저히"
    input2_2 = "처절히"
    input2_1list = list(input2_1)
    input2_2list = list(input2_2)

    word3=""
    word4=""
    for unit in input2_1list:
        char_code = ord(unit) - BASE_CODE
        char1 = int(char_code / CHOSUNG)
        a = CHOSUNG_LIST[char1]
        char2 = int((char_code - (CHOSUNG * char1)) / VOWEL)
        b = VOWEL_LIST[char2]
        char3 = int((char_code - (CHOSUNG * char1) - (VOWEL * char2)))
        c = JONGSUNG_LIST[char3]
        temp3 = a + b + c
        word3 = word3 + temp3

    for unit in input2_2list:
        char_code = ord(unit) - BASE_CODE
        char1_1 = int(char_code / CHOSUNG)
        d = CHOSUNG_LIST[char1_1]
        char1_2 = int((char_code - (CHOSUNG * char1_1)) / VOWEL)
        e = VOWEL_LIST[char1_2]
        char1_3 = int((char_code - (CHOSUNG * char1_1) - (VOWEL * char1_2)))
        f = JONGSUNG_LIST[char1_3]
        temp4 = d + e + f
        word4 = word4 + temp4
    result2 = calcEditDist(word3, word4)

    printResult(result1, result2, input1_1, input1_2, input2_1, input2_2)



def printResult(result1, result2, input1_1, input1_2, input2_1, input2_2):
    if (result1 > result2):
        print("(%s,%s):%d > (%s,%s):%d" % (input1_1, input1_2, result1, input2_1, input2_2, result2))
    elif (result1 < result2):
        print("(%s,%s):%d < (%s,%s):%d" % (input1_1, input1_2, result1, input2_1, input2_2, result2))
    else:
        print("(%s,%s):%d = (%s,%s):%d" % (input1_1, input1_2, result1, input2_1, input2_2, result2))


if __name__ == '__main__':
    # userInput()
    case1()
    case2()
    case3()
    case4()
    case5()
    case6()
    case7()
    case8()