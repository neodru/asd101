#Project: Mad Lib Generator
adj1 =input ("Enter an adjective: ").lower()
game = input ("Enter the name of an outdoor game: ")
adj2 = input ("Enter another adjective: ").lower()
friend =  input ("Enter name of a friend: ").captilize()
verb = input ("Enter a verb ending in 'ing: ").lower()
adj3 = input("Enter a third adjective: ").lower()

#This is the Mad Lib Story
story = (f"""

It was a {adj1} summer day at the beach.
My friends and I were in the water playing {game}.
As a {adj2} wave came closer, my friend, {friend} yelled,
'Look! there's a jellyfish {verb}!
As we got closer , we saw that the jellyfish was indeed {verb}!
{friend} ran out of the water and onto the sand.
{friend} was afraid of {verb} jellyfish.
The rest of us stayed in the water playing {game} because {verb} jellyfish are {adj3}.""")

print(story)
