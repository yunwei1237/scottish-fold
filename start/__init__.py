# coding=utf-8
import os

#print os.environ["PYTHONPATH"]
## 项目文件位置
projectPath = os.getcwd()+"\.."
makePath = os.path.join(projectPath,"make")
startPath = os.path.join(projectPath,"start")
## 脚本文件位置
scriptpath = os.getcwd()+"\..\script\ModuleSystem"
paths = [
    makePath,startPath,scriptpath
]
##将当前项目路径添加到环境变量中
os.environ["PYTHONPATH"] = ";".join(paths)