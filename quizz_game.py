quiz=[
    {
    'question': 'What do the Marauders call Remus Lupin?',
    'options':['A.Padfoot', 'B.Wolfie', 'C.Prongs', 'D.Moony'],
    'answer':'D'
    },
    {
    'question': 'Which one is not an Unforgivable Curse?',
    'options':['A.Crucio', 'B.Sectumsempra', 'C.Imperio', 'D.Avada Kedavra'],
    'answer':'B'
    },
    {
    'question': 'Who opened the Chamber of Secrets?',
    'options':['A.Rubeus Hagrid', 'B.Draco Malfoy', 'C.Ginny Weasley', 'D.Lucius Malfoy'],
    'answer':'C'
    },
    {
    'question': 'What house was Merlin in?',
    'options':['A.Slytherin', 'B.Gryffindor', 'C.Hufflepuff', 'D.Ravenclaw'],
    'answer':'A'
    }
]

def questions(quiz):
    score=0
    for keys in quiz:
        print(keys['question'])
        for option in keys['options']:
            print(option)
        while True:
            try:
                answer = input('Select your answer (A, B, C, D): ').upper()
                
                # Check if the answer is valid
                if answer not in ['A', 'B', 'C', 'D']:
                    raise ValueError("Invalid choice")  # Trigger exception if invalid
                
                # If valid, break out of the loop
                break
            except ValueError:
                print("Invalid input. Please enter A, B, C, or D.")

        if answer==keys['answer']:
            score+=1
            print('Correct!\n')
        else:
            print('Wrong!The correct answer was',keys['answer']+ '\n')
    print(f'Your final score is {score} out of {len(quiz)}')
        
        
questions(quiz)
