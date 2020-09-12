# Code adapted from global lesson: Flask
# Code adapted from https://github.com/chamkank/flask-chatterbot
# Code adapted from https://medium.com/datadriveninvestor/build-your-personal-chatbot-with-flask-6080d1cf1223
from flask import Flask, Response, request, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_most_frequent_response

app = Flask(__name__)

#Instantiate
chatbot = ChatBot(name = 'GA Bot', 
                  logic_adapters = [
                      {
                        "import_path": "chatterbot.logic.BestMatch",
                        "statement_comparison_function": "chatterbot.comparisons.JaccardSimilarity",
                        "default_response": "Sorry, I am unsure of the answer. For more information visit: generalassemb.ly",
                        "maximum_similarity_threshold": 0.95
                      }   
                  ],
                  preprocessors = ['chatterbot.preprocessors.clean_whitespace'],
                  storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
                  database_uri = 'sqlite:///database.sqlite3')

#Train
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english.ai')
trainer.train('chatterbot.corpus.english.botprofile')
trainer.train('chatterbot.corpus.english.computers')
trainer.train('chatterbot.corpus.english.conversations')
trainer.train('chatterbot.corpus.english.greetings')
trainer.train('chatterbot.corpus.custom.ga_info')
trainer.train('chatterbot.corpus.custom.ga_course_info')

list_trainer = ListTrainer(chatbot)
basic_convo = [
    'Hi',
    'Hello, how can I help you?',
    'What is General Assembly?',
    'Since 2011, General Assembly has transformed tens of thousands of careers through pioneering, experiential education in today’s most in-demand skills.',
    'What classes do you offer?',
    'We offer programs in web development, data science and analysis, user experience design, digital marketing, product management, and more.',
    'Are there part-time classes?',
    'Yes! Students can choose from a range of formats and modalities to help them best achieve their goals, including full-time, part-time, and short-form options — on campus, and online.',
    'Thank you',
    'No problem!',
    'Thank you',
    "You're welcome!",
    'Thank you!',
    'Any time!',
    'Thank you',
    "You're welcome",
    'Thanks',
    "You're welcome!"
]
list_trainer.train(basic_convo)


#Route 1
@app.route('/')
def home():
    return render_template('index.html')


# Make sure app route matches the ACTION in html form 
@app.route('/get')
def ga_chatbot_response():
    userText = request.args.get('msg') 
    while True:
        response = chatbot.get_response(userText)
        return str(response)
    


#Conditional statement to run the program server  in the terminal
if __name__ == '__main__': #if 'python chatbot_app.py' runs in in terminal
    app.run(debug=True)
