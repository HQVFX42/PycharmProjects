
class Card:
    def __init__(self, pattern, number):
        self.pattern = pattern     #스트링
        self.number = number        #스트링
    def __str__(self):
        return self.pattern + " " + self.number

class Deck:
    patternList = ["스페이드", "다이아몬드", "하트", "클로버"]
    numberList = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self):
        self.Cards = []
        for p in self.patternList:      #4개모양
            for n in self.numberList:   #13개 숫자
                self.Cards.append(Card(p,n))    #52장 카드객체
    def __str__(self):
        strList = [str(c) for c in self.Cards]
        return str(strList)

deck = Deck()
print(deck)
