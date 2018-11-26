Rachel_sort= [ 6, 24, 'x', 15, -6,'z', -5, 1, 4, 0, 3, 5]
evens=[]
odds =[]
characters = []
def list_sort():
    for a in  Rachel_sort:
        if type(a) == str:
            characters.append(a)
        elif type(a) == int:
            if a % 2 == 0:
                evens.append(a)
            elif  a % 2 ==1:
                odds.append(a)
    my_dict = {}    
    my_dict['evens'] = evens
    my_dict['odds'] = odds
    my_dict['characters'] = characters 
    return my_dict
function = list_sort()    
print(function)
