#-*-coding:utf-8-*-
import os
import re
import random
import file_util
import config
import data_troop
import base_data
from  output import *
## 复制SceneObj文件并提供别名
# def renameSceneObj(path,base,path2):
#     dirs = os.listdir(path)
#     for file in dirs:
#         no = re.search(r"\d+", file).group()  ##18
#         newfile = file.replace(no, str(int(no) + base))
#         sourceFile = os.path.join(path,file)
#         targetFile = os.path.join(path2,newfile)
#         open(targetFile, "wb").write(open(sourceFile, "rb").read())
#         print "完成："+targetFile

'''
    普通兵种面部
'''
faces = [
        "swadian_face_younger_1",
        "swadian_face_young_1",
        "swadian_face_middle_1",
        "swadian_face_old_1",
        "swadian_face_older_1",
        "swadian_face_younger_2",
        "swadian_face_young_2",
        "swadian_face_middle_2",
        "swadian_face_old_2",
        "swadian_face_older_2",
        "vaegir_face_younger_1",
        "vaegir_face_young_1",
        "vaegir_face_middle_1",
        "vaegir_face_old_1",
        "vaegir_face_older_1",
        "vaegir_face_younger_2",
        "vaegir_face_young_2",
        "vaegir_face_middle_2",
        "vaegir_face_old_2",
        "vaegir_face_older_2",
        "khergit_face_younger_1",
        "khergit_face_young_1",
        "khergit_face_middle_1",
        "khergit_face_old_1",
        "khergit_face_older_1",
        "khergit_face_younger_2",
        "khergit_face_young_2",
        "khergit_face_middle_2",
        "khergit_face_old_2",
        "khergit_face_older_2",
        "nord_face_younger_1",
        "nord_face_young_1",
        "nord_face_middle_1",
        "nord_face_old_1",
        "nord_face_older_1",
        "nord_face_younger_2",
        "nord_face_young_2",
        "nord_face_middle_2",
        "nord_face_old_2",
        "nord_face_older_2",
        "rhodok_face_younger_1",
        "rhodok_face_young_1",
        "rhodok_face_middle_1",
        "rhodok_face_old_1",
        "rhodok_face_older_1",
        "rhodok_face_younger_2",
        "rhodok_face_young_2",
        "rhodok_face_middle_2",
        "rhodok_face_old_2",
        "rhodok_face_older_2"
    ]

species = ["swadian","vaegir","khergit","nord","rhodok"]
periods = ["younger","young","middle","old","older"]
'''
    species:人种 1.swadian 2.vaegir 3.khergit 4.nord 5.rhodok
    period:时期 1.younger 2.young 3.middle 4.old 5.older
    
    如果没有找到就随机产生一个
'''
def getFace(species=None,period=None):
    result = file_util.filter(faces,(species if(species != None) else "")+"_face_"+(period+"_" if(period != None) else ""))
    if len(result) > 0:
        return result[random.randint(0,len(result)-1)]
    return faces[random.randint(0,len(faces)-1)]
