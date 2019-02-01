# coding=utf-8
import  re
import  random
import data_item
import parse_config
# trained 熟练的
# veteran 老兵
# champion 侍卫
auto = None
#重要的职业
professions={
    #hypaspist(盾兵)
    "infantry":[
        {
            "id":"recruit",
            "name":"新兵",
        },
        {
            "id":"footman",
            "name":"见习步兵",
        },
        {
            "id":"trained_footman",
            "name":"熟练步兵",
        },
        {
            "id":"warrior",
            "name":"战士",
        },
        {
            "id":"veteran",
            "name":"资深士兵",
        },
        {
            "id":"champion",
            "name":"皇家侍卫",
        },
    ],
    "crossbowman":[
        "veteran_crossbowman",
        "sharpshooter",
        {
            "id":"skirmisher",
            "name":"族人",
        },
        {
            "id":"crossbowman",
            "name":"弩手",
        },
        {
            "id":"trained_crossbowman",
            "name":"熟练弩手",
        },
        {
            "id":"veteran_crossbowman",
            "name":"资深弩手",
        },
        {
            "id":"champion",
            "name":"皇家侍卫",
        },
    ],
    "archer":[
        {
            "id": "skirmisher",
            "name": "族人",
        },
        {
            "id": "huntsman",
            "name": "猎人",
        },
        {
            "id": "archer",
            "name": "弓箭手",
        },
        {
            "id": "marksman",
            "name": "神射手",
        },
    ],
    "knight":[
        {
            "id": "recruit",
            "name": "新兵",
        },
        {
            "id": "infantry",
            "name": "步兵",
        },
        {
            "id": "sergeant",
            "name": "中士",
        },
        {
            "id": "man_at_arms",
            "name": "重骑兵",
        },
        {
            "id": "knight",
            "name": "骑士",
        },
    ],
    "horse_archer":[
        {
            "id": "tribesman",
            "name": "族人",
        },
        {
            "id": "skirmisher",
            "name": "弓箭手",
        },
        {
            "id": "horseman",
            "name": "骑手",
        },
        "horse_archer",
        {
            "id": "horse_archer",
            "name": "骑射手",
        },
        "veteran_horse_archer",
        {
            "id": "veteran_horse_archer",
            "name": "资深骑射手",
        },
    ],
    "spearman":[
        "tribesman",
        {
            "id": "tribesman",
            "name": "族人",
        },
        "spearman",
        {
            "id": "spearman",
            "name": "持矛兵",
        },
        "trained_spearman",
        {
            "id": "trained_spearman",
            "name": "熟练持矛兵",
        },
        "veteran_spearman",
        {
            "id": "veteran_spearman",
            "name": "资深持矛兵",
        },
        "sergeant",
        {
            "id": "sergeant",
            "name": "中士",
        },
    ]
}

'''
    config:
        1.reg 正则表达式，匹配一个符号
        2.typeError 不符合正则表达式时显示的错误信息
        3.asigns {"符号名":"要生成数据格式"}
        4.defaultValue 如果最后一个符号没有指定值，就提供一个默认值（20）
        5.range 符号所对应的值范围
        6.asignError 符号不匹配时显示的错误信息
        7.rangeError 符号所对应的值不在指定范围时显示的错误信息
'''
def getCond(format,config):
    #输入格式验证
    params = re.findall(config["reg"],format)
    #验证格式是否没有匹配成功
    if len(params) == 0:
        raise ValueError(config["typeError"] % format)
    #取出全部匹配成功的符号
    asigns= config["asigns"].keys()
    #整合结果
    result = []
    for i in range(len(params)):
        param = params[i]
        #匹配每一个子符号成功
        if param != None:
            asign = param[0]
            #如果符号输入不正确
            if(asign not in asigns):
                raise ValueError(config["asignError"]%asign)
            num = param[1]
            #处理默认值
            if num == None or num == "":
                num = config["defaultValue"]
            #验证数值范围
            if(int(num) not in range(config["range"][0],config["range"][1])):
                raise ValueError(config["rangeError"]%(num))
            #整合全部符号
            for k in asigns:
                if(k == asign):
                    result.append(config["asigns"][k] % (num))
    #返回整合后的数据
    return "|".join(result)

