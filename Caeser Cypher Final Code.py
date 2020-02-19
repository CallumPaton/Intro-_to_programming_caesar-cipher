#Import Library

import sys #Was unable to input multiline messages so had to import sys
import os #This function searches for a file and allows a while loop -

Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


def InputMessage():
    MsgOrFile = input("Is the message you would like to input from a file (yes/no)?:")
    if str(MsgOrFile.upper())=="YES":
        print ('**Remember :file must be placed in same folder as this programme**')
        FileName = input("What is the filename?")
        while (not os.path.exists(FileName)):
            FileName = input("Error - File not found, please re-enter file name: ")
        FileMessage = open(FileName, "r")
        YourMessage = FileMessage.read()
        YourMessage = YourMessage.upper()
#Using the import.sys function to allow multiline messages, converts message to upper in order to fit with alphabet
    else:
        print("What is your message?: ")
        print("Press enter and Ctrl d to end message")
        YourMessage = sys.stdin.read()
        YourMessage = YourMessage.upper()
    return(YourMessage)

def RotVal():
    RLoop = True
    RotationInput = input('What rotation value do you want?: ')
    while RLoop == True:
        if RotationInput.isnumeric()==True:
            Rotation = int(RotationInput)
            RLoop = False
        else:
            print("Error: You did not input a number")
            RotationInput = input('What rotation value do you want?: ')
    return (RotationInput)

def encrypt(YourMessage, Rotation):
#Loop to ask if user wants file - if they do, user inputs filename and a while loop is used to send error if file cant be found.
    
    print('~~~~~~~~~~~~~~~')
    print('Encrypted Message')
    print('~~~~~~~~~~~~~~~')
# While loop to make sure if user accidently doesnt input a number, the code doesnt break.
# Instead they are re asked to enter a number. loop ends when they do so.


    EncryptedAlphabet = {}
    EncryptedText = ' '

#Asigning a number to every letter in the list - Alphabet. New Letter is then this number plus rotation value.
#This is put into rotated Alphabet. %26 means if rotation is greater than 26, the remainder is given.    
    for i in range (0,26):
        Letter = Alphabet[i]
        EncryptedAlphabet[Letter] = Alphabet[(i + Rotation)%26]
        
#Now for every letter in message, it is replaced by the letter in the rotated alphabet.
#If it reaches a letter not in the alphabet (number or ! ...) it adds it to the message without any change.
    for Letter in YourMessage:
        if Letter in Alphabet:
            Letter = EncryptedAlphabet[Letter]
            EncryptedText += Letter
        elif Letter not in Alphabet:
            EncryptedText += Letter

    print(EncryptedText)
#See bottom for Message stats function.
    MessageStats(YourMessage)
        
def decrypt(YourMessage, Rotation):
# This function is the same as encrypt but instead takes away the rotation rather than adding it on. Thus getting back to original letter.
        
    print('~~~~~~~~~~~~~~~')
    print('Decrypted Message')
    print('~~~~~~~~~~~~~~~')

    EncryptedAlphabet = {}
    EncryptedText = ' '

#Until now this is same as encrypt, as user knows the rotation value, changing i + to i - gets you back to original message
    for i in range (0,26):
        Letter = Alphabet[i]
        EncryptedAlphabet[Letter] = Alphabet[(i - Rotation)%26]
        

    for Letter in YourMessage:
        if Letter in Alphabet:
            Letter = EncryptedAlphabet[Letter]
            EncryptedText += Letter
        elif Letter not in Alphabet:
            EncryptedText += Letter

    print(EncryptedText)
    MessageStats(YourMessage)
    

def auto_decrypt(YourMessage):
    

#This imports common words in the english language and places them in a string.
    CommonDict=open('commonwords.txt')
    CommonDict = CommonDict.read()
#This is the same process as encryption and decryption except its all embedded within a for loop that runs through rotations in range (1,26)   
    
    for Rotation in range (1,26):
        DecryptedDict = {}
        DecryptedText = ' '
        for i in range (0,26):
            Letter = Alphabet[i]
            NewLetter = Alphabet[(i + Rotation)%26]
            DecryptedDict[Letter] = NewLetter

        for Letter in YourMessage:
            if Letter in Alphabet:
                Letter =DecryptedDict[Letter]
                DecryptedText += Letter
            else:
                DecryptedText += Letter
#As the common words dict is all lower case, the encrypted text needs the .lower() operation. It then needs to be converted to a list with .split()                
        LowerDecryptedText = DecryptedText.lower()
        DecryptedList = LowerDecryptedText.split()