'''
 英雄面部
'''
heroFaces = [
    "0x0000000f45041105241acd2b5a66a86900000000001e98310000000000000000",
    "0x0000000ec50001400a2269f919dee11700000000001cc57d0000000000000000",
    "0x0000000cee0051cc44be2d14d370c65c00000000001ed6df0000000000000000",
    "0x0000000e2c0c028a068e8c18557b12a500000000001c0fe80000000000000000",
    "0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000",
    "0x0000000f45041105241acd2b5a66a86900000000001e98310000000000000000",
    "0x0000000ec50001400a2269f919dee11700000000001cc57d0000000000000000",
    "0x0000000cee0051cc44be2d14d370c65c00000000001ed6df0000000000000000",
    "0x0000000e2c0c028a068e8c18557b12a500000000001c0fe80000000000000000",
    "0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000",
    "0x0000000f45041105241acd2b5a66a86900000000001e98310000000000000000",
    "0x0000000ec50001400a2269f919dee11700000000001cc57d0000000000000000",
    "0x0000000cee0051cc44be2d14d370c65c00000000001ed6df0000000000000000",
    "0x0000000e2c0c028a068e8c18557b12a500000000001c0fe80000000000000000",
    "0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000",
    "0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000",
    "0x0000000f45041105241acd2b5a66a86900000000001e98310000000000000000",
    "0x0000000ec50001400a2269f919dee11700000000001cc57d0000000000000000",
    "0x0000000cee0051cc44be2d14d370c65c00000000001ed6df0000000000000000",
    "0x0000000e2c0c028a068e8c18557b12a500000000001c0fe80000000000000000",
    "0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000",
    "0x0000000f45041105241acd2b5a66a86900000000001e98310000000000000000",
    "0x0000000ec50001400a2269f919dee11700000000001cc57d0000000000000000",
    "0x0000000cee0051cc44be2d14d370c65c00000000001ed6df0000000000000000",
    "0x0000000e2c0c028a068e8c18557b12a500000000001c0fe80000000000000000",
    "0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000",
    "0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000",
    "0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000",
    "0x0000000c3e08601414ab4dc6e39296b200000000001e231b0000000000000000",
    "0x0000000c0f08000458739a9a1476199800000000001fb6f10000000000000000",
    "0x0000000c0610351048e325361d7236cd00000000001d532a0000000000000000",
    "0x0000000c03104490280a8cb2a24196ab00000000001eb4dc0000000000000000",
    "0x0000000c330855054aa9aa431a48d74600000000001ed5240000000000000000",
    "0x0000000c2a0805442b2c6cc98c8dbaac00000000001d389b0000000000000000",
    "0x0000000c380c30c2392a8e5322a5392c00000000001e5c620000000000000000",
    "0x0000000c3f10000532d45203954e192200000000001e47630000000000000000",
    "0x0000000c5c0840034895654c9b660c5d00000000001e34530000000000000000",
    "0x0000000c1e001500589dae4094aa291c00000000001e37a80000000000000000",
    "0x000000095108144657a1ba3ad456e8cb00000000001e325a0000000000000000",
    "0x0000000c010c42c14d9d6918bdb336e200000000001dd6a30000000000000000",
    "0x0000000c150045c6365d8565932a8d6400000000001ec6940000000000000000",
    "0x0000000c0f0c320627627238dcd6599400000000001c573d0000000000000000",
    "0x0000000cb700210214ce89db276aa2f400000000001d36730000000000000000",
    "0x00000008200012033d9b6d4a92ada53500000000001cc1180000000000000000",
    "0x0000000c4d0840d24a9b2ab4ac2a332400000000001d34db0000000000000000",
    "0x0000000c370c1194546469ca6c4e450e00000000001ebac40000000000000000",
    "0x0000000c0c1064864ba34e2ae291992b00000000001da8720000000000000000",
    "0x0000000c0a08038736db74c6a396a8e500000000001db8eb0000000000000000",
    "0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000",
    "0x0000000c2a0015d249b68b46a98e176400000000001d95a40000000000000000",
    "0x0000000c131031c546a38a2765b4c86000000000001e58d30000000000000000",
    "0x0000000c2f0832c748f272540d8ab65900000000001d34e60000000000000000",
    "0x0000000e310061435d76bb5f55bad9ad00000000001ed8ec0000000000000000",
    "0x0000000a0100421038da7157aa4e430a00000000001da8bc0000000000000000",
    "0x0000000c04100153335ba9390b2d277500000000001d89120000000000000000",
    "0x0000000c00046581234e8da2cdd248db00000000001f569c0000000000000000",
    "0x0000000c160451d2136469c4d9b159ad00000000001e28f10000000000000000",
    "0x0000000f7c00520e66b76edd5cd5eb6e00000000001f691e0000000000000000",
    "0x0000000c1d0821d236acd6991b74d69d00000000001e476c0000000000000000",
    "0x0000000c0f04024b2509d5d53944c6a300000000001d5b320000000000000000",
    "0x0000000c680432d3392230cb926d56ca00000000001da69b0000000000000000",
    "0x0000000c27046000471bd2e93375b52c00000000001dd5220000000000000000",
    "0x0000000de50052123b6bb36de5d6eb7400000000001dd72c0000000000000000",
    "0x000000085f00000539233512e287391d00000000001db7200000000000000000",
    "0x0000000a070c4387374bd19addd2a4ab00000000001e32cc0000000000000000",
    "0x0000000b670012c23d9b6d4a92ada53500000000001cc1180000000000000000",
    "0x0000000e070050853b0a6e4994ae272a00000000001db4e10000000000000000",
    "0x0000000f800021c63b0a6e4994ae272a00000000001db4e10000000000000000",
    "0x000000043000318b54b246b7094dc39c00000000001d31270000000000000000",
    "0x0000000c280461004929b334ad632aa200000000001e05120000000000000000",
    "0x0000000e880062c53b0a6e4994ae272a00000000001db4e10000000000000000",
    "0x0000000c23085386391b5ac72a96d95c00000000001e37230000000000000000",
    "0x0000000efe0051ca4b377b4964b6eb6500000000001f696c0000000000000000",
    "0x00000006f600418b54b246b7094dc31a00000000001d37270000000000000000",
    "0x0000000bdd00510a44be2d14d370c65c00000000001ed6df0000000000000000",
    "0x0000000abc00518b5af4ab4b9c8e596400000000001dc76d0000000000000000",
    "0x0000000a180441c921a30ea68b54971500000000001e54db0000000000000000",
    "0x0000000a3b00418c5b36c686d920a76100000000001c436f0000000000000000",
    "0x00000007d100534b44962d14d370c65c00000000001ed6df0000000000000000",
    "0x0000000bf400610c5b33d3c9258edb6c00000000001eb96d0000000000000000",
    "0x0000000bfd0061c65b6eb33b25d2591d00000000001f58eb0000000000000000",
    "0x0000000b6900514144be2d14d370c65c00000000001ed6df0000000000000000",
    "0x0000000c360c524b6454465b59b9d93500000000001ea4860000000000000000",
    "0x0000000c350c418438ab85b75c61b8d300000000001d21530000000000000000",
    "0x0000000c3c0821c647264ab6e68dc4d500000000001e42590000000000000000",
    "0x0000000c0810500347ae7acd0d3ad74a00000000001e289a0000000000000000",
    "0x0000000c1500510528f50d52d20b152300000000001d66db0000000000000000",
    "0x0000000f7800620d66b76edd5cd5eb6e00000000001f691e0000000000000000",
    "0x0000000c13002254340eb1d91159392d00000000001eb75a0000000000000000",
    "0x0000000c1610218368e29744e9a5985b00000000001db2a10000000000000000",
    "0x0000000c03040289245a314b744b30a400000000001eb2a90000000000000000",
    "0x0000000c3f1001ca3d6955b26a8939a300000000001e39b60000000000000000",
    "0x0000000ff508330546dc4a59422d450c00000000001e51340000000000000000",
    "0x00000005b00011813d9b6d4a92ada53500000000001cc1180000000000000000",
    "0x00000006690002873d9b6d4a92ada53500000000001cc1180000000000000000",
    "0x0000000f830051c53b026e4994ae272a00000000001db4e10000000000000000",
    "0x0000000c230401c6349c2e9b2168eb1a00000000001eb0630000000000000000",
    "0x000000084b0002063d9b6d4a92ada53500000000001cc1180000000000000000",
    "0x0000000ca100224d56a5d5c65c70c40a00000000001d54de0000000000000000",
    "0x0000000b9500020824936cc51cb5bb2500000000001dd4d80000000000000000",
    "0x0000000a300012c439233512e287391d00000000001db7200000000000000000",
    "0x0000000c0700414f2cb6aa36ea50a69d00000000001dc55c0000000000000000",
    "0x0000000d920801831715d1aa9221372300000000001ec6630000000000000000",
    "0x000000099700124239233512e287391d00000000001db7200000000000000000",
    "0x0000000c2f0442036d232a2324b5b81400000000001e55630000000000000000",
    "0x0000000c0d00118866e22e3d9735a72600000000001eacad0000000000000000",
    "0x0000000c0308225124e26d4a6295965a00000000001d23e40000000000000000",
    "0x0000000f630052813b6bb36de5d6eb7400000000001dd72c0000000000000000",
    "0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000",
    "0x0000000c390c659229136db45a75251300000000001f16930000000000000000",
    "0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000",
    "0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000",
    "0x0000000c060400c454826e471092299a00000000001d952d0000000000000000",
    "0x0000000c040804d2293c46a6a5669ce400000000001db7120000000000000000",
    "0x0000000c3a0455c443d46e4c8b91291a00000000001ca51b0000000000000000",
    "0x0000000c2c0844d42914d19b2369b4ea00000000001e331b0000000000000000",
    "0x0000000c130461054af448eb19cd40e400000000001d488a0000000000000000",
    "0x00000008e20011063d9b6d4a92ada53500000000001cc1180000000000000000",
    "0x0000000c170c14874752adb6eb3228d500000000001c955c0000000000000000",
    "0x0000000c080c13d056ec8da85e3126ed00000000001d4ce60000000000000000",
    "0x0000000cbf10100562a4954ae731588a00000000001d6b530000000000000000",
    "0x0000000c330805823baa77556c4e331a00000000001cb9110000000000000000",
    "0x0000000d51000106370c4d4732b536de00000000001db9280000000000000000",
    "0x0000000c06046151435b5122a37756a400000000001c46e50000000000000000",
    "0x0000000c081001d3465c89a6a452356300000000001cda550000000000000000",
    "0x0000000a3d0c13c3452aa967276dc95c00000000001dad350000000000000000",
    "0x0000000c3f08038245545e3b236a68de00000000001e37230000000000000000",
    "0x0000000d8a00514544be2d14d370c65c00000000001ed6df0000000000000000",
]
'''
    随机获得一个英雄面部
'''
def getRandomHeroFace():
    return heroFaces[random.randint(0,len(heroFaces)-1)]
