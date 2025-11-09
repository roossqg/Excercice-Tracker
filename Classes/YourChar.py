

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
            print(f"Congratulation! You gained {self.exp_roof*self.exp}")
        if self.exp>=self.exp_roof:
            self.lv+=1
            print(f"Congrats,you reached level {self.lv}")
            self.exp_roof+=self.exp_roof*0.1
            self.exp_grown+=0.05
            self.exp=0

    #def save(self):
        #return js_flie

