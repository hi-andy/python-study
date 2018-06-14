file_name = input("请输入文件名：")
file_name = file_name + ".txt"
something_file = open(file_name, "w")

stop_word = ":q"
file_content = ""
print("请输入内容【单独输入‘:q‘保存退出】：")
for line in iter(input, stop_word):
    file_content = file_content + line + "\n"
print(file_content, file=something_file)
something_file.close()
