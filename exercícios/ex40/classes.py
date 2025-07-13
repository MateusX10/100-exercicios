class Stack:


    def __init__(self):

        self.pilha = []

    
    def push(self, elemento):

        self.pilha.append(elemento)


    def pop1(self):


        if not self.is_empty():

            self.pilha.pop()

            return self.pilha[-1] if not self.is_empty() else "\033[1;31mPilha sem elementos!\033[m"
        
        else:


            print("\033[1;31mPilha vazia!\033[m")
        

    def top(self):


        if not self.is_empty():


            return self.pilha[-1]
        
        else:


            return "\033[1;31mPilha vazia!\033[m"
    

    def is_empty(self):


        if self.pilha:

            print("\033[1;32mPilha não está vazia!\033[m")

            return False


        else:

            print("\033[1;31mPilha vazia!\033[m")
    

            return True

        
    def size(self):


        return len(self.pilha)
