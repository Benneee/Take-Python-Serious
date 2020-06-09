print("Hey you! Welcome to the special quiz!!");
print("Try not to fail any of the questions :)");
print('You lose a point for every failed question');

print('Good luck!');

score = 0;
print('Scoreboard: ', str(score)+'/3');
while score < 3:
    que1 = 'Python is an interpreted language';
    print(que1);
    options = input('Enter a for true and b for false: ');
    if options == 'a':
        print("You're correct!")
        score +=1;
        print('Scoreboard: ', str(score)+'/3')
    else:
        print("Wrong choice");
        score -=1;
        print('Scoreboard: ', str(score)+'/3');
    
    print('=================');

    que2 = 'Python can be used for data science'
    print(que2);
    options = input('Enter a for true and b for false: ');
    if options == 'a':
        print("You're correct!")
        score +=1;
        print('Scoreboard: ', str(score)+'/3')
    else:
        print("Wrong choice");
        score -=1;
        print('Scoreboard: ', str(score)+'/3');
    
    print('=================');

    que3 = 'Only computer science graduates can learn to code'
    print(que3);
    options = input('Enter a for true and b for false: ');
    if options == 'b':
        print("You're correct!")
        score +=1;
        print('Scoreboard: ', str(score)+'/3')
    else:
        print("Wrong choice");
        score -=1;
        print('Scoreboard: ', str(score)+'/3');
    
    if score == 3:
        print('Congrats! top marks for you!!');
        exit();
    elif 3 > score > 0:
        print('Good job, your total score is: ', str(score)+'/3');
        exit()
    else:
        print('You can always try again!');
        exit();

exit();