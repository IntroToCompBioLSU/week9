# Week 9 Outline

## Notes
- Grades
- Submitting assignments
  - No need to create new branches from here on out
- Final Projects

## Reading and Other Resources
- Practical Computing, Chapters 10 and 11


## Reading and Writing from Files in Python

```
In-Class Assignment

Today, we will start taking steps toward building code that can process lots of
data easily and can be reused in other scripts that we may write in the future.
The goal of this week's in-class assignment is to write a script that will translate
a nucleotide sequence into an amino-acid sequence (like you did last week). But
it will do so for an arbitrary number of sequences in an arbitrary number of files.
Your script should:

- Accept any number of filenames as command-line arguments
- Each of these files can contain a separate nucleotide sequence on each line
- The script should contain a new function that takes each of these sequences,
translates them to amino acids, and prints all of them to one output file.
```

- [ ] Reading from files
  - To read or write from a file, you'll first need to define the file name
    - e.g., `inFileName = "FileToRead.txt"`
  - However, this is just a string variable with the file name. We need to create an object that can actually read the contents of a file.
  - Python has a built-in function to create a file object - `open(<FILENAME>,<MODE>)`
  - The `<FILENAME>` argument is just a string with the file's name (or path to the file)
  - The `<MODE>` argument tells Python whether we are reading from a file (`r`), writing to a file (`w`), or appending to a file (`a`).
  - To open up a new File object to read file contents, use syntax like this:
    - `inFile = open(inFileName,'r')`
  - There are several useful methods associated with file objects, but one of the most commonly used is `readline()`. This method will read lines one-by-one from the file. Note that the end of line character (\n) is retained when the line is read in.
    - `firstLine = inFile.readline()`
  - Files opened for reading can be used in a `for` loop, as follows, to go through all the lines in the file:
        for line in file:
            print("Length of line is: %d" % (len(line)))
  - Note that `line` is just a variable name we've chosen to hold each line as we iterate through the file. You can use any variable name you choose, as with any other `for` loop.


- [ ] Writing to Files
  - Writing to a file is very similar to reading from a file. First, you define an output file name
    - `outFileName = "FileToWrite.txt"`
  - To create a file object to use for writing, we'll again use the `open()` function, but we'll specify `'w'` for the `<MODE>`.
    - `outFile = open(outFileName,'w')`
  - To write to the file line-by-line, we can use the `.write()` method.
    - `outFile.write("This is a new sentence.\n")`
    - Note that the `write()` method does NOT, by default, add a new line character to strings. If we want to end a line, we have to explicitly include `\n`.


- [ ] Command-line Arguments
  - As with bash scripts, Python scripts can also take advantage of command-line arguments.
  - To easily deal with command-line arguments, we're going to take advantage of some functions in the `sys` library. So we'll need to start by importing that library:
    - `import sys`
  - Any command-line arguments we pass to a script can then be accessed using the `sys.argv` variable.
    - `print(sys.argv[2])`
    - Which argument is printed when you run the line above? Does that make sense with the 0-based indexing in Python?
  - We can also loop through all command-line arguments:
        for arg in sys.argv:
            print(arg)
  - These abilities are very useful in a variety of contexts, but particularly when a set of filenames are provided as command-line arguments and you want to iteratively process each file.


- [ ] Defining New Functions
  - Thankfully, we are not limited to only using the functions that Python has built-in
  - We can define our own functions to take care of repetitive tasks
  - As our scripts become more complicated it will become increasingly important to start "packaging" commands together. This will make our scripts more readable and our code more reusable.
  - The basic syntax for defining a function is really simple:
        def myNewFunc(anArgument):
        """Explain here what your function does"""
            print(anArgument)
  - The keyword `def` tells Python that you are creating a new function.
  - The name of any arguments that you provide in the parentheses can be accessed with that variable name inside the function.
  - The part in the quotes is known as the docstring. It documents what your function does. Running `help(myNewFunc)` then allows anyone to see what your function is about.
  - Each function can contain as many lines of code as you want/need, as long as they are all indented by the same amount.
  - Many functions end with `return` statements. The point of the return statement is to make the value of a variable available to be saved or manipulated. Return statements, when included, are always the last line in a function definition. Here's an example:
        def factorial(num):
            product = 1
            while (num > 0):
                product = product * num
                num = num - 1
            return product

        myNum = factorial(5)


## References
- [Python File Objects](https://docs.python.org/2.4/lib/bltin-file-objects.html)
- [Python Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
