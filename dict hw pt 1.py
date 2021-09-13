ClassDict = {'CS101':{'Room': '3004', 'Instructor': 'Haynes','Time': '8:00 a.m.'},
    'CS102':{'Room': '4501', 'Instructor': 'Alvarado','Time': '9:00 a.m.'},
    'CS103':{'Room': '6755', 'Instructor': 'Rich', 'Time': '10:00 a.m.'},
    'NT110':{'Room': '1244', 'Instructor': 'Burke', 'Time': '11:00 a.m.'},
    'CM241':{'Room': '1411', 'Instructor': 'Lee', 'Time': '1:00 p.m.'}}


userinput = input("Enter Course Number: ")

print('Room:',ClassDict[userinput]['Room'], ' - ', 'Instructor:',ClassDict[userinput]['Instructor'], ' - ', 'Time:',ClassDict[userinput]['Time'])