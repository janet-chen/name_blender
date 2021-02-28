import random

def name_blender(names): 
    assert(len(names) > 1), "there must be at least 2 names!"
    random.shuffle(names)

    combinedNames = ''
    # set first name as it's a special case (e.g. janet -> ja)
    combinedNames += splitFirstName(names[0])

    for name in names[1:]:
        splitName = splitSubsequentName(name)
        combinedNames += splitName
        # preserve the last vowel and rest of word for the last name
        if (name != names[-1]):
            combinedNames = last_vowel(combinedNames)
    print(combinedNames)

# returns the index of the first vowel in a word
# unless the word is the first name in the array, then it's the index of the second vowel     
def first_vowel(s, position):
    for index, char in enumerate(s):
        if (char in 'aeiouy'):
            if (position=='first' and index != 0):
                return index
            elif (position == 'sub'):
                return index
    raise Error('No vowel found')

# returns a string that's cut off after its last vowels
def last_vowel(combinedNames):
    indices = []
    for index, char in enumerate(combinedNames):
        if (char in 'aeiouy'):
            indices.append(index)
    indexLastVowel = indices[-1]
    return combinedNames[:indexLastVowel]
   
def splitFirstName(name):
    index = first_vowel(name, 'first')
    return name[:index]

def splitSubsequentName(name):
    index = first_vowel(name, 'sub')
    return name[index:]

    

# name_blender(['sam','amy','janet','jamie'])
# name_blender(['sam','amy','janet','jamie'])

# name_blender(['janet', 'sondra', 'deniz', 'thummim', 'jerry'])
# name_blender(['janet', 'sondra', 'deniz', 'thummim', 'jerry'])

name_blender(['sondra', 'josh'])
name_blender(['sondra', 'josh'])
name_blender(['sondra', 'josh'])

name_blender(['trent','hannah','kenny','nicole','rita','catherine','will','alison','mark','linnea','jayg','ruben','janet','mhiko','cathy','kaiya'])


name_blender(['nicole','hannah','linnea'])
name_blender(['nicole','hannah','linnea'])
name_blender(['nicole','hannah','linnea'])
