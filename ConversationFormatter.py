class ConversationFormatter:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text
    
    
    def format_conversation(self):
        # Split the text by '#' to separate the sentences
        sentences = self.text.split('#')
        
        # Capitalize the first letter of the first sentence
        sentences[0] = sentences[0].capitalize() + "..."
        
        # Capitalize the first letter of each subsequent sentence and add a period at the end
        for i in range(1, len(sentences)):
            sentences[i] = sentences[i][0].upper() + sentences[i][1:] + '.'
        
        # Join the sentences with new lines
        formatted_text = '\n'.join(sentences)
        
        return formatted_text