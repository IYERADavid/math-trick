import urllib2
import json

url = "https://questions.aloc.ng/api/q/7?subject=chemistry"


json_obj = urllib2.urlopen(url)
data = json.load(json_obj)

num =0
score =0
for item in data[u'data']:
    num +=1
    print str(num)+')',item[u'question']
    print ' a)'+item[u'option'][u'a']+'.\n b)'+item[u'option'][u'b']+'.\n c)'+item[u'option'][u'c']+'.\n d)'+item[u'option'][u'd']+'.'

    user_answer = raw_input('enter your choice:')

    if user_answer ==item[u'answer']:
        print 'correct'
        score +=1
    else:
        print 'wrong'
        print 'correct answer is '+item[u'answer']
print 'your total marks are '+ str(score)+'/'+ str(num)        