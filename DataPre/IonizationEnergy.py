from mendeleev.fetch import fetch_ionization_energies
a = fetch_ionization_energies()
b = open('dianlineg.csv', 'w')
c = [a.head(16)]
with open('dianlineg.csv', 'w') as f:
    for i in c:
        f.writelines(str(i)+'\n')
#a = H._ionization_energies
print(c)
