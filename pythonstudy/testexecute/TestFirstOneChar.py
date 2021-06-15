def FirstOnechar(str):
    dic = {}
    for i in range(len(str)):
        if str[i] in dic:
           dic[str[i]] += 1
        else:
            dic[str[i]] = 1

    print(dic)
    for i in range(len(str)):
        if dic[str[i]] == 1:
            return str[i]


if __name__ == '__main__':
 str = input("请输入一个字符串")
 print(FirstOnechar(str))