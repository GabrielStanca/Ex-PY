d1={"nume":"Gabi","numar":"0754326483"}
d2={"nume":"Babalacu","numar":"0755739816"}
d3={"nume":"Cristina","numar":"0754698213"}
d4={"nume":"Dorel","numar":"0757978531"}
d5={"nume":"Dani","numar":"0751234389"}
d6={"nume":"Narkis","numar":"0759283769"}
d7={"nume":"Giani","numar":"0757913648"}
d8={"nume":"Bobita","numar":"0759764315"}
d9={"nume":"Iulika","numar":"0752596743"}
d10={"nume":"Alexutzu","numar":"0754679851"}
l=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]
l.sort()
for i in l:
    print("Numele " +i.get("nume") +" cu numarul de telefon "+ i.get("numar"))


