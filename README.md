# scottish-fold
一个关于骑马与砍杀的剧本简单快速的制作工具

## 前言

​	在很久以前的时候，也就是刚开始玩骑砍的时候就想着能够制作一个自己的剧本，用于书写自己想要的故事。当我怀着远大的梦想去这么做的时候才发现，原来制作剧本没有自己想象的那么简单。摆面前的最大的问题就是我要学习python这样的语言，其次还有骑砍自己的语言（ModuleSystem）。那对于没有编程经验的小白来说，简直太复杂了，想要制作一个功能是那么的困难。就算想要为这个游戏中增加一个自己的城堡，都要学习大量的代码，也要修改大量的代码，经过无数次测试，才能在庞大的地图上显示一个小小的城堡（我以前成功添加自己城堡的时候，简直高兴得不行）。制作一个城堡都这么复制，那么如果我想要增加一个国家呢？那又是一个非常复杂的代码。在我们理想的地图上添加一个人，一个城堡，一个国家，甚至是一个复杂的功能（种地，开店，经营村庄，管理城堡，巡逻队，阵型系统，银行系统，招降劫匪，称号系统，官职系统，想要成为国王，国家与国家之间的外交等等），都需要学习骑砍大量的代码和看无数的教程才能够做出一点点成果。当我们攒足了勇气和时间轻轻打开入门教程和各个大神的功能代码时，你才发现，原来代码是那么地长和难于理解，不是有了勇气和时间就能够解决的。那么，制作剧本能不能不要这么复杂，能不能只要稍微修改一点点的东西，就能够生成我想要系统呢？

​	然后我就找啊找，发现，中间使用了各种工具（ txt修改器、魔球等），他们是非常优秀的制作工具，让我节省了不少的时间（我以前修改了一个剧本，看我帖子就知道了），可是，当我想要制作另一个剧本时，你就会发现这些功能可能需要再重新**复制粘贴**一次，甚至有一些功能还不能使用，而复制粘贴也没有那么简单，需要注意的地方还是有很多。一不小心，就会导致功能不能使用。本以为除了这些功能就没有其它问题了，其实不是这样子的，还有很多的问题，模型导入，特效的制作等等，都比较复杂。那么，我又在想，能不能简单一点地去制作剧本呢？我只是一个想要制作剧本的人，为什么不能把精力只放到剧本制作上面？为什么只有成为编程的大神才能制作我想要的剧本呢？

​	我从2009年开始玩骑砍到2019年，时间好长，一直都想要制作剧本，每一次鼓起勇气，都被代码的复杂和繁琐所打败，当然我也不能为自己的懒惰而辩护（哈哈，其实就是懒）。

​	就在上一个月，学校的效益不好（有一些认识我的人，知道我在学校工作），我就选择了辞职。在这将近半个月的时间，我就把骑砍剧本制作又拿出来了。这次，我就想着，一定要制作一个工具，让制作剧本更简单，然后制作一个自己理想的剧本【战国群雄】（我一直都想要制作的剧本，也有一些骑友只知道）。为了让剧本制作的人员更简单快速制作剧本，我就制作了这一个工具。到底有多简单，就那看这个工具的制作手册吧。当然，我会简单介绍一个这个工具，让大家了解它是多么地简单。

​	当然，我现在没有了工作，那就没有了收入来源，所以我要尽快努力找到工作。本来我想将这个工具制作完成，然后将战国群雄剧本制作完成，然后再让大家使用这个工具（不是我自私，而是工具没有制作好，会有很多的BUG，大家在用的时间遇到很多问题，肯定会给大家带来不便，有一些不友好的可能还会骂我）。但现在不得不拿出来，是因为我要在过年时间为找下一份工作作准备。

​	最后希望大家能够喜欢这个工具，也希望大家能够使用该工具完成自己的剧本（工具还没有完善，所以肯定会遇到很多问题，而过年我又没有时间为大家解答，所以很抱歉，希望大家能够理解）。

​	我将使用这个工具的人分成了两种

 - **剧本制作者**：只制作剧本，不需要写任何功能
- **工具制作者**：完善这个工具，需要写很多的代码

## 工具介绍

​	这个工具是一个没有界面的工具，制作者只需要修改配置文件（config.py），系统就会自动帮助制作者快速生成大量的代码。所以对于剧本制作者来说，只要了解这一个文件就行了，其它文件是工具制作者的任务。

​	工具中有三个文件夹

​	1.make：工具代码全部都在这个文件夹中

