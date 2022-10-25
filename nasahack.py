# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 15:54:30 2021
@author: Ibrahim Gok
"""
import pandas as pd
path=""
import requests

"""
location = "New Delhi"
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()
#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
print(temp_city,hmdt)
"""


def CtoF(Cels):
    return  (9.0/5.0)*Cels+32

def FtoC(Fahr):
    return (Fahr-32)*(5.0/9.0)




Hiexcl= pd.read_excel(path+'heatfactor.xlsx') 
heatindex=[]
degreex=[]
humx=[]
for i in Hiexcl["degree"]:
    degreex.append(i)

for i in Hiexcl["hum"]:
    humx.append(i)
    
def combineinto(list1,list2,list3,long):
    counter=0
    while long>counter:
        list3.append([list1[counter],list2[counter]])
        counter+=1
    
combineinto(degreex,humx,heatindex,len(Hiexcl))

counter=0
while len(heatindex)>counter:
    heatindex[counter].append(Hiexcl["dangerpoint"][counter])   
    counter+=1


def calcHi(warmth,hum):
    warmth=int(warmth)
    hum=int(hum)
    for i in heatindex:
        if i[0]==warmth and i[1]==hum:
            return int(i[2])
    return 0


def classifyHi(Hi):
    if Hi<95:
        return 0
    elif 95<Hi<99:
        return 1
    elif 100<Hi<104:
        return 2
    elif Hi<104:
        return 3
        
  
  



      
medicalHi =[[81,"Asthma"],[83,"Hearth disease"],[83,"dangereous for children, elderly, and overweight people"]]
def diagnoseHi(Hi):
    diagnose=""
    for i in medicalHi:
        if i[0]==Hi:
            diagnose+=i[1]+","
        else:
            return "NO"
    return diagnose







medicalWarm = [[100,"Heat exhaustion"],[104,"Heat Stroke"],[100,"Heat Rush"],[90,"Heat Cramp"]]
def diagnoseWarm(warmth):
    diagnose=""
    for i in medicalWarm:
        if i[0]==warmth:
            diagnose+=i[1]+","
        else:
            return "NO"
    return diagnose






forest_density=[
                
                ["WA",53],
                ["OR",49],
                ["ID",41],
                ["NV",16],
                ["CA",33],
                ["MT",27],
                ["WY",18],
                ["UT",34],
                ["AZ",26],
                ["CO",34],
                ["NM",32],
                ["ND",2],
                ["SD",4],
                ["NE",3],
                ["KS",5],
                ["OK",29],
                ["TX",37],
                ["MO",34],
                ["IA",8],
                ["AL",35],
                ["DT",56],
                ["AL",53],
                ["DT",49],
                ["AL",14],
                ["DT",56],
                ["DT",21],
                ["AL",49],
                ["DT",53],
                ["AL",65],
                ["DT",71],
                ["AL",67],
                ["DT",51],
                ["AL",68],
                ["DT",59],
                ["AL",63],
                ["DT",79],
                ["AL",59],
                ["DT",89],
                ["AL",78],
                ["DT",84],
                ["AL",61],
                ["DT",55],
                ["AL",54],
                ["DT",27],
                ["AL",42],
                ["DT",39],
                ["AL",31],
                ["DT",63],
                ["AL",35],
                ["DT",43],
                ]
def calcforestD(state,warm,hum):
    criticH=30
    criticW=108
    criticD=30
    for i in forest_density:
        if i[0]==state:
            density=i[1]
    if hum<criticH and warm>criticW and density>criticD:
        return 1
    else:
        return 0
    
    
shortlong=[
                
                ["AL","Alabama"],
                ["AK","Alaska"],
                ["AZ","Arizona"],
                ["AR","Arkansas"],
                ["CA","California"],
                ["CO","Colorado"],
                ["CT","Connecticut"],
                ["DE","Delaware"],
                ["FL","Florida"],
                ["GA","Georgia"],
                ["HI","Hawaii"],
                ["ID","Idaho"],
                ["IL","Illinois"],
                ["IN","Indiana"],
                ["IA","Iowa"],
                ["KS","Kansas"],
                ["KY","Kentucky"],
                ["LA","Louisiana"],
                ["ME","Maine"],
                ["MD","Maryland"],
                ["MA","Massachusetts"],
                ["MI","Michigan"],
                ["MN","Minnesota"],
                ["MS","Mississippi"],
                ["MO","Missouri"],
                ["MT","Montana"],
                ["NE","Nebraska"],
                ["NV","Nevada"],
                ["NH","New Hampshire"],
                ["NJ","New Jersey"],
                ["NM","New Mexico"],
                ["NY","New York"],
                ["NC","North Carolina"],
                ["ND","North Dakota"],
                ["OH","Ohio"],
                ["OK","Oklahoma"],
                ["OR","Oregon"],
                ["PA","Pennsylvania"],
                ["RI","Rhode Island"],
                ["SC","South Carolina"],
                ["SD","South Dakota"],
                ["TN","Tennessee"],
                ["TX","Texas"],
                ["UT","Utah"],
                ["VT","Vermont"],
                ["VA","Virginia"],
                ["WA","Washington"],
                ["WV","West Virginia"],
                ["WI","Wisconsin"],
                ["WY","Wyoming"],
                ] 

def wheathercheck():
    user_api = "6a94621c3e8306cb5a825b304cb14656"
    thelist=[]
    cell=[]
    for i in shortlong:
        cell=[]
        cell.append(i[0])
        location = i[1]
        complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()
        temp = CtoF((api_data['main']['temp']) - 273.15)
        hmdt = api_data['main']['humidity']
        cell.append(int(temp))
        cell.append(int(hmdt))
        thelist.append(cell)
    return thelist


            


def mainfunc():
    mainlist=wheathercheck()
    counter=0
    
    for i in mainlist:

        warm,hum=int(i[1]),int(i[2])

        try:
            Hi=calcHi(warm,hum)

            Hr=classifyHi(Hi)

            mainlist[counter].append(Hr)
        except:
            pass
        
        mainlist[counter].append(diagnoseWarm(warm)+diagnoseHi(Hi))
        mainlist[counter].append(calcforestD(i[0],warm,hum))
        counter+=1
        

        print(mainlist)
    return mainlist
    
        
 
mainlist=mainfunc()     

import csv
  
  
# field names 
fields =['State',"Warmth","Humidity", 'Condition', "Health Risks", 'Wildfire Risk']

    
df = pd.DataFrame(mainlist, columns =['State',"Warmth","Humidity", 'Condition', "Health Risks", 'Wildfire Risk'])
print(df)
  
 
       
