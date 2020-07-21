#\033[93m (yellow) \033[91 (red) \033[0m (white)
import time
print('\033[96m'+"A glowing circle looms before you. \nBrighter than a million suns, yet it does not blind you. \nIt's strange and foreign, and it pulls you closer.")
time.sleep(4)
choice0 = input('\033[0m'+"A) Let it pull you in \nB) Resist \n")
if choice0 == "B":
  print("End.")
  Hi = False
if choice0 == "A":
  Hi = True
while Hi == True:
  print("welcome to...")
  time.sleep(2)
  print('\033[91m'+"ALTER ORBIS")
  time.sleep(2)
  print('\033[0m'+"a game of choices and riddles.")
  time.sleep(3)
  print('\033[93m'+"'Hello, New Adventurer! I sense you are new here in Alter Orbis... maybe you have just fallen through a portal or something of the sort?")
  time.sleep(5)
  print("I wonder, why have you come to this land?'") 
  choice1 = input('\033[0m'+"A) 'I... do not actually know' \nB) 'I come to seek an adventure, of course!' \nC) 'I think I was sucked in by a portal!' \n")
  if choice1 == "A":
    print('\033[93m'+"'What a strange answer, indeed! \nWell, if you do not know why you are here, perhaps you would like for me to give you something to do; some tasks?'")
  elif choice1 == "B":
    print('\033[93m'+"'As, yes! That is what most in these parts seek!")
    time.sleep(2)
    print("Maybe I can assist? I have a number of tasks I need to be completed, for the last few people who said yes still have not returned, I'm afraid!'")
  elif choice1 == "C":
    print('\033[93m'+"'Just as I suspected!")
    time.sleep(2)
    print("Well... although I do not personally know how to get you home, maybe you will find the answer whilst completing some tasks for me?'")
  time.sleep(4)
  choice2 = input('\033[0m'+"A) 'Tasks? What do you mean?' \nB) 'Yes, please!' \n")
  if choice2 == "A":
    print('\033[93m'+"'Hohoho, you are a funny little one. What do the tasks entail, you ask? Well, I guess you'll just have to see...")
    time.sleep(4)
    print("That is, of course, if you choose to do these tasks?'")
    choice2A = input('\033[0m'+"A) 'Yes, I'd like to do the tasks' \nB) 'I don't think I want to do the tasks...' \n")
    if choice2A == "A":
      print('\033[93m'+"'Wonderful!'")
      time.sleep(2)
    if choice2A == "B":
      print('\033[93m'+"'Excuse me?")
      print('\033[96m'+"The man frowns at you.")
      print('\033[93m'+"And why, may I ask, do you wish to not complete these tasks for me? There is a reward, you know.'")
      choice2B = input('\033[0m'+"A) You know what, I'd actually like to do the tasks \nB) Fine, I'll do your silly tasks... but what is the reward? \n")
      if choice2B == "A":
        print('\033[93m'+"'Wonderful!'")
        time.sleep(3)
      if choice2B == "B":
        print('\033[93m'+"'What did you just say? You dare call these tasks 'silly'?!'")
        print('\033[96m'+"He raises his voice,")
        print('\033[93m'+"'These 'silly' tasks have gotten folk such as yourself killed! If you make the wrong choice, you die!")
        time.sleep(3)
        print("And the reward?")
        time.sleep(1)
        print("Do you question my word?")
        time.sleep(1)
        print("If I say there is a reward, there is a reward, and believe me when I say it is well worth your while.'")
        choice2C = input('\033[0m'+"A) Okay, okay... I'll do the tasks, without question! \nB) I'm sorry for saying that. I'm in. \n")
        if choice2C == "A":
          print('\033[96'+"'The man sneers at you,"+'\033[93m'+"'Very good.'")
          time.sleep(3)
        if choice2C == "B":
          print('\033[93m'+"'Very good.'")
          time.sleep(2)
  elif choice2 == "B":
    print('\\033[93'+"'What an eager one you are! I hope that does not get you into trouble... Well, anyways,'")
    time.sleep(3)
  print("'Here are your tasks...'")
  print('\033[96m'+"The man hands you a small, leather notebook.")
