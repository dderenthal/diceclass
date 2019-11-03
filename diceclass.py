import random as ra

class roll:

    def view(self):
        if self.num == 1 : print(' ______\n|      |\n|   *  |\n|______|')
        if self.num == 2 : print(' ______\n| *    |\n|      |\n|____*_|')
        if self.num == 3 : print(' ______\n| *    |\n|   *  |\n|_____*|')
        if self.num == 4 : print(' ______\n| *   *|\n|      |\n|_*___*|')
        if self.num == 5 : print(' ______\n| *   *|\n|   *  |\n|_*___*|')
        if self.num == 6 : print(' ______\n| *   *|\n| *   *|\n|_*___*|')

d1 = roll()
d2 = roll()
d3 = roll()
d4 = roll()
d5 = roll()
d6 = roll()

while input('r to roll (q to quit)') != 'q' :
    d1.num = ra.randint(1,6)
    d2.num = ra.randint(1,6)
    d3.num = ra.randint(1,6)
    d4.num = ra.randint(1,6)
    d5.num = ra.randint(1,6)
    d6.num = ra.randint(1,6)

    d1.view()
    d2.view()
    d3.view()
    d4.view()
    d5.view()
    d6.view()
