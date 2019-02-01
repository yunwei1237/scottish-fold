# coding=utf-8
import re
import  os
from  output import *
# 错误说明
# 未修改文件：没有写入任何数据
# 文件没有找到:路径配置错误
# 写入文件时出错：说明文件正在使用，或者文件是只读等等错误

## 项目文件位置
projectPath = os.getcwd()+"\.."
## 脚本文件位置
scriptpath = os.getcwd()+"\..\script\ModuleSystem"

def cat(file):
    for line in open(file,"r"):
        print line
'''
    在指定区间内修改文件内容
'''
def writeInRange(filepath,lines,startLine,endLine):
    start = -1
    end = -1
    try:
        fileLines = open(filepath,"r+").readlines()
        # 查找数据位置
        for idx in range(0, len(fileLines)):
            if fileLines[idx].startswith(startLine):
                start = idx
            if fileLines[idx].startswith(endLine):
                end = idx
    except IOError:
        print "文件没有找到："+filepath
        return

    if start != -1 and end != -1:
        try:
            #组装数据
            result = []
            for idx in range(0,start+1):
                result.append(fileLines[idx])
            for line in lines:
                result.append(line)
            for idx in range(end,len(fileLines)):
                result.append(fileLines[idx])
            #写入数据
            open(filepath,"w").writelines(result)
            print "成功修改文件："+filepath
        except BaseException,e:
            print "写入文件时出错："+filepath
            print "错误信息："+e
    else:
        print "未修改文件："+filepath
'''
    根据指定数据替换文件中的值
'''
def writeReplace(filepath,varMap):
    try:
        fileLines = open(filepath, "r+").readlines()
        result = []
        for idx in range(0, len(fileLines)):
            line = fileLines[idx]
            # 不以#号开头，并且包含=号
            if ((not line.startswith("#")) and line.find("=") != -1):
                matcher = re.match(r'\s*(\w+)\s*=\s*([-\w"]+)\s*(#[\w ]*)?', line)
                key = matcher.group(1)
                val = matcher.group(2)
                other = matcher.group(3)
                if (varMap.has_key(key)):
                    result.append("%s = %s %s\n" % (key, varMap[key], other if other != None else ""))
                    continue
            result.append(line)
        try:
            # 写入数据
            open(filepath, "w").writelines(result)
            print "成功修改文件：" + filepath
        except BaseException,e:
            print "写入文件时出错：" + filepath
            print "错误信息：" + e
    except IOError:
        print "文件没有找到：" + filepath

'''
    查找文件中指定的区间，
    返回值为数组，第一个值代表开始位置，第二个值代表结束位置
'''
def findRange(fileLines,startLine,endLine):
    start = -1
    end = -1
    # 查找数据位置
    for idx in range(0, len(fileLines)):
        if fileLines[idx].startswith(startLine):
            start = idx
        if fileLines[idx].startswith(endLine):
            end = idx
    if start != -1 and end != -1:
        return [start,end]
    return None

'''
    在指定区域内读取数据
'''
def readInRange(filepath,startLine,endLine):
    try:
        fileLines = open(filepath,"r+").readlines()
    except IOError:
        print "文件没有找到："+filepath
        return
    fileRange = findRange(fileLines,startLine,endLine)
    # 如果查找到区域位置
    if fileRange is not None:
        start = fileRange[0]
        end = fileRange[1]
        try:
            # 组装数据
            result = []
            for index in range(start+1,end):
                result.append(fileLines[index])
            print "成功读取文件中的数据："+filepath
            return result
        except BaseException,e:
            print "错误信息："+e
    else:
        print "在文件中没有找到数据："+filepath

'''
    从列表中过滤对象，返回一个过滤后的列表
'''
def filter(data,filter):
    if filter is None or len(filter.strip()) == 0:
        return data
    results = []
    for i in range(0,len(data)):
        item = data[i]
        ## 过滤掉空格
        if(len(item.strip()) == 0):
            continue
        ## 没有找到，就说明是需要的数据
        if (item.find(filter) == -1):
            results.append(item)

    return results

'''
    将提取的数据进行初步的过滤步骤
'''
def filterData(data):
    results = []
    for i in range(0,len(data)):
        item = data[i]
        ## 过滤空格
        if(len(item.strip()) == 0):
            continue
        index = item.strip().find("#")
        ## 过滤整行注释
        if (index == 0):
            continue
        ## 过滤语句后的注释
        if (index > 0):
            item = item[0:index]
        results.append(item)
    return results
item_types = [
        "imodbits_none",
        "imodbits_horse_basic",
        "imodbits_cloth",
        "imodbits_armor",
        "imodbits_plate",
        "imodbits_polearm",
        "imodbits_shield",
        "imodbits_sword",
        "imodbits_sword_high",
        "imodbits_axe",
        "imodbits_mace",
        "imodbits_pick",
        "imodbits_bow",
        "imodbits_crossbow",
        "imodbits_missile",
        "imodbits_thrown",
        "imodbits_horse_good",
        "imodbits_good",
        "imodbits_bad",
        ]
def isLineEnd(line):
    for type in item_types:
        if(line.__contains__(type)):
            return True
    return False
def mergeData(data):
    results = []
    fullLine = ""
    for line in data:
        if(isLineEnd(line)):
            results.append(fullLine+line)
            fullLine = ""
        else:
            fullLine += line
    return results
def textualData(data):
    results = []
    for i in range(0, len(data)):
        item = data[i].strip()
        newItem = item[0:1]
        reg = '(\w+\([\d.]+(,\w+)?\)\|?)+|\[\("\w+"\,\d+\)\]|(\w+\|?)+|("?\w+([ ]*\w)*\"?)+'
        subItems = []
        while True:
            matcher = re.search(reg, item)
            if matcher is not None:
                subItems.append(matcher.group())
                item = item[matcher.end():]
            else:
                break
        for subItem in subItems:

            newItem += "\"" + subItem.replace("\"","'") + "\","
        newItem += item[len(item)-2:]
        results.append(newItem)
    return results


# datas = readInRange(r"C:\Users\Administrator\Desktop\mb_module_system_1010_0\ModuleSystem\module_items.py","#items start","#items end")
# datas = filterData(datas)
# datas = mergeData(datas)
# datas = textualData(datas)
# itemss = "["
# for item in datas:
#     itemss += item
# itemss += "]"
#
# print itemss
# datass = eval(itemss)
# print datass[len(datass)-1]
