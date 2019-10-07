import os
import string
from collections import Counter
# Paths
resume_path = os.path.join(".", “Resources”, “resume.md”)
# Skills to match
REQUIRED_SKILLS = {“excel”, “python”, “mysql”, “statistics”}
DESIRED_SKILLS = {"r", "git", "html", "css", "leaflet", "modeling"}

def load_file(filepath):
   # Helper function to read a file and return the data.
   with open(filepath, "r") as resume_file_handler:
       resume_contents = resume_file_handler.read()
       resume_contents = resume_contents.lower()
       resume_tokens = resume_contents.split()
       return resume_tokens
# Grab the text for a Resume
word_list = load_file(resume_path)
# Create a set of unique words from the resume
resume = set()
# HINT: Single elements in a programming language are often referred to as tokens
for token in word_list:
   resume.add(token)
print('\nWORDS BEFORE MOVING PUNCTUATION')
print(resume)
# Remove Punctuation that were read as whole words
punctuation = set(string.punctuation)
# HINT: Attributes that are in resume that are not in punctuation (difference)
resume = resume - punctuation
print('\nWORDS AFTER MOVING PUNCTUATION')
print(resume)
# Calculate the Required Skills Match using Set Intersection
print('REQUIRED SKILLS')
print(resume & REQUIRED_SKILLS)
# Calculate the Desired Skills Match using Set Intersection
print('DESIRED SKILLS')
print(resume & DESIRED_SKILLS)
# Word Punctuation Cleaning
word_list = [word for word in word_list if word not in string.punctuation]
print('\nWORD LIST AFTER PUNCTUATION REMOVAL')
print(word_list)
# Character Punctuation Cleaning
word_list = [''.join(char for char in word if char not in string.punctuation) for word in word_list]
print('\nWORD LIST AFTER CHARACTER PUNCTUATION REMOVAL')
print(word_list)
# Clean Stop Words
stop_words = ["and", "with", "using", "##", "working", "in", "to"]
word_list = [word for word in word_list if word not in stop_words]
print('\nWORD LIST AFTER STOP WORDS')
print(word_list)
# Resume Word Count
# ==========================
# Initialize a dictionary with default values equal to zero
word_count = {}.fromkeys(word_list, 0)
# Loop through the word list and count each word.
for word in word_list:
   word_count[word] += 1
# print(word_count)
# Bonus using collections.Counter
word_counter = Counter(word_list)
# print(word_counter)
# Comparing both word count solutions
print(word_count == word_counter)
# Top 10 Words
print("Top 10 Words")
print("=============")
# Sort words by count and print the top 10
sorted_words = []
for word in sorted(word_count, key=word_count.get, reverse=True)[:10]:
   print(f"Token: {word:20} Count: {word_count[word]}")
