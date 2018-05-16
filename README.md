# SyntaxDB Python API

SyntaxDB is basically a powerful programming search engine that helps you to search various programming concepts and syntax with ease. Here, we focus on implementing a python module that helps you to utlise the API in an efficient manner in your Python programs.<br/>

We'll help you use the functionalities of SyntaxDB without any hassles. Do try it out and raise any issues that prevail. <br/>

## HOW TO USE THIS API ?
Firstly create an object of Syntaxdb class

    syntax_object = syntaxdb.Syntaxdb(user_choice = <>,user_search=<>,user_language=<>)

Here, you should fill in your own data inplace of <>.<br/>
Also, user_language and user_search could be optional args. You could use either one of them.

### user_choice
- Can be 0 or 1
- Use 0 if you want to search for a particular concept in a programming language.
```
     Example: If you want to know what a for loop does in python,
     syntax_object = syntaxdb.Syntaxdb(user_choice = 0,user_search= "for in python")
```
- Use 1 if you want to get all the concepts of a particular programming language.
```
     Example: If you want to know about all the basic concepts in Java,
     syntax_object = syntaxdb.Syntaxdb(user_choice = 1,user_langauge= "java")
```

### user_search and user_langauge
- user_search must be filled if choice is 0
- user_language must be filled if choice is 1
- The example in user_choice would make things clear for you! Please have a look again carefully.

## Support us if you like this project, by starring this repository
