
import pathlib
import exc_data
import datetime
from YourChar import Characterexp
import json
import ast


#Paths:
train_preset="C:\\Users\\augusto\\Documents\\Projects Dificult 3 [+7 days]\\Languages.py\\Chaos_Calistenics\\Training\\Train_preset.txt" # --> txt file 
stats_and_History="C:\\Users\\augusto\\Documents\\Projects Dificult 3 [+7 days]\\Languages.py\\Chaos_Calistenics\\Training\\Stats.txt" # --> txt file
char_savedata="C:\\Users\\augusto\\Documents\\Projects Dificult 3 [+7 days]\\Languages.py\\Chaos_Calistenics\\Training\\Char_save.txt" # --> txt file

#Create the exercise preset on Docs
def exc_Tracker(): 
    with open(train_preset,"w") as rf: #your path here!

        global i 

        for x in range(1): 
            i=exc_data.choose(exc_data.exercises)
            for x in i:
                rf.write(f"{x} \n ")

#Create the history on docs
def register(ff):
    with open(stats_and_History,"a") as df:  #your path here

        df.write(f" \n \n Training {datetime.datetime.now()} \n")
        for x,y in enumerate(ff[::2]):
            df.write(f" {ff[x]}  ||  {ff[x+1]} \n")

#Use atibutes from save str as num (int)
def num_transform(num):
    n=float(num)

    return int(n) if n.is_integer() else n

while True: #reload and save progress on each execution
    #create prest
    y=exc_Tracker()

    #open savedata
    with open(char_savedata,"r") as char:
        Stats_js=char.read()


    loading=[Stats_js][0] #loading save from txt file
    loading2=ast.literal_eval(loading) #transform str to a real list
    loading3=[num_transform(x) for x in loading2] # transform elements at the list in float and int atributes

    savedata=Characterexp(loading3[0],loading3[1],loading3[2],loading3[3]) #load atributes saved on txt file to Object atribute
    #with this,we can save our progress with the use of this script

    print(f'''
    Level : {savedata.lv}
    Xp: {savedata.exp} | {savedata.exp_roof}
          ''')

    #Put Train on stats document
    print(i)
    acceptance=input(" \n \n \n Do you will use this train preset? (yes/no)")
    if acceptance=="yes":
        register(i) #save that train on stats txt file

        savedata.train() #gain exp and level
        savedata.save(stats_and_History) #put the actual atributes on save txt file for load later and get the progress
        