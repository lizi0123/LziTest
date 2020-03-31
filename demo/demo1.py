
i = 0
#f='F:\自动化培训\实践项目\文件\小诗.txt'
with open('小诗.txt',encoding='utf-8') as f1 , \
        open('小诗2.txt','w',encoding='utf-8') as f2:
       for line in f1:
            i += 1
            index = line.find('')           #find('') 检测字符串中''
            # print(index)
            f2.write(str(i) +"  "+ line[index:])        #[index:]截取字符串到尾
            #  f1.close()

