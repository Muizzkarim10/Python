text = """
Oh-oh, oh-oh
Yeah
Uh, I say, uh
I don't need no molly to be savage, uh
When I'm on that molly, I feel savage, uh, uh
She the definition of a bad bitch
Stole her, I'm the definition of a bandit, uh, ayy
I don't need no molly to be savage, uh, ayy
But when I'm on the molly, I feel savage
Ayy, my girl the definition of a bad bitch
Stole her heart, I'm the definition of a bandit
Put the Percs down and picked up the jiggas, jiggas, jiggas
Tommy in the fucking Tommy Hilfiger, 'figer, 'figer
That Tommy hit a nigga, Tommy Hilfiger, fuck niggas
I'm nice, when I'm high off the pills, I'ma fuck with her
I don't smoke skunk, but tonight I'm getting stuck, nigga
Pour the codeine up and put some molly in the cup with it
I know she a freak, uh-huh, she gon' fuck with it
She my velcro, uh-huh, guess I'm stuck with her
I dive in it like a sailor, I love to nail her
Addicted to her paraphernalia, I had to tell her
I see it like a fortune teller
Your ex-nigga did good, I could do better
Bad bitch from the woods, I think she a hunter
She a killer and an eater, she a Jeffery Dahmer
I can tell when she in her feelings, I can read her like a book
No TEC, no Beretta, FN on me, am I understood?
Yeah, yeah, yeah
I don't need no molly to be savage, uh
When I'm on that molly, I feel savage, uh, uh
She the definition of a bad bitch
Stole her, I'm the definition of a bandit, uh, ayy
I don't need no molly to be savage, uh, ayy
But when I'm on the molly, I feel savage
Ayy, my girl the definition of a bad bitch
Stole her heart, I'm the definition of a bandit
My brother point her out and she a bad bitch, I'm on her
Must ain't heard that I'm a savage, once I get a bitch, I own her
I see she got swag, I got cash so I want her
See this four-five in my pants, put on your ass, push up on bruh
Shawty, she a rider with that glizzy on her (Glizzy on her)
And shawty, I'ma dada with no semi on me (Semi on me)
If we got a problem, we get rid of homie (Yeah)
Put 20 thousand in your pocket, we gon' get the money (Yeah)
I'm the definition of a bandit (Honest)
Took your heart from out his hands
And still ain't saying shit (On my mama)
Some new killers in my circle you done ran with it
Like this dirty .38, this bitch damage
Popping wheelies, 4K Trey, call when you land with it (Pop, pop, pop)
I let you drive and slide with my bros where they be laying with it
I work this bitch, I open up a can with it
Like fuck the stove, I make it jump without my hand in it
I don't need no molly to be savage, uh
When I'm on that molly, I feel savage, uh, uh
She the definition of a bad bitch
Stole her, I'm the definition of a bandit, uh, ayy
I don't need no molly to be savage, uh, ayy
But when I'm on the molly, I feel savage
Ayy, my girl the definition of a bad bitch
Stole her heart, I'm the definition of a bandit
"""

word_count = {}

for word in text.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)