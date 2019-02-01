# coding=utf-8
'''
    打印普通列表，如果子项也是列表就循环打印
'''
def printInfo(info):
    if type(info) == tuple or type(info) == list:
        for j in range(0, len(info)):
            if type(info[j]) in (tuple,list,dict):
                printInfo(info[j])
            else:
                print info[j]
    elif type(info) == dict:
        for k in info.keys():
            if type(info[k]) in (tuple,list,dict):
                printInfo(info[k])
            else:
                print "%s : %s"%(k,info[k])
    else:
        print info
'''
    打印普通列表，如果子项也是列表就循环打印(提供过滤功能)
'''
def printFilter(info,filter):
    for i in range(0,len(info)):
        item = info[i]
        if type(item) == tuple or type(item) == list:
            for j in range(0,len(item)):
                if(item[i].find(filter) != -1):
                    print item[j]
        else:
            if (item.find(filter) != -1):
                print item
