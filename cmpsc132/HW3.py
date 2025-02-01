# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        return self.top == None

    def __len__(self): 
        # YOUR CODE STARTS HERE
        count = 0
        temp = self.top
        while temp:
            count += 1
            temp = temp.next
        return count

    def push(self,value): 
        # YOUR CODE STARTS HERE
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node


     
    def pop(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return None
        else: 
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value

    def peek(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return None
        else:
            return self.top.value


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None
        


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        txt = txt.strip()
        try:
            float(txt)
            return True
        except:
            return False




    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack object for expression processing

            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix('( 2 { 5.0 } )')
            '2.0 5.0 *'
            >>> x._getPostfix(' 5 ( 2 + { 5 + 3.5 } )')
            '5.0 2.0 5.0 3.5 + + *'
            >>> x._getPostfix ('( { 2 } )')
            '2.0'
            >>> x._getPostfix ('2 * ( [ 5 + -3 ] ^ 2 + { 1 + 4 } )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('[ 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ]')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( { 2 * { { 5 + 3 } ^ 2 + ( 1 + 4 ) } } )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * ( -5 + 3 ) ^ 2 + [ 1 + 4 ]')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ]')
            >>> x._getPostfix(' ( 2 * { 5 + 3 ) ^ 2 + ( 1 + 4 ] }')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')
        '''

        # YOUR CODE STARTS HERE
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        operators = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary to store the precedence of the operators 3 is the highest
        if not self.isValid(txt): # check validity of the expression
            return None
        postfix = []
        txt = self.implicitMultiplication(txt)
        tokens = txt.split()
        for token in tokens:                        # convert infix to postfix
            if self._isNumber(token):               # if token is a number, append it to the postfix list
                postfix.append(float(token))       
            elif token in ['(','{','[']:            # if token is an opening bracket, push it to the stack
                postfixStack.push(token)
            elif token in [')','}',']']:            # if token is a closing bracket, pop all the operators from the stack and append them to the postfix list until an opening bracket is found
                while postfixStack.peek() not in ['(','{','[']:
                    postfix.append(postfixStack.pop())
                postfixStack.pop()
            else:                                  
                while not postfixStack.isEmpty() and postfixStack.peek() in operators and operators[postfixStack.peek()] >= operators[token] and token != '^': 
                    # if token is an operator, pop all the operators from the stack with higher or equal precedence and append them to the postfix list                
                    postfix.append(postfixStack.pop())
                postfixStack.push(token)
        while not postfixStack.isEmpty():          # pop all the remaining operators from the stack and append them to the postfix list
            postfix.append(postfixStack.pop())
        return ' '.join(map(str, postfix))        # return the postfix list as a string
    
    def implicitMultiplication(self, txt):
        tokens = txt.split() 
        for i in range(len(tokens)-1): 
            if self._isNumber(tokens[i]) and tokens[i+1] in ['(','{','[']: # if a number is followed by an opening bracket, insert a * between them
                tokens.insert(i+1,'*')
            elif tokens[i] in [')','}',']'] and (self._isNumber(tokens[i+1]) or tokens[i+1] in ['(','{','[']): # if a closing bracket is followed by a number or an opening bracket, insert a * between them
                tokens.insert(i+1,'*')
        return ' '.join(tokens) # return the modified expression as a string
    
    def isValid(self, txt):
        tokens = txt.split()
        brackets = Stack() # stack to store the brackets
        
        for i in range(len(tokens)-1): # check for invalid tokens and consecutive numbers/operators
            token = tokens[i]
            if not (self._isNumber(tokens[i]) or tokens[i] in ['+','-','*','/','^','(',')','{','}','[',']']):
                return False
            if (tokens[i] in ['+','-','*','/','^'] and tokens[i+1] in ['+','-','*','/','^']) or self._isNumber(tokens[i]) and self._isNumber(tokens[i+1]): 
                return False
        if tokens[0] in ['+','-','*','/','^'] or tokens[-1] in ['+','-','*','/','^']: # check for invalid starting and ending tokens
            return False
        for i in range(1, len(tokens)-1): # check for missing operands
            token = tokens[i]
            if tokens[i] in ['+','-','*','/','^'] and (tokens[i+1] in [')','}',']'] or tokens[i-1] in ['(','{','[']):
                return False
       
        for token in tokens: # check for unbalanced brackets
            if token in ['(','{','[']:
                brackets.push(token)
            elif token in [')','}',']']:
                if brackets.isEmpty():                    
                    return False
                if token == ')' and brackets.peek() != '(':                    
                    return False
                if token == '}' and brackets.peek() != '{':                    
                    return False
                if token == ']' and brackets.peek() != '[':                    
                    return False
                brackets.pop()
            
        
        if not brackets.isEmpty(): # check for unbalanced brackets
            return False
        return True
            
    
            







    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack object to compute the final result as shown in the video lectures
            

            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( [ ( 10 - 2 * 3 ) ] )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * { 3 - 2.45 * [ 4 - 2 ^ 3 ] } + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * [ 4 + 2 * { 5 - 3 ^ 2 } + 1 ] + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + { 3.0 } * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * [ 4 ] ) * [ 2 / 8 + 2 * ( 3 - 1 / 3 ) ] - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            >>> x.setExpr('( 3.5 ) [ 15 ]') 
            >>> x.calculate
            52.5
            >>> x.setExpr('3 { 5 } - 15 + 85 [ 12 ]') 
            >>> x.calculate
            1020.0
            >>> x.setExpr("( -2 / 6 ) + ( 5 { ( 9.4 ) } )") 
            >>> x.calculate
            46.666666666666664
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( ( 2 ) * 10 - 3 * [ 2 - 3 * 2 ) ]')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression

        # YOUR CODE STARTS HERE
        expession = self._getPostfix(self.__expr)
        if expession is None: # check validity of the expression
            return None
        tokens = expession.split()
        for token in tokens: 
            if self._isNumber(token):
                calcStack.push(float(token))
            else:                              # if token is an operator, pop the last two numbers from the stack, perform the operation and push the result back to the stack
                num2 = calcStack.pop()
                num1 = calcStack.pop()
                if token == '+':
                    calcStack.push(num1 + num2)
                elif token == '-':
                    calcStack.push(num1 - num2)
                elif token == '*':
                    calcStack.push(num1 * num2)
                elif token == '/':
                    if num2 == 0:
                        return None
                    calcStack.push(num1 / num2)
                elif token == '^':
                    calcStack.push(num1 ** num2)
        return calcStack.pop()



#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 [ x1 - 1 ];x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * { x1 / 2 };x1 = x2 * 7 / x1;return x1 ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * { x1 / 2 }': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        if len(word) != 0 and word[0].isalpha() and word.isalnum(): # check if the word starts with a letter and contains only letters and numbers
            return True
        return False
    

       

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 ( x1 - 1 )')
            '7 ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        tokens = expr.split()
        new_expr = []
        calcObj = Calculator()
        for token in tokens: # replace the variables with their values
            if self._isVariable(token):
                if token in self.states: # if the token is a variable, replace it with its value
                    new_expr.append(str(self.states[token]))
                else:
                    return None          # undefined variable
            else:
                if token in ['+','-','*','/','^','(',')','{','}','[',']'] or calcObj._isNumber(token): # if the token is an operator or a number or valid bracket, append it to the new expression
                    new_expr.append(token)
                else:
                    return None          # invalid token
        return ' '.join(new_expr)
            
    
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        out = {}
        expressions = self.expressions.split(';') # split the expressions
        for expression in expressions:
            if '=' in expression: # if the expression is an assignment, store the variable and its value in the states dictionary
                var, expr = expression.split('=')
                var = var.strip()
                expr = expr.strip()
                expr = self._replaceVariables(expr)
                if expr is None or not self._isVariable(var): # check validity of the expression and the variable
                    self.states = {}
                    return None
                else:
                    calcObj.setExpr(expr)
                    result = calcObj.calculate
                    if result is None: # calculation error
                        self.states = {}
                        return None
                    self.states[var] = result                    
                    out[expression] = self.states.copy()
            else:
                expr = self._replaceVariables(expression.split('return')[1].strip()) # get the expression after the return keyword and replace the variables with their values
                if expr is None: # check validity of the expression
                    self.states = {}
                    return None
                calcObj.setExpr(expr)
                result = calcObj.calculate
                if result is None: # calculation error
                    self.states = {}
                    return None
                out['_return_'] = calcObj.calculate
                
        return out



def run_tests():
    import doctest

    #- Run tests in all docstrings
    # doctest.testmod(verbose=True)
    
    #- Run tests per class - Uncomment the next line to run doctest by function. Replace Stack with the name of the function you want to test
    # doctest.run_docstring_examples(AdvancedCalculator.calculateExpressions, globals(), name='HW3',verbose=False)   
    

if __name__ == "__main__":
    run_tests()