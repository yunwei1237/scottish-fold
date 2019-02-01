# coding=utf-8
import re
import math
import random
from ModuleSystem.module_items import *
from ModuleSystem.header_items import *
from output import *

itemTypes = {
    "0":"none",
    "1":"horse",
    "2":"one_handed_wpn",
    "3":"two_handed_wpn",
    "4":"polearm",
    "5":"arrows",
    "6":"bolts",
    "7":"shield",
    "8":"bow",
    "9":"crossbow",
    "10":"thrown",
    "11":"goods",
    "12":"head_armor",
    "13":"body_armor",
    "14":"foot_armor",
    "15":"hand_armor",
    "16":"pistol",
    "17":"musket",
    "18":"bullets",
    "19":"animal",
    "20":"book"
}
#获得物品的类型
def get_weapon_type(y):
    no = y & 0xff
    return itemTypes[str(no)]
## 对物品进行价值评估
def valuate(item):
    val = 0
    type = item["type"]
    if type in ["one_handed_wpn","two_handed_wpn","polearm"]:
        #好武器的标准：伤害高（砍和刺），长度宽（一寸长一寸强），速度快，难度低（难度越大），重量轻（游戏中的重量对伤害没有加成）
        swing = item["swing_damage"] * 3 + item["weapon_length"] * 1.2 + item["speed_rating"]/2 - item["difficulty"] #- item["weight"]
        thrust = item["thrust_damage"] * 3 + item["weapon_length"] * 1.2 + item["speed_rating"]/2 - item["difficulty"] #- item["weight"]
        ##以价值高者为优
        val = max(swing,thrust)
    elif type in ["bow","crossbow","pistol","musket","thrown"]:
        # 好弓弩的标准：伤害高（砍和刺），装弹快，射速高，精准高，装弹多，难度低（难度越大），重量轻（游戏中的重量对伤害没有加成）
        val = item["swing_damage"] + item["thrust_damage"] + item ["speed_rating"] + item["shoot_speed"] + item["accuracy"] + item["max_ammo"] + item["difficulty"] + item["weight"]
    elif type in ["arrows","bolts","bullets"]:
        #好箭矢的标准：伤害高（砍和刺）,数量足，
        val = (item["swing_damage"] + item["thrust_damage"]) * item["max_ammo"] + item["max_ammo"]
    elif type in ["shield"]:
        #好盾的标准：耐久高，减伤大,速度快，面积广，
        val = item["hit_points"] * 2 + item["body_armor"] * 1.5 + item["speed_rating"] + item["weapon_length"]
    elif type in ["head_armor","body_armor","foot_armor","hand_armor"]:
        #好护甲的标准：减伤大（头，身，腿）,难度低，
        val = item["head_armor"] + item["body_armor"] + item["leg_armor"] - item["difficulty"]
    elif type in ["animal","horse"]:
        #好马儿的标准：护甲高（减免伤害和生命值），冲刺强，速度快，操控易
        val = item["body_armor"] * 3 + item["horse_charge"] * 1.5 + item["horse_speed"]  - item["horse_maneuver"]
    elif type in ["goods"]:
        #好商品的标准：质量高，数量多
        val = item["food_quality"] + item["max_ammo"]
    else:
        #其它物品价值都相同
        val = 0
    item["value"] = val
    return val
#对物品的集合进行排序
def sortItems(items):
    size = len(items)
    for i in range(size-1):
        for j in range(size-1-i):
            val1 = valuate(items[j])
            val2 = valuate(items[j+1])
            if val1 > val2:
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp
    return items

'''
    根据伤害类型取出正确的值
'''
def get_swing_damage_by_type(y,damage_type):
    return (y>>iwf_swing_damage_bits)&ibf_damage_mask^(damage_type << iwf_damage_type_bits)

def get_thrust_damage_by_type(y,damage_type):
    return (y>>iwf_thrust_damage_bits)&ibf_damage_mask^(damage_type << iwf_damage_type_bits)
'''
    自动根据获得砍伤值
'''
def get_auto_swing_damage(y):
    damage_types = [cut,pierce,blunt]
    for type in damage_types:
        damage = get_swing_damage_by_type(y,type)
        if damage <= ibf_armor_mask:
            return damage
