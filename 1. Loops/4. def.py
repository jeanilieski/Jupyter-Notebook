#there are STATEMENTS; FUNCTIONS; METHODS  in Python

                 
#def is recording code for re-use later
#these reusable pieces of code are called "FUNCTIONS"

def hello():
    print 'Hello' #what is within the '' is called 'ARGUMENT'
    print 'Fun'

hello()#invocing the function


def name():# what is indented is the code to be reused
    print max('hello77 66 world')#preference to letters
    print max('123')#3 works for strings
    print max(1,2,3)#3 works for tuples, but not for lists
    print [8,9]

#print max[1,2,3] would not get executed
#print a=[8,9] would not get executed, you cannot assign values in def

print 'the output for the def name:', name()
print 'sth'
name()
print '**************'


def greet(lang):#"lang" here is called "PARAMETER" or
    #a placeholder variable, not real variable
    if lang=='es':
        print 'Hola'
    elif lang =='fr':
        print 'Bonjour'
    else:
        print 'Hello'

greet('es'),'Migel' #'Migel' will not be printed out'
greet('other language')#'Hello', since its not 'es' or 'fr'
print '**************'

#print lang would give a TraceBack


def greet1():
    return "Hello"

print 'with return:',greet1(),'Glen'
print greet1(),'Tom'
greet1(),'Kim' #returns nothing



def greet(lang):
    if lang=='es':
        return 'Hola'#in place of 'print' we put 'return'
    elif lang =='fr':
        return 'Bonjour'
    else:
        return 'Hello'


print greet('fr'), 'Jean'


print '********************'
def addtwo(a,b): #we can define more then one parameter
    added=a+b
    return added

x=addtwo(3,5)
y=addtwo(5,7)
z=addtwo('dec','ember')
print x,y,z


#def may return no value. This is not wrong. These are
#called 'Void' functions


def devidetwo(a,b): 
    devided=a/b
    return devided

x=devidetwo(24,4)
print x


