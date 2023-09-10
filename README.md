# re ( regular expression )
Python re module is a set of functions that allow us to search, match, and extract patterns from strings. 
1. What exactly is a Regular Expression?
A regular expression, often called a pattern, is an expression used to specify a set of strings required for a particular purpose.

A simple way to specify a finite set of strings is to list its elements or members.
For example {file, file1, file2}.

However, there are often more concise ways to specify the desired set of strings.
For example, the set {file, file1, file2} can be specified by the pattern file(1|2)?.
We say that this pattern matches each of the three strings. Wanna check?

In most formalisms, if there exists at least one regular expression that matches a particular set then there exists an infinite number of other regular expressions that also match it, i.e. the specification is not unique.

For example, the string set {file, file1, file2} can also be specified by the pattern file\d?.
