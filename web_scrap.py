import requests
from bs4 import BeautifulSoup
import pandas

req=requests.get("https://www.fireandemergency.nz/incidents-and-news/incident-reports/")
req.raise_for_status()
soup = BeautifulSoup(req.content,"html.parser")



main=soup.find_all("div","incidentreport__region")
#print(main1)
regions=[]

for elem in main:
    #print(elem.text)
    days=[]
    for region in elem.find_all("ul"):
        #print(region.text)
        for day in region.find_all("li","region"):
            #print(day.a.get("href"))
            days.append(day.a.get("href"))
            
        regions.append(days)

#print(regions)

def Call(link):
    req1=requests.get('https://www.fireandemergency.nz/'+link)
    soup = BeautifulSoup(req1.content,"html.parser")
    return soup

Region_name=["North","Central","South"]
dict_final={}
list2=[]
list1 = []
for region in regions:
    for day in region:
        dict1={}
        sub_page=Call(day)
        print(sub_page.find("p","report__header__message").text)
        body=sub_page.find_all("div","report__table__body")
        for info in body:
            for row in info.find_all("div","report__table__row"):
            #print(info)
                key=row.find("div",class_="report__table__cell report__table__cell--key").text
                value=row.find("div",class_="report__table__cell report__table__cell--value").text
                dict1[key]=value
            list1.append(dict1)
        list2.append(list1)
#ast.literal_eval(string_dict)
#print(list2[0][0])
# for i in range(len(list2)):
#     dict2=list2[i]
#     dict_final["all_regions"]=dict2
#     df=pandas.DataFrame(dict_final)
#     df.to_csv("all_regions.csv")
    
dict2=list2[0:6]
dict3=list2[7:13]
dict4=list2[14:20]
for i in range(len(dict2)):
    dict_final["North"]=dict2[i]
    df=pandas.DataFrame(dict_final["North"])
    df.to_csv("North.csv")  

for j in range(len(dict3)):
    dict_final["Central"]=dict3[j]
    df=pandas.DataFrame(dict_final["Central"])
    df.to_csv("Central.csv")

for k in range(len(dict4)):
    dict_final["South"]=dict4[k]
    df=pandas.DataFrame(dict_final["South"])
    df.to_csv("South.csv")        
