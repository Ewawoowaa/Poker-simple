import random

class Deck:
    def __init__(self):
        self.cards=[]
        self.build()

    def build(self):
        for s in ['S','C','D','H']:
            for v in range(2,10):
                self.cards.append('{}{}'.format(v,s))
        for h in ['S','C','D','H']:
            for q in ['T','J','Q','K','A']:
                self.cards.append('{}{}'.format(q,h))
    def show(self):
        for c in self.cards:
            c.show()
    def print(self):
        for c in self.cards:
            print(c)


    def shuffle(self):
        random.shuffle(self.cards)

    def drawCard(self):
        return self.cards.pop()


class Player:
    def __init__(self):
        self.hand=[]

    def draw(self,deck):
        self.hand.append(deck.drawCard())


    def showHand(self):
        for card in self.hand:
            print(card)


    #def poker(self,hands):
        #hands = hands.split()
        #return max(hands,key=self.hand_rank)



    def card_rank(self):
        a=self.hand[0]
        b=self.hand[1]
        c=self.hand[2]
        d=self.hand[3]
        e=self.hand[4]
        for r,s in a:
            rank1 = '--23456789TJQKA'.index(r)
        for t,u in b:
            rank2 = '--23456789TJQKA'.index(t)
        for v,w in c:
            rank3 = '--23456789TJQKA'.index(v)
        for x,y in d:
            rank4 = '--23456789TJQKA'.index(x)
        for z,q in e:
            rank5 = '--23456789TJQKA'.index(z)

        ranks=[rank1,rank2,rank3,rank4]
        ranks.sort(reverse=True)

        print(ranks)


d=Deck()
d.shuffle()

Hero=Player()
Hero.draw(d)
Hero.draw(d)
Hero.draw(d)
Hero.draw(d)
Hero.draw(d)


#d.print()


print('Heroes hand:')
Hero.showHand()

Hero.card_rank()