#随机生成的数据都将分成7个级别




'''

    根据指定条件生成属性数据（属性包含：力(s)敏(a)智(i)魅(c)和等级(l，不是数字)）
    如果力敏智魅不提供数值默认为3，如果等级不提供数值默认为1
    如：s5a5i4c4l2        ==》 str_5|agin_5|int_4|cha_4|level(2)
    如：s25a15i4c24l22    ==》 str_25|agin_15|int_4|cha_24|level(22)
    如：sl                ==》 str_3|level(1)
    如：s14l120           ==》 str_14|level(120)
'''
def getAttr(format):
    attrConfig = {
        "reg": "([a-z]+)(\d+)?",
        "typeError": "您输入格式有误，常见格式，如：s25a15i4c24l22，您输入格式：%s",
        "asigns": {
            "s": "str_%s",
            "a": "agi_%s",
            "i": "int_%s",
            "c": "cha_%s",
        },
        "defaultValue": 3,
        "range": [3, 31],
        "asignError": "属性符号只有四种，如：s(力量),a（敏捷）,i（智力）,c（魅力）,l（等级），您的符号：%s",
        "rangeError": "属性的值的范围只能是（1-30），您指定的值为：%s"
    }
    levelConfig = {
        "reg": "([a-z]+)(\d+)?",
        "typeError": "您输入格式有误，常见格式，如：s25a15i4c24l22，您输入格式：%s",
        "asigns": {
            "l": "level(%s)",
        },
        "defaultValue": 1,
        "range": [1, 256],
        "asignError": "属性符号只有四种，如：s(力量),a（敏捷）,i（智力）,c（魅力）,l（等级），您的符号：%s",
        "rangeError": "属性的值的范围只能是（1-30），您指定的值为：%s"
    }
    #解析出等级格式符号
    levelFormat = re.search("l(\d+)?",format).group()
    #解析出属性格式符号
    attrFormat = format if levelFormat == None or levelFormat == "" else format.replace(levelFormat,"")
    return "|".join([getCond(attrFormat,attrConfig),getCond(levelFormat,levelConfig)])

# print getAttr("s5a5i4c4l2")
# print getAttr("s25a15i4c24l22")
# print getAttr("sl")
# print getAttr("s14l120")

'''
    确定数字在max和min之间
'''
def clamp(num,min,max):
    return max if(num>max) else min if(num<min) else num
'''
    根据当前兵种的下标，获得对应的属性和等级值
'''
def getAttrByIndex(index,size,maxAttrVal=25,maxLevel=30):
    perAttr = 1.0 * maxAttrVal / size
    perLvl = 1.0 * maxLevel / size
    min = index;
    max = index+1
    attrList = range(int(min*perAttr)-1,int(max*perAttr))
    lvlList = range(int(min*perLvl)-1,int(max*perLvl))
    strNum = random.choice(attrList)
    agiNum = random.choice(attrList)
    intNum = random.choice(attrList)
    chaNum = random.choice(attrList)
    lvlNum = random.choice(lvlList)
    return getAttr("s%sa%si%sc%sl%s"%(clamp(strNum,3,30),clamp(agiNum,3,30) ,clamp(intNum,3,30),clamp(chaNum,3,30),clamp(lvlNum,1,255)))

'''
    显示属性的大概分布
'''
def showAttrInfo(size=7,maxAttr=25,maxLevel=30):
    for i in range(size):
        print i, getAttrByIndex(i, size,maxAttr,maxLevel)

#showAttrInfo(7)

