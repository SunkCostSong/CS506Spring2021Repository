# Coding
import matplotlib.pyplot as plt
import pandas as pd
eleven = pd.DataFrame(pd.read_excel("2011_CityCouncil_Results_Race_Turnout.xlsx"))
thirteen = pd.DataFrame(pd.read_excel("2013_CityCouncil_Race_Turnout_Results.xlsx"))
fifteen = pd.DataFrame(pd.read_excel("2015_city_council.xlsx"))
seventeen =  pd.DataFrame(pd.read_excel("2017_CityCouncil_AtLarge_Turnout_Race.xlsx"))
nineteen = pd.DataFrame(pd.read_excel("2019_CityCouncil_Race Turnout.xlsx"))
Turnout = pd.read_csv("CC_turnout_all_years.csv")

mydict = dict(sorted(zip(eleven['Black Percentage'],Turnout['Turnout_2011'] )))
#mydict = dict(sorted(mydict.items, key=lambda item: item[1]))
lists = mydict.items()
print(lists)
x, y = zip(*lists)
plt.xlabel("Black Percentage")
plt.ylabel("Turnout In 2011")
plt.plot(x,y)
plt.show()
print(mydict)

plt.figure()
mydict = dict(sorted(zip(eleven['White Percentage'],Turnout['Turnout_2011'] )))
lists = mydict.items()
x, y = zip(*lists)
plt.xlabel("White Percentage")
plt.ylabel("Turnout In 2011")
plt.plot(x,y)
plt.show()

plt.figure()
mydict = dict(sorted(zip(eleven['Hispanic Percentage'],Turnout['Turnout_2011'] )))
lists = mydict.items()
x, y = zip(*lists)
plt.xlabel("Hispanic Percentage")
plt.ylabel("Turnout In 2011")
plt.plot(x,y)
plt.show()

# print(Turnout['Turnout_2011'])
# print(eleven['Black Percentage'])