@echo off
mode con cols=81 lines=25
color AF
echo ��ȷ���ѽ����ű�����FGO-AutomataĿ¼��
if exist core/Automata.py (pause) else (goto wrong)
echo ---------------------------------------------------------------------------------
set /p name=�������ļ���(�������Ĭ�Ϻ�׺.py,��Enterȷ��):
echo from core.Automata import Automata > %name%.py
echo ��������Ϸ����ƫ������(��Ϊ1920x1080��x,y����0):
set /p x=x=
set /p y=y=
echo ---------------------------------------------------------------------------------
echo 1=��һ�������� 2=��һ�����м� 3=��һ�����ϼ� 4=��һ��������
echo 5=�ܶ��������� 6=�ܶ������м� 7=�ܶ������ϼ� 8=�ܶ���������
echo 9=������������ 10=���������м� 11=���������ϼ� 12=������������
echo 13=���Ĺ������� 14=���Ĺ����м� 15=���Ĺ����ϼ� 16=���Ĺ�������
echo 17=���幷������ 18=���幷���м� 19=���幷���ϼ� 20=���幷������
echo 21=������������ 22=���������м� 23=���������ϼ� 24=������������
echo 25=���չ������� 26=���չ����м� 27=���չ����ϼ� 28=���չ�������
echo 29-32 �� 33-36 ǹ 37-40 �� 41-44 �� 45-48 �� 49-52 ɱ 53-56 ��
echo QP�� 57=���� 58=�м� 59=�ϼ� 60=����
echo ---------------------------------------------------------------------------------
set /p start=��ѡ��ؿ�(�����Ӧ����)ͼƬ����ӣ���ǰ��������:
set /p support=��������սͼƬ(����assets��,��ʽΪxxx.png):
echo # start  >> %name%.py
echo fgo = Automata("assets/%start%.png", "assets/%support%", (%x%, %y%)) >> %name%.py
set /p apple=�Ƿ�ʹ��ƻ�� ������1 ������2:
if %apple%==1 (goto :eat) else if %apple%==2 (goto :game) else (goto :game)
:wrong
echo ����!�뽫���ű�����FGO-AutomataĿ¼��
pause
exit
:eat
set /p a1=��ƻ������g ��ƻ������s:
set /p a2=��������:
echo fgo.set_apples(%a2%, "assets/%a1%.png") >> %name%.py
goto :game
:game
echo fgo.quick_start() >> %name%.py
goto :battle
:battle
cls
echo ---------------------------------------------------------------------------------
echo �밴˳������غ���(����δ���õڶ��غ�ֱ�����õ�һ�غ�!)
echo 1=��һ�غ� 2=�ڶ��غ� 3=�����غ� 4=��������
set /p ro=����������:
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
echo 1=��Ӵ��߼���[��ѡ]
echo 2=�����������[��ѡ]
echo 3=���ó���˳��[����]
echo 4=��ɻغ�����
echo 5=��������
set /p num=����������:
if %num%==1 (goto :skill) else if %num%==2 (goto :master) else if %num%==3 (goto :card) else if %num%==4 (goto :battle) else if %num%==5 (goto :extra) else (goto :menu)
:skill
cls
echo ---------------------------------------------------------------------------------
set /p sc=����1Ϊû��Ŀ����ߵļ���,����2Ϊ��Ŀ����ߵļ���,�����������ز˵�:
if %sc%==1 (goto :1) else if %sc%==2 (goto :2) else (goto :menu)
:1
set /p s1=����û��Ŀ����ߵļ��ܣ��硰ֱ��֮ħ�ۡ�������������1��9��������������:
echo fgo.select_servant_skill(%s1%) >> %name%.py
set /p sc1=�Ƿ������Ӵ��߼��� 1Ϊ�� 2Ϊ��:
echo ---------------------------------------------------------------------------------
if %sc1%==1 (goto :skill) else (goto :menu)
:2
echo ������Ŀ����ߵļ��ܣ��硰��ʼ��¬��������Ҫ�ṩ��������
echo ��һ��ͬ�ϣ��ڶ���ΪĿ����ߣ�1��3�������Ҷ�Ӧ�Ĵ��ߣ�
set /p n1=��һ������:
set /p n2=�ڶ�������:
echo fgo.select_servant_skill(%n1%, %n2%) >> %name%.py
set /p sc1=�Ƿ������Ӵ��߼��� 1Ϊ�� 2Ϊ��:
echo ---------------------------------------------------------------------------------
if %sc1%==1 (goto :skill) else (goto :menu)
:master
cls
echo ---------------------------------------------------------------------------------
set /p sc=����1Ϊû��Ŀ����ߵ���������,����2Ϊ��Ŀ����ߵ���������,�����������ز˵�:
if %sc%==1 (goto :3) else if %sc%==2 (goto :4) else (goto :menu)
:3
set /p s1=����û��Ŀ����ߵ���������,����������1��3��������������:
echo fgo.select_master_skill(%s1%) >> %name%.py
set /p sc2=�Ƿ��������������� 1Ϊ�� 2Ϊ��:
echo ---------------------------------------------------------------------------------
if %sc2%==1 (goto :master) else (goto :menu)
:4
echo ������Ŀ����ߵ���������,��Ҫ�ṩ��������
echo ��һ��ͬ�ϣ��ڶ���ΪĿ����ߣ�1��3�������Ҷ�Ӧ�Ĵ��ߣ�
set /p n1=��һ������:
set /p n2=�ڶ�������:
echo fgo.select_master_skill(%n1%, %n2%) >> %name%.py
set /p sc3=�Ƿ��������������� 1Ϊ�� 2Ϊ��:
echo ---------------------------------------------------------------------------------
if %sc3%==1 (goto :master) else (goto :menu)
:card
cls
echo ---------------------------------------------------------------------------------
echo ����Ҫ�ṩһ�����3��Ԫ�ص�����
echo ����1��5Ϊ�����ҵ�������ָͨ�
echo 6��8Ϊ�����ҵ�3�ű��߿�
echo ��Ҳ���Բ�ѡ��������ʣ�µĿ���������䡣
echo ��ʽ:��ֻ��һ�ſ������뵥������
echo �����ſ����ð��Ӣ�ķ���[ , ]�ָ� �� 1,2,3
set /p sel=������:
echo fgo.select_cards([%sel%]) >> %name%.py
echo ����˳�����
echo ---------------------------------------------------------------------------------
goto :menu
:extra
cls
echo ---------------------------------------------------------------------------------
echo 1=�����ȴ�
echo 2=�����Ļ
echo 3=��/�ر������������(��ȷ��)
echo 4=���ز˵�
set /p ex=����������:
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
set /p run=�Ƿ����ɸ����ű� ������1 ������2:
if %run%==1 (goto :bat) else (goto :complete)
:bat
echo @echo off > run.bat
echo :main >> run.bat
echo py %name%.py >> run.bat
echo goto :main >> run.bat
goto complete
:complete
echo ���~ �����ű�������run.bat ����������py %name%.py
echo ---------------------------------------------------------------------------------
pause
exit