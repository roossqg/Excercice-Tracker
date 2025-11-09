
import pathlib
import exc_data
import datetime


#Create the excercice preset on Docs
def exc_Tracker(): 
    with open("","w") as rf: #your path here!

        global i 

        for x in range(1): 
            i=exc_data.choose(exc_data.excercices)
            for x in i:
                rf.write(f"{x} \n ")

#Create the history on docs
def register(ff):
    with open("","a") as df:  #your path here

        df.write(f" \n \n Training {datetime.datetime.now()} \n")
        for x,y in enumerate(ff[::2]):
            df.write(f" {ff[x]}  ||  {ff[x+1]} \n")


y=exc_Tracker()

#Put Train on stats doc
acceptance=input(" \n \n \n Do you will train this preset? (yes/no)")
if acceptance=="yes":
    z=register(i)
    