ciao_text =  """
            ++++++++[>++++++++<-]>+++.
            <++++++[>++++++<-]>++.
            <++[>----<-]>.
            <++[>+++++++<-]>.             
        """
        
hello_world_text =  """
            +++++++++[>++++++++<-]>.
            <++++++[>+++++<-]>-.
            +++++++..
            +++.

            <++++++++[>>++++<<-]>>.
            <<++++++[>>+++++++++<<-]>>+.
            <.
            +++.
            ------.
            <++[>----<-]>.         
        """

A_char = """
            ++++[>++++[>++++<-]<-]>>+.            
            """
            
odd_brackets_text = """
                    ++++[>++++[>++++<-]<-]]>>.            
                    """ 

class OddBrackets(Exception):
    
    def __init__(self):
        super().__init__("Is missing a bracket")

class BrainFuckTape():
    def __init__(self, text:str, tape_size:int = 16):
        
    # IF THERE ARE NOT CLOSED BRACKETS TROW AN EXPECTION  
        brackets_num = 0
        for char in text:
            if char == '[' or char == ']':
                brackets_num+=1
        
        if brackets_num % 2 != 0: 
            raise OddBrackets()
        
        self.text = text
        self.head_position = 0
        self.tape = [0]*tape_size
     
    def convert_text(self):
        output_text = ""
        
        if len(self.text) < 1: return output_text
        
        text_index = 0
        while text_index != len(self.text):
            actual_command = self.text[text_index]
            text_index+=1
            
            if actual_command in (" ","\t","\n","\r"):
                continue
            
            elif actual_command == "+":
                self.tape[self.head_position]+=1
                self.tape[self.head_position] %= 256 
                
            elif actual_command == "-":
                self.tape[self.head_position]-=1
                self.tape[self.head_position] %= 256
                
            elif actual_command == ".":                
                output_text = output_text + (chr(self.tape[self.head_position]))
                
            elif actual_command == ",":
                self.tape[self.head_position] = ord(input())
                
            elif actual_command == ">":   
                self.head_position+=1                
                
            elif actual_command == "<":   
                self.head_position-=1                
                
            elif actual_command == "[":   
                if self.tape[self.head_position] == 0:
                    brackets_to_skip = 0
                    last_tape_index = text_index+2            
                    while last_tape_index != len(self.text):
                        if self.text[last_tape_index]== "]":
                            if brackets_to_skip == 0:
                                text_index = last_tape_index+1
                                break
                            else: 
                                brackets_to_skip -=1
                        elif self.text[last_tape_index]== "[":
                            brackets_to_skip +=1
                        last_tape_index+=1
                            
            elif actual_command == "]":   
                if self.tape[self.head_position] != 0:
                    brackets_to_skip = 0
                    last_tape_index = text_index-2            
                    while last_tape_index > 0:
                        if self.text[last_tape_index]== "[":
                            if brackets_to_skip == 0:
                                text_index = last_tape_index+1
                                break
                            else: 
                                brackets_to_skip-=1
                        elif self.text[last_tape_index]== "]":
                            brackets_to_skip +=1
                        last_tape_index-=1
    
        return output_text
        

if __name__ == "__main__":
    text = BrainFuckTape(hello_world_text).convert_text()
    print(text)
