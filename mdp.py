import sys
global p
p = float(sys.argv[1])
class State:

    def __init__(self, Psum, Dsum, Naces, isTwoCards, isBlackJack, pair, turn):
        self.Psum = Psum
        self.Dsum = Dsum
        self.Naces = Naces
        self.isTwoCards = isTwoCards
        self.isBlackJack = isBlackJack
        self.pair = pair
        self.turn = turn

    def transition_player(self,s2, action):
        if action==1 or action==2:   #1 for hit
            if self.isTwoCards == 0 and s2.isTwoCards== 1:
                return 0
            elif self.isTwoCards==0 and s2.isTwoCards== 0:
                if s2.Psum<=self.Psum:
                    return 0
                else:
                    if s2.Psum-self.Psum==10:
                        return p
                    elif s2.Psum-self.Psum<10:
                        return (1-p)/9
                    elif s2.Psum-self.Psum==11:
                        return (1-p)/9
                    else:
                        return 0
            elif self.isTwoCards==1 and s2.isTwoCards==0:
                if s2.Psum<=self.Psum:
                    return 0
                else:
                    if s2.Psum-self.Psum==10:
                        return p
                    elif s2.Psum-self.Psum<10:
                        return (1-p)/9
                    elif s2.Psum-self.Psum==11:
                        return (1-p)/9
                    else:
                        return 0
            else:
                return 0
        if action==3: #3 for split
            if s2.Psum<=(self.Psum/2):
                return 0
            else:
                if s2.Psum-(self.Psum/2)==10:
                    return p
                elif s2.Psum-(self.Psum/2)<10:
                    return (1-p)/9
                elif s2.Psum-(self.Psum/2)==11:
                    return (1-p)/9
                else:
                    return 0

    def transition_dealer(self,s2):
        if s2.Dsum<=self.Dsum:
            return 0
        else:
            if s2.Dsum-self.Dsum==10:
                return p
            elif s2.Dsum-self.Dsum<10:
                return (1-p)/9
            elif s2.Dsum-self.Dsum==11:
                return (1-p)/9
            else:
                return 0

    def reward(self):
        if self.Dsum<17:
            return 0
        elif self.Dsum >21 :
            return 1

        else:
            if self.Psum>self.Dsum:
                return 1
            elif self.Psum<self.Dsum:
                return -1
            else:
                return 0

    def next_state_player(self):
        states=[]





all_states=[]

for i in range(5,20):
    for j in range(10):
        all_states+=[State(i,j+2,0,1,0,0,0)]

for i in range(2,10):
    for j in range(10):
        all_states+=[State(i+1,j+2,1,1,0,0,0)]

for i in range(2,11):
    for j in range(10):
        all_states += [State(2*i, j+2, 0,1, 0, i, 0)]

for j in range(10):
    all_states += [State(2, j + 2, 2, 1, 0, 1, 0)]

for i in range(3,22):
    for j in range(10):
        all_states+=[State(i,j+2,0,0,0,0,0)]

for j in range(10):
    all_states += [State(21, j+2, 1,1, 1, 0, 0)]

for i in range(22,31):
    for j in range(10):
        all_states+=[State(i,j+2,0,0,0,0,0)]

print(len(all_states))

all_states_Dval=[[] for i in range(10)]

for i in range(62):
    for j in range(10):
        all_states_Dval[j]+=[all_states[i*10+j]]


values=[]
values2 = []
for a in range(4,22):
    player_sum=a
    action=2
    dealer_states=[]
    for i in range(2,27):
        dealer_states+= [State(player_sum, i, 0,0, 0, 0, 1)]


    dealer_values0 = [0]*(len(dealer_states))
    dealer_values1 = [0]*(len(dealer_states))

    for i in range(1000):
        for j in range(len(dealer_states)):
            s=0
            for k in range(len(dealer_states)):
                s+=dealer_states[j].transition_dealer(dealer_states[k])*(dealer_states[k].reward()+dealer_values0[k])

            dealer_values1[j]=s
        for j in range(len(dealer_states)):
            dealer_values0[j]=dealer_values1[j]

    values+=[dealer_values1]

    for i in range(len(values)):
        v=[]
        for j in values[i]:
            v+=[2*j]
        values2+=[v]



player_values0 = [0]*(len(all_states))
player_values1 = [0]*(len(all_states))

player_actions = [1]*(len(all_states)) #1 for Hit 2 for Double 3 for Split 4 for Stand


