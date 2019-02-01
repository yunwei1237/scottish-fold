# coding=utf-8

import sys
import os
projectPath = os.getcwd()+"\.."
makePath = os.path.join(projectPath,"make")
startPath = os.path.join(projectPath,"start")
scriptPath = os.path.join(projectPath,"script\ModuleSystem")

sys.path.append(projectPath)
sys.path.append(makePath)
sys.path.append(startPath)
sys.path.append(scriptPath)

from parse_config import *
from bat import *

# 让你的修改进行生效
run()
# 更新build.bat文件
updateBuildBat()
# 更新start.bat文件
#updateStartBat()
# 构造剧本
buildMod()
