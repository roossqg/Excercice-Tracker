
import pathlib
import exc_data
import datetime
from YourChar import Characterexp
import json


#Paths:
train_preset="" # --> txt file 
stats_and_History="" # --> txt file
char_savedata="" # --> txt file

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


y=exc_Tracker()

with open(char_savedata,"r") as char:
    Stats_js=char.read()

loading=[Stats_js][0]
loading2=loading[1:-1:2]

print(loading)
savedata=Characterexp(int(loading2[0]),int(loading2[1]),int(loading2[2]),int(loading2[3]))

#Put Train on stats doc
acceptance=input(" \n \n \n Do you will train this preset? (yes/no)")
if acceptance=="yes":
    savedata.train()
    savedata.save()
    z=register(i)
    