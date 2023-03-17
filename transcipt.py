# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 17:08:27 2023

@author: kbhatnag
"""
#Step 1 you need to install youtube_transcript_api package
#pip install youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi
import os

def take_input():
    url_id = input("enter the youtube video id for which you want to extract transcript : ")
    return(url_id)

def destination_path():
    file_name = input("Enter the name by which you want to save the file : ")
    if not file_name:
        file_name = url_id
    return(file_name.split('.')[0]+".txt")

def generate_transcript(id):
    transcript = YouTubeTranscriptApi.get_transcript(id)
    script = ""
    count=0
    #print(transcript)
    for text in transcript:
        t = text["text"]
        count += 1
        if t != '[Music]':
            script += t + " "
        if count%20 == 0:
            script+= "["+str(text["start"])+"]"+"\n"
    return script, len(script.split())
url_id =take_input()
t_content,length = (generate_transcript(url_id))

save_file = input("Do you want to save the content in a file ? \n Type y to save : ")
if save_file =='y':
    fname = destination_path()
    print(fname)
    
    with open(os.path.join("transcript_data",fname) , 'w',encoding='utf-8') as file:
        file.write(t_content)
        file.close()
print(t_content)    