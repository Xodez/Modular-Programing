# #
# def drawBox():
#     for i in range(1,4):
#         print("-      -")
#     print("+------+")
#
# drawBox()
# #
# #
# def drawBox():
#     for i in range(1, 4):
#         print("-        -")
#     print("+--------+")
#
#
# # 8 charas long
# def nose():
#     width = 0
#     inwidth = 2
#     print("    /\  ")
#     for i in range(1, 4):
#         print(" "* inwidth,"/", " " * width, '\ ')
#         width = width + 2
#         inwidth = inwidth - 1
#     print("+--------+")
#
# def thrusters():
#     width = 0
#     inwidth = 2
#     print("    //\\\\")
#     for i in range(1, 4):
#         print(" " * inwidth, "//", " " * width, "\\\\")
#         width = width + 2
#         inwidth = inwidth - 1
#
#
# def main():
#     nose()
#     drawBox()
#     thrusters()
# main()
# #
# #
# def song(number):
#     num = number
#     num2 = num-1
#     while num > 0:
#
#         print( num,"green bottles hanging on the wall,",num ,"green bottles hanging on the wall, And if one green bottle should accidentally fall, There'll be" ,num2, "green bottles hanging on the wall." )
#         num = num - 1
#         num2 = num2-1
# song(10)
# #
# #
# def hair(num):
#     i = 1
#     while i <= num :
#         print("####")
#         i = i+1
#
#
# def eyes(bulion):
#     if bulion == True:
#         print("----")
#         print("@  @")
#     elif bulion == False:
#         print("@  @")
#
#
# def nose(shape):
#     shape1 = str(shape)
#     print("", shape1*2, " ")
#
#
# def mouth(lenght):
#     print("=" * lenght)
#
#
# def main():
#     hair(2)
#     eyes(True)
#     nose(7)
#     mouth(4)
#
#
# main()
# #
# #
# def openFile(filename):
#     fileopen = filename
#     file = open(fileopen, "r")
#
# def contents(filename,displayType):
#     file = open(filename, "r")
#     if displayType == 1:
#         content =  file.read()
#         print(content)
#     elif displayType ==2:
#         content = file.read()
#         print(content.upper())
#     elif displayType ==3:
#         content = filename
#         for line in reversed(list(open(content))):
#             print(line.rstrip())
#
# def main():
#     openFile("employee.txt")
#     contents("employee.txt",3)
#
# main()
# #