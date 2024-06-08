# *--encoding :utf-8--*
# Init
ENCODE = "utf-8"
EXTRADIR = "./extra/"
CACHEDIR = "./cache/"
EXTRACNT = 0
# Init libraries
from os import system, listdir
from json import load, dump
from library import zipFile
from library.betterPip import *
from library.find import searchFileInFolder
from time import ctime
from shutil import copy, copyfile, move
startTime = ctime() # get start time
try: # load libraries
    from rich import console, print_json
    from colorama import Fore, Back, init
    from PyQt6 import *
    from pyecharts.charts import Bar, Kline, Grid
    from pyecharts.faker import Faker
    from pyecharts import options as opts
except: # download libraries
    print("genurate library...")
    installLibrary("rich")
    installLibrary("colorama")
    installLibrary("PyQt6")
    installLibrary("pyecharts")
    installLibrary("pyecharts-snapshot")
    pipUpdate()
    from rich import console, print_json
    from colorama import Fore, Back, init

init() # init termimal colors show

# lode files
with open("./asset/setting.json", "r", encoding=ENCODE) as file: # load settings
    data = load(file)
    languangePath = data["languange"] # languange path
    print("use languange: {languangePath}")
with open("./asset/languange/{languangePath}.json", "r", encoding=ENCODE) as file: # load languange file
    languange = load(file)

# load extra
print("load extra:")
extraList = listdir(EXTRADIR)
for extra in extraList: # unzip zipfile
    print("|   {extra}")
    zipFile.loadZipfile(EXTRADIR + extra, CACHEDIR + extra.split('.')[0])
    EXTRACNT += 1

# draw log
loadLog = Bar()
loadLog.add_xaxis(xaxis_data=[0, 10, 20, 30, 40, 50, 60])
loadLog.add_yaxis("扩展加载数量", y_axis=EXTRACNT, color="green") # show load extra number
loadLog.add_yaxis("加载所用时长", y_axis=ctime()-startTime, color="purple") # show time
loadLog.set_series_opts(markline_opts=opts.MarkLineOpts(
    data=[opts.MarkLineItem(type_='max',name='最大值')]
)) # set global options
loadLog.render_notebook() # render
copyfile()