'''
    根据指定条件生成属性数据（属性包含：单手(one)双手(two)长杆(polearm)弓箭(archery)弓弩(crossbow)投掷(throwing)和火枪（firearm））
    如果武器熟练度不提供数值默认为20
    
    one30two40polearm50archery60crossbow70throwing80firearm90   ==> wp_one_handed(30)|wp_two_handed(40)|wp_polearm(50)|wp_archery(60)|wp_crossbow(70)|wp_throwing(80)|wp_firearm(90)
    one30two40polearm50archery60                                ==> wp_one_handed(30)|wp_two_handed(40)|wp_polearm(50)|wp_archery(60)
    onetwopolearmarcherycrossbowthrowingfirearm                 ==> wp_one_handed(20)|wp_two_handed(20)|wp_polearm(20)|wp_archery(20)|wp_crossbow(20)|wp_throwing(20)|wp_firearm(20)
    one50twopolearm40archery                                    ==> wp_one_handed(50)|wp_two_handed(20)|wp_polearm(40)|wp_archery(20)
'''
def getwp(format):
    config = {
        "reg":"([a-z]+)(\d+)?",
        "typeError":"您输入格式有误，常见格式，如：archery60firearm90，您输入格式：%s",
        "asigns":{
            "wp":"wp(%s)",
            "melee":"wp_melee(%s)",
            "one":"wp_one_handed(%s)",
            "two":"wp_two_handed(%s)",
            "polearm":"wp_polearm(%s)",
            "archery":"wp_archery(%s)",
            "crossbow":"wp_crossbow(%s)",
            "throwing":"wp_throwing(%s)",
            "firearm":"wp_firearm(%s)"
        },
        "defaultValue":20,
        "range":[1,1024],
        "asignError":"属性符号只有七种，如：单手(one)双手(two)长杆(polearm)弓箭(archery)弓弩(crossbow)投掷(throwing)和火枪（firearm），您的符号：%s",
        "rangeError":"属性的值的范围只能是（1-1023），您指定的值为：%s"
    }
    return getCond(format,config)
'''
    根据格式符号生成对应的技能信息
    例如:
        riding4ironflesh5powerstrike6prisoner2  ==> knows_riding_4|knows_ironflesh_5|knows_power_strike_6|knows_prisoner_management_2
        riding9                                 ==> knows_riding_9
        riding9shield3                          ==> knows_riding_9|knows_shield_3       
        
'''
def getKnows(format):
    config = {
        "reg":"([a-z]+)(\d+)?",
        "typeError":"您输入格式有误，常见格式，如：archery60firearm90，您输入格式：%s",
        "asigns":{
            "trade":"knows_trade_$s",#交 易
            "leadership":"knows_leadership_%s",#统 御
            "prisoner":"knows_prisoner_management_%s",#俘 虏 管 理
            "engineer":"knows_engineer_%s",#工 程 学
            "firstaid":"knows_first_aid_%s",#急 救
            "surgery":"knows_surgery_%s",#手 术
            "treatment":"knows_wound_treatment_%s",#疗 伤
            "inventory":"knows_inventory_management_%s",#物 品 管 理
            "pathfinding":"knows_pathfinding_%s",#向 导
            "spotting":"knows_spotting_%s",#侦 察
            "tactics":"knows_tactics_%s",#战 术
            "tracking":"knows_tracking_%s",#跟 踪
            "trainer":"knows_trainer_%s",#教 练
            "archery":"knows_horse_archery_%s",#骑 射
            "riding":"knows_riding_%s",#骑 术
            "athletics":"knows_athletics_%s",#跑 动
            "weapon":"knows_weapon_master_%s",#武 器 掌 握
            "shield":"knows_shield_%s",#盾 防
            "powerdraw":"knows_power_draw_%s",#强 弓
            "powerthrow":"knows_power_throw_%s",#强 掷
            "powerstrike":"knows_power_strike_%s",#强 击
            "ironflesh":"knows_ironflesh_%s",#铁 骨
        },
        "defaultValue":1,
        "range":[1,11],
        "asignError":"技术符号共有21种，如：交易(trade)统御(leadership)工程学(engineer)急救(firstaid)手术(surgery)疗伤(treatment)物品管理（inventory)向导(pathfinding)战术(tactics)跟踪(tracking)教练(trainer)骑射(archery)骑术(riding)跑动(athletics)武器管理(weapon)盾防(shield)强弓(powerdraw)强掷(powerthrow)强击(powerstrike)铁骨(ironflesh),您的符号：%s",
        "rangeError":"属性的值的范围只能是（1-10），您指定的值为：%s"
    }
    return getCond(format,config)

# print getKnows("riding4ironflesh5powerstrike6prisoner2")
# print getKnows("riding9")
# print getKnows("riding9shield3")


