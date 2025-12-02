


class Characterexp():
    def __init__(self,exp,lv,exp_roof,badges,grown=0.2):
        self.exp=exp
        self.lv=lv
        self.badges=badges
        self.exp_roof=exp_roof
        self.exp_grown=grown
    
    
    def train(self):
    
        if self.exp<self.exp_roof:
            self.exp+=self.exp_roof*self.exp_grown
            print(f"Congratulation! You gained {self.exp_roof*self.exp}")
        if self.exp>=self.exp_roof:
            self.lv+=1
            print(f"Congrats,you reached level {self.lv}")
            self.exp_roof+=self.exp_roof*0.1
            self.exp_grown+=0.05
            self.exp=0

    def save(self):
        from Exercises_org import char_savedata
        char_savedata1=char_savedata
        origin=char_savedata1
        with open(origin,"w") as destiny:
            list="[" + ",".join(str(x) for x in [self.exp,self.lv,self.exp_roof,self.badges]) + "]"
            destiny.write(list)
            print("Save successful!")