'''
    将十进制数转换成16进制的数字，base代表宽度，如果不够，就在数字前面补0
    如：hexstr(10,2) ==> 0a
        hexstr(18,2) ==> 12
        hexstr(18,3) ==> 012
'''
def hexstr(num,base=2):
    info = hex(num)[2:]
    return info if(len(info)==base) else ("0"*(base-len(info)))+info
'''
    随机获得颜色
'''
def getRandomColor():
    r = hexstr(random.randint(0, 255))
    g = hexstr(random.randint(0, 255))
    b = hexstr(random.randint(0, 255))
    return "0x"+("%s%s%s" % (r, g, b)).upper()
'''
    随机获得指定数量的不重复的颜色列表
'''
def getRandomColors(num):
    clrs = []
    for i in range(0,num):
        clr = getRandomColor()
        if clrs.__contains__(clr):
            i = i-1
            continue
        clrs.append(clr)
    return clrs

'''
    生成指定数量的国家名称或id
'''
def getFactionNames(num):
    facs = {}
    for i in range(0,num):
        facs[i] = "kingdom_"+str(i+1)
    return facs

factions = base_data.sys_factions + config.factions
default_faction = config.default_faction
#保存生成的数据，即将要写入到脚本中的数据
dataList = {
    "cultures":[],##文化集合
    "factions":[],##国家集合
    "troops":[],##兵种集合
    "upgrades":[],##兵种升级集合
    "kings":[],##国王集合
    "lords":[],##领主集合
    "partyTemplate":[],##兵种模板集合
    "facCities":[],##属于国家的城堡
    "lordCities":[],##属于领主的城堡
    "kingCities":[],##属于领主的城堡
    "constants":{
        # "kingdoms_begin":"\"fac_player_supporters_faction\"",
        # "kingdoms_end":"\"fac_kingdoms_end\"",
        "kingdom_ladies_begin":"\"trp_knight_1_1_wife\"",
        #"kingdom_ladies_end":"\"trp_heroes_end\"",
        "kings_begin":"\"trp_kingdom_1_lord\"",
        "kings_end":"\"trp_knight_1_1\"",
        "kingdom_heroes_begin":"\"trp_kingdom_1_lord\"",
        #"kingdom_heroes_end":"kingdom_ladies_begin",
        # "heroes_begin":"kingdom_heroes_begin",
        # "kingdom_heroes_end":"kingdom_ladies_end",
        # "companions_begin":"\"trp_npc1\"",
        # "companions_end":"\"trp_kingdom_heroes_including_player_begin\"",
        # "soldiers_begin":"\"trp_farmer\"",
        # "soldiers_end":"\"trp_town_walker_1\"",
        "pretenders_begin":"\"trp_kingdom_1_pretender\"",
        #"pretenders_end":"kingdom_heroes_end"
    }
}

