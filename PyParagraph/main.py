#Steps
#1. import regex library (re) for processing the text
#2. Take the input from user as which data file he/she needs to process. File list (available to process) is saved in a dictionary and stored under raw_data directory.
#2. open & read the text file into a string object(txtData)
#3. using regex method findall & various regex patterns; find the letter/character, word & sentence counts.

#import the required libraries
import re
import os

#dictionary of input data files to provide a choice for user to process a specific file
inpFileDict = {0:'paragraph.txt', 1:'paragraph_1.txt', 2:'paragraph_2.txt'}

#take user input to select a specific file for processing
choice = input("Please choose a number to process the corresponding file:- " + str(inpFileDict) + " :")

#setting input and output filenames
filename=inpFileDict[int(choice)]

#file paths
inputFilePath = os.path.join("raw_data", filename)

# #take the fileName (containing the paragraph text) as an input from the user
# fileName = input("please enter the text file name containing the paragraph & make sure file is in same directory as this script: ")

#open and read the file data into a string variable
with open(inputFilePath, "r") as f:
  txtData = f.read()

#perform the paragraph analysis by using the regex method findall to calculate required values & print the analysis
print("")
print("------------------")
print("Paragraph Analysis")
print("------------------")
print("Approximate Total Charater Count: ", len(re.findall(r'.', txtData)))
print("Approximate Non Space-Charater Count: ", len(re.findall('[^ ]', txtData)))
print("Approximate Word Count: ", len(re.findall(r'\w+', txtData)))
#sentences can end with a '.', '?' or '!', hence counting instances of each of these
print("Approximate Sentence Count: ", len(re.findall(r'[\.\?\!]', txtData)))
print("Average Letter Count (Letters/Word): ", round(len(re.findall('[^ ]', txtData))/len(re.findall(r'\w+', txtData)),11))
print("Average Sentence Length (Words/Sentence): ", round(len(re.findall(r'\w+', txtData))/len(re.findall(r'[\.\?\!]', txtData)),1))
print("------------------")
