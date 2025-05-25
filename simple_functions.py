 #Honestly Mr Mubaraq I decided to just play around with both because the 2 questions were interesting
def text_reverser(text):

    """Reverse the input text."""
    reversed_text = text[::-1]
    
    print(f"This is the original: {text} \n This is the reversed: {reversed_text}")
    return reversed_text

def calculator(operation:str, num1, num2):
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
         result = num1 - num2
    elif operation == "*":
         result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        result = num1 / num2
    else:
        raise ValueError("Invalid operation. Use +, -, *, or /")
    print(f"calculation: {num1} {operation}  {num2} = {result}")
    return result

text_reverser("'heyy I am a Man of God'")

calculator("+",2,2)