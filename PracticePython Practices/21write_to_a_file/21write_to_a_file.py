'''
Exercise 21

Take the code from the How To Decode A Website exercise (if you didn’t 
do it or just want to play with some different code, use the code from t
he solution), and instead of printing the results to a screen, write the 
results to a txt file. In your code, just make up a name for the file 
you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved.
'''

import _17decode_a_web_page as article_obj
import os

obj = article_obj.Print_article_titles_NYTimes()
article_titles = obj.output_articles()

title = str(input("Name the title of the file: "))
title = title.replace(" ", "_")

current_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{current_dir}/{title}.txt", "w") as open_file:
    for i, titles in enumerate(article_titles):
        open_file.write(f"{i+1}. {titles}\n")

    
