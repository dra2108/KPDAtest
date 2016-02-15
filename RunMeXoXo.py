

#Code for a valentines day madlib for Dario.
# 2/5/2016

print ("Hi Dario!  Happy Valentine's Day.")

doing = input("How are you doing?")

print("I'm glad you're "+ doing + ".  Me too!")
# Let Dario say Yes or No

answer = input("Do you want to see the awesome card I made you?!")
if answer == "yes" or "Yes" : 
    print("Great! I'm gonna need some help though. I dozed off as I was writing, and I forgot a few words. I need your help filling them in.")
else :
    print("Oh, cmon, lazyface! Please say yes!")

moons = input("Gimme a plural noun.")
brunch = input("Name a party occasion.")
arrived = input("And a past tense verb.")
nice = input("Adjective.")
people = input("Type of animal, plural.")
charmed = input("Emotion.")
clothes = input("Type of clothing.")
handsome = input("Adjective.")
C3PO = input("Celebrity.")
Han = input("Another celebrity.")
animal = input("Animal.")
kilos = input("Unit of measurement, plural.")
threaded = input("Past tense verb.")
needle = input("Noun.")
exhibit = input("Type of party or event.")
beers = input("Beverage.")
Matching = input("Verb ending in -ing. Capitalized, please.")
Half = input("Noun, also capitalized.")
head = input("Body part.")
heels = input("Another body part.")
nickname = input("Nickname.")


answer2 = input("Thanks a lot!  That oughtta do the trick.  Ready for your message?")

if answer2 == "yes" or "Yes" :
    print("One Saturday morning many " + moons + " ago, I went to a " + brunch + " party hoping to meet some nice " + people + " .  And there you were in your fancy " +clothes+ ", more " + handsome + " than " + C3PO + " and more fascinating than " + Han + "--although, I admit, I didn't realize it at the time. In contrast, you thought I was as beautiful as a " + animal + " , and you spent several " + kilos + "  of time constructing a message that " + threaded + " the " + needle + " of flirtation and friendliness. It worked! We went to that Georgia O'Keeffe " + exhibit + " at the De Young and sipped some " + beers + " at the " + Matching +"  "+ Half + " Cafe.  Honestly, from then on I've been " + head + " over " + heels + ". Happy Valentine's Day, " +nickname+ "!"  )  
else: 
    print("Ha, ha, very funny.  Cmon, say yes :) ")