'''
    生成国家信息，可以提供名字列表和对应的颜色列表（数量要对应）
'''
def getFactions():
    facs = []
    for i in range(0,len(factions)):
        fac = factions[i]
        fac_id = fac["fac_id"] if(fac.has_key("fac_id")) else "kingdom_"+str(i+1);
        fac_name = fac["fac_name"] if(fac.has_key("fac_name")) else "kingdom_"+str(i+1);
        color = fac["color"] if(fac.has_key("color")) else getRandomColor();
        facs.append("(\"%s\",  \"%s\",    0, 0.9, [(\"outlaws\",-0.05),(\"peasant_rebels\", -0.1),(\"deserters\", -0.02),(\"mountain_bandits\", -0.05),(\"forest_bandits\", -0.05)], [], %s),\n"%(fac_id,fac_name,color))
        ## 生成城堡信息
        cities = fac["cities"] if (fac.has_key("cities")) else None
        if cities != None and len(cities) != 0:
            for city in cities:
                dataList["facCities"].append('(call_script, "script_give_center_to_faction_aux", "%s", "%s"),\n'%(city,"fac_"+fac_id))
    dataList["factions"] = facs
'''
    根据国家名字生成对应的文化信息
'''
def getCultures():
    culs = []
    for i in range(0,len(factions)):
        fac = factions[i]
        fac_id = fac["fac_id"] if (fac.has_key("fac_id")) else "kingdom_" + str(i+1);
        culs.append("(\"culture_%s\",  \"%s_culture\", 0, 0.9, [], []),\n"%(i+1,fac_id))
    dataList["cultures"] = culs
