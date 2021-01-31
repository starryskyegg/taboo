import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("taboo game").sheet1

easyend = 167
medend = 229
hardend = 262

easylist = list(range(2, easyend+1))
medlist = list(range(200, medend+1))
hardlist = list(range(250, hardend+1))

random.shuffle(easylist)
random.shuffle(medlist)
random.shuffle(hardlist)

mhlist = medlist
isrt = len(hardlist)
x = 0
while x < isrt:
    index = 2*x+1
    mhlist.insert(index, hardlist[x])
    x += 1

ttlist = easylist
isrt = len(mhlist)
x = 0
while x < isrt:
    index = 5*x+4
    ttlist.insert(index, mhlist[x])
    x += 1

print('\n\n\n\n\n\n\n\n')
x = 0
while x < len(ttlist):
    index = ttlist[x]
    row = sheet.row_values(index)
    if(index in hardlist):
        que = row[0]
        hint1 = row[2]
        hint2 = row[3]
        print('Question'+str(x+1)+' : '+que)
        print('Hints: '+hint1+' & '+hint2)
    else:
        que = row[0]
        ban1 = row[2]
        ban2 = row[3]
        print('Question'+str(x+1)+' : '+que)
        print('Bans: '+ban1+' & '+ban2)
    if(x+1 < len(ttlist)):
        if(ttlist[x+1] in hardlist):
            wait = str(input('PRESS ENTER TO UNLOCK INFERNO LEVEL'))
            if(wait == 'final'):
                break
        else:
            wait = str(input('PRESS ENTER TO CONTINUE'))
            if(wait == 'final'):
                break
    print(' \n\n\n\n\n\n\n\n')
    x += 1

print(' \n\n\n\n\n\n\n\n')
print('Now is the final battle')
wait = input()
print('It is a little bit hard')
wait = input()
print('But I trust you all can overcome this hardship')
wait = input()
print('Okay lets GO →→→\n')
team1 = ''
team2 = ''
while(team1 == ''):
    team1 = input('ENTER TEAM1')
while(team2 == ''):
    team2 = input('ENTER TEAM2')
print(' \n\n\n\n\n\n\n\n')

index1 = 0
index2 = 0

if(team1 == '1'):
    index1 = random.randrange(300, 301)
elif(team1 == '2'):
    index1 = random.randrange(302, 303)
elif(team1 == '3'):
    index1 = random.randrange(304, 305)
elif(team1 == '4'):
    index1 = random.randrange(306, 307)
elif(team1 == '5'):
    index1 = random.randrange(308, 309)
elif(team1 == '6'):
    index1 = random.randrange(310, 311)
if(team2 == '1'):
    index2 = random.randrange(300, 301)
elif(team2 == '2'):
    index2 = random.randrange(302, 303)
elif(team2 == '3'):
    index2 = random.randrange(304, 305)
elif(team2 == '4'):
    index2 = random.randrange(306, 307)
elif(team2 == '5'):
    index2 = random.randrange(308, 309)
elif(team2 == '6'):
    index2 = random.randrange(310, 311)
row = sheet.row_values(index1)
que = row[0]
hint1 = row[2]
hint2 = row[3]
print('Final Question: '+que)
print('Hints: '+hint1+' & '+hint2)
print('\n\n\n')
row = sheet.row_values(index2)
que = row[0]
hint1 = row[2]
hint2 = row[3]
print('Final Question: '+que)
print('Hints: '+hint1+' & '+hint2)

x = 0
while x == 0:
    wait = input()
    if(wait == 'yy'):
        print('\n\n\n\n\n\n\n\n')
        print('GOOD JOB TEAM'+team1+' & '+team2+'!!!\nYOU CAN LEAVE')
        x = 1
    elif(wait == 'yn'):
        print('\n\n\n\n\n\n\n\n')
        print('GOOD JOB TEAM'+team1+'!!!\nBAD JOB TEAM'+team2+'!!!\nYOU CAN LEAVE')
        x = 1
    elif(wait == 'ny'):
        print('\n\n\n\n\n\n\n\n')
        print('BAD JOB TEAM'+team1+'!!!\nGOOD JOB TEAM'+team2+'!!!\nYOU CAN LEAVE')
    elif(wait == 'nn'):
        print('\n\n\n\n\n\n\n\n')
        print('BAD JOB TEAM'+team1+' & '+team2+'!!!\nYOU CAN LEAVE')

