#Best Practices on Development Workshop

Material for the workshop on Best Practices on Development hosted at Science
For Life Laboratory, Stockholm, Sweden.

## Homework: To Read and Install Before the Workshop
###Git & GitHub

#### Read first
* [Understanding GitHub workflow](http://guides.github.com/overviews/flow/)
* [Forking projects](http://guides.github.com/overviews/forking/)

#### Read second
* [15 minutes hands-on Git tutorial](http://try.github.io/levels/1/challenges/1)
* [Mastering issues](http://guides.github.com/overviews/issues/)

#### Optional but useful
* [Master Markdown](http://guides.github.com/overviews/mastering-markdown/)

###Python et al
##### Virtual Environments with anaconda
Virtual environments allow you to maintain and switch quickly between
different sets of python binaries and packages.
For example, you can work on a project which requires python 2.6 and numpy 1.7
while also maintaining a project which requires python 2.7 and numpy 1.8.
Because packages are installed inside your home directory, virtual environments
also allow you to install python packages without root permissions (as we must
on UPPMAX).

[conda](http://conda.pydata.org/docs/) is a tool to create these isolated
virtual environments as well as a fantastic package management tool. It allows
simple installation of complex scientific packages (scipy, numpy, pandas, etc.)
via the meta-package [Anaconda](https://store.continuum.io/cshop/anaconda/),
and works together with other package mangers like pip.

We will go through the installation of conda/Anaconda at the beginning of the
workshop, but you are welcome to try installing on your own as well.

## Workshop Material

**Index:**

* [Styling Standards](#styling-standards)
    * [4 spaces per indentation level](#4-spaces-per-indentation-level)
    * [Indentation of Multi-Line Statements](#indentation-of-multi-line-statements)
    * [Maximum line length (soft rule)](#maximum-line-length-soft-rule)
    * [Imports](#imports)
    * [Whitespace in Expressions and Statements](#whitespace-in-expressions-and-statements)
    * [Comments](#comments)
        * [How to Think About Comments](#how-to-think-about-comments)
        * [Comment formatting](#comment-formatting)
        * [Inline comments](#inline-comments)
        * [Documentation strings - Docstrings](#documentation-strings-docstrings)
    * [Naming conventions](#naming-conventions)
    * [Other programming recommendations](#other-programming-recommendations)
* [IPython](#ipython)
* [Debugger](#debugger-ipdb)
    * [(i)pdb useful commands](#ipdb-useful-commands)

### Styling Standards

>Code is read much more often than it is written.
>     - A Wise Pythonista

 
We're focusing on Python development on this workshop. Python has its own styling
guide and patterns (which can actually also be applied to most of the existing
programming languages). These guide is called [PEP8](http://www.python.org/dev/peps/pep-0008/), 
and we will be establishing as standard at SciLifeLab the following subset
of these rules.:

####4 spaces per indentation level
Use 4 spaces per indentation level -- don't use tabs.
Spaces are preferred over tabs for the following reason: spaces are spaces on every
editor on every operating system. Tabs can be configured to act as 2, 4, 8 or whichever
number of *"spaces"* and this can make code unreadable when being shared.

This does not mean that you can't use the tab button. You can usually set your
editor to insert four spaces in place of a tab; in vim, you can add this code to your .vimrc:

```
filetype plugin indent on
autocmd FileType python set shiftwidth=4 | set expandtab | set tabstop=4 | set softtabstop=4 | set autoindent
```

You can enable similar functionality in [Xcode](http://stackoverflow.com/a/16263490/1256058) or in Eclipse by using PyDev.

####Indentation of Multi-Line Statements

When using a hanging indent, the following considerations should be applied:
* there should be no arguments on the first line; and
* further indentation should be used to clearly distinguish continuation lines from normal code.

An example to clarify:

Yes!
```python
# Continuation line aligned with opening delimiter
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Indentation used to distinguish the continuation from the next lines of code:
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```
No!
```python
# Arguments should not be used on the first line
#   when not using vertical alignment of continuation lines
#   (compare to first example, above):
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable from the
#   next lines of code:
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

####Maximum line length _(soft rule)_
Limit all lines to a maximum of 79 characters. Break down the line if it exceeds
the maximum length. For example:

```python
with open('/path/to/some/file/you/want/to/read') as file_1, \
        open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

**Tip:** Set up your editor to show you a line on the column 80, so you can 
easily see when your line is becoming too long:

<p align="center">
  <img src="https://raw2.github.com/guillermo-carrasco/BestPracticesWorkshop/master/images/vim_maxlength.png"
       alt="VIM configured to show maximum column length"/>
</p>

To do this in vim, you can add the following to your .vimrc:

```
if exists('+colorcolumn')
      let &colorcolumn="80"
      highlight ColorColumn ctermbg=235 guibg=#2c2d27
else
      au BufWinEnter * let w:m2=matchadd('ErrorMsg', '\%>80v.\+', -1)
endif
```

####Imports
Imports should usually be on separate lines, e.g.:

Yes:
```python
import os
import sys
```
No:
```python
import os, sys
```

Multiple submodule imports on the same line are okay:
```python
from subprocess import Popen, PIPE
```

Wildcard imports (```from <module> import *```) should be avoided, as they make
it unclear which names are present in the namespace, confusing both readers and
many automated tools. In case that the name of the module is very long and even
difficult readability, you can always make an alias:
```
import very_long_and_weird_module_name as long_module
```

It is also nice to alphabetize your imports though I doubt this is a convention.
Also, compartmentalize "from"-style imports separate from basic ones:
```
import collections
import numpy as np
import shutil

from matplotlib import pyplot as plt
from subprocess import check_output
```

####Whitespace in Expressions and Statements
Avoid extraneous whitespace in the following situations:

* Immediately inside parentheses, brackets or braces.

```
Yes: spam(ham[1], {eggs: 2})
No:  spam( ham[ 1 ], { eggs: 2 } )
```

* Immediately before a comma, semicolon, or colon:

```
Yes: if x == 4: print x, y; x, y = y, x
No:  if x == 4 : print x , y ; x , y = y , x
```

* Immediately before the open parenthesis that starts the argument list of a function call:

```
Yes: spam(1)
No:  spam (1)
```

* Immediately before the open parenthesis that starts an indexing or slicing:

```
Yes: dict['key'] = list[index]
No:  dict ['key'] = list [index]
```

* More than one space around an assignment (or other) operator to align it with another.

Yes:
```
x = 1
y = 2
long_variable = 3
```
No:
```
x             = 1
y             = 2
long_variable = 3
```

####Comments

#####How to Think About Comments
Always remember that the point of your comments is to help people reading it
understand two things:

* What the code does
* Why it does it

You should attempt to make the code "self-documenting" by using descriptive
names for functions and variables; when the reason for doing something
cannot be made clear, however, you can add a comment to explain the reason
for a piece of code.

For example:

No:
```python
def c_disp(v=0, t):
    g = 9.81
    return v*t + (1/2) * g * (t^2)
```

Yes:
```python
def calculate_displacement(velocity=0, time=0, acceleration=9.81):
    # We're using Newtonian physics here because quantum computing is too expensive
    return velocity*time + (1/2)(acceleration * time^2)
```

Yes!! Docstrings!
```python
def calculate_displacement(velocity=0, time=0, acceleration=9.81):
    """Calculate displacement of an object using the Newtonian equation
        x = vₒt + ½at²

    Default value for accleration is that for Earth near the surface.

    Keyword arguments:
      velocity: starting velocity
      time: elapsed time

    Returns a float of the displacement.

    """
    # We're using Newtonian physics here because quantum computing is too expensive
    return float(velocity*time + (1/2)(acceleration) * time^2))
```

Comments that contradict the code are worse than no comments; however,
**you should always make it a priority to keep the comments up-to-date
when the code changes!**

#####Comment Formatting
Comments should be complete sentences. If a comment is short, the period at the
end can be omitted. Block comments generally consist of one or more paragraphs
built out of complete sentences, and each sentence should end in a period.

Python coders from non-English speaking countries: please write your comments in
English, unless you are 120% sure that the code will never be read by people who
don't speak your language. Python's author is Dutch, and if he can do it,
you can do it.

#####Inline comments
Use inline comments infrequently.

An inline comment is a comment on the same line as a statement. Inline comments
should be separated by at least two spaces from the statement. They should start
with a `#` and a single space.

Inline comments are rarely necessary and in fact distracting if they state the obvious.

Don't do this:
```python
x = x + 1                 # Increment x
```

But this is useful:
```python
x = x + 1                 # Compensate for border
```

#####Documentation strings (Docstrings)
A docstring is a string literal that occurs as the first statement in a module,
function, class, or method definition. Such a docstring becomes the ```__doc__```
 special attribute of that object.

Write docstrings for all public modules, functions, classes, and methods.
Docstrings are not necessary for non-public methods, but you should have a comment
that describes what the method does. This comment should appear after the def line.

Use the docstrings to document the parameters of your function, so other people
can easily understand what the function does:
```python
def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
      real -- the real part (default 0.0)
      imag -- the imaginary part (default 0.0)

    Returns a float of the complex number.

    """
    if imag == 0.0 and real == 0.0: return complex_zero
    ...
```

__Suggestion__: Use [sphinx](http://sphinx-doc.org/)-style docstrings to generate 
readable documentation that can also be used to auto-generate full web-based docs.

####Naming conventions
There are a lot of different naming styles. It helps to be able to recognize what 
naming style is being used, independently from what they are used for.

In order to have an homogeneous-looking code, we will follow some simple naming
conventions:
* _Package and Module Names_: Modules should have short, all-lowercase names. Underscores
can be used in the module name if it improves readability. Since module names are mapped 
to file names, and some file systems are case insensitive and truncate long names, 
it is important that module names be chosen to be fairly short.
* _Class names_: Class names should normally use the CapWords convention (also called CamelCase).

```python
class MyNewClass(object):
```

* _Exception names_: Because exceptions should be classes, the class naming convention 
applies here.

```python
class MyNewException(Exception):
```

* _Function Names_: Function names should be lowercase, with words separated by underscores 
as necessary to improve readability.

```python
def my_new_function():
```

* _Function and method arguments_:
    * Always use ```self``` for the first argument to instance methods.
    * Always use ```cls``` for the first argument to class methods.
    * If a function argument's name clashes with a reserved keyword, it is generally 
    better to append a single trailing underscore rather than use an abbreviation or 
    spelling corruption. Thus class_ is better than clss. (Perhaps better is to avoid 
    such clashes by using a synonym.)
* _Method Names and Instance Variables_: 
    * Use the function naming rules: lowercase with words separated by underscores 
    as necessary to improve readability. 
    * Use one leading underscore only for non-public methods and instance variables.

```python
class MyNewClass(object):
    def _my_new_class_method(cls):
        ...

    def my_new_instance_method(self):
       ...
```

* _Constants_: Constants are usually defined on a module level and written in all 
capital letters with underscores separating words. Examples include MAX_OVERFLOW and TOTAL.

####Other programming recommendations
* Comparisons to singletons like `None` should always be done with `is` or `is not`, never 
the equality operators. _NOTE_: Also, beware of writing `if x` when you really mean
`if x is not None` -- e.g. when testing whether a variable or argument that defaults 
to `None` was set to some other value.
* When catching exceptions, mention specific exceptions whenever possible instead 
of using a bare `except`: clause. For example:
```python
try:
    import platform_specific_module
except ImportError:
    platform_specific_module = None
```
Better than:
```python
try:
    import platform_specific_module
except:
    platform_specific_module = None
```
A bare `except:` clause will catch `SystemExit` and `KeyboardInterrupt` exceptions, 
making it harder to interrupt a program with Control-C, and can disguise other problems.
* Use `''.startswith()` and `''.endswith()` instead of string slicing to check for prefixes or 
suffixes. `startswith()` and `endswith()` are cleaner and less error prone. For example:
```
Yes: if foo.startswith('bar'):
No:  if foo[:3] == 'bar':
```
* For sequences, (strings, lists, tuples), use the fact that empty sequences are false.
```
Yes: if not seq:
     if seq:

No: if len(seq)
    if not len(seq)
```
* Don't compare boolean values to True or False using ==:
```
Yes:   if greeting:
No:    if greeting == True:
Worse: if greeting is True:
```

###IPython
One of Python’s most useful features is its interactive interpreter. It allows for 
very fast testing of ideas without the overhead of creating test files as is typical 
in most programming languages. However, the interpreter supplied with the standard 
Python distribution is somewhat limited for extended interactive use.

[IPython](http://ipython.org/) is an alternative to the standard Python interpreter
which goal is to create a comprehensive environment for interactive and exploratory computing. 
To support this goal, IPython provides an enhanced interactive Python shell. You
can read detailed documentation [here](http://ipython.org/ipython-doc/stable/overview.html),
but these are some of the main features:

1 - Easily check methods and attributes of an object with the syntax `<object>. + TAB`:

<p align="center">
  <img src="https://raw2.github.com/guillermo-carrasco/BestPracticesWorkshop/master/images/ipython_list_methods.png"
       alt="Show object methods with <object>. + TAB"/>
</p>

2 - Read the docstring of any method with `<object>.<method>?` **(Hey! Docstrings are useful!)**:

<p align="center">
  <img src="https://raw2.github.com/guillermo-carrasco/BestPracticesWorkshop/master/images/ipython_show_docstring.png"
       alt="Show method docstring with <object>.?"/>
</p>

3.- Look at a method's/function's code without opening any file with `<object>.<method>??`:

<p align="center">
  <img src="https://raw2.github.com/guillermo-carrasco/BestPracticesWorkshop/master/images/ipython_show_code_1.png"
       alt="Show method code with <object>.??"/>
</p>

<p align="center">
  <img src="https://raw2.github.com/guillermo-carrasco/BestPracticesWorkshop/master/images/ipython_show_code_2.png"
       alt="Show method code with <object>.??"/>
</p>

4.- Directly write functions on the interpreter:

<p align="center">
  <img src="https://raw2.github.com/guillermo-carrasco/BestPracticesWorkshop/master/images/ipython_interactive_programming.png"
       alt="Write anything directly on the interpreter!"/>
</p>

5.- [Magic functions](http://ipython.org/ipython-doc/dev/interactive/tutorial.html)! 
To help you copy code into the interpreter and a lot more stuff:

<p align="center">
  <img src="https://raw2.github.com/guillermo-carrasco/BestPracticesWorkshop/master/images/ipython_magic_functions.png"
       alt="Copy paste code without indentation problems"/>
</p>

And more... just read the docs :-)

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