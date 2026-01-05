
# 14. Access Deeply Nested Dictionary 
# Given: 
company = { 
"sales": {"manager": "Kiran", "team": {"T1": "Raj", "T2": "Neha"}}, 
"tech": {"manager": "Asha", "team": {"T1": "Dev", "T2": "Sonia"}} 
} 
# �
# �
#  Print the name of "T2" in the "tech" department. --- 
# 15. Print Keys of Inner Dictionary 
# From the company dictionary, print all the team member IDs (T1, T2) of "sales".

print(company["tech"]["team"]["T2"])

print(company["sales"]["team"].keys())

print(company["sales"]["team"].keys())

print(company["tech"]["team"].keys())