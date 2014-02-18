#Best Practices on Development - Workshop material

Material for the workshop on Best Practices on Development hosted at Science
For Life Laboratory, Stockholm, Sweden.

##Previous reads and short tutorials
###Git & GitHub

* [15 minutes hands-on Git tutorial](http://try.github.io/levels/1/challenges/1)
* [Understanding GitHub workflow](http://guides.github.com/overviews/flow/) and
[Forking projects](http://guides.github.com/overviews/forking/) - **Those two are important**
* [Mastering issues](http://guides.github.com/overviews/issues/)
* (Optional but interesting) - [Master Markdown](http://guides.github.com/overviews/mastering-markdown/)

###Python and related
* [Anaconda and virtual environments](https://store.continuum.io/cshop/anaconda/)

##Styling standards
>Foolish Consistency is the Hobgoblin of Little Minds - "Guido van Rossum"

We're focusing on Python development on this workshop. Python has it's own styling
guide and patterns that actually can be applied to most of the existing programming
languages. These guide is called [PEP8](http://www.python.org/dev/peps/pep-0008/), 
and we will be establishing as standard the following subset:

####4 spaces per indentation level
Use 4 spaces per indentation level. Continuation lines should align wrapped elements 
either vertically using Python's implicit line joining inside parentheses, brackets
and braces, or using a hanging indent. When using a hanging indent the following 
considerations should be applied; there should be no arguments on the first line 
and further indentation should be used to clearly distinguish itself as a continuation line.

For example:

Yes:
```python
# Aligned with opening delimiter
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# More indentation included to distinguish this from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```
No:
```python
# Arguments on first line forbidden when not using vertical alignment
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

Spaces are preferred over tabs for the following reason: Spaces are spaces on every
editor on every operating system. Tabs can be configured to act as 2, 4, 8 or whichever
number of *"spaces"* and this can make code unreadable.

####Maximum line length _(solf rule)_
Limit all lines to a maximum of 79 characters. Break down the line if it exceeds
the maximum length. For example:

```python
with open('/path/to/some/file/you/want/to/read') as file_1, \
        open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

**Tip:** Set up your editor to show you a line on the column 80, so you can 
easily see if you're writing too long lines:

<p align="center">
  <img src="https://raw2.github.com/guillermo-carrasco/BestPracticesWorkshop/master/images/vim_maxlength.png"
       alt="VIM configured to show maximum column length"/>
</p>

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

If importing within the same package though, this is ok:
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
Comments that contradict the code are worse than no comments. **Always make a priority 
of keeping the comments up-to-date when the code changes!**

Comments should be complete sentences. If a comment is a phrase or sentence, its
first word should be capitalized, unless it is an identifier that begins with a 
lower case letter (never alter the case of identifiers!).

If a comment is short, the period at the end can be omitted. Block comments generally 
consist of one or more paragraphs built out of complete sentences, and each sentence 
should end in a period.

You should use two spaces after a sentence-ending period.

Python coders from non-English speaking countries: please write your comments in 
English, unless you are 120% sure that the code will never be read by people who 
don't speak your language.

#####Inline comments
Use inline comments sparingly.

An inline comment is a comment on the same line as a statement. Inline comments 
should be separated by at least two spaces from the statement. They should start 
with a `#` and a single space.

Inline comments are unnecessary and in fact distracting if they state the obvious. 
Don't do this:

```python
x = x + 1                 # Increment x
```

But this is useful:
```
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

    """
    if imag == 0.0 and real == 0.0: return complex_zero
    ...
```

__Suggestion__: Use [sphinx](ihttp://sphinx-doc.org/) style docstrings to generate 
nice and exportable configurations.

####Naming conventions
There are a lot of different naming styles. It helps to be able to recognize what 
naming style is being used, independently from what they are used for.

In order to have an homogeneous-looking code, we will follow some simple naming
conventions:
* _Package and Module Names_: Modules should have short, all-lowercase names. Underscores
can be used in the module name if it improves readability. Python packages should 
also have short, all-lowercase names, although the use of underscores is discouraged.
Since module names are mapped to file names, and some file systems are case insensitive 
and truncate long names, it is important that module names be chosen to be fairly short.
* _Class names_: Class names should normally use the CapWords convention.
* _Exception names_: Because exceptions should be classes, the class naming convention 
applies here.
* _Function Names_: Function names should be lowercase, with words separated by underscores 
as necessary to improve readability.
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
* _Constants_: Constants are usually defined on a module level and written in all 
capital letters with underscores separating words. Examples include MAX_OVERFLOW and TOTAL.

####Programming recommendations
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
A bare `except:` clause will catch SystemExit and KeyboardInterrupt exceptions, 
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