'''
    根据职业生成技能点
'''
def getKnowsByProfession():

    return None

def rangeReverse(start,end):
    rg = range(start,end)
    rg.reverse()
    return rg

'''
    得到一个比较平稳的装备数量,主要的目的就是:兵种等级超高,装备数量越少(装备等级超高,伤害超高)
    默认:
        [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8]
'''
# def getItemsCount(size = 16):
#     count = size/2 if size%2==0 else size/2+1
#     counts = []
#     for i in range(1,count+1):
#         for j in range(0,i+1):
#             counts.append(i)
#     return counts
# print getItemsCount()
'''
    
'''
# def getItemsByGuaranteeType(format,index,size,maxLevel = 10):
#     ##武器最大级别为10
#     perLevel = 1.0*maxLevel/size
#     level = int((index+1)*perLevel)
#     types = format.split("|")
#     ## 以下参数主要的目的就是:兵种等级超高, 装备数量越少(装备等级超高, 伤害超高)
#     #装备数量集合
#     counts = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8]
#     #等级数量集合,最高等级(10)用于领主等高级兵种
#     levels = [9,8,7,6,5,4,3,2,1]
#     #装备随机性,装备个数越少随机性越小(高手只用一件装备,哈哈)
#     randomneses = {
#         "r":[3,4,5],
#         "n":[2],
#         "m":[1]
#     }
#     #每个标识所对应的装备类型
#     guarantees = {
#         "tf_guarantee_boots":"foot_armor",
#         "tf_guarantee_armor":"body_armor",
#         "tf_guarantee_helmet":"head_armor",
#         "tf_guarantee_gloves":"hand_armor",
#         "tf_guarantee_horse":"horse",
#         "tf_guarantee_shield":"shield",
#         "tf_guarantee_ranged":"bow",#默认使用弓箭,弓弩和标枪等远程暂时没有考虑
#     }
#     items = []
#     for type in types:
#         count = counts[size-index]
#         level = levels[count]
#         for i in range(0,count):
#             random = "r"
#             for randomnes in randomneses.keys():
#                 if count in randomneses[randomnes]:
#                     random = randomnes
#                     break
#             items.append("%s:%s:%s%s" % (guarantees[type],level-i, random, i+1))
#     return items
# print getItemsByGuaranteeType("tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield",4,5)

def autoAttr(index,step=2):
    attr = (index+1)*step*1.3
    lvl = index*step*1.2
    return getAttr("s%sa%si%sc%sl%s" % (clamp(attr, 3, 30), clamp(attr, 3, 30), clamp(attr, 3, 30), clamp(attr, 3, 30), clamp(lvl, 1, 255)))

# for i in range(7):
#     print autoAttr(i)

def autowp(index,step=20):
    wp = (index+1)*step*1.12
    return getwp("wp%s"%(wp))

# for i in range(7):
#     print autowp(i)

def autoSkill(index,type,step=1):
    val = (index + step) * 0.9 - 1
    val = clamp(val,1,val)
    types = {
        "infantry":"powerstrike%sironflesh%sshield%sathletics%s"%(val+2,val+2,val,val),
        "crossbowman":"powerstrike%sironflesh%sshield%sathletics%s"%(val+1,val+1,val,1),
        "knight":"powerstrike%sironflesh%sshield%sriding%s"%(val,val,val,val+1),
        "spearman":"powerstrike%sironflesh%sshield%sathletics%s"%(val+2,val+2,val,val),
        "archer":"powerstrike%sironflesh%sshield%sathletics%spowerdraw%s"%(val+1,val+1,val,1,val+1),
        "horse_archer":"powerstrike%sironflesh%spowerdraw%sriding%sarchery%s"%(val,val,val+1,val,val+1),
    }
    return getKnows(types[type])

# for i in range(7):
#     print autoSkill(i,"archer")

