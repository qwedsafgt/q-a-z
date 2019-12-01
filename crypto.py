"""Crypto: tool for encrypting and decrypting messages.

Exercises

1. Review 'ord' and 'chr' functions and letter-to-number mapping.
2. Explain what happens if you use key 26.
3. Find a way to decode a message without a key.
4. Encrypt numbers.
5. Make the encryption harder to decode.

Adapted from code in https://inventwithpython.com/chapter14.html

"""

def encrypt(message, key):
    "Encrypted message."#给信息加密
    result = ''

    # Iterate letters in message and encrypt each individually.

    for letter in message:#对于句子进行循环
        if letter.isalpha():#判断是否全是字母


            # Letters are numbered like so:
            # A, B, C - Z is 65, 66, 67 - 90
            # a, b, c - z is 97, 98, 99 - 122

            num = ord(letter)#返回字母的ASCLL值

            if letter.isupper():#判断是否全是大写
                base = ord('A')#返回大写A的编码
            elif letter.islower():#判断是否全是小写
                base = ord('a') #返回小写a的编码



            num = (num - base + key) % 26 + base#%求余数

            result += chr(num)#用于表示ascil码对应的字符他的输入时数字

        elif letter.isdigit():#如果是数字

            # TODO: Encrypt digits.
            result += letter#那就加数字连接起来

        else:#所有其他的情况
            result += letter

    return result#运行这个函数，返回result

def decrypt(message, key):#使用密钥解密邮件
    "Decrypt message with key."
    return encrypt(message, -key)#调用加密函数使用密钥的相反数来解密

def decode(message):
    "Decode message without key."#无需密钥就可解码消息
    pass  # TODO

def get_key():#从使用者获得密钥
    "Get key from user."
    try:#异常处理
        text = input('Enter a key (1 - 25): ')#提示用户输入一个1到25的数
        key = int(text)#将这个数处理为整数
        return key#返回这个数
    except:#如果发生异常
        print('Invalid key. Using key: 0.')#不正确的密钥
        return 0#返回0这个密钥

print('Do you wish to encrypt, decrypt, or decode a message?')#您是否希望加密，解密或解码消息？
choice = input()#获取用户输入

if choice == 'encrypt':#如果输入是加密
    phrase = input('Message: ')#提示用户输入句子
    code = get_key()#得到密钥
    print('Encrypted message:', encrypt(phrase, code))#输出经过加密的消息
elif choice == 'decrypt':#如果是解密
    phrase = input('Message: ')#提示用户输入句子
    code = get_key()#得到密钥
    print('Decrypted message:', decrypt(phrase, code))#通过调用解密函数得到解密的消息
elif choice == 'decode':#如果用户输入是解码
    phrase = input('Message: ')#提示用户输入句子
    print('Decoding message:')#调用解码函数
    decode(phrase)
else:#如果用户没有输入这些
    print('Error: Unrecognized Command')#那么提示用户输入错误
#不是很懂这个解码有什么意义
