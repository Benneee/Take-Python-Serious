class Chocolate():
    
    def __init__(self, cacao_content):
        self.cacao_content = cacao_content


    @classmethod
    def sweet(cls):
        return cls(cacao_content=30)

    @classmethod
    def semisweet(cls):
        return cls(cacao_content=50)

    @classmethod
    def bittersweet(cls):
        return cls(cacao_content=70)

    @classmethod
    def bitter(cls):
        return cls(cacao_content=99)



agbo_guy = Chocolate.bitter()
print(agbo_guy.cacao_content);

sweet_tooth = Chocolate.sweet()
print(sweet_tooth.cacao_content);