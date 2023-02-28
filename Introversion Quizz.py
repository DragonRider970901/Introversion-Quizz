import random
import datetime

class Player:
    def __init__(self,input_username, input_password,input_age,input_bd):
        self.username = input_username
        self.password = input_password
        self.age = input_age
        self.birthdate = input_bd
        self.introversion = 0
        self.history = {}
        self.profilenr = 1

    def get_introversion(self,score):
        self.introversion = score
    
    def update(self,date,score):
        self.history[self.profilenr] = [date, score]
        self.profilenr+=1

    def __repr__(self):
        description = 'User: {username}\nAge: {age}\nIntroversion: '.format(username=self.username, age=self.age) + str(self.introversion) + '\nExtroversion: ' + str(100-self.introversion)
        return description

def ask(quiz,asked):
    flag = 0 
    for ask in asked:
        if quiz == ask:
            flag = 1
            break
    return flag
def quizz():

    introversion_score = 2
    questions = {1: [' Your friend group is composed of:\n', ' a. 4 people, tops (a)\n b. 5-9 people (b)\n c. over 10 people (c)\n'],
                 2: [' Your opinions usually:\n', ' a. are, in general, diffrent from the common opinions (a)\n b. change, depending on your mood (b)\n c. are the same as other people\'s (c)\n'],
                 3: [' You are ______ told that you think too much: ', ' a. often (a)\n b. sometimes (b)\n c. never (c)\n'],
                 4: [' You would like to live: ', ' a. in a house in the middle of a forest (a)\n b. anywhere I can have comfort (b)\n c. in the middle of a large city (c)\n'],
                 5: [' How would you rather work? ', ' a. from home(a)\n b. I do not have a preffernce (b)\n c. at an office or anyother place (c)\n'],
                 6: [' You usually annoyed by people who: ',' a. do not think much and tend to follow trends from the exterior (a)\n b. what annoys me depends on my current mood (b)\n c. can\'t see anything but their own interests (c)\n'],
                 7: [' You work more efficiently: ', ' a. alone (a)\n b. depends on my mood (b)\n c. in a team (c)\n'],
                 8: [' Your way of thinking is: ', ' a. stable, since you rely on your own logic (a)\n b. varies, depending on my mood (b)\n c. flexible, since I can adapt easily to the logic of the circumstances (c)\n'],
                 9: [' I make phone calls / I talk on the phone: ', ' a. only when I have to / with someone I have to (a)\n b. whenever I am in the mood (b)\n c. very often and with pleasure, even with strangers (c)\n'],
                 10: [' How much does your taste uasually match with the people around you (classmates, family, aquaintances)? ', ' a. not at all (a)\n b. maybe a bit, when it comes to cars and food (b)\n c. quite a lot (c)\n']}
    
    

    asked = [0]
    
    for i in range(1,8):
        asked_flag = 0
        quiz = random.randint(1,10)
        #print(quiz)
        asked_flag = ask(quiz, asked)

        

        if asked_flag == 1:
            while asked_flag == 1:
                quiz = random.randint(1,10)
                asked_flag = ask(quiz,asked)

        if asked_flag == 0:
            print(str(i) + questions[quiz][0])
            print(questions[quiz][1])
            asked.append(quiz)

            

            choice = input("Choice: ")
        
        if choice not in ['a','b','c']:
            while choice not in ['a','b','c']:
                choice = input("Choice not valid. Please try again...  ")


        if choice == 'a' or choice == 'A':
            introversion_score += 14
        elif choice == 'b' or choice == 'B':
            introversion_score += 9
        elif choice == 'c' or choice == 'C':
            introversion_score += 0
    print("\n\nSCORE: ",introversion_score,"\n\n")
    return introversion_score









username = input("Input username: ")
password = input("Input password: ")
age = input("Input age: ")       
birthdate = input("Input birthdate: (yyyy-mm-dd)  ")

player = Player(username, password, age, birthdate)
answer = 'y'

while answer!= 'n':
    player_introversion = quizz()
    player.get_introversion(player_introversion)

    now = datetime.datetime.now()
    date = now.strftime('%y-%m-%d   %H : %M : %S')

    player.update(date,player_introversion)
    answer = input('Would you like to retake the quiz?\n yes (y) / no (n)  ')

    if answer not in ['y','n']:
        while answer not in ['y','n']:
            answer = input("Choice not valid. Please try again... ")

print("\n\n")
print(player)
print("\n")
see_h = input('Would you like to see your history?\n yes (y) / no (n)  ')
print("\n")

if see_h not in ['y','n']:
    while see_h not in ['y','n']:
        see_h = input("Choice not valid...Please try again... ")


if see_h == 'y':
    print("----HISTORY----")
    print("\n")
    for key in player.history.keys():
        print(key, " ")
        print(player.history[key][0],"  ")
        print(player.history[key][1],"  ")
        print("\n\n")


#print(player.history)

