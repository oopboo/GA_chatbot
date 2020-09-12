# Project: General Assembly Chatbot
## History of Chatbots

The history of chatbots often starts around 1966 with one of the first chatbots created, [ELIZA](#http://psych.fullerton.edu/mbirnbaum/psych101/Eliza.htm)(http://psych.fullerton.edu/mbirnbaum/psych101/Eliza.htm). She was created by Joseph Weizenbaum to act as a Rogerian psychotherapist. ELIZA was able to fool people into believing that she was real by using pattern matching and echoing responses by using key words and phrases from user input. Chatbots have advanced significantly since 1966. They can be categorized into various buckets: rule/menu-based, natural language understanding (NLU), contextual, and personalized. **Rule/Menu-based** chatbots automate basic functions and respond to specific triggers, like buttons on a menu. These chatbots can be seen in automated answering systems, fast food ordering systems, etc. **Natural language understanding (NLU)** chatbots can interact at a slightly higher level than rule-based chatbots. These are able to recognize the intentions of the user in order to give a better response. These chatbots understand words and phrases, then response with the best corresponding script. However, these chatbots do not have advanced conversational skills. **Contextual** chatbot can handle more advanced conversations. These are less structured than NLU chatbots, but they still rely on programmed scripts to respond to the user. Lastly, **personalized** chatbots draw on past conversations and interactions with users. These personalized chatbots are the direction that the industry is heading toward. More information about these categories and chatbot can be found [here](#https://chatbotsmagazine.com/are-all-conversational-user-experiences-equal-f8876f8bf592)(https://chatbotsmagazine.com/are-all-conversational-user-experiences-equal-f8876f8bf592).

---

## Problem Statement

With the world becoming more technologically advanced and more people staying home due to current world events, chatbots may provide companies with much needed additional support for customer interactions. So many people, especially now, are looking to enhance their skills or change careers. Chatbots can help field basic questions from potential clients in order to ease the workload and support company employees. How well can a trained Chatterbot chatbot field questions regarding programming at General Assembly?

[Chatterbot](#https://chatterbot.readthedocs.io/en/stable/)(https://chatterbot.readthedocs.io/en/stable/) is language independent meaning it can be trained on practically any language. Chatterbot already has pre-made corpora in language including, but not limited to English, Korean, Hebrew, Turkish, Japanese, and so much more. This chatbot falls somewhere within the contextual chatbot category. It is able to "learn" from previous interactions and continue to learn and improve. It also uses preprogrammed scripted conversations to train on.

---

## Scraping Data
### Web Scraping General Assembly

To get the necessary information to train the chatbot, a web scraper was build to scrape the General assembly sites. The websites for each of the 32 cities and the sites for each of the 15 courses offered by General Assembly were scraped for relevant information. 

---

### EDA and Tableau

Exploratory data analysis (EDA) was performed on this data. Through this EDA, it can be seen that email is the best form of contact to General Assembly since every city has one. Contacting offices by phone (during office hours) would be second best, while going to the office, especially during this global pandemic, would have the lowest success rate. The countries with the most General Assembly offices are the US, with over 20 programs, followed distantly by Australia and the UK. Both Canada and Singapore only have one General Assembly location.

To further visualize this data, [Tableau Public](#https://public.tableau.com/views/GA_locations/Dashboard1?:language=en&:display_count=y&:origin=viz_share_link)(https://public.tableau.com/views/GA_locations/Dashboard1?:language=en&:display_count=y&:origin=viz_share_link) was used to map each of the campus locations on a map. Upon hovering over a specific city, viewers can see the location, email address, phone number, and programs offered at each location.

---

## Formatting the Data: .txt and .yml

Chatterbot is very specific about the type of the programming language it uses to train the chatbot as well as the format of the text file. YAML Ain't Markup Language (YAML) is a language that was made to be easily readable by humans. The easiest route to transforming the data correctly was to write the scraped data to a text file (.txt), then transform it again to a YAML file (.yml). This ensured that the quotation marks used in Python to denote a ```string``` would be removed.

---

## Training and Interacting with Chatterbot

Once the custom YAML files were formatted, they were placed in the custom corpus folder within the Chatterbot download locally. This step is critical in order to use custom corpora to train Chatterbot. Once the YAML files was relocated, they were called in for training through the ```ChatterBotCorpusTrainer```. To ensure that the Chatterbot was indeed working, interacting with the chatbot and asking it questions relevant to General Assembly was vital. 

---

## Flask Deployment

After ensuring that the Chatterbot worked, deploying the app on Flask was the next step. Flask deployment can be tricky without the proper tools for formatting HTML and CSS. Fortunately, this [github page](#https://github.com/chamkank/flask-chatterbot)(https://github.com/chamkank/flask-chatterbot) had a basic HTML code that was adapted for this project. A demo of this trained Chatterbot project can be found [here](#https://youtu.be/NmjOmBH0bLg) (https://youtu.be/NmjOmBH0bLg).

---

## Challenges and Future Steps

Although the Chatterbot works well and it answers questions about General Assembly and programming, there still needs to be some additional tweaking and training to improve accuracy of the responses. The biggest and the most time consuming challenge was reformatting the scraped data to YAML to then be used accurately for training. The second hurdle was understanding that Chatterbot although very helpful is fairly limited in its responses. It needs a variety of input and training to be able to answer the numerous types of questions from users. However, Chatterbot's programming allows it to store conversations in order to continue to "learn" from those interactions.

Future steps for this project would include additional train and refinement of scripts from General Assembly regarding their programming. Although this project is deployed on Flask, it can only be hosted locally. Future actions to implement the program on Heroku or Django may be beneficial. Chatterbot has a lot of great qualities and could be a powerful tool used to interact with future General Assembly students to field frequently asked questions about the programs.# GA_chatbot
