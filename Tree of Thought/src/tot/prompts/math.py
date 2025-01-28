
standard_prompt = ''' You are a math expert, answer the following question. When you respond, thinking step by step. 
At the end of the solution, when you give your final answer, write it in the form "I hope it is correct #### $answer$" 
'''

cot_prompt = ''' You are a math expert, answer the following question. When you respond, thinking step by step and
write out each line of reasoning/working like how a student at school would write his homework. 
At the end of the solution, when you give your final answer, write it in the form "I hope it is correct #### $answer$" 
'''

propose_prompt = '''
Input: Solve \(x^2 - 5x + 6 = 0\)
Possible next steps: 
I can factorize \(x^2 - 5x + 6\) into \((x - 2)(x - 3) = 0\)
I can use the quadratic formula: \(x = \frac{-(-5) \pm \sqrt{(-5)^2 - 4(1)(6)}}{2(1)}\)
I can complete the square by rewriting \(x^2 - 5x = -6\)
I can use the rational root theorem to find the roots of the polynomial
Input: Simplify \(\frac{2x + 4}{x + 2}\)
Possible next steps:
I can factor out a 2 from the numerator to get \(2(x + 2)\)
I can rewrite the fraction as \(\frac{2x}{x+2} + \frac{4}{x + 2}\)
I can use long division to simplify the fraction
Input: Solve \(2x + 5 > 3x - 1\)
Possible next steps:
I can subtract \(2x\) from both sides to get \(5 > x - 1\)
I can subtract \(3x\) from both sides: \(2x - 3x + 5 > -1\)
I can rearrange the equation to \(2x - 3x > -1 - 5\)
Input: {input}
Possible next steps: 
'''

value_prompt = r'''Evluate if this line of reasoning is correct (sure/likely/impossible)
If \(x^2 = 4\), then \(x = 2\)
The equation \(x^2 = 4\) has two solutions: \(x = 2\) and \(x = -2\)
The reasoning only considers one solution, so it is incomplete but not entirely wrong
likely
To find the derivative of \(x^3\), we use the power rule and get \(3x^2\)
The power rule for derivatives states \( \frac{d}{dx} [x^n] = nx^{n-1} \)
Applying this to \(x^3\), we get \(3x^2\), which is correct
sure
The integral of \(e^x\) with respect to \(x\) is \(e^x + C\)
The integral of \(e^x\) is a well-known result and evaluates to \(e^x + C\), where \(C\) is the constant of integration
This reasoning is accurate and complete
sure
The equation \(x + 2 = x + 3\) has infinitely many solutions
Subtract \(x\) from both sides: \(2 = 3\), which is clearly false.
The reasoning is fundamentally incorrect since no solution exists, let alone infinitely many
impossible
''' + "{input}"