print('''
*******************************************************************************
  ___------~~~~~~~~~~~----__         .:.         __----~~~~~~~~~~~------___   
 ~~ ~--__          ......====\\~~    .:::.    ~~//====......          __--~ ~~ 
         ~\ ...::::~~~~~~  //|||    .:::::.    |||\\  ~~~~~~::::... /~         
        -~~\_            //  |||***.(:::::).***|||  \\            _/~~-        
             ~\_        // *******.:|\^^^/|:.******* \\        _/~             
                \      / ********.::(>: :<)::.******** \      /                
Collage by       \   /  ********.::::\\|//::::.********  \   /                 
 John Lawrence    \ /   *******.:::::(o o):::::.*******   \ /                  
                   /.   ******.::::'*|V_V|***`::.******   .\                   
                     ~~--****.:::'***|___|*****`:.****--~~                     
                           *.::'***//|___|\\*****`.*                           
                           .:'  **/##|___|##\**    .                           
                          .    (v(VVV)___(VVV)v)
*******************************************************************************
''')
print("Welcome to Mount Dacon.")
print("Your mission is to find the dragon's treasure horde.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input('You\'re at a crossroads. What do you want to do? Type "left" or "right".').lower()
if choice1 == "left":
    choice2 = input("It is almost night time. There is a single rope spanning a chasm. What do you do? Type \"wait\" or \"cross\"").lower()
    if choice2 == "wait":
      choice3 = input('''
As you wait the moon shines on the chasm and reveals an ethereal bridge glistening in the moonlight. Your cross safely. You see three doors,
a big door with intricate carvings, a small door with no design, and medium sized door that glows faintly. Which door do you choose? Type "big" "medium" or "small"''').lower()
      if choice3 == "big":
          print('''
You swing open the door. The sound of wood and steel groaning echoe throughout a massive cavern. You hear a mighty "ROOOAAAAR!!" ass the dragon
pounces on you and ends your attempt on his horde. Game Over''')
      elif choice3 == "medium":
          print('''
You step into a dark room. Fires begin to light around the edges of the room and you can see it is empty. But, they don't stop lighting and trap you between the raging flames! Game Over.''')
      else:
          choice4 = input('''
You crawl on your hands and knees and find the door is locked. A voice says he is the defender of the door and asks what you want. What do you do? Type "sing" or "threaten"''').lower()
          if choice4 == "sing":
            print('''
You sing the most beautiful song heard in the world. You hear sniffling and a "kathunk" as the door opens to find a gnome crying. 
He says "That is the most beautiful song I have heard in a millenia. It reminds me of the homeland I left so long ago. 
I must be off to see my family again, thank you for reminding me of all I have left behind. Please help yourself to the horde I am defending".
He runs off and you can see down the tunnel the dazzling piles of gold, jewels and treasures you seek. 
            
Congratulations!! You have become the richest person in all the lands''')
          else:
              print('''
You threaten the life of whomever guards the door if they don't open it. "HA, you think you can threaten Glomstorn the third, royal treasury defender of the highest degree?!". You hear a "BAAAAAAWOOOOOOOM" as a horn sounds and echoes through the cavern. Suddenly, the large doors bang open as the mighty dragon "ROOOOOOOAAAAAAAAR"s casting the entire hallway in flames and burning you for your hubris. Game Over. ''')
    else:
        print("The windy chasm causes you to lose your footing. You fall to your doom. Game Over.")
else:
    print("You are attacked by bears. Game Over.")
