import numpy as np
from lxml import html
import requests

print("BOT: Please wait until I wake up")

INFO_SET = np.load("dataset/info.npy")
GREETING_SET = np.load("dataset/greeting.npy")
PRONOUN_SET = np.load("dataset/pronoun.npy")
BEVERB_SET = np.load("dataset/beverb.npy")
ARTICLE_SET = np.load("dataset/article.npy")
INTERRO_SET = np.load("dataset/interro.npy")
OTHER_SET = np.load("dataset/other.npy")

GREETING = PRONOUN = BEVERB = ARTICLE = INTERRO = OTHER = []
WEATHERREQ = [None, None]

def clearPunc(sent):
    if '!' in sent:
        sent = sent.replace("!", "")
    if ',' in sent:
        sent = sent.replace(",", "")
    if '?' in sent:
        sent = sent.replace("?", "")
    if '.' in sent:
        sent = sent.replace(".", "")

    return sent

def searchDict(word):
    page = requests.get('http://dictionary.cambridge.org/us/dictionary/english/'+word)
    tree = html.fromstring(page.content)
    wordT = tree.xpath('//span[@class="pos"]/text()')

    return wordT[0]

def weatherReq(ARR):
    page = requests.get('https://www.wunderground.com/us/'+ARR[1]+'/'+ARR[0])
    tree = html.fromstring(page.content)
    Temp = tree.xpath('//span[@class="wx-value"]/text()')[5]
    Deg = tree.xpath('//span[@class="wx-unit"]/text()')[5]
    Weather = tree.xpath('//span[@class="wx-value"]/text()')[4]

    return [Weather, Temp, Deg]


def teachBot(word):
    wtype = searchDict(word)
    if wtype == 'noun':
        NOUN_SET.append(word)
        NOUN.append(word)
    # elif wtype == ''


def parseInput(IN):
    for word in IN:
        if word in GREETING_SET:
            GREETING.append(word)
        elif word in PRONOUN_SET:
            PRONOUN.append(word)
        elif word in BEVERB_SET:
            BEVERB.append(word)
        elif word in ARTICLE_SET:
            ARTICLE.append(word)
        elif word in INTERRO_SET:
            INTERRO.append(word)
        elif word in OTHER_SET:
            continue
        # else:
            # print("What does", word, "mean?\n[greeting, pronoun, other]")
            # answer = input()
            # if 'greeting' in answer:
            #     GREETING.append(word)
            #     GREETING_SET.append(word)
            #     np.save("dataset/greeting", GREETING)
            # elif 'pronoun' in answer:
            #     PRONOUN.append(word)
            #     PRONOUN_SET.append(word)
            #     np.save("dataset/pronoun", PRONOUN)
            # elif 'other' in answer:
            #     OTHER_SET.append(word)
            #     np.save("dataset/other", OTHER)



    return



if INFO_SET[0] == None:
    print("BOT: I don't think we have met before.")
    print("BOT: What is your name?")
    INFO_SET[0] = input()
    print("BOT: Hi,", INFO_SET[0].title()+".","Nice to meet you!")

else:
    print("BOT: Are you", INFO_SET[0].title()+"?")
    ANS = input()
    if ANS in POSITIVE:
        print("BOT: Welcome back,", INFO_SET[0].title()+"!")
    elif ANS in NEGATIVE:
        print("BOT: Sorry. What is your name?")
        INFO_SET[0] = input()
        print("BOT: Hi,", INFO_SET[0].title()+".","Nice to meet you!")

while(1):
    RAWINPUT = input()
    INPUT = clearPunc(RAWINPUT)
    P_INPUT = np.array(INPUT.split(" "))
    P_INPUT = np.char.lower(P_INPUT)
    parseInput(P_INPUT)
    if any(np.in1d(P_INPUT, GREETING_SET)):
        print(np.random.choice(GREETING_SET).title()+",",INFO_SET[0].title())
    elif '?' in RAWINPUT:
        QUESTION = 1
        if 'weather' in P_INPUT:
            if 'in' in P_INPUT:
                 WEATHERREQ[0] = P_INPUT[1+P_INPUT.tolist().index('in')]
                 WEATHERREQ[1] = P_INPUT[2+P_INPUT.tolist().index('in')]
            else:
                print("BOT: In which city and states do you want to know the weather?")
                SUBINPUT = input()
                P_SUBINPUT = np.array(SUBINPUT.split(" "))
                P_SUBINPUT = np.char.lower(P_SUBINPUT)
                if P_SUBINPUT[0] == 'in':
                     WEATHERREQ[0] = P_SUBINPUT[1]
                     WEATHERREQ[1] = P_SUBINPUT[2]

            WEATHER = weatherReq(WEATHERREQ)
            print("BOT: It is", WEATHER[1]+WEATHER[2]+', and', WEATHER[0], 'in', WEATHERREQ[0].title()+', '+WEATHERREQ[1].upper())
