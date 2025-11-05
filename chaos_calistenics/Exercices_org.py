
import pathlib
import chaos_calistenics.exc_data as exc_data
import datetime


rg=pathlib.Path("c:\\Users\\User\\Documents\\Training\\Model One.txt")#Exc Preset (Your Path here)
ry=pathlib.Path("c:\\Users\\User\\Documents\\Training\\Statistics.txt")#Exc preset history  (Your Path here)


#Create the excercice preset on Docs
def exc_Tracker(rg): 
    with open(rg,"w") as rf: 
        global i
        for x in range(1): 
            i=exc_data.choose(exc_data.excercices)
            for x in i:
                rf.write(f"{x} \n ")



#Create the history on docs
def register(ry,ff):
    with open(ry,"a") as df: 
        df.write(f" \n \n Training {datetime.datetime.now()} \n")
        for x,y in enumerate(ff[::2]):
            df.write(f" {ff[x]}  ||  {ff[x+1]} \n")

y=exc_Tracker(rg)

#Put Train on stats doc
acceptance=input(" \n \n \n Do you confirm this training preset? (yes/no)")
if acceptance=="yes":
    z=register(ry,i)
    