'''
    根据国家名称生成对应的部队模板信息
'''
def getPartyTemplate():
    temps = []
    troop_max_num = default_faction["troop_max_num"]
    for i in range(0,len(factions)):
        fac = factions[i]
        fac_id = fac["fac_id"] if (fac.has_key("fac_id")) else "kingdom_" + str(i + 1);
        ##计算该国家所对应的第一个兵种的位置
        idx = troop_max_num * i;
        troop1_id = "trp_"+re.search("\w+",dataList["troops"][idx]).group() #获得该国家第一个兵种
        troop2_id = "trp_"+re.search("\w+",dataList["troops"][idx+1]).group() #获得该国家第二个兵种
        troop3_id = "trp_"+re.search("\w+",dataList["troops"][idx+2]).group() #获得该国家第三个兵种
        troop4_id = "trp_"+re.search("\w+",dataList["troops"][idx+3]).group() #获得该国家第四个兵种
        temps.append("(\"{}_reinforcements_a\", \"{}_reinforcements_a\", 0, 0, fac_commoners, 0, [({},2,6),({},4,7)]),\n".format(fac_id,fac_id,troop1_id,troop2_id))
        temps.append("(\"{}_reinforcements_b\", \"{}_reinforcements_b\", 0, 0, fac_commoners, 0, [({},2,6),({},4,7)]),\n".format(fac_id,fac_id,troop2_id,troop3_id))
        temps.append("(\"{}_reinforcements_c\", \"{}_reinforcements_c\", 0, 0, fac_commoners, 0, [({},3,6)]),\n".format(fac_id,fac_id,troop4_id))
    dataList["partyTemplate"] = temps


'''
    生成国家编号
'''
def getFacId(fac_index):
    return "kingdom_" + str(fac_index + 1)

'''
    如果没有配置兵种信息时,可以获得默认的兵种配置
    troopsKey:兵种的关键字,如:king,lords,wifes等
    fac:当前国家的信息
    troop:当前兵种信息
    trp_index:当前兵种所对应的编号:如:0,1,2,3
'''
def getDefaultTroop(troopsKey,fac,trp_index):
    troops = fac[troopsKey] if (fac.has_key(troopsKey)) else default_faction[troopsKey]
    #如果生成(国王,领主,妻子,女儿)时,没有提供,数据就随机从默认数据里提取
    if troopsKey in ["king","lords","wifes","daughters"]:
        return random.choice(default_faction[troopsKey])
    else:#如果生成士兵时,没有提供数据,就依次从默认的数据里提取
        return troops[trp_index] if (trp_index < len(troops)) else random.choice(default_faction[troopsKey])
'''
    生成兵种id
    troopsKey:兵种的关键字,如:king,lords,wifes等
    fac_index:国家的编号,如:0,1,2,3
    troop:当前兵种信息
    trp_index:当前兵种所对应的编号:如:0,1,2,3
'''
def getTroopId(troopsKey,fac_index,troop,trp_index):
    troopId = ""
    if troopsKey == "troops":
        troopId = troop["id"] if(troop.has_key("id")) else "troop_%s_%s"%(fac_index+1,trp_index+1)
    elif troopsKey == "king":
        troopId = troop["id"] if (troop.has_key("id")) else "%s_lord" % (getFacId(fac_index))
    elif troopsKey == "lords":
        troopId = troop["id"] if(troop.has_key("id")) else "knight_%s_%s"%(fac_index+1,trp_index+1)
    elif troopsKey == "wifes":
        troopId = troop["id"] if(troop.has_key("id")) else "wife_%s_%s"%(fac_index+1,trp_index+1)
    elif troopsKey == "daughters":
        troopId = troop["id"] if(troop.has_key("id")) else "daughter_%s_%s"%(fac_index+1,trp_index+1)
    else:
        troopId = troop["id"] if(troop.has_key("id")) else "hero_%s"%(trp_index+1)
    return troopId
