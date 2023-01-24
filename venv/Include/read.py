import xml.dom.minidom as xdm
import re
from wordcloud import WordCloud
import PIL.Image as image
import numpy as np

class readXML():
    domTree=xdm.parse("./本草纲目.xml")                                                                                #打开本草纲目.xml
    herbs = domTree.documentElement                                                                                   #挂载xml文件的根节点
    nodes=herbs.getElementsByTagName('herb')                                                                           #获取herbs根节点下所有tag名为herb的节点
    herb_list=[]         #所有的药
    flag=-1
    input_str=""
    for node in nodes:
        herb_list.append(node.getAttribute("name"))



    def getNodeByName(self,str):                                                                                        #通过药材名搜索节点
        for node in self.nodes:                                                                                           #遍历节点
            if(str in node.getAttribute('name')or str in node.getElementsByTagName("nick_name")[0].childNodes[0].data):  #herb属性name，或者通过子节点nickname进行匹配
                if str in node.getElementsByTagName("nick_name")[0].childNodes[0].data:                                #如果输入的是别名，则输出学名
                    print("学名:"+node.getAttribute("name"))
                return node                                                                                            #返回节点
        return None



    def getNodeBySick(self,str):                                                                                         #通过病症获取节点
        li=[]                                                                                                            #建立空列表
        for node in self.nodes:                                                                                           #遍历节点
            major = node.getElementsByTagName("major")[0].childNodes[0].data                                          #获取所有节点下major标签的文本类容
            ma = re.compile("\d+、.*?。")                                                                               #正则适配以数字开头以句号结尾的内容
            majors = re.findall(ma, major)
            for m in majors:                                                                                            #遍历所有病症，如果病症包含关键字str将节点加入列表
                if str in m:
                    li.append(node);
        if li:
            return li
        else:
            return None                                                                                                 #返回节点列表

    def getPrescription(self,str):
        li = []  # 建立空列表
        for node in self.nodes:  # 遍历节点
            major = node.getElementsByTagName("major")[0].childNodes[0].data  # 获取所有节点下major标签的文本类容
            ma = re.compile("\d+、.*?\n")
            majors = re.findall(ma, major)
            for m in majors:  # 遍历所有病症，如果病症包含关键字str将节点加入列表
                if str in m :
                    li.append(re.split("\d+、",m)[1]);
        return li

    def getSmell(self,str):                                                                                               #获取气味节点文本
        node=self.getNodeByName(str)
        return node.getElementsByTagName("smell")[0].childNodes[0].data



    def getMajor(self,str):                                                                                              #获取主治的文本内容
        node=self.getNodeByName(str)
        major=node.getElementsByTagName("major")[0].childNodes[0].data
        return major



    def getSick(self,str):                                                                                                #获取特定药材可以治疗的病症，返回病症列表
        ms=self.getMajor(str)
        s=re.compile("\d+.*?。")
        return re.findall(s,ms)

    def countHerb(self,str):                                                                                             #传入病症，返回字典，key为药名value为药出现的次数
        dict={}                                                                                                          #空字典
        ms=self.getNodeBySick(str)                                                                                      #获取包含病症节点
        s=re.compile("\d+、.*?")                                                                                         #编译正则
        for m in ms:
            major=m.getElementsByTagName("major")[0].childNodes[0].data
            majors=re.split(s,major)                                                                                      #将主治疾病切割为列表
            for ma in majors:                                                                                            #遍历疾病，找到药方，遍历药材列表，统计药物出现的次数
                if str in ma:
                    for herb in self.herb_list:
                        if herb in ma:
                            if herb in dict:
                                dict[herb]+=1
                            else:
                                dict[herb]=1
        s_h=[]
        a=100
        for dk in dict.keys():
            i=dict[dk]
            if i<a:
                for d in dict.keys():
                    if i <= dict[d] and dict[d] < a:
                        i = dict[d]
                for d in dict.keys():
                    a = i
                    if i == dict[d]:
                        s_h.append(d)
        return s_h

    # 词云部分
    def pic(self,str):
        text=''
        print(2)
        if self.getNodeByName(str):
            print(1)
            majors = self.getSick(str)
            for major in majors:
                major += "\n"
                text += major  # 读取文件内容存储在text中
            self.flag = 0
            self.input_str = str
        elif self.getNodeBySick(str):
            sicks = self.countHerb(str)
            for h in sicks:
                text += h
                text += '\n'
            self.flag = 1
            self.input_str = str

        else:
            text="本草纲目,尚未收录，如有疑问，还请百度，讳疾忌医，实属自误，衷心祝您，早日康复"
            self.flag=2
        mask = np.array(image.open("中草药1.jpg"))
        wordcloud = WordCloud(
            background_color="white", \
            mask=mask, \
            font_path="STXINGKA.TTF"
        ).generate(text)

        image_produce = wordcloud.to_file("效果图.png")