import random
# Define the states and UTs along with their capitals
states = {
    'Andhra Pradesh': 'Hyderabad',
    'Arunachal Pradesh': 'Itanagar',
    'Assam': 'Dispur',
    'Bihar': 'Patna',
    'Chhattisgarh': 'Raipur',
    'Goa': 'Panaji',
    'Gujarat': 'Gandhinagar',
    'Haryana': 'Chandigarh',
    'Himachal Pradesh': 'Shimla',
    'Jharkhand': 'Ranchi',
    'Karnataka': 'Bengaluru',
    'Kerala': 'Thiruvananthapuram',
    'Madhya Pradesh': 'Bhopal',
    'Maharashtra': 'Mumbai',
    'Manipur': 'Imphal',
    'Meghalaya': 'Shillong',
    'Mizoram': 'Aizawl',
    'Nagaland': 'Kohima',
    'Odisha': 'Bhubaneswar',
    'Punjab': 'Chandigarh',
    'Rajasthan': 'Jaipur',
    'Sikkim': 'Gangtok',
    'Tamil Nadu': 'Chennai',
    'Telangana': 'Hyderabad',
    'Tripura': 'Agartala',
    'Uttar Pradesh': 'Lucknow',
    'Uttarakhand': 'Dehradun',
    'West Bengal': 'Kolkata'
}

uts = {
    'Andaman and Nicobar Islands': 'NA',
    'Chandigarh': 'Chandigarh',
    'Dadra and Nagar Haveli and Daman and Diu': 'NA',
    'Lakshadweep': 'NA',
    'Delhi': 'New Delhi',
    'Puducherry': 'Puducherry',
    'Jammu and Kashmir': 'Srinagar (Summer), Jammu (Winter)',
    'Ladakh': 'Leh'
}

# Define a function to generate a quiz with 36 random questions
def generate_quiz(quiz_num):
    # Shuffle the order of the states and UTs
    shuffled_states = list(states.items())
    random.shuffle(shuffled_states)
    shuffled_uts = list(uts.items())
    random.shuffle(shuffled_uts)
    
    # Choose 28 random states and 8 random UTs
    quiz_questions = random.sample(shuffled_states, 28) + random.sample(shuffled_uts, 8)
    
    # Shuffle the order of the questions
    random.shuffle(quiz_questions)
    
    # Create the quiz and answer key files
    quiz_filename = f"quiz{quiz_num}.txt"
    answer_filename = f"ans{quiz_num}.txt"
    
    # Write the quiz file header
    with open(quiz_filename, 'w') as f:
        f.write(f"Indian states and UTs and their capitals\n\nName:\nDate:\n\n")
    
    # Write the quiz questions and answers
    with open(quiz_filename, 'a') as f, open(answer_filename, 'w') as ans_f:
        for i, (state, capital) in enumerate(quiz_questions):
            # Write the question
            f.write(f"{i+1}. What is the capital of {state}?\n")
            
            # Choose the correct answer and three random wrong
            options = [capital] + [c for s, c in random.sample(list(states.items()) + list(uts.items()), 3)]
            random.shuffle(options)

            # Write the answer options
            for j, option in enumerate(options):
                f.write(f"   {'ABCD'[j]}. {option}\n")

            # Write the correct answer to the answer key file
            ans_f.write(f"{i+1}. {'ABCD'[options.index(capital)]}\n")

            # Write a blank line between questions
            f.write("\n")

    print(f"Quiz {quiz_num} generated successfully.")

# Generate 42 unique quizzes
for i in range(1, 43):
    generate_quiz(i)