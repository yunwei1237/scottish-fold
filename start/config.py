# coding=utf-8

from base_data import *

#剧本路径（指定要修改的剧本位置）
modPath = "D:/game/Mount&Blade/Modules/Native/"
# # 国家相关的数据信息
# # 主要的配置信息,默认规则请参看：base_data（在本文件最后）
factions=[
    {
        #"fac_id":"kingdom_6",#国家id（1-5，已经被系统国家所使用，要么不要指定，要么指定一个5以上id）
        "fac_name":"Kingdom of china",#国家名称
        "color":"0xFF0000",#国家的颜色
        "king":{
			"id":"kingdom_6_lord", #国王的id(要么不指定，要么指定5以上的编号)
			"troop_name":"King mao",#国王的名字
            "flag":"tf_hero",
			#国家的装备信息
             "items":"[itm_charger,itm_rich_outfit,itm_blue_hose,itm_iron_greaves,itm_plate_armor,itm_gauntlets,itm_bastard_sword_b,itm_tab_shield_heater_cav_b,itm_great_helmet,]",
			#国王的属性
             "attr":"knight_attrib_5",
			#国王的武器熟练度
             "wp":"wp(220)",
			#国家的技能（骑术，强弓等）
             "skill":"knight_skills_5|knows_trainer_5",
			#国王的容貌(这个是哈劳斯国王容貌，你也可以改成其它的)
             "face1":"0x0000000f45041105241acd2b5a66a86900000000001e98310000000000000000",
             #将【艾车莫尔】这个城堡给国王，这个属性也可以应用到国家，国王，领主
             "cities":["p_town_17"]
        },
        "lords":[{},{}],#国家的领主（使用哈劳斯国王全部手下信息）
        "troops":swadian_troops,#指定国家的士兵信息（使用哈劳斯国王的兵种，当然，你也可以学习下一章的内容，然后添加属于自己的兵种）
        #将【乌鲁兹达克堡】这个城堡给新增的国家，最后分给哪个领主，是随机的
        "cities":["p_castle_22"]
    },
]