​	2.script：剧本代码全部都在这个文件夹中（暂时只支持1.011版本，也就是原版，战团还不支持，如果你是工具制作者，那这个工具对你来说就没有任何限制了）

​	3.start：剧本的配置文件和运行都在这个文件夹中，配置文件（config.py），运行文件（run.py），你每一次修改文件都要运行才能让你的修改生效（有时间运行可能需要运行两次，制作过剧本的人应该都了解）。



## 1.剧本制作者

​	在这里，我们讨论的内容是配置文件（config.py），对于剧本制作者，你只需要了解这一个文件就行

​	我给剧本制作者暂时提供的功能有（还有很多的功能在我脑子里，没有实现）

- 1.添加国家：快速生成一个国家

- 2添加领主：快速生成一个领主

- 3.添加士兵：快速生成一个兵种

  

### 剧本路径

在config.py文件中开头就有这个配置，用于指定剧本在哪个文件夹中，使用以下功能时一定要记得修改这个配置。

```python
###   modPath = "剧本的路径"
modPath = "D:/game/Mount&Blade/Modules/Native/"
```

### 1.添加国家

如果你想要在地图上添加一个新的国家，那么你只需要写的内容如下：

```python
factions=[
    {}
]

#这对花括号【{}】就是你的国家，运行一下工具你就会发现，一个新的国家已经生成，并为这个国家，生成一个国王和20个领主14个兵种，国家id是fac_kingdom_1,国家的名字也是这个，生成的内容包含，国王，文化，领主，兵种，和队伍模板，只是里面的数据会按照一些简单的规则生成（如：国名和人名等），有一些信息会随机生成（装备，武器熟练度，颜色，容貌等）

##运行一个你的游戏看下，是否已经生成了 ^_^,开心不！
```

如果你想要生成5个国家，非常简单

```python
factions=[{},{},{},{},{},]
```

如果你对自动生成的信息不满意，那你还可以这样写（属性如何不提供，就会自动生成）

```python
#以斯瓦迪亚国家为例
factions=[
    {
        "fac_id":"kingdom_1",#国家id
        "fac_name":"Kingdom of Swadia",#国家名称
        "color":"0xDD8844",#国家的颜色
        "king":swadian_kings[0],#国家的国王
        "lords":swadian_lords,#国家的领主
        "lord_items":swadian_lords[random.randint(0,len(swadian_lords)-1)]["items"],#其它领主的装备
        "lord_max_num":20,#国家共有领主数量（不包括女人和士兵）
        "troops":swadian_troops,#指定国家的士兵信息
    },
]
```

### 2.添加领主

#### 1.添加国王

添加国王需要使用到国家配置中的king属性

```python
"king":{}
# 这样就可以了，会为新的国家生成一个国王信息，只是所有的属性都是自动生成的。
```

那我们也可以指定如下信息：

```python
"king":{
    "id":"kingdom_1_lord", #国王的id
    "troop_name":"King Harlaus",#国王的名字
    "flag":"tf_hero",#国王的兵种标识
    #国家的装备信息
    "items":"[itm_charger,itm_rich_outfit,itm_blue_hose,itm_iron_greaves,itm_plate_armor,itm_gauntlets,itm_bastard_sword_b,itm_tab_shield_heater_cav_b,itm_great_helmet,]",
    #国王的属性
    "attr":"knight_attrib_5",
    #国王的武器熟练度
    "wp":"wp(220)",
    #国家的技能（骑术，强弓等） 
    "skill":"knight_skills_5|knows_trainer_5",
    #国王的容貌
    "face1":"0x0000000f45041105241acd2b5a66a86900000000001e98310000000000000000",
    #对于英雄来说，没有用，当然可以不用配置的
    "face2":"swadian_face_older_2",
},
```

如果你想运行成功，一定要把king这个配置放到指定的国家中才可以，记得我们之前的国家配置吗？

完整代码如下：

