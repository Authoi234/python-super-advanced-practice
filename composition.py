class Nonte:
    def __init__(self):
        self.math = 100

    def math_marks(self):
        return self.math
    
class Monte:
    def __init__(self):
        self.english = 86

    def english_marks(self):
        return self.english
    
class Fonte:
    def __init__(self):
        self.science = 90

    def science_marks(self):
        return self.science

class Jhontu:
    def __init__(self):
        self.n = Nonte()
        self.f = Fonte()
        self.m = Monte()
    
    def math_marks(self):
        return self.n.math_marks()
    
    def english_marks(self):
        return self.m.english_marks()
    
    def science_marks(self):
        return self.f.science_marks()
    
j = Jhontu()
print("Nonte er Math marks:", j.math_marks())
print("Monte er English marks:", j.english_marks())
print("Fonte er Science marks:", j.science_marks())