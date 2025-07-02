import random_text_generator

def main():
    '''
    Purpose:
        To interact with the user, get options for text generation,
        and either print the generated random text or save it to a file.
    Parameter(s):
        None. Takes user input from the terminal.
    Return Value:
        None. Prints or writes the generated text.
    '''
    # Get number of words, must be positive int
    correct_choice = False
    while correct_choice == False:
        num_words_str = input("How many words do you want in the text? ")
        if num_words_str.isdigit() and int(num_words_str) > 0:
            num_words = int(num_words_str)
            correct_choice = True
        else:
            print("Please enter a positive integer for number of words.")

    # Capitalize random words? y/n
    correct_choice = False
    while correct_choice == False:
        cap_choice = input("Do you want random capitalization of some words? (y/n) ").strip().lower()
        if cap_choice in ['y', 'n']:
            capitalize_random_words = (cap_choice == 'y')
            correct_choice = True
        else:
            print("Please enter 'y' for yes or 'n' for no.")

    # Output option: terminal or file
    correct_choice = False
    while correct_choice == False:
        output_choice = input("Print to terminal or save to file? (t/f) ").strip().lower()
        if output_choice in ['t', 'f']:
            correct_choice = True
        else:
            print("Please enter 't' for terminal or 'f' for file.")

    # Generate the text
    generated_text = random_text_generator.random_words(num_words, capitalize_random_words)

    if output_choice == 't':
        # Print text to terminal
        print("\nGenerated text:\n")
        print(generated_text)
    else:
        # Ask for filename
        file_name = input("Enter filename (without extension): ").strip()
        if not file_name:
            file_name = "output"

        file_name = "output/" + file_name

        # Use existing file-writing code from random_text_generator
        random_text_generator.random_file(file_name, num_words, capitalize_random_words)
        print(f"Text saved to {file_name}.txt")

if __name__ == "__main__":
    main()
