print 'Please think of a number between 0 and 100!'
low = 0
high = 100
while 1:
    ans = (high + low) / 2
    print ('Is your secret number ' + str(ans) + '?')
    crt = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. > ")
    if crt == 'h':
        high = ans
    elif crt == 'l':
        low = ans
    elif crt == 'c':
        print ('Game over. Your secret number was: ' + str(ans))
        break
    else:
        print 'Sorry, I did not understand your input.'