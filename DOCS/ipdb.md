[BACK TO INDEX](../README.md)
__________
###Debugger (i)pdb
Debugging is a methodical process of finding and reducing the number of bugs, 
or defects, in a computer program. **All of you** have debugged some program or script
in any moment of your developer's life, but probably not all of you have used a
debugger.

A debugger is a tool that helps you explore the execution of your code in a very
controlled way, allowing you to execute it line by line and change the behaviour
"on the go".

Some of the reasons why you _**want**_ to use a debugger are:

* Trying to spot a bug with print statements withing the code is hard, probably
useless and chances are that you're gonna forget some of these statements when
you "clean up" your code afterwards.
* It is practically useless to "debug" if you cannot interact with or change what
is causing the bug (again, print is not helpful here).
* Check and change values of variables, methods, objects, etc. _while_ debugging

pdb, or the IPython debugger ipdb allows you to debug your python code. To enter
the debugger, you just have to insert a single statement in your code. 

Let's look at it with an example, imagine that you have this function:
```python
def sum_list(l):
    """Sum all elements in a list

    Arguments:
        l -- list to sum
    """
    return sum(l)
```

This method will crash if you pass it a list with mixed integers and strings, for example,
but you don't know that because the function is inside a module, that is called by
another function, that bla bla... What you'd do is to add the following statement:
```python
def sum_list(l):
    """Sum all elements in a list

    Arguments:
        l -- list to sum
    """
    import ipdb; ipdb.set_trace()
    return sum(l)
```

The `ipdb.set_trace()` statement will print a trace so you know where you are.

When you run your method, ipdb will stop the execution where that statement is
located and you'll be on an interactive shell, where you can do whatever you want.

For example, we could explore the variable l to see its contents:
<p align="center">
  <img src="https://raw2.github.com/guillermo-carrasco/BestPracticesWorkshop/master/images/ipdb.png"
       alt="Interactive debugging"/>
</p>

With this small example you can see how useful can be ipdb. In this case would be enough
to raise an exception with a proper message or try so sum only the int values.

Here it follows a list of the most common used ipdb commands. For a complete documentation, 
go [here](http://docs.python.org/2/library/pdb.html)!

####(i)pdb useful commands

* _**h**(elp) [command]_: Without argument, print the list of available commands. With
a command as argument, print help about that command.
* _**w**(here)_: Print a stack trace, with the most recent frame at the bottom. 
An arrow indicates the current frame, which determines the context of most commands.
* _**s**(tep)_: Execute the current line, stop at the first possible occasion 
(either in a function that is called or on the next line in the current function).
* _**n**(ext)_: Continue execution until the next line in the current function is reached or it returns.
(The difference between `next` and `step` is that `step` stops inside a called function, 
while `next` executes called functions at (nearly) full speed, only stopping at the 
next line in the current function.)
*_**c**(ontinue)_: Continue execution, only stop when a breakpoint is encountered.
*_**a**(rgs)_: Print the argument list of the current version.
* _**p** expression_: Evaluate the expression in the current context and print its value.
* _**q**(uit)_: Quit from the debugger. The program being executed is aborted.
__________
[BACK TO INDEX](../README.md)