```python
#以斯瓦迪亚国家为例
factions=[
    {
        "fac_id":"kingdom_1",#国家id
        "fac_name":"Kingdom of Swadia",#国家名称
        "color":"0xDD8844",#国家的颜色
        #以哈劳斯国王为例
        "king":{
			"id":"kingdom_1_lord", #国王的id
			"troop_name":"King Harlaus",#国王的名字
			"flag":"tf_hero",#国王的兵种标识
			#国家的装备信息
             "items":"[itm_charger,itm_rich_outfit,itm_blue_hose,itm_iron_greaves,itm_plate_armor,itm_gauntlets,itm_bastard_sword_b,itm_tab_shield_heater_cav_b,itm_great_helmet,]",
			#国王的属性
             "attr":"knight_attrib_5",
			#国王的武器熟练度
             "wp":"wp(220)",
			#国家的技能（骑术，强弓等） 
             "skill":"knight_skills_5|knows_trainer_5",
			#国王的容貌
             "face1":"0x0000000f45041105241acd2b5a66a86900000000001e98310000000000000000",
			#对于英雄来说，没有用，当然可以不用配置的
             "face2":"swadian_face_older_2",
        },
        "lords":swadian_lords,#国家的领主
        "lord_items":swadian_lords[random.randint(0,len(swadian_lords)-1)]["items"],#其它领主的装备
        "lord_max_num":20,#国家共有领主数量（不包括女人和士兵）
        "troops":swadian_troops,#指定国家的士兵信息
    },
]
```

#### 2.添加领主

添加领主需要使用到国家配置中的lords属性，这个属性是可以配置多个领主，和配置王国有一点不同，不过他们的属性都是完全一样的。

添加两个领主信息

```python
"lords":[{},{}]
```

为领主增加详细的信息

```python
"lords":[
    #克拉格斯
    {
		"id":"knight_1_1",#领主id
		"troop_name":"Lord Klargus",#领主名字
		"flag":"tf_hero",#领主标识
		#领主装备
         "items":"[itm_saddle_horse,itm_courtly_outfit,itm_heraldic_mail_with_surcoat,itm_nomad_boots,itm_splinted_greaves,itm_great_helmet,itm_sword_medieval_c,itm_scale_gauntlets,itm_tab_shield_heater_cav_a,]",
		#领主属性
        "attr":"knight_attrib_1",
		#领主的熟练度
         "wp":"wp(130)",
		#技能
         "skill":"knight_skills_1|knows_trainer_1|knows_trainer_3",
		#容貌 
         "face1":"0x0000000c3e08601414ab4dc6e39296b200000000001e231b0000000000000000",
		#对于英雄没有用
         "face2":"swadian_face_middle_2",
	},
    #普拉伊斯
	{
		"id":"knight_1_2",
		"troop_name":"Lord Plais",
		"flag":"tf_hero",
		"items":"[itm_steppe_horse,itm_gambeson,itm_heraldic_mail_with_surcoat,itm_blue_hose,itm_mail_boots,itm_nasal_helmet,itm_scale_gauntlets,itm_fighting_pick,itm_tab_shield_heater_c,]",
		"attr":"knight_attrib_2",
		"wp":"wp(160)",
		"skill":"knight_skills_2",
		"face1":"0x0000000c0f08000458739a9a1476199800000000001fb6f10000000000000000",
		"face2":"swadian_face_old_2",
	},
]
```

完整代码：

```python
#以斯瓦迪亚国家为例
factions=[
    {
        "fac_id":"kingdom_1",#国家id
        "fac_name":"Kingdom of Swadia",#国家名称
        "color":"0xDD8844",#国家的颜色
        "king":swadian_kings[0],#国家的国王
        "lords":[
            #克拉格斯
            {
                "id":"knight_1_1",#领主id
                "troop_name":"Lord Klargus",#领主名字
                "flag":"tf_hero",#领主标识
                #领主装备
                 "items":"[itm_saddle_horse,itm_courtly_outfit,itm_heraldic_mail_with_surcoat,itm_nomad_boots,itm_splinted_greaves,itm_great_helmet,itm_sword_medieval_c,itm_scale_gauntlets,itm_tab_shield_heater_cav_a,]",
                #领主属性
                "attr":"knight_attrib_1",
                #领主的熟练度
                 "wp":"wp(130)",
                #技能
                 "skill":"knight_skills_1|knows_trainer_1|knows_trainer_3",
                #容貌 
                 "face1":"0x0000000c3e08601414ab4dc6e39296b200000000001e231b0000000000000000",
                #对于英雄没有用
                 "face2":"swadian_face_middle_2",
            },
            #普拉伊斯
            {
                "id":"knight_1_2",
                "troop_name":"Lord Plais",
                "flag":"tf_hero",
                "items":"[itm_steppe_horse,itm_gambeson,itm_heraldic_mail_with_surcoat,itm_blue_hose,itm_mail_boots,itm_nasal_helmet,itm_scale_gauntlets,itm_fighting_pick,itm_tab_shield_heater_c,]",
                "attr":"knight_attrib_2",
                "wp":"wp(160)",
                "skill":"knight_skills_2",
                "face1":"0x0000000c0f08000458739a9a1476199800000000001fb6f10000000000000000",
                "face2":"swadian_face_old_2",
            },
        ]
        "lord_items":swadian_lords[random.randint(0,len(swadian_lords)-1)]["items"],#其它领主的装备
        "lord_max_num":20,#国家共有领主数量（不包括女人和士兵）
        "troops":swadian_troops,#指定国家的士兵信息
    },
]
```