#Now, for each rotation, whenever a word matches a word in the common word list, a 'point' is 'scored'.
#When more than half of the words in the message are also in the commonword dict. The decrypted message is printed.
        Score = 0
        for Word in DecryptedList:
            if Word in CommonDict:
                Score+= 1
        if (Score/len(DecryptedList)) > 0.5:
            print(str(DecryptedText))
            print('The encrypted message was rotated' , (26 - Rotation), 'Times')
        
    MessageStats(YourMessage)




def MessageStats(YourMessage):

    print ('~~~~~~~~~~~~~~~')
    print('Message Stats')
    print ('~~~~~~~~~~~~~~~')

#Message Length - converts message to list and counts number of items in list
    MessageLength = len(YourMessage.split())
    print ('The Number of Words in This Message is:', MessageLength)

#UniqueWords - To do this, I made a set from a set of the split words.
#This is because there is no repitition in sets and thus it only adds words that occure once 
    UniqueSet = set([])
    for Words in YourMessage.split():
        UniqueSet.add(Words)
        NumberOfUniqueWords = len(UniqueSet)
    print('The Number of Unique Words in Your Message:' ,NumberOfUniqueWords)

#Min and Max Word Length - runs through list form of message. when length of word is < or > than words before it, it becomes MaxLength or MinLength.
    MaxLength = 0
    for Words in YourMessage.split():
        if len(Words) > MaxLength:
            MaxLength = len(Words)
    print('The length of the longest word in your message is:', MaxLength)
    MinLength = 1000
    for Words in YourMessage.split():
        if len(Words)<MinLength:
            MinLength = len(Words)
    print('The length of the shortest word in your message is:', MinLength)

#Average Length of Words in Message - for each word in the message, it works out length.
#It then adds this up and divides by i which is number of words in the message.
    SumOfWordLengths = 0
    i = 0
    for Words in YourMessage.split():
        WordLength = len(Words)
        SumOfWordLengths += WordLength
        i += 1
    AverageWordLength = SumOfWordLengths / i
    print('Average Length of Words in your message is:', AverageWordLength)

#Most Frequent Letter - use .count function to count characters. most characters becomes 'MostFrequentLetter'.
    MostFrequentLetter = 0
    for Characters in YourMessage:
        if YourMessage.count(Characters) >MostFrequentLetter:
            MostFrequentLetter = YourMessage.count(Characters)
    print('The most common Letter in your message is:' ,Characters,'=' ,MostFrequentLetter, 'Times')

#Most Common Words Dictionary - Adds all words in the message 'list' to a dictionary.
#The dictionary can then be sorted by occurence of words in the list, the 'key' of the dictionary.
#By making a second dictionary 'Top 3 Words' which is ordered by size of key. you can obtain the first 3 items in the dictionary with :3.    
    WordsDict = {}
    Top3WordsDict = {}
    for Words in YourMessage.split():
        if Words in WordsDict:
            WordsDict[Words] += 1
        else:
            WordsDict[Words] = 1
    CommonWords = sorted(WordsDict, key = WordsDict.get, reverse = True)   
    Top3Words = CommonWords[:3]
    for Words in Top3Words:
        Top3WordsDict[Words] = (YourMessage.split()).count(Words)
         
    print('These are the 3 most common words in your message are:', Top3WordsDict)


    
#This while loop allows user to continue inputting until either encrypt or decrypt is written.
#If decrypt is chosen, it runs through a second loop for auto or manual decrypt
EorD = input ("Do you want to encrypt or decrypt: ")
EorDloop = True   

while EorDloop == True: 
    if EorD.lower() == "encrypt":
        YourMessage = InputMessage()
        RotationInput = int(RotVal())
        encrypt(YourMessage, RotationInput)
        EorDloop = False
    elif EorD.lower() =="decrypt":
        DecryptionType = input ("Type 1 for manual decryption, 2 for auto decryption: ")
        DecryptionLoop = True
        while DecryptionLoop == True:
            if DecryptionType == '1':
                YourMessage = InputMessage()
                RotationInput = int(RotVal())
                decrypt(YourMessage, RotationInput)
                DecryptionLoop = False
            elif DecryptionType == '2':
                YourMessage = InputMessage()
                auto_decrypt(YourMessage)
                DecryptionLoop = False
            else:
                DecryptionType = input ("Type 1 for manual decryption, 2 for auto decryption: ")
        EorDloop = False
    else:
        print('Incorrect Input')
        EorD = input ("Do you want to encrypt or decrypt ")
