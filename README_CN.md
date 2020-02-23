# FGO-Automata 中文版README

注：这版本的README仅包括安装和配置。

## 安装

需要的外部应用： *ADB*。 需要的Python Package： *PIL*, *OpenCV* 和 *numpy*

1. Clone 这个 repo: ```git clone https://github.com/Meowcolm024/FGO-Automata.git```
2. 安装 *ADB*
    - (macOS): ```brew cask install android-platform-tools```
    - Windows可以考虑使用Chocolately安装： ```choco install adb```
3. 安装必要的Python包: ```pip install -r requirements.txt```
4. 安装 *Tesseract* (`pytesseract`要用到的)
   - macOS: ```brew install tesseract```
   - Windows: 点击 [这里](https://github.com/tesseract-ocr/tesseract/wiki#windows)

## 设定

对于*Windows*用户，双击`config.bat`以配置脚本。

## ⚠️ 注意事项

1. 需要**关闭**技能确认。
2. 如果使用`config.bat`或`demon.py`来配置脚本，需要保证能**3T**过关。
3. 建议缩短敌人消失时间和使用二倍速
4. 推荐分辨率为`1920x1080`，非16:9长宽比需要设定画面偏移（`shift`）

## FGO-Automata Script

请参见Wiki中[Automata Script](https://github.com/Meowcolm024/FGO-Automata/wiki/Automata-Script)条目。

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

#### 1. 快速开始

```python
shiki.quick_start()
```

* 使用这个语句开始战斗
* **注意**：如果不使用`quick_start()`，需要分别设置下面三个命令

#### 2. 重新设定关卡（可选）

```python
shiki.select_checkpoint("assets/checkpoint2.png") # the argument is optional
```

* 参数为模板图片路径

#### 3. 使用进阶助战选择（可选）

```python
rin.advance_support()  # w/o any param
ryougi.advance_support(tms=5)  # update time only
shiki.advance_support(spt="assets/sp3.png", tms=1)
```

* `spt`是模板图片路径（可选），`tms`是助战列表刷新次数（可选）

#### 4. 开始战斗（可选）

```python
shiki.start_battle()
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

## 自动战斗

```python
# use_dynamica(target)
shiki.use_dynamica(2)
```

- 参数`target`为目标battle数
- 注：这是类似项目[FGO-One](https://github.com/Meowcolm024/FGO-One)的全自动战斗功能
- 但是要注意`tesseract`可能会经常识别错误

> 目前`Dynamica`会忽略*EX攻击*,，*宝具卡*和*技能*

## 制作模板图片

以下是模板图片的两个例子：

![checkpoint](assets/event.png)

* 关卡模板图片

![support](assets/sp2.png)

* 助战模板图片

> 关于助战的模板图片，可以考虑先用游戏中的礼装过滤，再使用从者头像作为助战的模板图片。
