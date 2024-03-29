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

    def transition_player(self, s2, action):
        if action == 1 or action == 2:  # 1 for hit
            if self.isTwoCards == 0 and s2.isTwoCards == 1:
                return 0
            elif self.isTwoCards == 0 and s2.isTwoCards == 0:
                if s2.Psum <= self.Psum:
                    return 0
                else:
                    if s2.Psum - self.Psum == 10:
                        return p
                    elif s2.Psum - self.Psum < 10:
                        return (1 - p) / 9
                    elif s2.Psum - self.Psum == 11:
                        return (1 - p) / 9
                    else:
                        return 0
            elif self.isTwoCards == 1 and s2.isTwoCards == 0:
                if s2.Psum <= self.Psum:
                    return 0
                else:
                    if s2.Psum - self.Psum == 10:
                        return p
                    elif s2.Psum - self.Psum < 10:
                        return (1 - p) / 9
                    elif s2.Psum - self.Psum == 11:
                        return (1 - p) / 9
                    else:
                        return 0
            else:
                return 0
        if action == 3:  # 3 for split
            if s2.Psum <= (self.Psum / 2):
                return 0
            else:
                if s2.Psum - (self.Psum / 2) == 10:
                    return p
                elif s2.Psum - (self.Psum / 2) < 10:
                    return (1 - p) / 9
                elif s2.Psum - (self.Psum / 2) == 11:
                    return (1 - p) / 9
                else:
                    return 0

    def transition_dealer(self, s2):
        if self.Dsum >= 17:
            return 0
        if s2.Dsum <= self.Dsum:
            return 0
        else:
            if s2.Dsum - self.Dsum == 10:
                return p
            elif 1 < s2.Dsum - self.Dsum < 10:
                return (1 - p) / 9
            elif s2.Dsum - self.Dsum == 11:
                return (1 - p) / 9
            else:
                return 0
        # if self.isTwoCards == 0 and s2.isTwoCards == 1:
        #     return 0
        # elif self.isTwoCards == 0 and s2.isTwoCards == 0:
        #     if s2.Dsum <= self.Dsum:
        #         return 0
        #     else:
        #         if s2.Dsum - self.Dsum == 10:
        #             return p
        #         elif s2.Dsum - self.Dsum < 10:
        #             return (1 - p) / 9
        #         elif s2.Dsum - self.Dsum == 11:
        #             return (1 - p) / 9
        #         else:
        #             return 0
        # elif self.isTwoCards == 1 and s2.isTwoCards == 0:
        #     if s2.Dsum <= self.Dsum:
        #         return 0
        #     else:
        #         if s2.Dsum - self.Dsum == 10:
        #             return p
        #         elif s2.Dsum - self.Dsum < 10:
        #             return (1 - p) / 9
        #         elif s2.Dsum - self.Dsum == 11:
        #             return (1 - p) / 9
        #         else:
        #             return 0
        # else:
        #     return 0

    def reward(self):
        if self.Dsum < 17:
            return 0
        elif self.Dsum > 21:
            return 1

        else:
            if self.Psum > self.Dsum:
                return 1
            elif self.Psum < self.Dsum:
                return -1
            else:
                return 0


all_states = []

for i in range(5, 20):
    for j in range(10):
        all_states += [State(i, j + 2, 0, 1, 0, 0, 0)]

for i in range(2, 10):
    for j in range(10):
<<<<<<< HEAD
        all_states+=[State(i+11,j+2,1,1,0,0,0)]
=======
        all_states += [State(i + 11, j + 2, 1, 1, 0, 0, 0)]
>>>>>>> 3e0fb43c1a5c8b8d9599f9891243a9d5e5e832c0

for i in range(2, 11):
    for j in range(10):
        all_states += [State(2 * i, j + 2, 0, 1, 0, i, 0)]

for j in range(10):
    all_states += [State(12, j + 2, 2, 1, 0, 1, 0)]

for i in range(3, 22):
    for j in range(10):
        all_states += [State(i, j + 2, 0, 0, 0, 0, 0)]

for j in range(10):
    all_states += [State(21, j + 2, 1, 1, 1, 0, 0)]

for i in range(22, 31):
    for j in range(10):
        all_states += [State(i, j + 2, 0, 0, 0, 0, 0)]

# print(len(all_states))

all_states_Dval = [[] for i in range(10)]

for i in range(62):
    for j in range(10):
        all_states_Dval[j] += [all_states[i * 10 + j]]

