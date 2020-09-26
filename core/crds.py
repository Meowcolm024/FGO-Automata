# This file stores the coordinates of the buttons and the path to images


def map_dict(f, a):
    return dict(zip(a, map(f, a.values())))


# shifts: 10, 10
SERVANT_SKILLS = [
    # Servatn 1
    (100, 850),
    (250, 850),
    (380, 850),
    # Servant 2
    (580, 850),
    (730, 850),
    (860, 850),
    # Servant 3
    (1060, 850),
    (1200, 850),
    (1340, 850)
]

# shifts: 40, 40
MASTER = (1780, 470)

# shifts: 10, 10
MASTER_SKILLS = [
    (1360, 470),
    (1490, 470),
    (1630, 470)
]

# shifts: 100, 100
ATTACK = (1700, 900)

# shifts: 50, 100
CARDS = [
    # Normal
    (190, 760),
    (560, 760),
    (960, 760),
    (1340, 760),
    (1740, 760),
    # NP
    (620, 320),
    (970, 320),
    (1310, 320)
]

# shifts: 90, 90
SERVANTS = [
    (200, 530),
    (520, 530),
    (820, 530),
    (1110, 530),
    (1400, 530),
    (1710, 530)
]

# shifts: 150, 150
TARGETS = [
    (500, 680),
    (960, 680),
    (1440, 680)
]

# path to images
# change the path if you're play FGO other than the CN version
IMAGE_BASE = "assets/cn/"

IMAGE = map_dict(lambda x: IMAGE_BASE + x, {
    "attack": "attack.png",
    "select": "select.png",
    "order_change": "order_change.png",
    "no_ap": "noap.png",
    "update_support": "update.png",
    "confirm_update": "uplist.png",
    "finish": "finish.png",
    "item": "item.png",
    "close": "close.png",
    "decide": "decide.png",
    "start": "start.png"
})

CARD_IMAGE_BASE = "assets/cn/extra/"

CARD_IMAGE = map_dict(lambda x: CARD_IMAGE_BASE + x, {
    "resist": "resist.png",
    "weak": "weak.png",
    "quick": "quick.png",
    "arts": "arts.png",
    "buster": "buster.png"
})