'''
    生成兵种名称
'''
def getTroopName(troopsKey,fac_index,troop,trp_index):
    troopId = ""
    if troopsKey == "troops":
        troopId = troop["troop_name"] if(troop.has_key("troop_name")) else "troop %s %s"%(fac_index+1,trp_index+1)
    elif troopsKey == "king":
        troopId = troop["troop_name"] if (troop.has_key("troop_name")) else "%s lord" % (getFacId(fac_index))
    elif troopsKey == "lords":
        troopId = troop["troop_name"] if(troop.has_key("troop_name")) else "knight %s %s"%(fac_index+1,trp_index+1)
    elif troopsKey == "wifes":
        troopId = troop["troop_name"] if(troop.has_key("troop_name")) else "wife %s %s"%(fac_index+1,trp_index+1)
    elif troopsKey == "daughters":
        troopId = troop["troop_name"] if(troop.has_key("troop_name")) else "daughter %s %s"%(fac_index+1,trp_index+1)
    else:
        troopId = troop["troop_name"] if(troop.has_key("troop_name")) else "hero %s"%(trp_index+1)
    return troopId

'''
    获得兵种的装备信息
    寻找策略如下:
        1.如果用户配置了装备信息，优先使用，
        2.如果用户没有配置就找该国家的(troop_items,king_items,lord_items,wife_items,daughter_items,hero_items)配置信息，
        3.如果还没有找到,就找default_troop提供的配置信息
    
'''
def getTroopItems(troopsKey,fac,troop,default_troop):
    items = ""
    if troopsKey == "troops":
        items = troop["items"] if (troop.has_key("items")) else (fac["troop_items"] if (fac.has_key("troop_items")) else default_troop["items"])
    elif troopsKey == "king":
        items = troop["items"] if (troop.has_key("items")) else (fac["king_items"] if (fac.has_key("king_items")) else default_troop["items"])
    elif troopsKey == "lords":
        items = troop["items"] if (troop.has_key("items")) else (fac["lord_items"] if (fac.has_key("lord_items")) else default_troop["items"])
    elif troopsKey == "wifes":
        items = troop["items"] if (troop.has_key("items")) else (fac["wife_items"] if (fac.has_key("wife_items")) else default_troop["items"])
    elif troopsKey == "daughters":
        items = troop["items"] if (troop.has_key("items")) else (fac["daughter_items"] if (fac.has_key("daughter_items")) else default_troop["items"])
    else:
        items = troop["items"] if (troop.has_key("items")) else (fac["hero_items"] if (fac.has_key("hero_items")) else default_troop["items"])
    return items

def getTroopWp(troopsKey,troop):
    wp = ""
    if troopsKey == "troops":
        wp = troop["wp"] if(troop.has_key("wp")) else "wp("+str(random.randint(80,200))+")"
    elif troopsKey == "king":
        wp = troop["wp"] if (troop.has_key("wp")) else "wp(" + str(random.randint(300, 500)) + ")"
    elif troopsKey == "lords":
        wp = troop["wp"] if (troop.has_key("wp")) else "wp(" + str(random.randint(200, 350)) + ")"
    elif troopsKey == "wifes":
        wp = troop["wp"] if (troop.has_key("wp")) else "wp(" + str(random.randint(100, 120)) + ")"
    elif troopsKey == "daughters":
        wp = troop["wp"] if (troop.has_key("wp")) else "wp(" + str(random.randint(50, 80)) + ")"
    else:
        wp = troop["wp"] if (troop.has_key("wp")) else "wp(" + str(random.randint(20, 600)) + ")"
    return wp

