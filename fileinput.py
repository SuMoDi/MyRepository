import fileinput
# fileinpput.input 参数 '1.txt'为操作文件， backup='xcx'指定备份之后的后缀 inplace=1直接修改文件 inplace=0 不修改文件,修改后的内容打印出来
for line in fileinput.input('1.txt',backup='xcx',inplace=1):
    line = line.replace('cd','11')
    print (line,end='')
