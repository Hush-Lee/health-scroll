import xml.dom.minidom as xdm
import re

domTree = xdm.parse("./本草纲目.xml")
herbs = domTree.documentElement
print(herbs.toxml)
nodes = herbs.getElementsByTagName('herb')
ma=re.compile("\d+、.*?。")
file=open("./illnesses.txt")
for node in nodes:
    major = node.getElementsByTagName("major")[0].childNodes[0].data
# file=open("./本草纲目.txt",encoding="utf-8").read()
# nfile=open("./本草纲目.txt",encoding="utf-8").readlines()
# for n in file:
#     if n!="\n":
#         print(n)
# list=[]
# name=re.compile("当前页：.*?下一页:")
# names=re.findall(name,file)
# print(len(names))
# for n in names:
#     list.append(n[4:-3])
# print(list)
# tp=re.split("下一页：",file)
# print(len(tp))
# for t in tp:
#     h=re.split("「释名」",t)
#     if len(h)>1:
#         f = re.split("「气味」", h[1])
#         if len(f)<2:
#             print("无气味")
#         else:
#             d=re.split("「主治」",f[1])
#         a=re.split("上一页",d[1])
#     else:
#         print("无释名")
#     print(h[0])
#     print(f[0])#释名
#     print(d[0])#气味
#     print(a[0])#主治
    # print(t)
# print(a)
# illness=re.compile("[0-9]+、.*?。")
# illnesses=re.findall(illness,file)
# print(illnesses)
# for i in list:
#     ns=re.findall(i+".*?上一页：",file)
#     print(ns)
# print(len(list))