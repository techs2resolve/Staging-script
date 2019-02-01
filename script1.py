import os
import subprocess


project_name = input("Enter the Project Name:- ")
project_pass = input("Enter the Password:- ")
mysql_pass = input("Enter the Mysql Password:- ")

#os.chdir('/Users/sarfaraz/Desktop')
#os.mkdir('project_name/test')
#print(os.listdir('/Users/sarfaraz/Desktop'))

#print(os.path.exists('/Users/sarfaraz/Desktop'))
#print(os.path.isdir('/Users/sarfaraz/Desktop'))
#print(os.path.isfile('/Users/sarfaraz/Desktop'))
#
# if os.path.exists('/Users/sarfaraz/Desktop/testing') == True:
#     print("Path Exist")
# else:
#     print("Not exist")


project_path = os.path.join('/Users/sarfaraz/Desktop', project_name)
print(project_path)
os.mkdir(project_path)