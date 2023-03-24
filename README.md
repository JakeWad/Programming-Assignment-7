Lewis University SP23-CPSC-46000-LT1-Programming Languages
Programming-Assignment-7

1. Given a well-balanced algebraic expression (all parentheses given).  Construct a corresponding expression syntax tree. (All)number or id single digit or letter assumed)
 
	You may use Stack, infixToPostfix, and other programs from Lecture 8.  
		a. Get an infix expression. 
		b.Convert it to postfix. 
		c.Then, use postfix to build an evaluation tree.
		d.After that, perform infix traversal
 
	Sample Input:

		4 + ((7 + 9) * 2)
 
	Sample Output:

		Infix:  4+((7+9)*2)

		Postfix:  479+2*+

		Infix Traversal of the Eval-Tree: (4 + ((7 + 9 )* 2 ))
