# coding=utf-8
import  os
from file_util import *
from config import *

commands = [
        "@echo off",
        "python %s\process_init.py",
        "python %s\process_global_variables.py",
        "python %s\process_strings.py",
        "python %s\process_skills.py",
        "python %s\process_music.py",
        "python %s\process_animations.py",
        "python %s\process_meshes.py",
        "python %s\process_sounds.py",
        "python %s\process_skins.py",
        "python %s\process_map_icons.py",
        "python %s\process_factions.py",
        "python %s\process_items.py",
        "python %s\process_scenes.py",
        "python %s\process_troops.py",
        "python %s\process_particle_sys.py",
        "python %s\process_scene_props.py",
        "python %s\process_tableau_materials.py",
        "python %s\process_presentations.py",
        "python %s\process_party_tmps.py",
        "python %s\process_parties.py",
        "python %s\process_quests.py",
        "python %s\process_scripts.py",
        "python %s\process_mission_tmps.py",
        "python %s\process_game_menus.py",
        "python %s\process_simple_triggers.py",
        "python %s\process_dialogs.py",
        "python %s\process_global_variables_unused.py",
        "@del %s\*.pyc",
        "echo.",
        "echo ______________________________",
        "echo.",
        "echo Script processing has ended.",
        "echo Press any key to exit. . .",
        "pause>nul",
    ]
def builderBatFile(lines,filepath,commandpath):
    file = open(filepath, "w")
    for line in lines:
        if line.__contains__("%s"):
            data = line % (commandpath)
        else:
            data = line
        file.write("%s\n" % (data))
def updateBuildBat():
    builderBatFile(commands,os.path.join(scriptpath, "build_module.bat"),scriptpath)
starts = [
    "@echo off",
    "python %s\ run.py",
]
def updateStartBat():
    builderBatFile(starts,os.path.join(projectPath, "start\start.bat"),os.path.join(projectPath, "start"))

def buildMod():
    writeReplace(os.path.join(scriptpath,"module_info.py"),{"export_dir":'"%s"'%(modPath)})
    os.system(os.path.join(scriptpath,"build_module.bat"))

#cat(os.path.join(projectPath,"start/start.bat"))