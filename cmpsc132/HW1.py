# HW1
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

# COLLABORATION STATEMENT:
    # used the homework 1 orientation video and lecture videos VERY HELPFUL FOR QUESTION 10 AND 11
    # planned how to solve has_hoagie() and is_identical() with Ishaan Narang using pictures

def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #- YOUR CODE STARTS HERE
    hailList =[]
    while(num>1):
        hailList.append(int(num))
        if(num % 2 == 0):                                   # num even
            num /= 2
        else:                                               # num odd
            num = (3 * num) + 1 
    hailList.append(1)                                      # add 1 to the end as the loop doesnt include it
    return hailList


def to_decimal(oct_num):
    """
        >>> to_decimal(237) 
        159
        >>> to_decimal(35) 
        29
        >>> to_decimal(600) 
        384
        >>> to_decimal(420) 
        272
    """
    #- YOUR CODE STARTS HERE
    baseTen = 0
    exponent = 0
    while(oct_num > 0):
        lastDigit = oct_num % 10 
        baseTen += (8 ** exponent) * lastDigit 
        exponent += 1
        oct_num //= 10
    return baseTen



def has_hoagie(num):
    """
        >>> has_hoagie(737) 
        True
        >>> has_hoagie(35) 
        False
        >>> has_hoagie(-6060) 
        True
        >>> has_hoagie(-111) 
        True
        >>> has_hoagie(6945) 
        False
    """
    #- YOUR CODE STARTS HERE
    num = abs(num)
    while(num//100 > 0):                                # repeat until num is 2 digits this also takes care of nums under 3 digits
        section = num % 1000                            # save the last 3 digits
        if(section // 100 == section % 10):             # check if the hundereds = ones 
            return True
        num //= 10                                      # remove last digit
    return False  


def is_identical(num_1, num_2):
    """
        >>> is_identical(51111315, 51315)
        True
        >>> is_identical(7006600, 7706000)
        True
        >>> is_identical(135, 765) 
        False
        >>> is_identical(2023, 20) 
        False
    """
    #- YOUR CODE STARTS HERE
    newNum_1 = 0
    exp_1 = 0
    newNum_2 = 0
    exp_2 = 0
    while(num_1 > 0):
        window = num_1 % 100                                # take last 2 digits
        if(window // 10 != window%10):                      # add the last digit to the simplified newNum(1/2) if the second to last digit doesnt equal the last digit
            newNum_1 += (10 ** exp_1) * (window%10)
            exp_1 += 1
        num_1 //= 10                                        # move on to the next set of digits
                                                                    
    while(num_2 > 0):                                       # same thing but with number 2
        window = num_2 % 100
        if(window // 10 != window%10):
            newNum_2 += (10 ** exp_2) * (window%10)
            exp_2 += 1
        num_2 //= 10

    return newNum_1 == newNum_2

            


def frequency(txt):
    '''
        >>> frequency('mama')
        {'m': 2, 'a': 2}
        >>> answer = frequency('We ARE Penn State!!!')
        >>> answer
        {'w': 1, 'e': 4, 'a': 2, 'r': 1, 'p': 1, 'n': 2, 's': 1, 't': 2}
        >>> frequency('One who IS being Trained')
        {'o': 2, 'n': 3, 'e': 3, 'w': 1, 'h': 1, 'i': 3, 's': 1, 'b': 1, 'g': 1, 't': 1, 'r': 1, 'a': 1, 'd': 1}
    '''
    # - YOUR CODE STARTS HERE -
    chars = []
    freqDict = {}
    for char in txt:                                        #put all alphabets in a list as lowercase letters
        if(char.isalpha()):
            chars.append(char.lower())
    for item in chars:                                      #put the alphabets in a dict if its not in it, if it is increment the count/value
        if item not in freqDict:
            freqDict[item] = 1
        else:
            freqDict[item] += 1
    return freqDict

    






def invert(d):
    """
        >>> invert({'one':1, 'two':2,  'three':3, 'four':4})
        {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        >>> invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3})
        {3: 'three'}
        >>> invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'}) 
        {'Sara': '123-456-78', 'sara': '258715'}
    """
    # - YOUR CODE STARTS HERE -
    dvals = list(d.values())                                #get the list of the values and keys of dict d in separate lists
    dkeys = list(d.keys())
    invertDict = {}
    for i in range (len(d)):                                #use the dvalue element as a key for the inverted dict only if the count 1 meaning unique, inverted value would be the corresponding key in dict d
        if dvals.count(dvals[i]) == 1:
            invertDict[dvals[i]] = dkeys[i]
    return invertDict
    
    




def employee_update(d, bonus, year):
    """
        >>> records = {2020:{"John":["Managing Director","Full-time",65000],"Sally":["HR Director","Full-time",60000],"Max":["Sales Associate","Part-time",20000]}, 2021:{"John":["Managing Director","Full-time",70000],"Sally":["HR Director","Full-time",65000],"Max":["Sales Associate","Part-time",25000]}}
        >>> employee_update(records,7500,2022)
        {2020: {'John': ['Managing Director', 'Full-time', 65000], 'Sally': ['HR Director', 'Full-time', 60000], 'Max': ['Sales Associate', 'Part-time', 20000]}, 2021: {'John': ['Managing Director', 'Full-time', 70000], 'Sally': ['HR Director', 'Full-time', 65000], 'Max': ['Sales Associate', 'Part-time', 25000]}, 2022: {'John': ['Managing Director', 'Full-time', 77500], 'Sally': ['HR Director', 'Full-time', 72500], 'Max': ['Sales Associate', 'Part-time', 32500]}}
    """
    # - YOUR CODE STARTS HERE -
    with_bonus = {}                                         #new dict for the new year
    for employee, employeeInfo in d[year-1].items():        #iterate through the latest year's people and their info and save their name and info list
        newInfo = employeeInfo.copy()                       #create a copy of the list so the reference is not tainted
        newInfo[len(newInfo)-1] += bonus                    #increase the salary by the bonus
        with_bonus[employee] = newInfo                      #add updated person with bonus to the new dict
    d[year] = with_bonus                                    #add to original dict with the new year as the key
    return d



def overloaded_add(d, key, value):
    """
        Adds the key value pair to the dictionary. If the key is already in the dictionary, the value is made a list and the new value is appended to it.
        >>> d = {"Alice": "Engineer"}
        >>> overloaded_add(d, "Bob", "Manager")
        >>> overloaded_add(d, "Alice", "Sales")
        >>> d == {"Alice": ["Engineer", "Sales"], "Bob": "Manager"}
        True
    """
    #- YOUR CODE STARTS HERE
    if key in d:                                            #check if the key (person) is in the dict
        if isinstance(d[key], list):                        #if their value is a list add the new value (profession) to their list, if not a list make one and add their current value and new value to it

            d[key].append(value)
        else:
            infoList = []
            infoList.append(d[key])
            infoList.append(value)
            d[key] = infoList
    else:
        d[key] = value                                      #if its not in the dict add it


def by_department(d):
    """
        >>> employees = {
        ...    1: {'name': 'John Doe', 'position': 'Manager', 'department': 'Sales'},
        ...    2: {'position': 'Budget Advisor', 'name': 'Sara Miller', 'department': 'Finance'},
        ...    3: {'name': 'Jane Smith', 'position': 'Engineer', 'department': 'Engineering'},
        ...    4: {'name': 'Bob Johnson', 'department': 'Finance', 'position': 'Analyst'},
        ...    5: {'position': 'Senior Developer', 'department': 'Engineering', 'name': 'Clark Wayne'}
        ...    }

        >>> by_department(employees)
        {'Sales': [{'emp_id': 1, 'name': 'John Doe', 'position': 'Manager'}], 'Finance': [{'emp_id': 2, 'name': 'Sara Miller', 'position': 'Budget Advisor'}, {'emp_id': 4, 'name': 'Bob Johnson', 'position': 'Analyst'}], 'Engineering': [{'emp_id': 3, 'name': 'Jane Smith', 'position': 'Engineer'}, {'emp_id': 5, 'name': 'Clark Wayne', 'position': 'Senior Developer'}]}
    """
    #- YOUR CODE STARTS HERE
    deptDict = {}                                           # make a dict for departments 
    for id in d:                                            # iterate through the d dict and save the id of the person
        deptartment = d[id]['department']                   # obtain the department of the current person
        if deptartment not in deptDict:                     # add the department to the deptartment dict if its not already there and give it a list value
            deptDict[deptartment] = []
        employeeInfo = {}                                   # create a dict with the info of the current person
        employeeInfo['emp_id'] = id                         # add id of the person to the info dict with the id (key) from d 
        employeeInfo['name'] = d[id]['name']                # obtain their name from d and add to info dict 
        employeeInfo['position'] = d[id]['position']        # same but position ^
        deptDict[deptartment].append(employeeInfo)          # add info dict to the persons dept list
    return deptDict


def successors(file_name):
    """
        >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
        >>> returnedDict = successors('items.txt')
        >>> expected == returnedDict
        True
        >>> returnedDict['.']
        ['We', 'Maybe']
        >>> returnedDict['to']
        ['learn', 'have', 'make']
        >>> returnedDict['fun']
        ['.']
        >>> returnedDict[',']
        ['eat']
    """
    with open(file_name, 'r') as f: 
        contents = f.read()  # You might change .read() for .readlines() if it suits your implementation better 
    #- YOUR CODE STARTS HERE
    contents = ''.join(contents.split("\n"))                # remove \n and save as a long string
    contentLst = list(contents)                             # make it a list so any alterations will be saved
    for i in range(len(contentLst)):                        # add space before and after characters that aren't alphabets or numbers i.e punctuation and special charecters
        if not contentLst[i].isalnum():
            contentLst[i] = ' ' + contentLst[i] + ' '
            print(contentLst[i])
    words = (''.join(contentLst)).split()                   # create a list of words and punctuation 
    sDict = {}                                              # new dict for the words and their successors
    sDict['.'] = [words[0]]                                 # words[0] is a successor of . because its the first word in the text file 

    for index in range(len(words)-1):                       # add an element as a key to sDict if it isnt already then add the next element to the sDict value for the element if its unique (stop len-1 to avoid index out of range)
        if words[index] not in sDict:
            sDict[words[index]] = []
        if words[index+1] not in sDict[words[index]]:
            sDict[words[index]].append(words[index+1]) 
    
    return sDict




def addToTrie(trie, word):
    """
        The following dictionary represents the trie of the words "A", "I", "Apple":
            {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}}}
       
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> addToTrie(trie_dict, 'art')
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}}
        >>> addToTrie(trie_dict, 'moon') 
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}, 'm': {'o': {'o': {'n': {'word': True}}}}}
    """
    
    node = trie                                             # pointer points to trie
    for char in word:                                       # go through each letter. If letter is not in the current pointer, add it. if it is in it point to the dict value
        if char not in node:
            node[char] = {}
        node = node[char]
    node['word'] = True                                     # add 'word':True to the end
    



def createDictionaryTrie(file_name):
    """        
        >>> trie = createDictionaryTrie("words.txt")
        >>> trie == {'b': {'a': {'l': {'l': {'word': True}}, 't': {'s': {'word': True}}}, 'i': {'r': {'d': {'word': True}},\
                     'n': {'word': True}}, 'o': {'y': {'word': True}}}, 't': {'o': {'y': {'s': {'word': True}}},\
                     'r': {'e': {'a': {'t': {'word': True}}, 'e': {'word': True}}}}}
        True
    """
    with open(file_name, 'r') as f: 
        contents = f.read()  # You might change .read() for .readlines() if it suits your implementation better 
    #- YOUR CODE STARTS HERE
    contents = contents.split('\n')                         # make a list of the words without the \n
    trie = {}                                               # create the dict that will become the trie
    for word in contents:                                   # run addToTrie for each word in the list
        addToTrie(trie, word.lower())
    return trie                                             # return the completed trie



def wordExists(trie, word):
    """
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> wordExists(trie_dict, 'armor')
        False
        >>> wordExists(trie_dict, 'apple')
        True
        >>> wordExists(trie_dict, 'apples')
        False
        >>> wordExists(trie_dict, 'a')
        True
        >>> wordExists(trie_dict, 'as')
        False
        >>> wordExists(trie_dict, 'tt')
        False
    """
    #- YOUR CODE STARTS HERE
    node = trie                                             # same logic for addToTrie but when the letter is not in pointer it returns false. Only returns true if the last node has the key:value 'word':True
    for char in word:
        if char not in node:
            return False
        node = node[char]
    return node['word']

def run_tests():
    import doctest
    # Run start tests in all docstrings
    doctest.testmod(verbose=True)
    
    
    # Run start tests per function - Uncomment the next line to run doctest by function. Replace rectangle with the name of the function you want to test
    # doctest.run_docstring_examples(wordExists, globals(), name='HW1',verbose=False)

if __name__ == "__main__":
    run_tests()
