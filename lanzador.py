from ConversationFormatter import ConversationFormatter


def main():
    # Original text
    text = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
    
    # Create an instance of ConversationFormatter
    formatter = ConversationFormatter(text)
    
    # Format the conversation
    formatted_text = formatter.format_conversation()
    
    # Print the formatted conversation
    print(formatted_text)