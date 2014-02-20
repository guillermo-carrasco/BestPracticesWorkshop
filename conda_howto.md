##conda / anaconda installation and usage guide

###Anaconda

[Anaconda](http://docs.continuum.io/anaconda/) is a free collection of powerful packages for Python that enables large-scale data management, analysis, and visualization for Business Intelligence, Scientific Analysis, Engineering, Machine Learning, and more.
These packages are installed via the command-line tool "conda" (see next section).
Anaconda is available for Linux, OS X, and Windows, and works the same way for all of them.

###conda

[conda](http://conda.pydata.org/docs/index.html) is used to:

* Create and swtich between isolated virtual environments (like virtualenv or PyEnv)
* Download and install (mostly scientific) packages for use with Python (like pip)

The conda package and environment management system allows users to install multiple versions of binary packages (and any required libraries) appropriate for their platform and easily switch between them, as well as easily download updates from an upstream repository. It also works in tandem with pip, so each system is aware of changes made by the other.

conda a concept of environments which are conceptually similar to virtualenvs, but which use filesystem-level hard links to create entirely self-contained Python runtime layouts. By using the ‘conda’ command line tool, users can easily switch between environments, create environments, and install different versions of libraries and modules into them.

### Warnings

conda does not play nicely with virtualenv. You cannot install Anaconda inside a virtualenv, and I personally suggest disabling virtualenv (or PyEnv) entirely before installing and using Anaconda. You won't need them anymore, anyway. It's time to move on.

The most common way of disabling virtualenv would be to find and comment out any lines looking like this inside your .bashrc or .bash_profile:

Change this:
```
if [ -f $HOME/.venvburrito/startup.sh ]; then
    . $HOME/.venvburrito/startup.sh
fi
```

To this:
```
#if [ -f $HOME/.venvburrito/startup.sh ]; then
#    . $HOME/.venvburrito/startup.sh
#fi
```

You must also comment out any virtualenv initialization lines like:

```
workon my_root_environment
```

or

```
source $HOME/.virtualenvs/my_root_environment/bin/activate
```

If you need help with this you can contact Mario.

###Installation of conda / Anaconda

Installation instructions for Linux, OS X, and Windows are available here:
> http://docs.continuum.io/anaconda/install.html

The default parameters / installation locations are fine.

### Usage

#### create an environment

When creating a new environment under conda, we must specify which packages to install. These can include something as basic as python or as expansive as the full Anaconda suite.
We'll create a new environment called "bsw" (for "Best Practices Workshop"). We'll start with a base Python 2.7.6 install:

```
mario@milou1 ~ $ conda create -n bsw python=2.7.6
```
```
Package plan for installation in environment /home/mario/anaconda/envs/bsw:

The following packages will be linked:

    package                    |            build
    ---------------------------|-----------------
    openssl-1.0.1c             |                0   hard-link
    python-2.7.6               |                1   hard-link
    readline-6.2               |                2   hard-link
    sqlite-3.7.13              |                0   hard-link
    system-5.8                 |                1   hard-link
    tk-8.5.13                  |                0   hard-link
    zlib-1.2.7                 |                0   hard-link

Proceed ([y]/n)? y

Linking packages ...
[      COMPLETE      ] |########################################################################################| 100%
#
# To activate this environment, use:
# $ source activate bsw
#
# To deactivate this environment, use:
# $ source deactivate
#
mario@milou1 ~ $
```

Let's check to see which environments I have now:

```
mario@milou1 ~ $ conda info -e
```
```
# conda environments:
#
bsw                      /home/mario/anaconda/envs/bsw
root                  *  /home/mario/anaconda

mario@milou1 ~ $
```

The asterisk indicates that I'm currently in the "root" environment."

Next, I'll enter the "bsw" environment:

```
mario@milou1 ~ $ source activate bsw
```
```
prepending /home/mario/anaconda/envs/bsw/bin to PATH
(bsw)mario@milou1 ~ $
```

#### install new packages in the environment

Now -- I'm fairly sure we'll be using iPython during the workshop. I'll see which versions are available:
```
(bsw)mario@milou1 ~ $ conda search ipython
```
```
ipython                      0.13                     py26_0  defaults        
                             0.13                     py27_0  defaults        
                             0.13                     py26_1  defaults        
                             0.13                     py27_1  defaults        
                             0.13                     py33_1  defaults        
                             0.13.1                   py26_1  defaults        
                             0.13.1                   py27_1  defaults        
                             0.13.1                   py33_1  defaults        
                             0.13.2                   py26_0  defaults        
                             0.13.2                   py27_0  defaults        
                             0.13.2                   py33_0  defaults        
                             1.0.0                    py26_0  defaults        
                             1.0.0                    py27_0  defaults        
                             1.0.0                    py33_0  defaults        
                             1.1.0                    py26_0  defaults        
                          *  1.1.0                    py27_0  defaults        
                             1.1.0                    py33_0  defaults        
ipython-notebook             0.13.2                   py27_0  defaults        
                             1.0.0                    py27_0  defaults        
                             1.1.0                    py26_0  defaults        
                          *  1.1.0                    py27_0  defaults        
                             1.1.0                    py33_0  defaults        
                             1.1.0                    py26_1  defaults        
                             1.1.0                    py27_1  defaults        
                             1.1.0                    py33_1  defaults        
ipython-qtconsole            0.13.2                   py27_0  defaults        
                             1.0.0                    py27_0  defaults        
                          *  1.1.0                    py27_0  defaults        
                             1.1.0                    py27_1  defaults
```

We see the default version is 1.1.0 for Python v2.7. That's fine, so we can install it without specifying a version number:

```
(bsw)mario@milou1 ~ $ conda install ipython
```
```
Package plan for installation in environment /home/mario/anaconda/envs/bsw:

The following packages will be linked:

    package                    |            build
    ---------------------------|-----------------
    ipython-1.1.0              |           py27_0   hard-link

Proceed ([y]/n)? y

Linking packages ...
[      COMPLETE      ] |########################################################################################| 100%
(bsw)mario@milou1 ~ $
```

Let's see which packages we have installed now:
```
(bsw)mario@milou1 ~ $ conda list
```
```
# packages in environment at /home/mario/anaconda/envs/bsw:
#
ipython                   1.1.0                    py27_0  
openssl                   1.0.1c                        0  
python                    2.7.6                         1  
readline                  6.2                           2  
sqlite                    3.7.13                        0  
system                    5.8                           1  
tk                        8.5.13                        0  
zlib                      1.2.7                         0
```

#### deactivating and switching environments

Alright so I'm set for the workshop. Now it's time to go back to my real passion in life, backend web development using the Python-based Django framework.

Somehow, web developers got ahead of the curve and have already begun migrating to Python 3. I think it's reflective of their reckless attitude toward the establishment. Or maybe they're just too iterative to have any legacy code to support. In any event, we'll create a new environment with Python 3 and Django.


First, we'll leave our current environment:

```
(bsw)mario@milou1 ~ $ source deactivate
```
```
discarding /home/mario/anaconda/envs/bsw/bin from PATH
mario@milou1 ~ $
```

Now we'll see what versions of Python are available to us:

```
mario@milou1 ~ $ conda search python
```
```
                             ...                  ...         ...
python                       2.6.8                         1  defaults        
                             2.6.8                         2  defaults        
                             2.6.8                         3  defaults        
                             2.6.8                         4  defaults        
                             2.6.8                         5  defaults        
                             2.6.8                         6  defaults        
                             2.6.8                         7  defaults        
                             2.6.9                         0  defaults        
                             2.7.3                         2  defaults        
                             2.7.3                         3  defaults        
                             2.7.3                         4  defaults        
                             2.7.3                         5  defaults        
                             2.7.3                         6  defaults        
                             2.7.3                         7  defaults        
                             2.7.4                         0  defaults        
                             2.7.5                         0  defaults        
                             2.7.5                         1  defaults        
                             2.7.5                         2  defaults        
                             2.7.5                         3  defaults        
                             2.7.6                         0  defaults        
                          *  2.7.6                         1  defaults        
                             3.3.0                      pro0  defaults        
                             3.3.0                      pro1  defaults        
                             3.3.0                         2  defaults        
                             3.3.0                         3  defaults        
                             3.3.0                         4  defaults        
                             3.3.1                         0  defaults        
                             3.3.2                         0  defaults        
                             3.3.2                         1  defaults        
                             3.3.3                         0  defaults        
                             3.3.4                         0  defaults        
                             ...                  ...         ...
mario@milou1 ~ $
```

Plenty of versions available (if you do this search yourself, you'll also see many other packages I'm omitting here, including iPython, Biopython, and more). Let's install python 3.3.4:

```
mario@milou1 ~ $ conda create -n django-webdev python=3.3.4
```
```
Package plan for installation in environment /home/mario/anaconda/envs/django-webdev:

The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    python-3.3.4               |                0        18.6 MB

The following packages will be linked:

    package                    |            build
    ---------------------------|-----------------
    openssl-1.0.1c             |                0   hard-link
    python-3.3.4               |                0   hard-link
    readline-6.2               |                2   hard-link
    sqlite-3.7.13              |                0   hard-link
    system-5.8                 |                1   hard-link
    tk-8.5.13                  |                0   hard-link
    zlib-1.2.7                 |                0   hard-link

Proceed ([y]/n)? y

Fetching packages ...
python-3.3.4-0.tar.bz2 100% |###############################################################| Time: 0:00:15   1.28 MB/s
Extracting packages ...
[      COMPLETE      ] |########################################################################################| 100%
Linking packages ...
[      COMPLETE      ] |########################################################################################| 100%
#
# To activate this environment, use:
# $ source activate django-webdev
#
# To deactivate this environment, use:
# $ source deactivate
#
```

Now we need to install Django. Let's enter the environment and see if the Anaconda repos have it:

```
(django-webdev)mario@milou1 ~ $ conda search django
(django-webdev)mario@milou1 ~ $
```

Nope! That makes sense of course because it's not a scientific package. We can just download it using pip instead, because both pip and conda make use of Python's setuptools distribution management system:

```
(django-webdev)mario@milou1 ~ $ pip install django
```
```
Downloading/unpacking django
  Downloading Django-1.6.2-py2.py3-none-any.whl (6.7MB): 6.7MB downloaded
Installing collected packages: django
Successfully installed django
Cleaning up...
(django-webdev)mario@milou1 ~ $
```

Alright so... that's it. That's all I got.
