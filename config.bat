@echo off
mode con cols=81 lines=25
color AF
echo 请确认已将本脚本放于FGO-Automata目录中
if exist core/Automata.py (pause) else (goto wrong)
echo ---------------------------------------------------------------------------------
set /p name=请设置文件名(无需添加默认后缀.py,按Enter确认):
echo from core.Automata import Automata > %name%.py
echo # start  >> %name%.py
echo 请设置游戏画面偏移坐标(若为1920x1080则x,y均填0):
set /p x=x=
set /p y=y=
set /p support=请设置助战图片(放于assets中,格式为xxx.png):
goto :select
:select
cls
echo ---------------------------------------------------------------------------------
echo 请选择每日副本
echo 1=狗粮 2=修炼场 3=QP本
set /p stage=请选择(输入对应数字):
if %stage%==1 (goto :ember) else if %stage%==2 (goto :training) else if %stage%==3 (goto :qp) else (goto :select)
:ember
echo 1=狗粮初级   2=狗粮中级   3=狗粮上级   4=狗粮超级
echo ---------------------------------------------------------------------------------
set /p start1=请选择等级(输入对应数字):
echo fgo = Automata("assets/Ember%start1%.png", "assets/%support%", (%x%, %y%)) >> %name%.py
goto :appleconfirm
:training
echo ---------------------------------------------------------------------------------
echo 1=修炼场初级 2=修炼场中级 3=修炼场上级 4=修炼场超级
set /p start2=请选择等级(输入对应数字):
echo fgo = Automata("assets/Training%start2%.png", "assets/%support%", (%x%, %y%)) >> %name%.py
goto :appleconfirm
:qp
echo ---------------------------------------------------------------------------------
echo 1=QP本初级   2=QP本中级  3=QP本上级  4=QP本超级
set /p start3=请选择等级(输入对应数字):
echo fgo = Automata("assets/Qp%start3%.png", "assets/%support%", (%x%, %y%)) >> %name%.py
goto :appleconfirm
:appleconfirm
set /p apple=是否使用苹果 是输入1 否输入2:
if %apple% gtr 2 (goto :applewrong) else (goto :applenext)
:applewrong
echo 请输入1或2!
pause
goto :appleconfirm
:applenext
if %apple%==1 (goto :eat) else if %apple%==2 (goto :game) else (goto :game)
:wrong
echo 错误!请将本脚本放于FGO-Automata目录中
pause
exit
:eat
set /p a1=金苹果输入1 银苹果输入2:
set /p a2=输入数量:
if %a1%==1 (goto :gold) else if %a1%==2 (goto :silver) else (goto :eat)
:gold
echo fgo.set_apples(%a2%, "assets/gold.png")>>%name%.py
goto :game
:silver
echo fgo.set_apples(%a2%, "assets/silver.png")>>%name%.py
goto :game
:game
echo fgo.quick_start() >> %name%.py
goto :battle
:battle
cls
echo ---------------------------------------------------------------------------------
echo 请按顺序输入回合数(不可未设置第二回合直接设置第一回合!)
echo 1=第一回合 2=第二回合 3=第三回合 4=结束设置[必须]
set /p ro=请输入数字:
if %ro%==1 (goto :battle1) else if %ro%==2 (goto :battle2) else if %ro%==3 (goto :battle3) else if %ro%==4 (goto :finish) else (goto :battle)
:battle1
cls
echo # battle1 >> %name%.py
goto :menu
:battle2
cls
echo # battle2 >> %name%.py
goto :menu
:battle3
cls
echo # battle3 >> %name%.py
goto :menu
:menu
cls
echo ---------------------------------------------------------------------------------
echo 1=添加从者技能[可选]
echo 2=添加御主技能[可选]
echo 3=设置出卡顺序[必须]
echo 4=完成回合设置
echo 5=其他设置
set /p num=请输入数字:
if %num%==1 (goto :skill) else if %num%==2 (goto :master) else if %num%==3 (goto :card) else if %num%==4 (goto :battle) else if %num%==5 (goto :extra) else (goto :menu)
:skill
cls
echo ---------------------------------------------------------------------------------
echo 使用前请关闭技能使用确认!
echo 输入1为没有目标从者的技能,输入2为有目标从者的技能,输入其它返回菜单:
set /p sc=请输入数字:
if %sc%==1 (goto :1) else if %sc%==2 (goto :2) else (goto :menu)
:1
set /p s1=对于没有目标从者的技能（如“直死之魔眼”）则输入数字1～9，从左往右数。:
echo fgo.select_servant_skill(%s1%) >> %name%.py
echo 添加完成
set /p sc1=是否继续添加从者技能 1为是 2为否:
echo ---------------------------------------------------------------------------------
if %sc1%==1 (goto :skill) else (goto :menu)
:2
echo 对于有目标从者的技能（如“初始的卢恩”）需要提供两个数字
echo 第一个同上，第二个为目标从者（1～3，从左到右对应的从者）
set /p n1=第一个数字:
set /p n2=第二个数字:
echo fgo.select_servant_skill(%n1%, %n2%) >> %name%.py
echo 添加完成
set /p sc1=是否继续添加从者技能 1为是 2为否:
echo ---------------------------------------------------------------------------------
if %sc1%==1 (goto :skill) else (goto :menu)
:master
cls
echo ---------------------------------------------------------------------------------
echo 输入1为没有目标从者的御主技能,输入2为有目标从者的御主技能
echo 输入3添加Order Change技能(需要礼装),输入其它返回菜单:
set /p sc=请输入数字:
if %sc%==1 (goto :3) else if %sc%==2 (goto :4) else if %sc%==3 (goto :oc) else (goto :menu)
:3
set /p s1=对于没有目标从者的御主技能,则输入数字1～3，从左往右数。:
echo fgo.select_master_skill(%s1%) >> %name%.py
echo 添加完成
set /p sc2=是否继续添加御主技能 1为是 2为否:
echo ---------------------------------------------------------------------------------
if %sc2%==1 (goto :master) else (goto :menu)
:4
echo 对于有目标从者的御主技能,需要提供两个数字
echo 第一个同上，第二个为目标从者（1～3，从左到右对应的从者）
set /p n1=第一个数字:
set /p n2=第二个数字:
echo fgo.select_master_skill(%n1%, %n2%) >> %name%.py
echo 添加完成
set /p sc3=是否继续添加御主技能 1为是 2为否:
echo ---------------------------------------------------------------------------------
if %sc3%==1 (goto :master) else (goto :menu)
:oc
set /p o1=请输入被替换的从者(1～3，前三个从左到右对应的从者):
set /p o2=请输入上场的从者(1～3，后三个从左到右对应的从者):
echo fgo.select_master_skill(3, %o1%, %o2%) >> %name%.py
echo Order Change添加完成
set /p sc4=是否继续添加御主技能 1为是 2为否:
echo ---------------------------------------------------------------------------------
if %sc4%==1 (goto :master) else (goto :menu)
:card
cls
echo ---------------------------------------------------------------------------------
echo 您需要提供一个最多3个元素的数组
echo 数字1～5为从左到右的五张普通指令卡
echo 6～8为从左到右的3张宝具卡
echo 您也可以不选满，这样剩下的卡会随机补充。
echo 格式:若只有一张卡则输入单个数字
echo 若多张卡请用半角英文符号[ , ]分隔 如 1,2,3
set /p sel=请输入:
echo fgo.select_cards([%sel%]) >> %name%.py
echo 出卡顺序完成
pause
echo ---------------------------------------------------------------------------------
goto :menu
:extra
cls
echo ---------------------------------------------------------------------------------
echo 1=场景等待
echo 2=点击屏幕
echo 3=打开/关闭御主技能面板(无确认)
echo 4=返回菜单
set /p ex=请输入数字:
if %ex%==1 (goto :wait) else if %ex%==2 (goto :tap) else if %ex%==3 (goto :panel) else (goto :menu)
:wait
echo It allows you idle the script till a certain scene
echo It receives an argument of the path of the template image.
echo Example  assets/checkpoint.png
set /p wa=Enter the path:
echo ---------------------------------------------------------------------------------
echo fgo.wait("%wa%") >> %name%.py
goto :menu
:tap
echo Allows to tap a certain point in the screen
echo The first arg is a tuple of the coordinate (x, y)
echo The 2nd and the 3rd args are random shifts in x and y,
echo if you don't want have any shifts, replace with 0
echo Example (100, 100), 0, 0 You only need enter the number
set /p tax=Enter the number x:
set /p tay=Enter the number y:
set /p ta2=Enter the number 2nd:
set /p ta3=Enter the number 3rd:
echo ---------------------------------------------------------------------------------
echo fgo.tap((%tax%, %tay%), %ta2%, %ta3%) >> %name%.py
goto :menu
:panel
echo You can use this function to turn on/off the Master skill panel.
echo ---------------------------------------------------------------------------------
echo fgo.toggle_master_skill() >> %name%.py
goto :menu
:finish
cls
echo #finish >> %name%.py
echo ---------------------------------------------------------------------------------
echo fgo.finish_battle() >> %name%.py
set /p run=是否生成复读脚本 是输入1 否输入2:
if %run%==1 (goto :bat) else (goto :complete)
:bat
echo @echo off > run.bat
echo :main >> run.bat
echo py %name%.py >> run.bat
echo goto :main >> run.bat
goto complete
:complete
echo 完成 复读脚本请运行run.bat 正常运行请py %name%.py
echo ---------------------------------------------------------------------------------
pause
exit