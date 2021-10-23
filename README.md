# GSHG
A script for generating simple html glossaries.


# Usage

You will need Python installed for the script to work. If you don't have python installed on your system you can download it here: https://www.python.org/.

1). Donwload the thing. Either by cloning the repo or download the zip archive by clicking green "code" button and then the "zip" button.

.

2). Every entry and also the word and it's defenition are separated by delimiter characters. Those are the characters that shouldn't be anywhere else in your text, otherwise everything's gonna break. By default the entry delimeter is $%$ and word-definition delimiter is #$#. But you can change them - for that open "main.py" and edit "delimiter" variable on the string 37 to change the word-definition delimiter, so for example edit it to "-" instead of "#$#", and do the same with "end_delimiter" on the string 38 for entry delimiter. 

.

3). You will put your keys and definitions into the "list.txt" file. There are already three entries in the file provided for reference which you should delete, but in general - you put in a word, then the word delimiter, then the definition and then the entry delimiter, with default delimiters would look like this:

A word #$# a long definition $#$

The white space after the word and before the definition will be automatically removed so you can safely have them for the sake of readability (e.g. you dont have to do that: A word#$# a long definition$#$)
.

4). After you populated the list.txt with entries run main.py in the program folder, I think on windows you can just double click the file or you can do it through the terminal - cd into the directory(type: "cd path/to/the/folder" into the terminal(without quotes)) and then type in either "python3 main.py" or "python main.py". It should do it. If it throws an error you can submit it here.


.

5). The html will be generated in the "html" folder. The index.html is where the list of all the words and by clicking on any of them it'll forward you to the word's dedicated page in the "contents" folder.
.

# Инструкция

Вам понадобится Python для этого скрипта. Если он не установлен на вашей системе вы можете скачать его здесь: https://www.python.org/.

1). Скачайте программу, либо клонировав репозиторий, либо скайайте zip архив нажав зелёную кнопку "Code" и затем кнопку "zip". 

.

2). Каждое слово, а также целое вхождение, разделяется разделительными знаками. Эти знаки не должны появляться больше нигде в тексте, иначе всё сломается. По умолчанию разделительный знак для вхождения: $%$ и разделительный знак для слова-определения: #$#. Но вы можете их изменить: для этого откройте файл "main.py" в текстовом редакторе и отредактируйте переменную "delimiter" находящююся в строке 37, для того чтобы поменять разделитель слова-определения, так например вы можете изменить его с "#$#" на "-", и сделайте то же самое для "end_delimiter" на строчке 38 для разделителя вхождений. 

.

3). Вы будете вписывать ваши слова и определения в файл "list.txt". Там уже находяться 3 вхождения, просто для примера, которые вам следует будет удалить, прежде чем писать свои, но в целом работает это примерно так:  вы вписываете слово, затем разделитель слова, затем определение и затем разделитель вхождения, с разделителями по умолчанию это будет выглядеть как-то так:

Слово #$# А это его определение $#$

Пробелы и подобные ему знаки будут автоматически убираться с начала и конца, так что вы можете спокойно оставлять их, чтобы список было удобнее читать (т.е. не обязательно делать так: Слово#$#А это его определение$#$) (e.g. you dont have to do that: A word#$# a long definition$#$)
.

4). После того как вы наполнили list.txt вхождениями запустите main.py в папке с программой, я полагаю на windows вы скорее всего можете просто два раза кликнуть по файлу либо же вы можете сделать это через консоль - перейдите в папку с программой (впишите: "cd путь/к/папке" в консоль (без скобочек)) и затем пропишите либо "python3 main.py" либо же "python main.py". Всё поидее должно сработать. Если выскакивает ошибка - напишите её здесь.


.

5). html код будет сгенерирован в папке "html". index.html это страница, где находится список всех слов, клацая на одно из них вы перейдёте к странице слова, которая находится в папке "contents".
.


