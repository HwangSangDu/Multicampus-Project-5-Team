import json
import csv
import sys
import requests



f = open('./영화사목록.json')
# print(f)
# sys.exit()
# json_val = json.dump(f)

data = json.load(f)





# for i in range(0,11849)



i = 0
# print( str(data["companyListResult"]["companyList"][i]['companyCd']))
x = {'Arr': []}
for i in range(0,11849):
  response = requests.get('http://kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyInfo.json?key=430156241533f1d058c603178cc3ca0e&companyCd=' + str(data["companyListResult"]["companyList"][i]['companyCd']))
  dict1 = response.text
  x['Arr'].append(dict1)


print(x)
with open('data22.json', 'w') as fp:
    fp.write(str(x))

  

# print(type(response.text))
# resData = json.loads(response.text)
# print(resData)


# # print(x["Arr"])
# x["Arr"].append(response.text)
# print(str(x))
# # y = json.dumps(x)
# # print(y)

# with open('data22.json', 'w') as fp:
#     fp.write(str(x))
# with open('data22.json', 'r') as file:
    # file.write(str(x))




# dict1 = { 'name' : 'song', 'age' : 10 }
# dict1 = response.text


# print ("dict1 = %s" % dict1)

# print ("dict1 type = %s" % type(dict1))

# with open('data22.json', 'w') as fp:
#     fp.write(str(dict1))

# print ("================")



# CONVERT dictionary to json using json.dump

# json_val = json.dumps(dict1)



# print ("json_val = %s" % json_val)

# print ("json_val type = %s" % type(json_val))










# data = {"companyInfoResult":{"companyInfo": 0}}



# print(data["companyListResult"]["companyList"][0])




sys.exit()
f.close()


f = open('./data.csv')
csv_file = csv.writer(f)
for item in data:
 print(item)
 csv_file.writerow(item)

f.close()