'''
    自动根据获得刺伤值
'''
def get_auto_thrust_damage(y):
    damage_types = [cut,pierce,blunt]
    for type in damage_types:
        damage = get_thrust_damage_by_type(y,type)
        if damage <= ibf_armor_mask:
            return damage

# for i in range(4):
#     type = cut
#     thrust = weight(6.25)|spd_rtng(94)|weapon_length(128)|swing_damage(119,blunt)|thrust_damage(32,blunt)
#     print get_auto_swing_damage(thrust),get_auto_thrust_damage(thrust)

#分类所有物品并解析出需要的属性
def classifyItem(items):
    itemDatas = {}
    for item in items:
        type = get_weapon_type(item[3])
        value = item[6]
        if(not itemDatas.has_key(type)):
            itemDatas[type] = []
        itemDatas[type].append({
            "item_id":item[0],#物品id
            "type":type,#物品类型
            "weapon_length":get_weapon_length(value),#武器长度
            "speed_rating":get_speed_rating(value),#攻击速度
            "swing_damage":get_auto_swing_damage(value),#砍伤害
            "thrust_damage":get_auto_thrust_damage(value),#刺伤害
            "weight":get_weight(value),#物品重量
            "abundance":get_abundance(value),#物品商店售卖机率
            "difficulty":get_difficulty(value),#物品使用难度
            "hit_points":get_hit_points(value),#盾牌承受伤害值
            "head_armor":get_head_armor(value),#头部护甲
            "body_armor":get_body_armor(value),#身体护甲
            "leg_armor":get_leg_armor(value),#腿部护甲
            "max_ammo":get_max_ammo(value),#箭支、子弹数量，货物数量
            "shoot_speed":get_missile_speed(value),#弓弩手枪射击速度
            "accuracy": get_leg_armor(value),#弓弩手枪精确度
            "horse_speed":get_missile_speed(value),#马匹移动速度
            "horse_maneuver":get_speed_rating(value),#马匹操控值
            "horse_charge":get_thrust_damage(value),#马匹冲刺
            "food_quality":get_head_armor(value),#食物数量
            "value":0
        })
    ##将物品按价值排序（从低到高）
    for k in itemDatas.keys():
        itemDatas[k] = sortItems(itemDatas[k])
    return itemDatas


#加载时就对物品进行分类
itemDatas = classifyItem(items)




'''
    将物品划归一个级别（最大级别为10）
    index:物品索引
    size:物品个数
    maxLevel:级别的个数
'''
def getLevel(index,size,maxLevel=10):
    level = int(math.ceil(1.0 * (index+1) / size * maxLevel))
    return level if(level <= maxLevel) else maxLevel
'''
    根据级别获得所有物品的下标
    
    level:级别编号
    size:物品个数
    maxLevel:级别的个数
'''
def getIndexsByLevel(level,size,maxLevel = 10):
    indexs = []
    for i in range(size):
        if(getLevel(i,size,maxLevel) == level):
            indexs.append(i)
    return indexs
'''
    根据物品的个数，将这些物品索引平均存放到每一个级别中
    由于实现的不同，有以下两种情况
    1.物品个数大于级别个数，尽可能平均分配
    2.物品个数少于级别个数，一个物品可能会出现在多个级别中
    
    无论何种情况，保证全部的物品索引都会存入各个级别中。
    
    size:物品的个数
    maxLevel:级别的个数
'''
def getAllLevelIndexs(size,maxLevel=10):
    levels = []
    for l in range(maxLevel):
        levels.append(getIndexsByLevel(l+1,size,maxLevel))
    ## 平均结果
    rge = range(len(levels))
    rge.reverse()
    for l in rge:
        if len(levels[l]) == 0:
            levels[l] = levels[l+1]
    return levels
'''
    用于测试getAllLevelIndexs方法的生成索引的情况
'''
def detailLevels(size):
    levels = getAllLevelIndexs(size)
    for l in range(len(levels)):
        print "level=" + str(l+1)+"\tsize:"+str(len(levels[l]))+"\tindex=" + str(levels[l])
