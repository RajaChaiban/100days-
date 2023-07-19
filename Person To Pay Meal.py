import random
names=[]
names.extend(["Raja","Jadyou","Mazen","Suk","Chickho","Chakoura","Selwan"])
# num_names=len(names)
# random=random.randint(0,num_names -1)
# person=names[random]
person=random.choice(names)
print(f"{person} will pay the bill")

place=[]
place.extend(["Iris","GrandFac","Caprice"])
club=random.choice(place)
print(club)