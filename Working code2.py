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


    def poker(self,hands):
        hands = hands.split()
        return max(hands,key=self.hand_rank)



    def card_rank(self):
        ranks = []
        for card in self.hand:
            r, s = card
            rank = '--23456789TJQKA'.index(r)
            ranks.append(rank)
            ranks.sort(reverse=True)

        print(ranks)

        def straight(self):
            if (max(ranks)-min(ranks)==4 and len(set(ranks))==5):
                return True

        def kind(n,ranks):
            for r in ranks:
                if ranks.count(r) == n:return r
                return None

        def two_pair(ranks):
            pair=self.kind(2,ranks)
            lowpair=self.kind(2,list(reversed(ranks)))
            if pair and lowpair !=pair:
                return (pair, lowpair)
            else:
                return None

    def flush(hand):
        suits=[]
        for card in self.hand:
            r,s=card
            suits.append(s)
        if len(set(suits)) == 1:
            return True





    def hand_rank(self):
        ranks = self.card_rank(self)

        if self.straight(ranks) and self.flush(self.hand):
            return (8, max(ranks))

        elif self.kind(4, ranks):
            return (7, self.kind(4, ranks), self.kind(1, ranks))

        elif self.kind(3, ranks) and self.kind(2, ranks):
            return (6, self.kind(3, ranks), self.kind(2, ranks))

        elif self.flush(self.hand):
            return (5, ranks)

        elif self.straight(ranks):
            return (4, max(ranks))

        elif self.kind(3, ranks):
            return (3, self.kind(3, ranks), ranks)

        elif self.two_pair(ranks):
            return (2, self.two_pair(ranks), ranks)

        elif self.kind(2, ranks):
            return (1, self.kind(2, ranks), ranks)

        else:
            return (0, ranks)





































d=Deck()
d.shuffle()

Hero=Player()

Hero.draw(d)
Hero.draw(d)
Hero.draw(d)
Hero.draw(d)
Hero.draw(d)




print('Heroes hand:')
Hero.showHand()

print('Hero rank:')
Hero.card_rank()

Hero.card_rank.straight()
