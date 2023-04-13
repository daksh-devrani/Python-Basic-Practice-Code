"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts her
f=open('question.txt','r')
question=[line.strip() for line in f.readlines()]
f.close()
score=0
max=len(question)
for line in question:
    a=line.split('=')
    b=input(f'{a[0]}=')
    if b == a[1]:
        score+=1
f=open('result.txt','w')
f.write(f'Your final score {score}/{max}')
f.close()