values = []
values2 = []
for a in range(4, 22):
    player_sum = a
    action = 2
    dealer_states = []
    for i in range(4, 27):
        dealer_states += [State(player_sum, i, 0, 0, 0, 0, 1)]

    # for i in range(2,21):
    #     dealer_states+= [State(player_sum, i, 0,1, 0, 0, 1)]

    dealer_values0 = [0] * (len(dealer_states))
    dealer_values1 = [0] * (len(dealer_states))

    for i in range(100):
        for j in range(len(dealer_states)):
            s = 0
            for k in range(len(dealer_states)):
                s += dealer_states[j].transition_dealer(dealer_states[k]) * (dealer_states[k].reward() + dealer_values0[k])
                # if a == 21 and j == 0 and i == 99:
                #     print(dealer_states[j].transition_dealer(dealer_states[k]))
                #     print(dealer_states[k].Dsum)

            dealer_values1[j] = s
        for j in range(len(dealer_states)):
            dealer_values0[j] = dealer_values1[j]

    values += [dealer_values1]

    for i in range(len(values)):
        v = []
        for j in values[i]:
<<<<<<< HEAD
            v+=[2*j]
        values2+=[v]

for i in values:
    print(i)


=======
            v += [2 * j]
        values2 += [v]
>>>>>>> 3e0fb43c1a5c8b8d9599f9891243a9d5e5e832c0

# for i in values:
#     print(i)
player_values0 = [0]*(len(all_states))
player_values1 = [0]*(len(all_states))

player_actions = [1]*(len(all_states)) #1 for Hit 2 for Double 3 for Split 4 for Stand


# check this function:  player_values update ; max over s1 ans s4 only; match with pseudocode
for i in range(10):
    print(i)
    for a in range(10):
        for j in range(len(all_states_Dval[a])):
            if all_states_Dval[a][j].Psum<=21:
                s1 = 0
                s2 = 0
                s3 = 0
                s4 = 0
                if all_states_Dval[a][j].isTwoCards == 1:
                    #Hit
                    for k in range(len(all_states_Dval[a])):
                        if all_states_Dval[a][k].Psum<=21:
                            s1 += all_states_Dval[a][j].transition_player(all_states_Dval[a][k],1)*(player_values0[62*a+k])
                        else:
                            s1 -= all_states_Dval[a][j].transition_player(all_states_Dval[a][k],1)
                    # print("first s1 is ", s1)
                    #double
                    # for k in range(len(all_states_Dval[a])):
                    #     s2 += all_states_Dval[a][j].transition_player(all_states_Dval[a][k],1)*(values2[all_states_Dval[a][k].Psum-4][all_states_Dval[a][k].Dsum-2])
                    # #Split
                    # if all_states_Dval[a][j].pair!=0:
                    #     for k in range(len(all_states_Dval[a])):
                    #         for n in range(len(all_states_Dval[a])):
                    #             s3 += all_states_Dval[a][j].transition_player(all_states_Dval[a][k],3)*all_states_Dval[a][j].transition_player(all_states_Dval[a][n],3)*(player_values0[62*a+k]+player_values0[62*a+n])


                else:
                    #Hit
                    for k in range(len(all_states_Dval[a])):
                        if all_states_Dval[a][k].Psum<=21:
                            s1 += all_states_Dval[a][j].transition_player(all_states_Dval[a][k],1)*(player_values0[62*a+k])
                        else:
                            s1 -= all_states_Dval[a][j].transition_player(all_states_Dval[a][k],1)


                #Stand
                s4 = values[all_states_Dval[a][j].Psum - 4][all_states_Dval[a][j].Dsum - 2]
                l=[s1,s4]
                player_values1[62*a+j]=max(l)
                player_actions[62*a+j]=l.index(max(l))+1
                if all_states_Dval[a][j].Psum==6 and all_states_Dval[a][j].isTwoCards==1:
                    print("s4 is   ", s4,"           s1 is   ", s1,  "     and     ", a,"-",j)
                    print(l.index(max(l))+1)
                # player_values1[62 * a + j] = s1

    # print(player_values1)
    for j in range(len(all_states)):
        player_values0[j] = player_values1[j]

# print(player_actions)
# print(player_values1)


two_cards_states=[]
two_cards_values=[]
two_cards_actions=[]
for i in range(len(all_states)):
    if all_states[i].isTwoCards==1 and all_states[i].isBlackJack==0:
        two_cards_states+=[all_states[i]]
        two_cards_values+=[player_values1[i]]
        two_cards_actions+=[player_actions[i]]



actions=[]
for i in range(len(two_cards_actions)):
    if two_cards_actions[i]==1:
        actions+=["H"+str(two_cards_states[i].Psum)]
    else:
        actions+=["S"+str(two_cards_states[i].Psum)]

for i in range(0,len(actions),10):
    print(actions[i]," ",actions[i+1]," ",actions[i+1]," ",actions[i+3]," ",actions[i+4]," ",actions[i+5]," ",actions[i+6]," ",actions[i+7]," ",actions[i+8]," ",actions[i+9])