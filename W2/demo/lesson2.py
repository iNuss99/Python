# # # f = open("data.txt", "r", encoding = "utf-8")
# # # content = f.read(5)
# # # print(content)
# # # f.close()

# # f = open("baitho.txt", "r", encoding = "utf-8")
# # content = f.readline()
# # print(content)
# # content = f.readline()
# # print(content)
# # f.close()

# f = open("numbers.txt","r", encoding = "utf-8"  )
# content = f.readline()
# print(content)
# print(type(content))
# f.close()

# f = open("output.txt", "w", encoding = "utf-8")
# f.write("Hello, World!")
# f.close()

# f = open("output.txt", "w", encoding = "utf-8")
# f.write("hom nay troi dep qua!")
# f.close()

# f = open("output2.txt", "a", encoding = "utf-8")
# f.write("Mua he ve con ve keu\n")
# f.close()

f = open("output2.txt", "a", encoding = "utf-8")
f.write("Mua he di ve ve het keu!")
f.close()
