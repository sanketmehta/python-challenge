# Steps
# 1. Read csv 1 & 2 data into lists
# 2. Iterate through the lists while simultaneously performing the formatting of data.
# 3. Each row data is temporarily stored into a list(rec) which is added into a list of lists(recArr) 
# 4. Open/create the csv file (finalData.csv) and write the contents of recArr into it.

#import the required modules
import csv
import datetime
from us_state_abbrev import * 


#open the csv files and using csv reader method create the list objects to iterate through the data
with open('./employee_data1.csv', 'r') as wb1:
  reader1 = csv.reader(wb1)
  wb1_list = list(reader1)
with open('./employee_data2.csv', 'r') as wb2:
  reader2 = csv.reader(wb2)
  wb2_list = list(reader2)

#creating a list to store column headers.
rec = ['Emp ID','First Name','Last Name','DOB','SSN','State']

#create a recArr for all rows (both CSVs)
recArr = [[] for x in range(len(wb1_list) + len(wb2_list) - 1)]

#setting first list as value of column headers
recArr[0] = rec
#resetting the list(rec) to reuse the same
rec = []

#iterating through the first csv data list[wb1_list] and saving the row data(formatted) into a temp list(rec) to add it into list of lists(recArr)
for j in range(1,len(wb1_list)):
    rec.append(wb1_list[j][0])
    rec.append(wb1_list[j][1].split(' ',1)[0])
    rec.append(wb1_list[j][1].split(' ',1)[1])
    rec.append(datetime.datetime.strptime(wb1_list[j][2], '%Y-%m-%d').strftime('%d/%m/%Y'))
    rec.append(wb1_list[j][3].replace((wb1_list[j][3])[:6],'***-**'))
    rec.append(us_state_abbrev.get(wb1_list[j][4]))
    recArr[j] = rec
    rec = []

#iterating through the second csv data list[wb2_list] and saving the row data(formatted) into a temp list(rec) to add it into list of lists(recArr)
for k in range(1,len(wb2_list)):
    rec.append(wb2_list[k][0])
    rec.append(wb2_list[k][1].split(' ',1)[0])
    rec.append(wb2_list[k][1].split(' ',1)[1])
    rec.append(datetime.datetime.strptime(wb2_list[k][2], '%Y-%m-%d').strftime('%d/%m/%Y'))
    rec.append(wb2_list[k][3].replace((wb2_list[k][3])[:6],'***-**'))
    rec.append(us_state_abbrev.get(wb2_list[k][4]))
    recArr[len(wb1_list)+k-1] = rec
    rec = []

#open a new csv file(finalData.csv) to write the data from the list of lists(recArr)
with open("./finalData.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(recArr)
