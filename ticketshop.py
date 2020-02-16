import torben

choose = {}
def add_kunde():  
    p1=torben.Kunde(input('Name: '),input('Alter: '),input('Postleizahl: '))
    p1.ausgabe()
choose['add']= add_kunde

def list_kunden():
    print('list')
choose['list']= list_kunden

def end():
    exit(0)
choose['end']= end

while True:

    selection = input('Action? {0} \n'.format(', '.join(choose)))
    action = choose.get(selection,None)
    if action is None:
        print('Du Idiot')
        continue
    action()

