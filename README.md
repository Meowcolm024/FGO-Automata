# FGO-Automata

[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/Meowcolm024/FGO-Automata?include_prereleases)](https://github.com/Meowcolm024/FGO-Automata/releases)
[![GitHub issues](https://img.shields.io/github/issues/Meowcolm024/FGO-Automata)](https://github.com/Meowcolm024/FGO-Automata/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/Meowcolm024/FGO-Automata)](https://github.com/Meowcolm024/FGO-Automata/pulls)
[![GitHub](https://img.shields.io/github/license/meowcolm024/FGO-Automata)](https://github.com/Meowcolm024/FGO-Automata/blob/master/LICENSE)

**FGO-Automata** allows you to play _Fate/GO_ just like writting *Python* Script

**注意FGO-Automata适用于国服的Fate/Grand Order.** PS：[中文版README](README_CN.md)

If you're playing with other versions of _Fate/GO_ (like TW or US), you may need to remake the template images in `/assets`

## Table of Contents

<details>

- [FGO-Automata](#fgo-automata)
  - [Table of Contents](#table-of-contents)
  - [Install](#install)
  - [Setup](#setup)
  - [Notice](#notice)
  - [FGO-Automata Script](#fgo-automata-script)
    - [Usage](#usage)
    - [Cheatsheet](#cheatsheet)
  - [References](#references)
    - [1. Initialization](#1-initialization)
      - [1. Import package](#1-import-package)
      - [2. Setup the Class](#2-setup-the-class)
      - [3. AP related (Optional)](#3-ap-related-optional)
    - [2. Start battle](#2-start-battle)
      - [1. Quick Start (Recommended)](#1-quick-start-recommended)
      - [2. Reset Checkpoint (Optional)](#2-reset-checkpoint-optional)
      - [3. Reset Support (DEPRECATED)](#3-reset-support-deprecated)
      - [4. Use Advance Support Selection (Optional)](#4-use-advance-support-selection-optional)
      - [5. Start Battle (Optional)](#5-start-battle-optional)
    - [3. During battle](#3-during-battle)
      - [1. Select cards](#1-select-cards)
      - [2. Select Servant skills](#2-select-servant-skills)
      - [3. Select Master skills](#3-select-master-skills)
      - [4. Select Servant](#4-select-servant)
      - [5. Change Servants](#5-change-servants)
    - [4. Finish battle](#4-finish-battle)
    - [5. Other functions](#5-other-functions)
      - [1. Wait for a certain scene](#1-wait-for-a-certain-scene)
      - [2. Tap screen](#2-tap-screen)
      - [3. Toggle Master Skill](#3-toggle-master-skill)
      - [4. Update Support List](#4-update-support-list)
      - [5. Battle ID related](#5-battle-id-related)
    - [6. Dynamic Battle](#6-dynamic-battle)
    - [7. Reset Shifts](#7-reset-shifts)
  - [Making Templates](#making-templates)
  - [TO-DO](#to-do)

</details>

## Install

Required libs: *ADB*, *PIL*, *OpenCV*,  *numpy* and *pytesseract*

1. Install *ADB*
   - macOS: ```brew cask install android-platform-tools```
   - Windows: ```choco install adb```
2. Install *PIL*, *OpenCV* and *numpy*: ```pip install opencv-python numpy pillow pytesseract```
3. Install *Tesseract* (Required by `pytesseract`)
   - macOS: ```brew install tesseract```
   - Windows: Click [here](https://github.com/tesseract-ocr/tesseract/wiki#windows)
4. Clone the repo: ```git clone https://github.com/Meowcolm024/FGO-Automata.git```

## Setup

There are mainly 3 ways to set up *FGO-Automata*(as automation script):

- If you are familiar with _Python_, you can try to manually write the scipt. (See: [References](#references)) (You can also checkout the [example.py](example.py))
- If you are using _Windows_, double click `config.bat` to set up the script.（中文）
- If you are using _macOS_(or _Linux_), run `demon.py` to set up the script.
- You can also use the *FGO-Automata Script* (See: [FGO-Automata Script](#fgo-automata-script))

You can also use *FGO-Automata* as an API in your own project, just import the package :)

## Notice

When using FGO-Automata as a automation script, notice the following things:

1. Turn **OFF** skill confirmation(*Quick Cast*).
2. When using `config.bat` or `demon.py`, make sure you can pass the Checkpoint within **3 turns**.
3. Recommended: turn ON *Speed Up Death Animation* and *2x Speed*

## FGO-Automata Script

### Usage

- Start REPL: `python REPL.py` (Interactive environment)
- Run `FGO-Automata Script`: `python REPL.py [script file]`

### Cheatsheet

<details>

``` python
# comments start with '#'

sft=(248,0) # set shifts

ckp="assets/Qp4.png" # reset checkpoint
spt="assets/eg-sp1.png" # reset support

start # quick start

s7 # select servant skill 7
s5t1 # select servant skill 5 target 1

m1 # select master skill 1
m2t3 # select master skill 2 target 3
m3o1t2 # select Order Change org 1 tar 2

c2 # select card 2
c65 # select card 6, 5

finish # finish battle

show # show current setting
```

</details>

## References

### 1. Initialization

#### 1. Import package

```python
from core.Automata import Automata
```

- First import the package

#### 2. Setup the Class

```python
rin = Automata("assets/checkpoint.png", "assets/qp.png")
shiki = Automata("assets/checkpoint.png", "assets/qp.png", sft=(248, 0))
ryougi = Automata("assets/checkpoint.png", "assets/qp.png", sft=(248, 0), apl=(1, "assets/silver.png"))
```

* The first argument and the second one refers to the **path** of your **template** of checkpoint and **support servant**.
* For the *optional* param `sft`: if you screen resolution is *1920x1080*, just ignore it. But if there are blues straps at the edges, it is the shift of the top left corner. For `(x, y)`, *x* refers to the shifts in x-axis shift, *y* refers to y-axis shift.
* For the *optional* param `apl`: it is a tuple of `(int, str)`, the first item is number, representing how many apples will be consumed. The second one refers to the **path** of your **template** of the type of the apple (incl. *Quartz*). **(It has the same function as `set_apples`)**

#### 3. AP related (Optional)

```python
# .set_apples(<number of the apples>, <path to the apples>)
shiki.set_apples(0, "assets/silver.png")
```

- **NOTICE: It will override the set apples and the counter**
- If you are using it as a automation bot, you may encounter AP problem which need to use *Gold Apples*.
- Notice that the function recieves 2 arguments. The first item is number, representing how many apples will be consumed. The second one refers to the **path** of your **template** of the type of the apple (incl. *Quartz*).

### 2. Start battle

#### 1. Quick Start (Recommended)

```python
# .quick_start(advance=True)
shiki.quick_start()
```

- If you don't need to modify your checkpoints and supports you can use this. (Then you can skip the following 4 articles)
- By default, this method will use the `Advance Support Selection`(See [Advance Support Selection](#4-use-advance-support-selection-optional)). But you can also turn it OFF, which use the old way, by setting `advance=False`.

#### 2. Reset Checkpoint (Optional)

```python
shiki.select_checkpoint("assets/checkpoint2.png") # the argument is optional
```

- This method is implemented in `.quick_start()` without the argument.
- You can reset checkpoint image if needed.

#### 3. Reset Support (DEPRECATED)

```python
# start
shiki.select_support("assets/qp2.png") # the argument is optional
```

- **NOTICE: The function of this method is replaced by `Advance Support Selection`**
- This method is implemented in `.quick_start()` without the argument.
- * You can reset support image if needed.

> **About support selection**  
> It will onlt select the *support servant* in first page(the first 3 servants) if there isn't any match, it will automatically select the **first** support servant by default

#### 4. Use Advance Support Selection (Optional)

```python
rin.advance_support()  # w/o any param
ryougi.advance_support(tms=5)  # update time only
shiki.advance_support(spt="assets/sp3.png", tms=1)
```

- This is the advance support selection, it will check the first 3 support, if none matches, it will scroll down to have another check. If there is still isn't any matches, it will try to update the support list, then repeat the cycle.
- The argument `spt` is optional, you can override the original support servant.
- The argument `tms` is the times the script will update the support list, default is `3`.

#### 5. Start Battle (Optional)

```python
shiki.start_battle()
```

- If you did **NOT** use `.quick_start()`, you need to use this command to start the battle.

### 3. During battle

#### 1. Select cards

```python
# .select_cards(<list of the desired cards(in order)>)
shiki.select_cards([7])
rin.select_cards([8,6])
ryougi.select_cards([1,2,3])
```

- Notice this function receives a *list* of maximum **3** numbers. If the list is empty or has less numbers, more cards from normal cards will be selected randomly.
- For the numbers' meaning: Number **1~5** refer to the *normal cards* from **left** to **right**. Number **6,7,8** refer to *NP cards*.
- Cards will be taped in orders

#### 2. Select Servant skills

```python
# skill w/o target
# .select_servant_skill(<id of the skill>)
shiki.select_servant_skill(4)
```

- Notice this function receives a number.
- The number can be in the range of **1~9**, each refers to the skill counted from left.

```python
# with target Servant
# select_servant_skill(<id of the skill>, <id of the target servant>)
ryougi.select_servant_skill(2, 3)
```

- You can also add the second argument for the target *Servant*(See: [*Select Servants*](#4-select-servant)). The second argument receives a number. The number can be in the range of **1~3**, each refers to the *Servant* counted from left.

#### 3. Select Master skills

```python
# skill w/o target
# .select_master_skill(<id of the skill>)
shiki.select_master_skill(2)
```

- Notice this function receives a number.
- The number can be in the range of **1~3**, each refers to the skill counted from left.

```python
# with target Servant
# .select_master_skill(<id of the skill>, <id of the target servant>)
ryougi.select_master_skill(1, 3)
```

- You can also add the second argument for target *Servant*(See: [*Select Servants*](#4-select-servant)). The second argument receives a number. The number can be in the range of **1~3**, each refers to the *Servant* counted from left.

```python
# Order Change
# .select_master_skill(<id of the skill>, <id of the first servant>, <id of the second servant>)
rin.select_master_skill(3, 1, 1)
```

- If the skill is *Order Change*, you can add the third argument(See: [*Change Servants*](#5-change-servants)). In the second and third argument, each should be a number in the range of **1~3**. The second arg refers to the first 3 Servants and the third one refers to the last 3.

#### 4. Select Servant

```python
# .select_servant(<id of the skill>)
shiki.select_servant(1)
```

- **NOTICE: This function has been integrated to `select_servant_skill` and `select_master_skill`, so you don't need to use it explicitly. (Besides, the reference below is still vaild.)**
- There are some skills in *FGO* have target servant, if the skill you have chosen is this kind of skill, you may need to use this function to choose the desired *Servant*.
- Notice this function receives a number.
- The number can be in the range of **1~3**, each refers to the *Servant* counted from left.

#### 5. Change Servants

```python
# .change_servant(<id of the first servant>, <id of the second servant>)
shiki.change_servant(1, 1)
```

- **NOTICE: This function has been integrated to `select_master_skill`, so you don't need to use it explicitly. (Besides, the reference below is still vaild.)**
- This function receives 2 numbers, each should be in the range of **1~3**.
- The first arg refers to the first 3 Servants and the second one refers to the last 3.

### 4. Finish battle

```python
# finish
shiki.finish_battle()
```

- This function allows the program tap through the ending of battle.

### 5. Other functions

#### 1. Wait for a certain scene

```python
shiki.wait("assets/checkpoint.png")
```

- It allows you idle the script till a certain scene
- It receives an argument of the *path* of the template image.

#### 2. Tap screen

```python
shiki.tap((100, 100), 0, 0)
```

- Allows to tap a certain point in the screen
- The first arg is a tuple of the coordinate `(x, y)`
- The 2nd and the 3rd args are random shifts in x and y, if you don't want have any shifts, replace with `0`

#### 3. Toggle Master Skill

```python
shiki.toggle_master_skill()
```

- You can use this function to turn on/off the _Master_ skill panel.

#### 4. Update Support List

```python
# .update_support() -> bool
x = shiki.update_support()
```

- It returns `True` if the *support list* is successfully updated, otherwise is `False`.

#### 5. Battle ID related

```python
# .get_current_battle -> int
x = shiki.get_current_battle()
```

- Returns the number of current battle id (like `1`, `2` or `3`)

```python
# .reached_battle(target) -> bool
x = shiki.reached_battle(2)
```

- Receives a number of the target battle (like `2` in battle `2/3`)
- Returns `True` if reached else `False`

### 6. Dynamic Battle

```python
# use_dynamica(target)
shiki.use_dynamica(2)
```

- The param `target` is the target battle id.
- It allows the script to run fully automatically (See: [FGO-One](https://github.com/Meowcolm024/FGO-One) for the basic idea and how it works)
- Do notice that `tesseract` **fails frequently**

> The `Dynamica` will ignore *Brave Chain*, *NP Cards* and *Skills*

### 7. Reset Shifts

``` python
shiki.reset_shifts((0, 0))
```

- You can reset shift using this function

## Making Templates

Here are two examples of the template:

<details>

![checkpoint](assets/eg-ckp.png)
![another checkpoint](assets/Training4.png)

- These are templates of _checkpoints_

![support](assets/eg-sp2.png)
![another support](assets/eg-sp3.png)

- These are templates of _supports_

</details>

> The template image of the support can either be an image of a *Craft Essence* or a *Servant*(You don't need to precisely cut the image like above.).  
> You can use the *filter feature* in the game to filter the crafts and use an image of a desired *Servant* for selection.

**Notice that your template should be distinctive.**

## TO-DO

- [x] Advance support selection
- [x] Battle recognition
- [x] Dynamic battle analysis (See: [FGO-One](https://github.com/Meowcolm024/FGO-One) for the idea)
- [ ] Dynamica: Brave Chain and NP card support
- [ ] Mulitple support servants
- [ ] FGO-Automata Script
