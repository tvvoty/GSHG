import re
str = "y o "

end_spc = re.compile(r"\s$")
no_spc_yo = end_spc.sub("", str)

print(no_spc_yo + "yo")