'''
    根据类别等级获得物品
    参数：类型:级别(最大为10):rmn最大数量（不限制）
        如：horse:8:r2
        
        类型：物品类型
        级别：物品级别
        rmn:如果生成物品数量较多，而指定的最大数量比较小时，取舍的策略（r:随机生成，m:最大值，n:最小值）
        最大数量
'''
def getItemsByTypeLevel(cond,maxLevel = 10):
    reg = "^(\w+)(:(\d+))?(:([rmn])?(\d+))?(:\[(\w+(,\w+)*)\])?$"
    matcher = re.search(reg,cond)
    if(matcher == None):
        raise ValueError("参数格式有误，语法：类型:级别(最大为10):rmn最大数量（不限制）:[过滤关键字，多个之间用逗号]，如：horse:8:r2:[hunter,warhorse]，您的格式："+cond)
    type = matcher.group(1)
    if not itemDatas.has_key(type):
        raise ValueError("类型错误（常用类型，如：horse,arrows,shield等）：" + type)
    ##默认级别为1
    level = 1
    if matcher.group(3) != None:
        level = int(matcher.group(3))
    if (level > maxLevel or level < 1):
        raise ValueError("超出级别范围（有效范围：1-10）,您的级别为" + str(level))
    ##默认策略随机获取
    strategy = "r"
    if matcher.group(5) != None:
        strategy = matcher.group(5)
    ##默认生成1个物品
    maxNum = 1
    if matcher.group(6) != None:
        maxNum = int(matcher.group(6))
    keywords = []
    if matcher.group(8) != None:
        keywords = matcher.group(8).split(",")
    repertory = itemDatas[type]
    #根据当前物品数量获得所有级别的物品索引
    indexs = getAllLevelIndexs(len(repertory),maxLevel)
    #获得当前物品的索引
    myIndexs = indexs[level-1]
    results = []
    size = len(myIndexs)
    ##如果只有一件物品时，就直接返回
    if(len(myIndexs) == 1):
        results=myIndexs
    else:
        if strategy == "m":
            for i in range(size-maxNum,size):
                results.append(myIndexs[i])
        elif strategy == "n":
            for i in range(0,maxNum):
                results.append(myIndexs[i])
        else:
            results = random.sample(myIndexs, maxNum if(len(myIndexs)>=maxNum) else len(myIndexs))
    result = ""
    for i in results:
        id = repertory[i]["item_id"]
        want = False
        if len(keywords) != 0:
            for keyword in keywords:
                if id.__contains__(keyword):
                    want = True
        else:
            want = True
        if want:
            result += "itm_" + id +","
    return result
'''
    批量生产物品
'''
# def buildItems(*conds):
#     result = "["
#     for i  in range(len(conds)):
#         result += getItemsByTypeLevel(conds[i])
#     result += "]"
#     return result
def buildItemsForArray(conds):
    result = "["
    for i in range(len(conds)):
        result += getItemsByTypeLevel(conds[i])
    result += "]"
    return result
'''
    显示物品分类信息
    type:指定要显示的类别，如：shield
    如果不指定，默认显示全部类别信息
'''
def showItemsRank(*types):
    colums = ["item_id", "difficulty", "value", "swing_damage", "thrust_damage", "speed_rating", "accuracy", "weapon_length", "max_ammo",  "hit_points", "head_armor", "leg_armor", "body_armor", "shoot_speed", "weight", "horse_charge", "horse_speed", "horse_maneuver", "type","abundance", "food_quality"]
    for k in itemDatas.keys():
        if types == None or len(types) == 0 or k in types:
            print "【" + k + "】"
            print "%-15s" % ("level"),
            for i in colums:
                if(i == "item_id"):
                    print "%-35s" % (i),
                else:
                    print "%-15s" % (i),
            print
            for i in range(len(itemDatas[k])):
                item = itemDatas[k][i]
                print "%-15s" % (getLevel(i, len(itemDatas[k]))),
                for j in colums:
                    if (j == "item_id"):
                        print "itm_%-35s" % (item[j]),
                    else:
                        print "%-15s" % (item[j]),
                print

#showItemsRank("bow")
#printInfo(getItemsByTypeLevel("one_handed_wpn:3:10"))

#printInfo(buildItems("crossbow","bolts:3","head_armor:2","shield:4","one_handed_wpn:4"))
#printInfo(buildItems("one_handed_wpn:1:3","body_armor:1:3","foot_armor:1:2","foot_armor:2:1","shield:1:3"))
#printInfo(buildItems("one_handed_wpn:10:m1","body_armor:10:r1","foot_armor:10:m1","head_armor:10:m1","shield:10:m1"))
