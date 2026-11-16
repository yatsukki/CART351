# Open rainbow.txt in append mode
rainbowFile = open("files/rainbow.txt", "a")

rainbowFile_r = open("files/rainbow.txt", "r")
#read first 4 bytes (1 char per byte)
out4 = rainbowFile_r.read(4)
# print(out4)
#read entire text - but note if we read before... 
# then we will be reading from where we read last...
#and once it has consumed the entire file - you can no longer read...
out_all = rainbowFile_r.read()
# print(out_all)
#so to go back to start then - > use the seek function...
rainbowFile_r.seek(0)
out_all_a = rainbowFile_r.read()

#go back to beginning
rainbowFile_r.seek(0)

#stored in a list - each line is one element in the list
allLines = rainbowFile_r.readlines()
# print(allLines)
# print(allLines[0])
oneLine = rainbowFile_r.readline()
# print(oneLine)


sampleFile = open("files/sample_text_rev.txt", "w")

# for i in range(3): 
#     a_name = input("Enter the name of the animal: ") 
#     sampleFile.write(a_name) 
#     sampleFile.write("\n") 
# sampleFile.close() 
# print("Data is written into the file.") 

sampleFile_a = open("files/sample_text.txt", "a")
nameList = []
# 3 in this case stands for the number of names you want to enter, the amount of times you want to loop through the input function
for i in range(3): 
    a_name = input("Enter the name of someone in your class: ") 
    nameList.append(a_name + '\n') 
sampleFile_a.writelines(nameList) 
sampleFile_a.close() 
print("Data is written into the file.") 