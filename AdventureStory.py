# AdventureStory.py
# ICS201 Vashisht
# January 21, 2021

# Introductory Dialogue
print("You wake up in a desert.") 
print("In front of you, you see a figure, running away.")
print("You notice you don't have a lot of time, as they are running away quickly.")

choice1 = int(input("\nDo you: stay where you are [1], or chase them [2]? "))

if choice1 == 1: # Chose to stay where they are
    print("\nYou stay where you are.")
    print("You start looking around. You have bad vision.")
    print("Only after a while, you notice 2 bottles beside you.")
    print("One is of water, while the other, is of Pepsi.")

    choice1a = int(input("\nDo you: drink the water [1], or drink the Pepsi [2]? "))
    
    if choice1a == 1: # Chose Water
        print("\nYou decide to carefully open the bottle of water.")
        print("Dehydrated, you hastily take a sip.")
        print("You start feeling sick.")
        print("Unbeknownst to you, the shadowy figure poisoned the water.")
        print("You fall back down and go to sleep for a very long time.")
        print("\nEnd.") # Ending 1
        
    elif choice1a == 2: # Chose Pepsi
        print("\nYou slowly grab the bottle of Pepsi.")
        print("Hesitantly, you unscrew the cap on it.")
        print("You start drinking it.")
        print("Suddenly, you feel very energetic and... 'epic'.")
        print("Against your will, your legs start moving. You start running.")
        print("Your body is moving in the direction of the figure.")

        choice1b = int(input("\nDo you: keep going [1], or try to stop [2]? "))

        if choice1b == 1: # Chose to keep on running
                print("\nYou keep running.")
                print("Second by second, you can feel yourself running faster.")
                print("Still, you are getting nowhere even near the figure.")
                print("Hours pass.")
                print("Eventually, the figure stops.")

                choice1ba = int(input("\nDo you: approach them [1], or keep running [2]? "))

                # Choose to approach the figure
                if choice1ba == 1:
                    print("\nYou start to slow down.")
                    print("Eventually, you start nearing the figure.")
                    print("They stay stopped in place.")
                    print("You stop running. You are behind the figure.")
                    print("They turn around.")
                    print("\nThe figure is Reevai Ackahmahn from Attack on Titan.")
                    print("\nThe simulation ends.")
                    print("The end.") # Ending 4

                # Choose to keep running    
                elif choice1ba == 2:
                    print("\nYou keep running.")
                    print("After a while, you pass the figure.")
                    print("You catch but a glimpse of their appearance.")
                    print("Small eyes, split bangs-- and quite a short stature.")
                    print("Suddenly, you enter a black void.")
                    print("It's empty.")
                    print("You keep running.")
                    print("\nEnd") # Ending 3
                    
            
        elif choice1b == 2: # Chose try to stop
                print("\nYou try to stop.")
                print("Your grind your feet against the ground, trying your hardest to stop moving.")
                print("Your feet start heating up.")
                print("They catch on fire.")
                print("The shadowy figure is nowhere to be seen. They are the least of your worries right now.")
                print("Your body continues moving.")
                print("You fall asleep.")
                print("\nEnd") # Ending 4
                
elif choice1 == 2: # Chose to stay chase shadowy figure
    print("\nYou start chasing the shadowy figure.")
    print("You notice they keep getting farther and farther away.")
    print("Your legs are slowly getting tired.")

    choice2 = int(input("\nDo you decide to: push through it and keep running [1], or stop and take a break [2]? "))

    if choice2 == 1: # Chose to keep running
        print("\nYou decide to push through and keep running.")
        print("The shadowy figure refuses to slow down.")
        print("Hours pass. Days, even. You keep running.")
        print("Eventually, you fall.")
        
        choice2a = int(input("\nDo you: give up [1], or keep going [2]? "))
        
        if choice2a == 1: # Chose to give up
            print("\nYou stop.")
            print("No longer can you keep going. Your spirit is crushed and your day is ruined.")
            print("You thought you could chase the figure.")
            print("You could not.")
            print("You stay there and weep.")
            print("Good night.")
            print("\nEnd.") # Ending 5

        if choice2a == 2: # Chose to keep going
            print("\nYou start to crawl.")
            print("Your arms are weak. You can't keep this up for much longer.")
            print("Still, you keep fighting. 'Fight. Fight.', you say to yourself.")
            print("Eventually, your arms get tired and you can not keep crawling.")
            print("You fall down, with your face hitting the sand as you do.")
            print("Just as you're about to fall asleep, the figure stops.")
            print("They turn around and ask you a question,")

            choice2ab = int(input("\nPepsi [1] or Coke [2]? "))

            if choice2ab == 1: # Chose Pepsi
                print("\nThe figure smiles.")
                print("'Good Choice.'")
                print("They turn back around and starts running.")
                print("You lay there, confused.")
                print("\nEnd.") # Ending 6

            elif choice2ab == 2: # Chose Coke
                print("\n'...'")
                print("The figure puts their hand into their shirt.")
                print("Slowly, they pull out a circular object.")
                print("They throw it in your direction.")
                print("Closer. Closer. The object is getting closer every second.")
                print("'A f-frisbie...?'")
                print("Moments after you find out what the object is, it hits your head.")
                print("You fall back down.")
                print("You go to sleep.")
                print("\nEnd.") # Ending 7

    elif choice2 == 2: # Chose to take a break
        print("\nYou decide to stop running.")
        print("You fall down and rest.")
        print("The shadowy figure disappears into the horizon. They are no longer visible at all.")
        print("You lie down and start to think about your last meal.")
        print("You tell yourself you did great.")
        print("Eventually, you fall asleep. Right there in the desert.")
        print("\nEnd") # Ending 8



    
