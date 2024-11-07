class collagefest:
    collage_name = "vignan"
    def _init_(self,name,rollno,game):
        self.name = name
        self.rollno = rollno
        self.game = game
        print(self.name)
        print(self.rollno)
        print(self.game)

    def m1(self,name,game):
        self.name = name
        self.game = game
        print(self.name)
        print(self.game)

    @classmethod
    def m2(cls):
        cls.branch = "mechanical"
        print(cls.branch)

    @staticmethod
    def m3():
        secure = "winners"
        print(secure)

c = collagefest("siva",11,"kabaddi")
print(c.collage_name)
c.m1("kamal","kabaddi")
c.m2()
c.m3()                    