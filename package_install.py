import os


pkg_nm = input("Enter the package name you want to install :- ")

soft = "sudo apt-get install -y "+(pkg_nm)

print(soft)
os.system(soft)