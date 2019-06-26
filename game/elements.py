print ("this quiz will tell you wich element you are most like");
print ("please type the letter that correspondsto your answer and then hit enter\n");

fire=0
water=0
air=0
earth=0

response = input("whats your favorite color? A. red B. blue C. green D. other\n")
if response == "A" :
    fire += 1
elif response == "B" :
    water += 1
elif response == "C" :
    earth += 1
elif response == "D" :
    air += 1
else :
    print ("Answer not recognized");

response = input("what animal do you like most A. dog B. cat C.bunny D. other\n")
if response == "A" :
    fire += 1 
elif response == "B" :
    water += 1
elif response == "C" :
    earth += 1
elif response == "D" :
    air += 1
else :
    print ("Answer not recognized");
response = input("what type of food do you like most A. pizza B. taco C. steak D. other\n")
if response == "A" :
    fire += 1
elif response == "B" :
    water += 1
elif response == "C" :
    earth += 1
elif response == "D" :
    air += 1
else :
    print ("Answer not recognized");
response = input("whats your favorite thing to do A. draw B. electronics C. sleeping D. other\n")
if response == "A" :
    fire += 1
elif response == "B" :
    water += 1
elif response == "C" :
    earth += 1
elif response == "D" :
    air += 1
else :
    print ("Answer not recognized");
print ("calculating results...")
print ("your result is: ")

result = max(air, earth, fire, water)

if result == air :
    print("air")
elif result == earth :
    print("earth")
elif result == fire :
    print("fire")
else :
    print("water")
