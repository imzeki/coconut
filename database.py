"""
Generate a database for you to rely on, this module then saves it at Coconut's folder name 'databases'. The format is alwyas python so yhou can load it. If you want to access it, you must do something ike this:
>>> from coconut.databases import Example
>>> #Do whatever you want with the code
"""
import backend
import os
from shutil import rmtree


class DatabaseError(BaseException):
    """
    Root of all DatabaseErrors
    """
    pass


class InvalidTypeDatabaseError(DatabaseError):
    """
    The format type given is invalid
    """
    pass


class DatabaseNameError(DatabaseError):
    """
    Name of database is invalid
    """
    pass


class NoDatabaseError(DatabaseError):
    """
    Error raised when Database does not exist
    """
    pass


def createDatabase(name: str) -> bool:
    """
    Creates a database in the format of python. If spaces are in the name, it will be cut off through trim(). Returns true if the database is successfully created.
    >>> import coconut
    #The database format must always be python, it still supports if name has no .py
    >>> coconut.database.createDatabase("Example.py")
    True
    """
    if backend.trim(name) == '':
        raise DatabaseNameError(f'Name {name} is invalid and is just spaces')
    else:
        if not name.lower().endswith('.py'):
            if len(name.split('.')) > 1:
                raise InvalidTypeDatabaseError('Extension type {} is invalid'.format(name.split('.')[-1]))
            else:
                if name.endswith('.py'):
                    pass
                else:
                    name = name + '.py'
                os.chdir(os.path.join(backend.throwback(), 'databases'))
                f = open(f'{name}', 'w+')
                f.close()
                return True
        else:
            os.chdir(os.path.join(backend.throwback(), 'databases'))
            f = open(f'{name}', 'w+')
            f.close()
            return True


def deleteDatabase(name: str) -> bool:
    """
    Deletes the database.
    Returns True if the database has been successfully deleted.
    Raises NoDatabaseError if the name of the database does not exist.
    Raises InvalidTypeDatabaseError if name of database does not exist or type of file given is invalid.
    >>> import coconut.database
    >>> coconut.database.deleteDatabase("Example")
    """
    if not name.endswith('.py'):
        raise InvalidTypeDatabaseError(f'Name of database is invalid.')
    else:
        pass
    os.chdir(os.path.join(backend.throwback(), 'databases'))
    if os.path.exists(name):
        os.remove(name)
        return True
    else:
        raise NoDatabaseError(f'Database {name} does not exist')


def readDatabase(name: str) -> str:
    """
    Reads the database
    """
    if not name.endswith('.py'):
        raise InvalidTypeDatabaseError(f'Name of database is invalid.')
    else:
        pass
    os.chdir(os.path.join(backend.throwback(), 'databases'))
    if os.path.exists(name):
        with open(name, 'r') as text:
            return text.read()
    else:
        raise NoDatabaseError(f'Database {name} does not exist')


def appendDatabase(filename: str, code: str) -> bool:
    """
    Appends a code of line to the database, that is where the real part kicks in!
    """
    if not filename.endswith('.py'):
        raise InvalidTypeDatabaseError('Name of database is invalid.')
    else:
        pass
    os.chdir(os.path.join(backend.throwback(), 'databases'))
    if os.path.exists(filename):
        with open(filename, 'a+') as Code:
            Code.write(str(code))
            Code.close()
            return True
    else:
        raise NoDatabaseError(f'Database {filename} does not exist')


def executeDatabase(filename: str) -> bool:
    """
    Executes a database
    """
    if not filename.endswith('.py'):
        raise InvalidTypeDatabaseError('Name of database is invalid.')
    else:
        pass
    os.chdir(os.path.join(backend.throwback(), 'databases'))
    if os.path.exists(filename):
        with open(filename, 'r') as code:
            exec(code.read())
            code.close()
            return True
    else:
        raise NoDatabaseError(f'Database {filename} does not exist')