我给出的都完全的配置信息，只要你希望任何一个属性自动生成，都可以省略不写，连属性名称都不用写了。就像我们开始时，只要给一个花括号就可以了。

如果你想随机生成3个领主代码如下：

```python
"lords":[{},{},{}]
```

那如何我想生成300个领主呢？代码如下(使用lord_max_num属性可以快速生成300个领主)：

```python
"lord_max_num":300,#国家共有领主数量（不包括女人和士兵）
```

### 3.添加兵种

添加兵种和领主都大致差不多

生成两个兵种

```python
#指定国家的士兵信息
"troops":[
    {},{}
],
```

详细信息配置

```python
"troops":[
    #芮尔典新兵 
    {
		"id":"swadian_recruit",
		"troop_name":"Swadian Recruit",
		"flag":"tf_guarantee_armor",
		"items":"[itm_scythe,itm_hatchet,itm_pickaxe,itm_club,itm_stones,itm_tab_shield_heater_a,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_nomad_boots,itm_wrapping_boots,]",
		"attr":"def_attrib|level(4)",
		"wp":"wp(60)",
		"skill":"knows_common",
		"face1":"swadian_face_younger_1",
		"face2":"swadian_face_middle_2",
	},
    #芮尔典民兵
	{
		"id":"swadian_militia",
		"troop_name":"Swadian Militia",
		"flag":"tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield",
		"items":"[itm_bolts,itm_spiked_club,itm_fighting_pick,itm_boar_spear,itm_hunting_crossbow,itm_tab_shield_heater_a,itm_padded_cloth,itm_leather_armor,itm_leather_cap,itm_arming_cap,itm_padded_coif,itm_ankle_boots,itm_wrapping_boots,]",
		"attr":"def_attrib|level(9)",
		"wp":"wp(75)",
		"skill":"knows_common",
		"face1":"swadian_face_young_1",
		"face2":"swadian_face_old_2",
	},
]
```

如果你希望自动生成兵种，并且要控制兵种的特点：

```python
## 兵种类型有infantry（步兵）、crossbowman（弩兵）、knight（骑士）、spearman（枪兵）、archer（弓兵）、horse_archer（骑射兵）
## infantry1：生成一个1级的步兵
## crossbowman2：生成一个2级的弩兵
## spearman4:生成一个4级的枪兵
## 等级越高装备越好，技能越高，伤害越高（最高大概7级，每一个兵种等级不同，超过最高级全按最高级生成）
"autoTroops":["infantry1","crossbowman2"，"spearman4"],
```

### 4.添加城堡(未完成)

设想：我的想法就是指定城堡的名称、角度、位置，等就自动生成一个城堡，包含城堡地形，管理者，武器商人，镇长（村长）等等一系列信息。

**【伪配置】**

```python
cities=[
    {
        "id":"town_1",#城堡id
        "city_name":"Sargoth",#城堡名称
        "icon":"icon_town|pf_town",#城堡图标
        "fac":"fac_neutral",#城堡阵营
        "behavior":"ai_bhvr_hold",#城堡ai行为
        "location":"(-1.55, 66.45)",#城堡的地点
        "coordinate":"170"#城堡的角度
    }
]
```

### 5.添加功能(未完成)

设想：我的想法就是直接在配置文件中开启该功能就可以了，不用写任何的代码。

**【伪代码】**

```python
functions={
    #巡逻队功能
    "patrols":{
        "enable":True,#开启巡逻队功能
        "village_num":2,#村子巡逻队数量
        "castle":4,#城堡巡逻队数量
        "town":8#城堡巡逻队数量
    }，
    #劝降劫匪功能
    "persuade":{
        "enable":True
    }
}
```

### 运行剧本

运行run.py文件就可以了.

## 2.工具制作者

我知道，这个工具还有很多的功能要做，还有很多的代码要写，靠我一个人，肯定是速度很慢，特别是添加功能这个想法，功能有很多，也需要写很多的代码，需要python的大神和ms的大神共同来完成这样的功能，如果你喜欢这个工具，并想为这个工具添加自己的功能和设想，或者你想查看这个工具的实现代码。



