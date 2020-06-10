from sys import argv;

script, user_name = argv;

prompt = '> ';

print(f"Hi {user_name}, I'm the {script} script");

print("I'd like to know you better");

print(f"Do you think I like rice as much as {user_name} does?");
likes = input(prompt);

print(f"Where does {user_name} live?");
lives = input(prompt);

print(f"What type of mobile phone do you use?");
phone = input(prompt);

print(f""" 
Alright, so you said {likes} about liking rice like me. You live
in {lives}. I think I know where that is and you use a {phone} phone, Nice! 
""")