def createTroop(lords, trp_index, troopsKey, fac, fac_index, fac_id):
    troop = lords
    if type(lords) is list:
        # 当前用户配置的领主信息
        troop = lords[trp_index] if (trp_index < len(lords)) else {}
    # 如果用户没有配置时采用的备用信息
    default_troop = getDefaultTroop(troopsKey, fac, trp_index)
    id = getTroopId(troopsKey,fac_index,troop,trp_index)
    troop_name = getTroopName(troopsKey, fac_index, troop, trp_index)
    flag = troop["flag"] if (troop.has_key("flag")) else default_troop["flag"]
    items = getTroopItems(troopsKey, fac, troop, default_troop)
    attr = troop["attr"] if (troop.has_key("attr")) else default_troop["attr"]
    wp = getTroopWp(troopsKey, troop)
    skill = troop["skill"] if (troop.has_key("skill")) else default_troop["skill"]
    face1 = troop["face1"] if (troop.has_key("face1")) else getRandomHeroFace()
    face2 = troop["face2"] if (troop.has_key("face2")) else getFace(period="young")
    ## 生成城堡信息
    cities = troop["cities"] if (troop.has_key("cities")) else None
    if cities != None and len(cities) != 0:
        for city in cities:
            if type(lords) is list:
                dataList["lordCities"].append('(call_script, "script_give_center_to_lord", "%s", "%s", 0),\n' % (city, "trp_" + id))
            else:
                dataList["kingCities"].append('(call_script, "script_give_center_to_lord", "%s", "%s", 0),\n' % (city, "trp_" + id))
    return "[\"{}\", \"{}\", \"{}\", {}, 0, reserved,  {}, {},   {},{},{}, {}, {}],\n".format(id, troop_name, troop_name,flag, "fac_" + fac_id, items,attr, wp, skill, face1,face2)

'''
    生成各种人物信息,如:国王,领主,妻子,女儿,士兵,其它兵种或英雄等信息
'''
def createTroops(troopsKey,maxNumKey=None):
    results = []
    for fac_index in range(0,len(factions)):
        troop_start_index = len(results)
        fac = factions[fac_index]
        fac_id = fac["fac_id"] if (fac.has_key("fac_id")) else getFacId(fac_index)
        lords = fac[troopsKey] if(fac.has_key(troopsKey)) else []
        max_num = fac[maxNumKey] if(fac.has_key(maxNumKey)) else default_faction[maxNumKey] if(default_faction.has_key(maxNumKey)) else 1
        if type(lords) is list:
            for trp_index in range(0,len(lords)):
                results.append(createTroop(lords, trp_index, troopsKey, fac, fac_index, fac_id))
        else:
            results.append(createTroop(lords, 0, troopsKey, fac, fac_index, fac_id))
        autoLen = 0
        if troopsKey == "troops":
            autos = fac["autoTroops"] if fac.has_key("autoTroops") else None
            if autos != None and len(autos)>0:
                autoLen = len(autos)
                autoConfigs = data_troop.getTroopConfigList(autos,fac)
                for trp_index in range(0, len(autoConfigs)):
                    results.append(createTroop(autoConfigs, trp_index, troopsKey, fac, fac_index, fac_id))
        for trp_index in range(len(lords)+autoLen,max_num):
            results.append(createTroop(lords, trp_index, troopsKey, fac, fac_index, fac_id))
        ##兵种升级信息troop_start_index
        if troopsKey == "troops":
            upgradeKingdom = fac["upgradeKingdom"] if fac.has_key("upgradeKingdom") else []
            for upgrade in upgradeKingdom:
                troop1 = getDataId(results[troop_start_index+upgrade[0]-1])
                troop2 = getDataId(results[troop_start_index+upgrade[1]-1])
                if len(upgrade) == 2:
                    dataList["upgrades"].append('upgrade(troops,"%s","%s")\n'%(troop1,troop2))
                elif len(upgrade) == 3:
                    troop3 = getDataId(results[troop_start_index + upgrade[2] - 1])
                    dataList["upgrades"].append('upgrade2(troops,"%s","%s","%s")\n'%(troop1, troop2,troop3))
    dataList[troopsKey] = results

def getDataId(troop):
    return re.match("\w+",re.sub(r"[\"\[\]]","",troop)).group();

'''
    生成的国王信息
'''
def getKings():
    createTroops("king")
    # 生成常量值
    kings_begin = "\"trp_"+getDataId(dataList["king"][0])+"\""
    dataList["constants"]["kings_begin"] = kings_begin
    dataList["constants"]["kingdom_heroes_begin"] = kings_begin
'''
    生成的叛军首领信息
'''
def getPretenders():
    createTroops("pretender")
    #生成常量值
    pretenders_begin = "\"trp_"+getDataId(dataList["pretender"][0])+"\""
    dataList["constants"]["pretenders_begin"] = pretenders_begin
'''
    生成的国王信息
'''
def getLords():
    createTroops("lords", "lord_max_num")
    # 生成常量值
    kings_end = "\"trp_" + getDataId(dataList["lords"][0])+"\""
    dataList["constants"]["kings_end"] = kings_end
