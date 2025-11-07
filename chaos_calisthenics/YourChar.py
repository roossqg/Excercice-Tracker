

#link it with Train stats

#exp and level progress
#rewards


class Characterexp():
    def __init__(self,exp,lv,exp_roof,badges,data:list,grown=0.2):
        self.exp=exp
        self.lv=lv
        self.badges=badges
        self.exp_roof=exp_roof
        self.exp_grown=grown
        self.data=data
    
    def train(self):
        if self.exp<self.exp_roof:
            self.exp+=self.exp_roof*self.exp_grown
        if self.exp>=self.exp_roof:
            self.exp_roof+=self.exp_roof*0.1
            self.exp_grown+=0.
            self.exp=0


