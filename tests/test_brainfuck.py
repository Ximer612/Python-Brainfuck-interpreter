import unittest
from brainfuck import BrainFuckTape, OddBrackets

# command to start test => python -m unittest .\tests\test_brainfuck.py   

class Vector2Test(unittest.TestCase):
    
    def test_hello_world(self):
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
        
        text = BrainFuckTape(hello_world_text).convert_text()
        self.assertEqual(text,"Hello World")   
     
    def test_add(self):        
        one_add_text = BrainFuckTape("+.").convert_text()        
        self.assertEqual(ord(one_add_text),1)  
        
    def test_subtract(self):        
        one_sub_text = BrainFuckTape("-.").convert_text()        
        self.assertEqual(ord(one_sub_text),255)
        
    def test_just_print(self):        
        one_print = BrainFuckTape(".").convert_text()        
        self.assertEqual(ord(one_print),0)
        
    def test_one_move_forward(self):        
        one_move_forward = BrainFuckTape(">+.").convert_text()        
        self.assertEqual(ord(one_move_forward),1)  
        
    def test_negative_move_tape(self):        
        one_move_backward = BrainFuckTape("<+.").convert_text()        
        self.assertEqual(ord(one_move_backward),1)  
        
    def test_no_text(self):        
        text = BrainFuckTape("").convert_text()
        self.assertEqual(text,"")     
        
    def test_nested_loops(self):       
        nested_loop_text = """
                    ++++[>++++[>++++<-]<-]>>.            
                    """ 
        text = BrainFuckTape(nested_loop_text).convert_text()
        self.assertEqual(text,"@")    
    
    def test_odd_brackets(self):       
        odd_text = """
                    ++++[>++++[>++++<-]<-]]>>.            
                    """ 
        with self.assertRaises(OddBrackets):
            tape = BrainFuckTape(odd_text)
        
    def test_not_valid_text(self):       
        test_text = """
                    asbdouabsoaihcd2398c4yascda2@#|3sadc.           
                    """ 
        
        tape = BrainFuckTape(test_text)    
        text =  tape.convert_text()
        self.assertEqual(ord(text),0)
        
if __name__ == '__main__':
    unittest.main()