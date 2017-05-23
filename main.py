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
#WEATHERREQ = [CITY, STATE]
WEATHERREQ = [None, None]
#QUEST = [INTERRO, POSSESIVE, SUBJECT, BEVERB]
QUEST = [None, None, None]
QuestFlag = 0

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



if INFO_SET[0] == "USER":
    print("BOT: I don't think we have met before.")
    print("BOT: What is your name?")
    INFO_SET[0] = input("USER: ")
    print("BOT: Hi,", INFO_SET[0].title()+".","Nice to meet you!")

else:
    print("BOT: Are you", INFO_SET[0].title()+"?")
    ANS = input()
    if ANS in POSITIVE:
        print("BOT: Welcome back,", INFO_SET[0].title()+"!")
    elif ANS in NEGATIVE:
        print("BOT: Sorry. What is your name?")
        INFO_SET[0] = input("USER: ")
        print("BOT: Hi,", INFO_SET[0].title()+".","Nice to meet you!")

while(1):
    QuestFlag = 0
    QUEST = [None, None, None, None]
    WEATHERREQ = [None, None]

    RAWINPUT = input(INFO_SET[0].title()+": ")
    INPUT = clearPunc(RAWINPUT)
    P_INPUT = np.array(INPUT.split(" "))
    P_INPUT = np.char.lower(P_INPUT)
    parseInput(P_INPUT)

    COREINPUT = np.array([])

    # greeting check
    # remove greeting
    greetBool = np.in1d(P_INPUT, GREETING_SET)
    if any(greetBool):
        print("BOT: "+np.random.choice(GREETING_SET).title()+",",INFO_SET[0].title())
        for idx in range(len(greetBool)):
            if greetBool[idx] == False:
                COREINPUT = np.append(COREINPUT, P_INPUT[idx])

    # question check
    if ('?' in RAWINPUT) or (any(np.in1d(COREINPUT, INTERRO_SET))) or (COREINPUT[0] in BEVERB_SET):
        QuestFlag = 1
        idx = 0
        # question with interro
        if COREINPUT[0] in INTERRO_SET:
            while (COREINPUT[idx] not in BEVERB_SET):
                idx += 1
            QUEST[3] = COREINPUT[idx]
            while (COREINPUT[idx] not in POSS_SET):
                idx += 1
            QUEST[3] = COREINPUT[idx]
            while (COREINPUT[idx] not in BEVERB_SET):
                idx += 1
            QUEST[3] = COREINPUT[idx]

        # question starting with be-verb
        elif COREINPUT[0] in BEVERB_SET:

        # question with only question mark
        else:




    #
    # if any(np.in1d(P_INPUT, INTERRO_SET)):
    #     INTERRO_idx = np.where(np.in1d(P_INPUT,INTERRO_SET) == True)[0][0]
    #     INTERRO = P_INPUT(INTERRO_idx)
    #     QUESTION = 1
    #     for idx in range(INTERRO_idx, len(P_INPUT)):
    #         if
    #







        # if 'weather' in P_INPUT:
        #     if 'in' in P_INPUT:
        #          WEATHERREQ[0] = P_INPUT[1+P_INPUT.tolist().index('in')]
        #          WEATHERREQ[1] = P_INPUT[2+P_INPUT.tolist().index('in')]
        #     else:
        #         print("BOT: In which city and states do you want to know the weather?")
        #         SUBINPUT = input()
        #         P_SUBINPUT = np.array(SUBINPUT.split(" "))
        #         P_SUBINPUT = np.char.lower(P_SUBINPUT)
        #         if P_SUBINPUT[0] == 'in':
        #              WEATHERREQ[0] = P_SUBINPUT[1]
        #              WEATHERREQ[1] = P_SUBINPUT[2]
        #
        #     WEATHER = weatherReq(WEATHERREQ)
        #     print("BOT: It is", WEATHER[1]+WEATHER[2]+', and', WEATHER[0], 'in', WEATHERREQ[0].title()+', '+WEATHERREQ[1].upper())
