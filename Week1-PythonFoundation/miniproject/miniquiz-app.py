# miniquiz-app.py
import streamlit as st

#  Question Class 
class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer

# Quiz Class
class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def run(self):
        st.title("Mini Quiz App")
        st.write("Answer the following questions:")

        # Store user answers in a list
        user_answers = []

        # Simple loop over questions
        i = 0
        while i < len(self.questions):
            q = self.questions[i]
            st.write("Question " + str(i + 1) + ": " + q.prompt)
            
            # Let user select answer
            choice = st.radio("Choose an option:", q.options, key=str(i))
            user_answers.append(choice)
            i = i + 1

        # Submit button
        if st.button("Submit Quiz"):
            score = 0
            st.write("---")
            st.write("Quiz Results")
            j = 0
            while j < len(self.questions):
                st.write("Question " + str(j + 1) + ": " + self.questions[j].prompt)
                st.write("Your answer: " + user_answers[j])
                st.write("Correct answer: " + self.questions[j].answer)
                if self.questions[j].check_answer(user_answers[j]):
                    score = score + 1
                st.write("---")
                j = j + 1
            st.write("Your final score is: " + str(score) + " / " + str(len(self.questions)))

        # Retake button
        if st.button("Retake Quiz"):
            st.experimental_rerun()

#  Questions:
q1 = Question("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], "Paris")
q2 = Question("2 + 2 equals?", ["3", "4", "5", "6"], "4")
q3 = Question("What color is the sky?", ["Blue", "Green", "Red", "Yellow"], "Blue")

#  Run Quiz 
quiz = Quiz([q1, q2, q3])
quiz.run()
