# Import necessary libraries for text preprocessing
import string
import re
from textblob import TextBlob # A library used for text analysis and processing
from bs4 import BeautifulSoup

# %% 1. Removing extra spaces in texts
text1 = "Hello,    World!      2025"

# text.split() creates a list: ['Hello,', 'World!', '2025']
# " ".join() combines them back with a single space
cleaned_text1 = " ".join(text1.split())
print("1. Cleaned Spaces:", cleaned_text1)


# %% 2. Converting text to lowercase
text2 = "Hello, World! 2025"
cleaned_text2 = text2.lower()
print("2. Lowercase Text:", cleaned_text2)


# %% 3. Removing punctuation marks
text3 = "Hello, World! 2025"

# The first two arguments of maketrans can be used to replace specific characters (e.g., "a" to "b")
# The third argument removes the specified characters (string.punctuation)
cleaned_text3 = text3.translate(str.maketrans("", "", string.punctuation))
print("3. Without Punctuation:", cleaned_text3)


# %% 4. Removing special characters using Regex
text4 = "Hello, World! 2025%"

# The regex pattern [^A-Za-z0-9\s] keeps only alphanumeric characters and spaces
cleaned_text4 = re.sub(r"[^A-Za-z0-9\s]", "", text4)
print("4. Without Special Characters:", cleaned_text4)


# %% 5. Correcting spelling mistakes
text5 = "Hellıo, Wirld! 2035"

# .correct() fixes typos (Note: TextBlob is mainly optimized for English texts)
cleaned_text5 = TextBlob(text5).correct() 
print(f"5. Spelling Correction -> Original: {text5} | Cleaned: {cleaned_text5}")


# %% 6. Removing HTML tags
html_text = "<div> Hello, World! 2035</div>"

# BeautifulSoup parses the HTML and .get_text() extracts only the human-readable text
cleaned_text6 = BeautifulSoup(html_text, "html.parser").get_text()
print("6. Without HTML Tags:", cleaned_text6)