wordFilter = set()
# file = open('/home/tuzhenyu/github/python_project/smallProgramEveryDay/program011/words.txt','r')
file = open('D://tuzhenyu/GitHub/python_project/smallProgramEveryDay/program011/words.txt','r')
for word in file.readlines():
    wordFilter.add(word.rstrip('\n'))
wordInput = input()
if wordInput in wordFilter:
    print('Freedom')
else:
    print('Human Rights')
