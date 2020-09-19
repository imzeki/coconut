import os

def listcategoriesanddatabases():
    """
    List down all the categories and databases inside the databases folder
    """
    for root, dirs, files in os.walk("."):
        for filename in files:
            print(filename)
        for rootname in root:
            print(rootname)
        for directory in dirs:
            print(directory)
        
listcategoriesanddatabases()