"""Bagels, a number puzzle game.

Exercises:

1. Can you guess the number?
2. How much harder is 6 digits? Do you need more guesses?
3. What's the maximum number of digits we could support?

Adapted from code in https://inventwithpython.com/chapter11.html

"""

from random import sample, shuffle#从random模块中引入sample，shuffle

digits = 3#给出需要猜出得位数
guesses = 10#给出给用户猜测的机会

print('I am thinking of a', digits, 'digit number.')#给用户的提示
print('Try to guess what it is.')#让用户猜数字
print('Here are some clues:')#给出线索
print('When I say:    That means:')#给出不同的提示所代表的意思
print('  pico         One digit is correct but in the wrong position.')#不同的提示所分别代表的意思
print('  fermi        One digit is correct and in the right position.')
print('  bagels       No digit is correct.')
print('There are no repeated digits in the number.')

# Create a random number.

letters = sample('0123456789', digits)#随机返回位数为digits并且数字由0到9组成的列表
if letters[0] == '0':
    letters.reverse()#如果返回的列表的数字是以0开头的，那么将这个列表倒序排列

number = ''.join(letters)#把字符之间用“-”分割
print('I have thought up a number.')#我在猜一个数字
print('You have', guesses, 'guesses to get it.')#提示用户有十次机会去猜

counter = 1#开始第一次猜测

while True:
    print('Guess #', counter)#显示猜测的次数
    guess = input()#把用户输出的值赋予guess

    if len(guess) != digits:#如果用户输入的值的长度不符合要求
        print('Wrong number of digits. Try again!')#那么输出提示
        continue#循环继续

    # Create the clues.

    clues = []#创建一个列表

    for index in range(digits):#对于三位数的每一位进行循环
        if guess[index] == number[index]:#判断用户输入是否于答案数字与位置都相同
            clues.append('fermi')#如果是，在列表中添加提示
        elif guess[index] in number:#如果用户输入与答案数字相同但不是在同一位置
            clues.append('pico')#那么在列表中添加提示pico

    shuffle(clues)#将列表clues乱序，增加游戏难度

    if len(clues) == 0:#如果列表的结果为0
        print('bagels')#那么输出
    else:
        print(' '.join(clues))#将字符之间用-分离


    counter += 1#将猜测次数加一

    if guess == number:#如果用户输入于结果一样
        print('You got it!')#那么结束循环，结束游戏
        break

    if counter > guesses:#如果猜测次数大于指定次数，
        print('You ran out of guesses. The answer was', number)#告诉用户结果
        break#结束游戏
