# FGO-Automata 中文版README

注：这版本的README仅包括安装和配置。

## Install

需要的外部应用： *ADB*。 需要的Python Package： *PIL*, *OpenCV* 和 *numpy*

1. 安装 *ADB*(macOS): ```brew cask install android-platform-tools``` （Windows可以考虑使用Chocolately安装： ```choco install adb```）
2. 安装 *PIL*, *OpenCV* 和 *numpy*: ```pip install opencv-python numpy pillow```
3. Clone 这个 repo: ```git clone https://github.com/Meowcolm024/FGO-Automata.git```

## 设定

对于*Windows*用户，双击`config.bat`以配置脚本。

## 指南

### 1. 初始化

#### a. 导入Package

```python
from core.Automata import Automata
```

#### b. 建立 Class

```python
shiki = Automata("assets/checkpoint.png", "assets/qp.png", (248, 0))
```

```python
ryougi = Automata("assets/checkpoint.png", "assets/qp.png")
```

* 第一个参数为指向**关卡**模板图片的**路径**，第二个参数为指向**助战**模板图片的**路径**。
* 第三个为可选参数， i如果您的屏幕分辨率是 *1920x1080*, 可以留空这个参数或者填上 `(0,0)`.
* 假如您的游戏界面左右或上下有间隔（非标准16:9，有蓝色条纹什么的），请添加这样一个 `(x, y)`, *x* 指的是画面横向的偏移（真正游戏画面最左端的x坐标）， *y* 指的是画面纵向偏移。

#### c. AP相关（可选）

```python
shiki.set_apples(0, "assets.silver.png")
```

* 您可以不设置此项，则默认不会使用金苹果。
* 参函数接受两个参数，第一个为苹果的数量，第二个为苹果（包括石头）模板图片的路径（也就是选择补充AP的物品）。

### 2. 开始战斗

```python
# start
shiki.select_checkpoint("assets/checkpoint2.png") # the argument is optional
shiki.select_support("assets/qp2.png") # the argument is optional
shiki.start_battle()
```

* 您也可以手动设定其他的关卡和助战
* 但一般情况使用下面的语句即可

```python
shiki.quick_start()
```

### 3. 战斗中

#### 1. 选择指令卡

```python
shiki.select_cards([7])
```

```python
ryougi.select_cards([1,2,3])
```

* 需要提供一个最多3个元素的数组，数字*1～5*为从左到右的五张普通指令卡，*6～8*为从左到右的3张宝具卡。您也可以不选满，这样剩下的卡会随机补充。

#### 2. 选择从者技能

```python
# skill w/o target
shiki.select_servant_skill(4)
```

```python
# with target Servant
ryougi.select_servant_skill(2, 3)
```

* 对于没有目标从者的技能（如“直死之魔眼”）传入一个参数。即*1～9*，从左往右数。
* 对于有目标从者的技能（如“初始的卢恩”）需要提供两个参数，第一个同上，第二个为目标从者（*1～3*，从左到右对应的从者）

#### 3. 选择御主技能

```python
# skill w/o target
shiki.select_master_skill(2)
```

```python
# with target Servant
ryougi.select_master_skill(1, 3)
```

```python
# Order Change
rin.select_master_skill(3, 1, 1)
```

* 大体上同从者技能。*1～3*为从左往右数的三个御主技能。
* 可选的第二个参数为目标从者。
* 对于换人服的换人技能，需要提供三个参数。第一个为技能代号应该是第3个。第二个为先发从者代号（1～3），第三个为支援从者代号（1～3）。

### 4. 结束战斗

```python
# finish
shiki.finish_battle()
```
