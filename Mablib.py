"""Hello World, This program is about building a fun story by 
asking users to choose some words that will be inserted in the middle of sentenses"""
print ("Hi! Welcome to Mab Libs!")
hero = raw_input ("Lets start by choosing the main character's name of your story:")
adjective_1 = raw_input ("Ok, now chose an adjective, let's say a positive one:")
adjective_2 = raw_input ("Now, a negative one:")
adjective_3 = raw_input ("And a third one, just for fun:")
verb_1 = raw_input ("You are now going to eneter a verb:")
verb_2 = raw_input ("A secound one:")
verb_3 = raw_input ("A third one:")
verb_4 = raw_input ("And a fourth one:")
noun_1 = raw_input ("Now, your are going to choose four nouns. Here comes the first one:")
noun_2 = raw_input ("The secound one:")
noun_3 = raw_input ("The third one:")
noun_4 = raw_input ("And the fourth one (this one is the most important;) just kidding, no pressure):") 
animal = raw_input ("Now, please choose an animal:")
food = raw_input ("Tell me what is your favourite food:")
fruit = raw_input ("What about your favourite fruit?")
number = raw_input ("Please enter a number:")
super_hero = raw_input ("Tell me Who is you favourite superhero:")
country = raw_input ("Choose a country:")
dessert = raw_input ("Tell me what is your favourite desert (after that we're done talking about food I promise)")
year = raw_input ("Last question: please enter a year of your choice:")
                 

#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."

print STORY % (adjective_1, hero, verb_1, adjective_2, noun_1, noun_2, animal,food, verb_2, noun_3, fruit, adjective_3, hero, verb_3, number, hero, super_hero, super_hero, hero, country, hero, dessert, hero, year, noun_4)
