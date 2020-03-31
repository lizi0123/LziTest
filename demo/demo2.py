
i = 0
#f='F:\自动化培训\实践项目\文件\小诗.txt'
# \将一行语句分多行显示
with open('小诗.txt',encoding='utf-8') as f1 , \
          open('小诗2.txt','w',encoding='utf-8') as f2:     #以写方式打开
        line = f1
        while line:
            i = i + 1
            line = f1.readline()
            if not line:    #判断是否读取到内容
                break
            f2.write(str(i)+"   "+str(line))
import time
time.sleep(2)
i=0
with open('小诗2.txt', encoding='utf-8') as f2, \
        open('report.txt', 'w', encoding='utf-8') as f3:
    for line in f2:
        i =i+1
        index = line.find('')  # find('') 检测字符串中''
        num=line[index:]
        if str(i)in num:
            f3.write(line[0:2] + "   ")
            f3.write("passed"+"\n")
        else:
            f3.write("failed")