'''
    生成的士兵信息
'''
def getTroops():
    createTroops("troops", "troop_max_num")
'''
    生成的女士信息
'''
def getladies():
    createTroops("wifes", "wife_max_num")
    createTroops("daughters", "daughter_max_num")
    # 生成常量值
    if len(dataList["wifes"]) > 0:
        kingdom_ladies_begin = "\"trp_" + getDataId(dataList["wifes"][0])+"\""
        dataList["constants"]["kingdom_ladies_begin"] = kingdom_ladies_begin

def productData():
    print "generate cultures data……"
    getCultures()
    print "generate factions data……"
    getFactions()
    print "generate kings data……"
    getKings()
    print "generate pretenders data……"
    getPretenders()
    print "generate lords data……"
    getLords()
    print "generate ladies data……"
    getladies()
    print "generate troops data……"
    getTroops()
    print "generate party template data……"
    getPartyTemplate()
'''
    预览生成的相关数据（文化，国家，国王，领主，妻女,兵种，部队模板）
'''
def viewMod():
    print "\n[module_factions.py]===================\n"
    print "cultures info……"
    if len(dataList["cultures"])>0:
        printInfo(dataList["cultures"])
    else:
        print "no cultures info……"
    print "factions info……"
    if len(dataList["factions"]) > 0:
        printInfo(dataList["factions"])
    else:
        print "no factions info……"
    print "\n[module_troops.py]===================\n"
    print "kings info……"
    if len(dataList["king"]) > 0:
        printInfo(dataList["king"])
    else:
        print "no kings info……"
    print "pretenders info……"
    if len(dataList["pretender"]) > 0:
        printInfo(dataList["pretender"])
    else:
        print "no pretenders info……"
    print "lords info……"
    if len(dataList["lords"]) > 0:
        printInfo(dataList["lords"])
    else:
        print "no lords info……"
    print "ladies info……"
    if len(dataList["wifes"]) > 0:
        printInfo(dataList["wifes"])
    else:
        print "no wifes info……"
    if len(dataList["daughters"]) > 0:
        printInfo(dataList["daughters"])
    else:
        print "no daughters info……"
    print "cities info……"
    if len(dataList["facCities"]) > 0:
        printInfo(dataList["facCities"])
    else:
        print "no faction cities info……"
    if len(dataList["lordCities"]) > 0:
        printInfo(dataList["lordCities"])
    else:
        print "no lord cities info……"
    print "troops info……"
    if len(dataList["troops"]) > 0:
        printInfo(dataList["troops"])
    else:
        print "no troops info……"
    print "troops upgrade info……"
    if len(dataList["upgrades"]) > 0:
        printInfo(dataList["upgrades"])
    else:
        print "no troops upgrade info……"
    print "\n[module_party_templates.py]===================\n"
    print "party template info……"
    if len(dataList["partyTemplate"]) > 0:
        printInfo(dataList["partyTemplate"])
    else:
        print "no party template info……"
    print "\n[module_constants.py]===================\n"
    print "constants info……"
    if len(dataList["constants"]) > 0:
        printInfo(dataList["constants"])
    else:
        print "no constants info……"

updateItems = [
    ["module_troops.py",["troops"],"#troop start","#troop end"],
    ["module_troops.py",["upgrades"],"#upgrade start","#upgrade end"],
    ["module_troops.py",["king","lords","pretender","wifes","daughters"],"#king start","#king end"],
    ["module_factions.py",["cultures"],"#culture start","#culture end"],
    ["module_factions.py",["factions"],"#faction start","#faction end"],
    ["module_scripts.py",["facCities","lordCities","kingCities"],"#city start","#city end"],
    ["module_party_templates.py","partyTemplate","#party templates start","#party templates end"],
]
def concatData(keys):
    data = []
    if(type(keys) == list):
        for key in keys:
            data.append("## %s\n"%(key))
            data += dataList[key]
    else:
        data.append("## %s\n"%(keys))
        data = dataList[keys]
    return data
def updateMod():
    for updateItem in updateItems:
        file_util.writeInRange(
            os.path.join(file_util.scriptpath, updateItem[0]),
            concatData(updateItem[1]),
            updateItem[2],
            updateItem[3])
    ##写入常量信息
    file_util.writeReplace(file_util.scriptpath + "\module_constants.py", dataList["constants"])

def run():
    #产生数据
    productData()
    #预览数据
    viewMod()
    #写入数据
    updateMod()