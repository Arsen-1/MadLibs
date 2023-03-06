import random
user_input = int(input("Write a number between 1 to 3: "))
def template_1():

    a1 = input("input a number: ")
    a2 = input("input a measure of time: ")
    a3 = input("input a mode of transportation: ")
    a4 = input("input an adjective: ")
    a5 = input("input another adjective: ")
    a6 = input("input a noun: ")
    a7 = input("input a color: ")
    a8 = input("input a part of the body: ")
    a9 = input("input a verb: ")
    a10 = input("input another number: ")
    a11 = input("input another noun: ")
    a12 = input("input another noun: ")
    a13 = input("input another part of the body: ")
    a14 = input("input a verb: ")
    a15 = input("input another noun: ")
    a16 = input("input another adjective: ")
    a17 = input("input a silly word: ")
    a18 = input("input another noun: ")

    text1 = f'"It was about {a1} {a2} ago when I arrived at the hospital in a {a3}. The hospital is a/an {a4} place, there are a lot of {a5} {a6} here. \
There are nurses here who have {a7} {a8}. If someone wants to come into my room I told them that they have to {a9} first. I’ve decorated my room with {a10} {a11}. \
Today I talked to a doctor and they were wearing a {a12} on their {a13}. I heard that all doctors {a14} {a15} every day for breakfast. \
The most {a16} thing about being in the hospital is the {a17} {a18} !"'
    return text1

def template_2():

    b1 = input("input a proper noun(persons name): ")
    b2 = input("input a noun: ")
    b3 = input("input an adjective(feeling): ")
    b4 = input("input a verb: ")
    b5 = input("input another adjective(feeling): ")
    b6 = input("input an animal: ")
    b7 = input("input another verb: ")
    b8 = input("input a color: ")
    b9 = input("input a verb(ending in ing): ")
    b10 = input("input an adverb(ending in ly): ")
    b11 = input("input a number: ")
    b12 = input("input a measure of time: ")
    b13 = input("input a color: ")
    b14 = input("input an animal: ")
    b15 = input("input a number: ")
    b16 = input("input a silly word: ")
    b17 = input("input another noun: ")

    text2 = f'"This weekend I am going camping with {b1}. I packed my lantern, sleeping bag, and {b2}. I am so {b3} to {b4} in a tent. \
I am {b5} we might see a/n {b6}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {b7}. I have heard that the {b8} \
lake is great for { b9}. Then we will {b10} hike through the forest for {b11} {b12}. If I see a {b13} {b14} while hiking, \
I am going to bring it home as a pet! At night we will tell {b15} {b16} stories and roast {b17} around the campfire!!"'
    return text2

def template_3():

    c1 = input("input a proper noun(person name): ")
    c2 = input("input an adjective: ")
    c3 = input("input a color: ")
    c4 = input("input a animal: ")
    c5 = input("input a place: ")
    c6 = input("input another adjective: ")
    c7 = input("input a magical creature(plural): ")
    c8 = input("input another adjective: ")
    c9 = input("input another magical creature(plural): ")
    c10 = input("input a room in a house: ")
    c11 = input("input a noun: ")
    c12 = input("input another noun: ")
    c13 = input("input another noun(plural): ")
    c14 = input("input another adjective: ")
    c15 = input("input another noun plural: ")
    c16 = input("input a number: ")
    c17 = input("input a measure of time: ")
    c18 = input("input a verb ending in ing: ")
    c19 = input("input another adjective: ")
    c20 = input("input another noun: ")

    text3 = f'"Dear {c1}, I am writing to you from a {c2} castle in an enchanted forest. I found myself here one day after going for a ride on a {c3} {c4} \
in {c5}. There are {c6} {c7} and {c8} {c9} here! In the { c10} there is a pool full of {c11}. \
I fall asleep each night on a {c12} of {c13} and dream of {c14} { c15}. It feels as though I have lived here for {c16} { c17}. \
I hope one day you can visit, although the only way to get here now is {c18} on a {c19} {c20}!!"'
    return text3

if user_input == 1:
    print(template_1())
elif user_input == 2:
    print(template_2())
elif user_input == 3:
    print(template_3())
else:
    random.choice(template_3(),template_2(),template_1())
