class StringUtility:
    def countWord(self, text):
        words = text.split(" ")
        count = 0
        i = 0
        
        while i < len(words):
            if words[i] != "":
                count = count + 1
            i = i + 1
        return count

    def findMostUsedChar(self, text):
        i = 0
        most = ""
        mostCount = 0
        
        # Goes through each character one by one
        while i < len(text):
            current = text[i]

            # Skip spaces
            if current.isspace():
                i = i + 1
                continue
            
            count = 0
            j = 0
            
            # This inner while loop is to count how many times the current character appears
            while j < len(text):
                if text[j] == current:
                    count = count + 1
                j = j + 1
            # Checks if this character has appeared more than the previous most
            if count > mostCount:
                mostCount = count
                most = current
            i = i + 1

        return most

# Main function to test the class
def main():
    utility = StringUtility()

    message1 = "Hello, My name is Silver and I play the accordion."
    print(f"Message:", message1)
    print(f"Word Count:", utility.countWord(message1))
    print(f"Most Used Character:", utility.findMostUsedChar(message1))
    print("\n") # New line to seperate messages.

    message2 = "Sally sold seashells by the seashore."
    print(f"Message:", message2)
    print(f"Word Count:", utility.countWord(message2))
    print(f"Most Used Character:", utility.findMostUsedChar(message2))
    # Added another message just to see a different output.

if __name__ == "__main__":
    main()

# Just a quick comment, before I implemented the skip space method my most used char for message1 was " ".
# I didn't like it this way so I used the ".isspace" from the modules to make a method that skips spaces.
