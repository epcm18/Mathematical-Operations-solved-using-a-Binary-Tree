class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def get_output(self):
        '''
        Print the output depending on the evaluated value.
        If the 0 <= value <= 999 the value is printed.
        If the value < 0, UNDERFLOW is printed.
        If the value > 999, OVERFLOW is printed.

        :return: None
        '''
        value = self.evaluate()
        if value > 999:
            print('OVERFLOW')
        elif value < 0:
            print('UNDERFLOW')
        else:
            print(value)

    #####################################################################
    ######### Your task is to implement the following methods. ##########
    #####################################################################
    
    def insert(self, data, bracketed):
        '''
        Insert operators and operands into the binary tree.

        :param data: Operator or operand as a tuple. E.g.: ('OPERAND', 34), ('OPERATOR', ‘+’)
        :param bracketed: denote whether an operator is inside brackets or not. If the operator is inside brackets,
        we set bracketed as True.
        :return: self
        '''
        
        #Include your code here
        
        #Everytime when the function is calling it created a node and 
        #assigned it to a variable
        temp_node= Node(data)
        
        #when the braketed is true the right root will be the new node's left
        #and the new node will become the right root
        if bracketed is True:
            temp_node.left = self.right
            self.right = temp_node
        
        elif (data[0])=='OPERATOR' and bracketed is False:
            #the new node will become the parent of the binary tree
            temp_node.left = self
            self = temp_node
        
        elif (data[0]) == 'OPERAND':
            if self.right is None:
                #when there's no right child the new data added to that root
                self.right = temp_node
            else:
                #when there's data in the right root it created a new right
                #root for it and assigned the data
                self.right.right = temp_node
                
        return self

    def evaluate(self):
        '''
        Process the expression stored in the binary tree and compute the final result.
        To do that, the function should be able to traverse the binary tree.

        Note that the evaluate function does not check for overflow or underflow.

        :return: the evaluated value
        '''
        
        #Include your code here
        
        #evaluate the value recursively
        #base case gives the value when it is a leaf
        if self.data[0]=='OPERAND':
            return self.data[1]
        if self.data[0]=='OPERATOR':
            #evaluate left children and right children and then combine
            #them
            result=Node.arithmatic(self.left.evaluate(),self.data[1],self.right.evaluate())
            return result
            
            
    @staticmethod
    def arithmatic(num1,operation,num2):
        '''
        use this function to evaluate the values of the binary tree
        :num1 - integer
        :num2 - integer
        :operation - mathematical operations like (+,-,*,^)
        when the three parameters are given it perform the mathematical
        operation.
        
        '''
        if operation=='+':
            return num1 + num2
        if operation=='-':
            return num1 - num2
        if operation=='*':
            return num1 * num2
        if operation=='^':
            return num1 ** num2