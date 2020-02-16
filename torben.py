class Kunde:
    def __init__ (self,name,alter,postleizahl):
        self.name= name
        self.alter= alter
        self.postleizahl = postleizahl
    
    def ausgabe(self):
        print(self.name)
        print(self.alter)
        print(self.postleizahl)
    
class Ticketarten:
    def __init__(self,name,anzahl,klasse):
        self.name= name
        self.anzahl = anzahl
        self.klasse = klasse
    
    def ausgabe (self):
        print(self.name)
        print(self.anzahl)
        print(self.klasse)

class Tickets:
    def __init__(self,ticketart,kundenid):
        self.ticketart
        self.kundenid
    
        