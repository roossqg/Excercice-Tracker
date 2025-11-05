
import random

# exc[3] --> 3: cardio/back, 2: Legs, 1: Arms
excercices={"straight arm plank (in seconds)":[(2,3),(20,30),1],"pike hold (in seconds)":[(3,4),(20,30),1],
            "bodyweight squat": [(3,4),(25,30),2],
            "incline push-ups":[(2,3),(5,7),1],"incline pike push-ups":[(1,2),(5,7),1],"lunges":[(2,3),(20,30),2],
            "hollow body hold":[(2,3),(15,25),2],"push-ups":[(3,4),(7,12),1],"pike push-ups":[(1,2),(5,8),1],
            "jumping squats":[(2,4),(10,15),2],"sphinx-push ups":[(1,2),(6,10),1],
            "body weight lateral raises":[(2,4),(7,13),1],
            "l sit (in seconds)":[(2,3),(5,10),2],"dips":[(3,4),(12,16),1],"crow pose (in seconds)":[(1,2),(10,15),2],
            "frog stand (in seconds)":[(1,2),(10,15),2],"pistol squats (in seconds)":[(2,3),(15,20),2],
            "elevated push ups":[(2,3),(5,10),1],
            "decline push ups":[(2,3),(6,8),1],"cardio (in seconds)":[(4,5),(20,35),3]}

def choose(ec):  #Actual config: Arms: 3 exc / Legs : 3 exc/Back,Cardio: 3 exc
        e=[]
        k=0
        p=0
        p1=0
        p2=0
        l=[x for x in excercices.keys()]
        while True:
                c=random.choice(l)
                if excercices[f"{c}"][2]== 1:
                        p+=1
                        if p>3:
                                None
                        else:
                                e.append(f"{c}: {random.randint(excercices[f"{c}"][0][0],
                                excercices[f"{c}"][0][1])}x{random.randint(excercices[f"{c}"][1][0],excercices[f"{c}"][1][1])}")
                                k+=1
                                if k==9:
                                        return e
                                

                elif excercices[f"{c}"][2]==2:
                        p1+=1
                        if p1>3:
                                None
                        else:
                                e.append(f"{c}: {random.randint(excercices[f"{c}"][0][0],
                                excercices[f"{c}"][0][1])}x{random.randint(excercices[f"{c}"][1][0],excercices[f"{c}"][1][1])}")
                                k+=1
                                if k==9:
                                        return e

                elif excercices[f"{c}"][2]==3:
                        p2+=1
                        if p2>3:
                                None
                        else:
                                e.append(f"{c}: {random.randint(excercices[f"{c}"][0][0],
                                excercices[f"{c}"][0][1])}x{random.randint(excercices[f"{c}"][1][0],excercices[f"{c}"][1][1])}")
                                k+=1
                                if k==9:
                                        return e
        