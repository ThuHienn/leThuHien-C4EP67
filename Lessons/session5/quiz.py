import random
quizzes = [
# quiz = {
    {
    'question': 'Con nhện có mấy chân?',
    'choices': [
        '2 chân',
        '4 chân',
        '6 chân',
        '8 chân'
    ],
    'right_answer': 3
    },
    {
    'question': 'Con chó có mấy chân?',
    'choices': [
        '2 chân',
        '4 chân',
        '6 chân',
        '8 chân'
    ],
    'right_answer': 1  
    },
    {
    'question': 'Con vịt có mấy chân?',
    'choices': [
        '2 chân',
        '4 chân',
        '6 chân',
        '8 chân'
    ],
    'right_answer': 0  
    }
]
# for i in range(len(quiz['choices']))
dung = 0
random.shuffle(quizzes)
# for j in range(len(quizzes)): dàiiiii
#     print(quizzes[j]['question'])
#     choices = (quizzes[j]['choices'])
for quiz in quizzes: #quiz['question'] == quizzes[i]['question']
    print(quiz['question'])
    choices = quiz['choices']
    for i in range(len(choices)):
        # print(str(i) + '.' +choices[1]) mệt
        print(f'{i+1}. {choices[i]}') #string format
    user_choice = int(input('trả lời đê!!')) - 1
    if user_choice == quiz['right_answer']:
        print('bạn giỏi thật!!')
        dung += 1
    else:
        print('bạn sai mất rồi')
print(f'Kết quả: {round(dung/len(quizzes)*100,2)}%')