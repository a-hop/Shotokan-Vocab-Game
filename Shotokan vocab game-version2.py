#Shotokan vocab game
#Must type in answer exactly as it appears in the vocabDictionary

import random

answer = input("Play game? ('y' to continue) ")
print(" ")
while answer == "y":

    vocabDictionary = {      #dictionary/key pairs for definitions
        "dachi" : "stance", "zuke" : "punch", "uke" : "block", "geri" : "kick",
        "ge dan barai" : "downward block", "age-uke" : "rising block",
        "soto uke": "inward block", "uchi-uke" : "outward block", "mae-geri-keage" : "front snap kick",
        "mae-geri" : "front kick", "mawashi-geri" : "roundhouse kick", "ushiro-geri" : "back kick", "yoko kekomi geri" : "side thrust kick", "yoko-geri-keagi" : "side snap kick",
        "zenkutsu-dachi" : "front stance", "kokutsu-dachi" : "back stance", "kiba-dachi" : "horse stance", "neko-ashi-dachi" : "cat stance",
        "ken-tsui" : "hammer fist", "nukite" : "spear hand", "oi zuki" : "step forward front punch", "shuto" : "knife hand", "haito": "ridge hand strike", "choku-zuki" : "front punch",
        "gyaku-zuki" : "reverse punch", "kamae" : "sparring stance", "shin" : "mind",
        "ki" : "spirit", "waza" : "technique", "empi-uchi" : "elbow strike",
        "mikazuki-geri" : "crescent kick", "juji-uke" : "x block", "kizami-zuki" :
        "jab", "morote-uke" : "assisted block", "tate uraken uchi" : "back fist"
        }

    keyword_list = list(vocabDictionary.keys()) #turns words into a list

    random.shuffle(keyword_list) #shuffle keywords
    correct = 0
    wrong = 0
    for keyword in keyword_list:
        display = "{}"
     
        print(display.format(keyword))
        userInputAnswer = input("ANSWER: ")
        print(vocabDictionary[keyword])
        print(" ")

        if userInputAnswer == (vocabDictionary[keyword]):
            print("CORRECT")
            correct += 1
        else:
            print("WRONG")
            wrong += 1
        print('_'*25)   #line separator
        
    # final score
    displayScore = "SCORE: {} correct and {} wrong"
    print(displayScore.format(correct, wrong))
    answer = input("Play again? ('y' to continue) ")
print(" ")
print("Thanks for playing")
    

    

