#Steps
#1. import regex library (re) for processing the text
#2. open & read the text file into a string object(txtData)
#3. using regex method findall & various regex patterns; find the letter/character, word & sentence counts.

#import the required libraries
import re

#take the fileName (containing the paragraph text) as an input from the user
fileName = input("please enter the text file name containing the paragraph & make sure file is in same directory as this script: ")

#open and read the file data into a string variable
with open("./"+fileName, "r") as f:
  txtData = f.read()

#perform the paragraph analysis by using the regex method findall to calculate required values & print the analysis
print("")
print("------------------")
print("Paragraph Analysis")
print("------------------")
print("Approximate Total Charater Count: ", len(re.findall(r'.', txtData)))
print("Approximate Non Space-Charater Count: ", len(re.findall('[^ ]', txtData)))
print("Approximate Word Count: ", len(re.findall(r'\w+', txtData)))
print("Approximate Sentence Count: ", len(re.findall(r'\.', txtData)))
print("Average Letter Count (Letters/Word): ", round(len(re.findall('[^ ]', txtData))/len(re.findall(r'\w+', txtData)),11))
print("Average Sentence Length (Words/Sentence): ", round(len(re.findall(r'\w+', txtData))/len(re.findall(r'\.', txtData)),1))
print("------------------")