def autoItem(index,type,step=1):
    val = int((index + step) * 0.9)
    val = clamp(val, 1, val)
    types = {
        "infantry": ["one_handed_wpn:%s:%s" % (val,2),"one_handed_wpn:%s:%s" % (val+1,2),"foot_armor:%s:%s" % (val,2),"body_armor:%s:%s" % (val,2),"hand_armor:%s:%s" % (val,2),"shield:%s:%s" % (val,2),"head_armor:%s:%s" % (val,2)],
        "crossbowman": ["one_handed_wpn:%s:%s" % (val,2),"one_handed_wpn:%s:%s" % (val+1,2),"foot_armor:%s:%s" % (val,2),"body_armor:%s:%s" % (val,2),"shield:%s:%s" % (val,2),"head_armor:%s:%s" % (val,2),"crossbow:%s:%s" % (val,2),"bolts:%s:%s" % (val,2)],
        "knight": ["polearm:%s:%s" % (val,2),"polearm:%s:%s" % (val+1,2),"foot_armor:%s:%s" % (val,2),"body_armor:%s:%s" % (val,2),"hand_armor:%s:%s" % (val,2),"shield:%s:%s" % (val,2),"head_armor:%s:%s" % (val,2),"horse:%s:%s" % (val,2)],
        "spearman": ["polearm:%s:%s" % (val,2),"polearm:%s:%s" % (val+1,2),"foot_armor:%s:%s" % (val,2),"body_armor:%s:%s" % (val,2),"hand_armor:%s:%s" % (val,2),"shield:%s:%s" % (val,2),"head_armor:%s:%s" % (val,2)],
        "archer": ["one_handed_wpn:%s:%s" % (val,2),"one_handed_wpn:%s:%s" % (val+1,2),"foot_armor:%s:%s" % (val,2),"body_armor:%s:%s" % (val,2),"shield:%s:%s" % (val,2),"head_armor:%s:%s" % (val,2),"bow:%s:%s" % (val,2),"arrows:%s:%s" % (val,2)],
        "horse_archer": ["one_handed_wpn:%s:%s" % (val,2),"foot_armor:%s:%s" % (val,2),"body_armor:%s:%s" % (val,2),"hand_armor:%s:%s" % (val,2),"shield:%s:%s" % (val,2),"head_armor:%s:%s" % (val,2),"horse:%s:%s" % (val,2),"bow:%s:%s" % (val,2),"arrows:%s:%s" % (val,2)],
    }
    return data_item.buildItemsForArray(types[type])

def autoFlag(type):
    types = {
        "infantry": "tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet",
        "crossbowman": "tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield",
        "knight": "tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield",
        "spearman": "tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet",
        "archer": "tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor",
        "horse_archer": "tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_shield",
    }
    return types[type]

def getTroopConfig(format,fac):
    reg = "^([a-z]+)(\d+)$"
    matcher = re.search(reg,format)
    if matcher == None:
        raise ValueError("语法格式有误，语法：类型:级别(1-7),如:knight4")
    type = matcher.group(1)
    if type not in professions.keys():
        raise ValueError("兵种类型错误,没有此类兵种:"+type)
    troops = professions[type]
    level = matcher.group(2)
    index = 0;
    if level == None or int(level) <= 0:
        level = 1
    level = int(level)
    if level > len(troops):
        index = len(troops)-1
    else:
        index = level -1
    troop = troops[index]
    troop["id"] = fac["fac_id"]+"_"+troop["id"]
    troop["troop_name"] = fac["fac_id"] + " " + troop["id"]
    troop["attr"] =autoAttr(index)
    troop["items"] = autoItem(index,type)
    troop["wp"] = autowp(index)
    troop["flag"] = autoFlag(type)
    troop["skill"] = autoSkill(index,type)
    troop["face1"] = parse_config.getFace(period=random.choice(parse_config.periods))
    troop["face2"] = parse_config.getFace(period=random.choice(parse_config.periods))
    return troop

# for i in range(10):
#     print getTroopConfig("knight%s"%(i))["name"]

def getTroopConfigList(formats,fac):
    if checkRepeat(formats):
        raise ValueError("提供的兵种模板有重复的数据："+formats)
    configs = []
    for format in formats:
        configs.append(getTroopConfig(format,fac))
    return configs

def checkRepeat(formats):
    counts = {}
    for format in formats:
        if(not counts.has_key(format)):
            counts[format] = []
        counts[format].append(1)
    for format in formats:
        if len(counts[format]) > 1:
            return True
    return False


##print checkRepeat([1])
