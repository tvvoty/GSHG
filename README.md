# GSHG
A script for generating simple html glossaries.


# Usage Eng

You will need Python installed for the script to work. If you don't have python installed on your system you can download it here: https://www.python.org/.

1). Donwload the thing. Either by cloning the repo or download the zip archive by clicking green "code" button and then the "zip" button.

.

2). Every entry and also the word and it's defenition are separated by delimiter characters. Those are the characters that shouldn't be anywhere else in your text, otherwise everything's gonna break. By default the entry delimeter is $%$ and word-definition delimiter is #$#. But you can change them - for that open "main.py" and edit "delimiter" variable on the string 37 to change the word-definition delimiter, so for example edit it to "-" instead of "#$#", and do the same with "end_delimiter" on the string 38 for entry delimiter. 

.

3). You will put your keys and definitions into the "list.txt" file. There are already three entries in the file provided for reference which you should delete, but in general - you put in a word, then the word delimiter, then the definition and then the entry delimiter, with default delimiters would look like this:

A word #$# a long definition $#$

The white space after the word and before the definition will be automatically removed so you can safely have them for the sake of readability (e.g. you dont have to do that: A word#$# a long definition$#$)
.

4). After you populated the list.txt with entries run main.py in the program folder, I think on windows you can just double click the file or you can do it through the terminal - cd into the directory(type: "cd path/to/the/folder" into the terminal(without parathesis)) and then type in either "python3 main.py" or "python3 main.py". It should do it. If it throws an error you can submit it here.


.

5). The html will be generated in the "html" folder. The index.html is where the list of all the words and by clicking on any of them it'll forward you to the word's dedicated page in the "contents" folder.
.



