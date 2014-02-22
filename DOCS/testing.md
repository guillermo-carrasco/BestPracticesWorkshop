[BACK TO INDEX](../README.md)
__________
###Testing and Continuous Integration
####Testing
Testing is one of the most abandoned good practices on development... and that's a real pity. 

One should think like this:

>Man, I just love unit tests, I've just been able to make a bunch of changes to the way something works, 
>and then was able to confirm I hadn't broken anything by running the test over it again...

But instead we usually think like this:

>Yay! I finished coding my functionality, that I'm pretty sure it works... maybe I should write
>some tests... I don't have time, I'll do some manual checks and this should be ok.

I can admit that sometimes writing a test can be even more difficult than writing the actual
functionality to be tested, but one should always prioritize the testing. This specially applies to teams of developers.

If you're developing a project together with other people, it is very probable that you cannot keep track
of all of what your partners are doing, leading you to a situation where you don't understand all the
project's code. This is OK, that's why you're on a team, and not working alone. However, this doesn't mean that
both you and your team doesn't have to take care about not breaking other's code.

Here is where testing helps. Test-driven development (TDD) is a software development process that relies 
on the repetition of a very short development cycle: first the developer writes an (initially failing) 
automated test case that defines a desired improvement or new function, then produces the minimum amount 
of code to pass that test, and finally refactors the new code to acceptable standards.

THe advantages of writing this tests and executing them after each new addition to the code are (extracted
from [this post](http://stackoverflow.com/questions/67299/is-unit-testing-worth-the-effort)):

1. Unit Tests allows you to make big changes to code quickly. You know it works now because you've run the tests, when you make the changes you need to make, you need to get the tests working again. This saves hours.
2. The tests and the code work together to achieve better code. Your code could be bad / buggy. 
Your TEST could be bad / buggy. In TDD you are banking on the chances of both being bad / buggy being low. 
Often it's the test that needs fixing but that's still a good outcome.  
3. TDD helps with coding constipation. When faced with a large and daunting piece of work ahead writing 
the tests will get you moving quickly.
4. Unit Tests help you really understand the design of the code you are working on. Instead of writing code 
to do something, you are starting by outlining all the conditions you are subjecting the code to and what 
outputs you'd expect from that.
5. Unit Tests give you instant visual feedback, we all like the feeling of all those green lights 
when we've done. It's very satisfying. It's also much easier to pick up where you left off after 
an interruption because you can see where you got to - that next red light that needs fixing.
6. Contrary to popular belief unit testing does not mean writing twice as much code, or coding slower. 
It's faster and more robust than coding without tests once you've got the hang of it. 
Test code itself is usually relatively trivial and doesn't add a big overhead to what you're doing. 
This is one you'll only believe when you're doing it :)
7. Good unit tests can help document and define what something is supposed to do

#####A short example - TDD cycle
You have to write a method that takes an integer as a parameter and returns:

* The same number if that number is odd
* The next integer if the number is even

The TDD cycle would be:

1. Write the test

    ```python
    def test_odd(self):
        """Testing odd method
        """
        with self.assertRaises(ValueError):
            exercises.odd('1')
        self.assertEqual(1, exercises.odd(1))
        self.assertEqual(3, exercises.odd(2))
    ```
    This is a complete test for this functionality: We're testing that the parameter is an integer,
    that it returns the same number if the parameter is odd and that it returns the next integer if
    the parameter is even.

2. Write the code

    ```python
    def odd(n):
        """Return the closest odd number to n
    
        Paramss:
            n - An integer
        """
        if not n%2:
            return n+1
        return n
    ```

3. Run the test

    In this case the test will fail, because the first assertion (checking that 
    the value is an integer), will raise TypeError. This is because we're no checking that the value 
    is an integer, and therefore our function will try to execute `n%2`, n being a character, and will crash.

4. Fix the code

    ```python
    def odd(n):
        """Return the closest odd number to n
    
        Paramss:
            n - An integer
        """
        if not isinstance(n, int):
            raise ValueError("The parameter must be an integer!")
        if not n%2:
            return n+1
        return n
    ```

5. Run the test again: And in this case the test will pass. Otherwise we will go back to 4

As you can see this iterative process enforces the correctness of the code. Obviously, the tests
have to be meaningful also, and takes time to learn how to write these tests.

####Continuous Integration
Continuous integration is a way of easing the live to developers. Basically it automates the testing process.
It does not automate the actual writing of the tests of course, but saves a lot of time and ensures that the tests
are run **always**. [Travis-CI](http://docs.travis-ci.com/user/getting-started/) is one of these systems. You can integrate your GitHub project in Travis-CI and it will run your test suite in a fresh environment **on every new commit**!
Isn't it fantastic? We will show how to do this in the workshop, but if you want to try it yourself, the
documentation is great ;-)



__________
[BACK TO INDEX](../README.md)
