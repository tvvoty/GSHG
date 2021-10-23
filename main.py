import re


def get_template_html(template_file):
    with open(template_file, mode='r', encoding='utf-8') as template:
        for line in template:
            html_from_template = template.readlines()
            #print(f'html lines are: {html_lines}')
        return html_from_template


# def get_list_of_entries():
#     delimiter = "-|-"
#     with open("list.txt", mode='r', encoding='utf-8') as f:
#         list_of_entries = []
#         read_entry = f.readlines()
#         # print(read_entry)
#         for entry in read_entry:
#             list_of_entries.append(entry.split(delimiter))
#         print(list_of_entries)
#         # for line in f:
#         #     # print(f"{line}/")
#         #     read_entry = f.readlines()
#         #     print(read_entry)
#         #     split_entry = read_entry.split(delimiter)
#         #     list_of_entries.append(split_entry)
#         #print(f'html lines are: {html_lines}')
#         return list_of_entries


def get_list_of_entries():
    """Looks into the file with entries, splits it with the given delimeters append
    then returnes a list of list, where the first index is a word and the Second
    index is the defenition like this:
    [['economy', 'siens abaut maney\n'], ['vowel', 'no stop\n'], ['cons ', 'yes stop\n']]"""

    delimiter = "#$#"
    end_delimiter = "$%$"
    list_of_entries = []
    with open("list.txt", mode='r', encoding='utf-8') as f:
        read = f.read()
        entry_list = read.split(end_delimiter)
        begin_spc = re.compile(r"^\s")
        end_spc = re.compile(r"\s$")
        # print(read_entry)
        for entry in entry_list:
            word, definition = entry.split(delimiter)
            sub_word = end_spc.sub("", word)
            sub_def = begin_spc.sub("", definition)
            one_entry_list = [sub_word, sub_def]
            list_of_entries.append(one_entry_list)
        print(f"list of entries is: {list_of_entries}\n")
        # for line in f:
        #     # print(f"{line}/")
        #     read_entry = f.readlines()
        #     print(read_entry)
        #     split_entry = read_entry.split(delimiter)
        #     list_of_entries.append(split_entry)
        #print(f'html lines are: {html_lines}')
        return list_of_entries


def write_list_to_html_file(list_of_entries):
    html_from_template = get_template_html("index_html_template.html")
    index_page = "html/index.html"
    try:
        with open(index_page, mode='w', encoding='utf-8') as f:
            # for line in html_from_template[0:70]:
            for line in html_from_template[0:31]:
                # print(line)
                f.write(line)
            for entry in list_of_entries:
                f.write(f'<a href="contents/{entry[0]}.html">{entry[0]}</a><br>')
            # for line in html_from_template[70:74]:
            for line in html_from_template[31:34]:
                f.write(line)
    except Exception as e:
        print(f"Something wrong with your file or name: \n{e}\n Lets try again")


def write_entries_to_html_files(list_of_entries):
    html_from_template = get_template_html("html_template.html")

    for entry in list_of_entries:
        page = f"html/contents/{entry[0]}.html"
        try:
            with open(page, mode='w', encoding='utf-8') as f:
                # for line in html_from_template[0:70]:
                for line in html_from_template[0:46]:
                    # print(line)
                    f.write(line)
                f.write(f'<b>{entry[0]}</b> - {entry[1]}</a><br>')
                # for line in html_from_template[70:74]:
                for line in html_from_template[46:50]:
                    f.write(line)
        except Exception as e:
            print(f"Something wrong with your file or name: \n{e}\n Lets try again")


def main():
    list_of_entries = get_list_of_entries()
    write_list_to_html_file(list_of_entries)
    write_entries_to_html_files(list_of_entries)


main()