class NewCategory():
    """
    Creates a new category for databases and adds databases.

    Note
    ====
    It is case-sensative.

    In the sub categories part, os.path.join is needed if you want to go deeper in the database directory
    """

    def __init__(self, nameofcategory: str):
        self.nameofcategory = str(nameofcategory)
        self.path = os.path.join(backend.throwback(), 'databases', self.nameofcategory)
        if os.path.exists(self.path):
            self.exists = True
        else:
            self.exists = False

    def createCategory(self):
        """
        Creates a new category under the databases
        """
        try:
            os.mkdir(self.path)
            os.chdir(self.path)
            self.createInitFile()
            return True
        except:
            return False

    def createSubCategory(self, name: str):
        """
        Creates a sub category, do os.path.join() if you want to create two sub categories
        """
        try:
            subdirectories = name.split("\\")
            currentpath = self.path
            for sd in subdirectories:
                os.chdir(currentpath)
                os.mkdir(sd)
                currentpath = os.path.join(currentpath, sd)
                self.createInitFile()
                os.chdir(currentpath)

            self.createInitFile()
            return True
        except:
            return False

    def truncateCategory(self):
        """
        Makes the category entirely empty
        """
        rmtree(self.path)
        os.mkdir(self.path)
        os.chdir(self.path)
        self.createInitFile()
        return True

    def opencategory(self):
        """
        Opens category for editing purposes
        """
        os.startfile(self.path)

    def createDatabaseWithin(self, name: str) -> bool:
        """
        Cretes a database within the category itself. The format of the database must always be .py
        """
        os.chdir(self.path)
        if backend.trim(name) == '':
            raise DatabaseNameError(f'Name {name} is invalid and is just spaces')
        else:
            if not name.lower().endswith('.py'):
                if len(name.split('.')) > 1:
                    raise InvalidTypeDatabaseError('Extension type {} is invalid'.format(name.split('.')[-1]))
                else:
                    if name.endswith('.py'):
                        pass
                    else:
                        name = name + '.py'
                    f = open(f'{name}', 'w+')
                    f.close()
                    return True
            else:
                os.chdir(os.path.join(backend.throwback(), 'databases'))
                f = open(f'{name}', 'w+')
                f.close()
                return True

    def deleteDatabaseWithin(self, name: str) -> bool:
        """
        Deletes the database within
        """
        os.chdir(self.path)
        if backend.trim(name) == "":
            raise DatabaseNameError(f'Name {name} is invalid and is just spaces')
        else:
            if os.path.exists(os.path.join(self.path, name)):
                if name.endswith(".py"):
                    pass
                else:
                    name = name + ".py"
                if name == "__init__.py":
                    return False
                else:
                    os.remove(name)
                    return True
            else:
                return False

    def appendDatabaseWithin(self, name: str, code: str) -> bool:
        """
        Appends something to the database
        """
        os.chdir(self.path)
        if name.endswith(".py"):
            pass
        else:
            name = name + ".py"
        if os.path.exists(os.path.join(self.path, name)):
            f = open(name, "a+")
            f.write(str(code))
            f.close()
            return True
        else:
            return False

    def executeDatabaseWithin(self, name: str) -> bool:
        """
        Executes the database within
        """
        os.chdir(self.path)
        if name.endswith(".py"):
            pass
        else:
            name = name + ".py"
        if os.path.exists(os.path.join(self.path, name)):
            f = open(name, "r")
            exec(f.read())
            return True
        else:
            return False

    def deleteCategory(self):
        """
        Deletes the entire category
        """
        rmtree(self.path)

    def createDatabaseWithinSubcategory(self, pathway, name) -> bool:
        """
        Creates a database within. If you want to go deeper, join pathway thorugh os.path.join.
        """
        os.chdir(os.path.join(self.path, pathway))
        if backend.trim(name) == "":
            raise DatabaseNameError(f"Name {name} is invalid and is just spaces")
        else:
            if name.endswith(".py"):
                pass
            else:
                name = name + ".py"
            f = open(name, "w+")
            f.close()
            return True

    def deleteDatabaseWithinSubcategory(self, pathway, name) -> bool:
        """
        Deletes the database within the subbcategory, going deeper requires os.path.join for pathway
        """
        os.chdir(os.path.join(self.path, pathway))
        if name.endswith(".py"):
            pass
        else:
            name = name + ".py"
        if os.path.exists(name):
            os.remove(name)
            return True
        else:
            return False

    def appendDatabaseWithinSubcategory(self, pathway, name, code: str) -> bool:
        """
        Appends lines of code to the database within a subcategory of the main category, going deeper requires os.path.join for pathway
        """
        os.chdir(os.path.join(self.path, pathway))
        if name.endswith(".py"):
            pass
        else:
            name = name + ".py"
        if os.path.exists(name):
            f = open(name, "a+")
            f.write(str(code))
            f.close()
            return True
        else:
            return False

    def executeDatabaseWithinSubcategory(self, pathway, name) -> bool:
        """
        Executes the given database with its name and path
        """
        os.chdir(os.path.join(self.path, pathway))
        if name.endswith(".py"):
            pass
        else:
            name = name + ".py"
        if os.path.exists(name):
            f = open(name, "r")
            exec(f.read())
            f.close()
            return True
        else:
            return False

    @staticmethod
    def createInitFile():
        """
        Creates a __init__.py file in the categories for import usage
        """
        f = open("__init__.py", "w+")
        f.close()
        return True
