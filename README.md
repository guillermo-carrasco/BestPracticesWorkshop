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

[Here](DOCS/conda_howto.md) you can find a really good guide written by Mario Giovacchini about
installation and usage of Ana/conda.

## Workshop Material

**Index:**

* [Styling Standards](DOCS/styling.md)
    * [4 spaces per indentation level](DOCS/styling.md#4-spaces-per-indentation-level)
    * [Indentation of Multi-Line Statements](DOCS/styling.md#indentation-of-multi-line-statements)
    * [Maximum line length (soft rule)](DOCS/styling.md#maximum-line-length-soft-rule)
    * [Imports](DOCS/styling.md#imports)
    * [Whitespace in Expressions and Statements](DOCS/styling.md#whitespace-in-expressions-and-statements)
    * [Comments](DOCS/styling.md#comments)
        * [How to Think About Comments](DOCS/styling.md#how-to-think-about-comments)
        * [Comment formatting](DOCS/styling.md#comment-formatting)
        * [Inline comments](DOCS/styling.md#inline-comments)
        * [Documentation strings - Docstrings](DOCS/styling.md#documentation-strings-docstrings)
    * [Naming conventions](DOCS/styling.md#naming-conventions)
    * [Other programming recommendations](DOCS/styling.md#other-programming-recommendations)
* [IPython](DOCS/ipython.md)
* [Debugger](DOCS/ipdb.md)
    * [(i)pdb useful commands](DOCS/ipdb.md#ipdb-useful-commands)
* [Testing](DOCS/testing.md)
* [Advanced Git](DOCS/git_advanced.md)

-----------

[![Build Status](https://travis-ci.org/guillermo-carrasco/BestPracticesWorkshop.png?branch=master)](https://travis-ci.org/guillermo-carrasco/BestPracticesWorkshop)

###Development workflow at Science For Life Laboratory
<p align="center">
  <img src="https://raw.githubusercontent.com/guillermo-carrasco/BestPracticesWorkshop/master/images/development_workflow.png"
       alt="Development workflow at SciLifeLab"/>
</p>
