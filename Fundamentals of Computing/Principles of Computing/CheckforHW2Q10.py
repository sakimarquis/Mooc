# Working Checker for Question 10 of the Homework
# This homework assignment was quite poorly explained but after several hours I was able to build this
# 
# Copy/Paste the incorrect function into the function bad_format()
# make sure you change the parameter to the name the used as sometimes it isn't t

TEST_CASES = [0]*10

# generate a list of 10 items at the intervals of 599 * counter
 
def bad_format(t):
    pass

def good_format(t):
    minutes = str(t // 600)
    secs = str(t % 600)
    while len(secs) < 3:
        secs = "0" + secs
    return minutes + ":" + secs[:-1] + "." + secs[-1]

counter = 0

mistake_found = False

def Checker():
    for idx, num in enumerate(list(TEST_CASES)):
        TEST_CASES[idx] = idx * 599
    mistake_found = False
    while not mistake_found:
        for item_idx, item in enumerate(TEST_CASES):
            bad_result = bad_format(item)
            good_result = good_format(item)
            for str_idx in range(6):
                if bad_result[str_idx] != good_result[str_idx]:
                    mistake_found = True
            if mistake_found:
                print str(TEST_CASES) + '\n'
                return 'Mistake at list index ' + str(item_idx) + '\n' + 'Returned ' + bad_result + '\n' + 'Expected ' + good_result            
        for idx, num in enumerate(list(TEST_CASES)): 
            TEST_CASES[idx] = num + 1
 
print Checker()
