import random
import time

texts = {"111111": ["乾", "Qian", "The Creative"],
         "000000": ["坤", "Kun", "The Receptive", "Resting in Firmness"],
         "010001": ["屯", "Zhun", "Initial Difficulty"],
         "100010": ["蒙", "Meng", "Youthful Folly, Obscurity"],
         "010111": ["需", "Xu", "Waiting, Nourishment"],
         "111010": ["訟", "Song", "Conflict"],
         "000010": ["師", "Shi", "The Army, Group Action"],
         "010000": ["比", "Bi", "Holding Together, Union"],
         "110111": ["小畜", "Xiaoxu", "The Taming Force, Small Restraint"],
         "111011": ["履", "Lü", "Treading Carefully"],
         "000111": ["泰", "Tai", "Peace"],
         "111000": ["否", "Pi", "Stagnation"],
         "111101": ["同人", "Tongren", "Union of Men"],
         "101111": ["大有", "Dayou", "Great Possession, Abundance"],
         "000100": ["謙", "Qian", "Modesty"],
         "001000": ["豫", "Yu", "Harmony, Joy, Enthusiasm"],
         "011001": ["隨", "Sui", "Following"],
         "100110": ["蠱", "Gu", "Arresting Decay"],
         "000011": ["臨", "Lin", "Approach, Advance"],
         "110000": ["觀", "Guan", "Contemplation"],
         "101001": ["噬嗑", "Shihe", "Biting Through"],
         "100101": ["賁", "Bi", "Adornment"],
         "100000": ["剝", "Bo", "Falling Apart"],
         "000001": ["複", "Fu", "Returning"],
         "111001": ["無妄", "Wuwang", "Correctness, Innocence"],
         "100111": ["大畜", "Daxu", "The Great Taming Force"],
         "100001": ["頤", "Yi", "Correctness, Innocence"],
         "011110": ["大過", "Daguo", "Excess"],
         "010010": ["坎", "Kan", "The Perilous Pit"],
         "101101": ["離", "Li", "The Clinging; Brightness"],
         "011100": ["咸", "Xian", "Influence"],
         "001110": ["恆", "Heng", "Preseverance, Duration"],
         "111100": ["遯", "Dun", "Retreat"],
         "001111": ["大壯", "Dazhuang", "The Power of the Great"],
         "101000": ["晉", "Jin", "Progress"],
         "000101": ["明夷", "Mingyi", "Darkening of the Light"],
         "110101": ["家人", "Jiaren", "The Family"],
         "101011": ["睽", "Kui", "Disunion, Mutual Alienation"],
         "010100": ["蹇", "Jian", "Arresting Movement"],
         "001010": ["解", "Jie", "Removing Obstacles"],
         "100011": ["損", "Sun", "Decrease"],
         "110001": ["益", "Yi", "Increase"],
         "011111": ["夬", "Guai", "Removing Obstruction, Breaking Through"],
         "111110": ["姤", "Gou", "Encountring"],
         "011000": ["萃", "Cui", "Gathering Together"],
         "000010": ["升", "Sheng", "Ascending"],
         "011010": ["困", "Kun", "Oppression"],
         "010110": ["井", "Jing", "A Well"],
         "011101": ["革", "Ge", "Revolution"],
         "101110": ["鼎", "Ding", "The Cauldron"],
         "001001": ["震", "Zhen", "Thunder, Exciting Power"],
         "100100": ["艮", "Gen", "Mountain, Arresting Movement"],
         "110100": ["漸", "Jian", "Gradual Progress, Growth"],
         "001011": ["歸妹", "Guimei", "The Marrying Maiden; Propriety"],
         "001101": ["豐", "Feng", "Abundance, Prosperity"],
         "101100": ["旅", "Lü", "Travelling Stranger"],
         "110110": ["巽", "Xun", "Gentle Penetration"],
         "011011": ["兌", "Dui", "Joy, Pleasure"],
         "110010": ["渙", "Huan", "Dispersion"],
         "010011": ["節", "Jie", "Regulation, Restraining"],
         "110011": ["中孚", "Zhongfu", "Inmost Sincerity"],
         "001100": ["小過", "Xiaoguo", "Small Excesses"],
         "010101": ["既濟", "Jiji", "Completion"],
         "101010": ["未濟", "Weiji", "Before Completion"]}


full = ["⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛"*2, "0"]
broken = ["⬛⬛⬛⬛⬛⬛⬛⬛⬛        "*2, "1"]

cache = ""

print("\n")
for i in range(6):
    choice = random.choice([full, broken])
    for i in choice[0]:
        print(i, end="", flush=True)
        if i != " ":
            time.sleep(0.025)
    print('\n')
    cache += choice[1]

for i in texts[cache]:
    for n in i:
        print(n, end="", flush=True)
        if n != " ":
            time.sleep(0.05)
    print("")
