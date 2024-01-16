
import re

def parse_markdown(file_path):
    # Define a dictionary to store replaced text
    references = {}

    # Read the Markdown file using an absolute path
    with open(file_path, 'r') as file:
        markdown_content = file.read()

    # Define the regex pattern to find text between double brackets
    pattern = r'\[\[(.*?)\]\]'

    # Use regex to replace text surrounded by double brackets with increasing question marks
    def replace_text(match):
        text_to_replace = match.group(1)
        references[len(references)] = text_to_replace
        question_marks = '?' * (len(references) + 2)  # Append two extra question marks for each replacement
        return f'[[{question_marks}]]'

    replaced_content = re.sub(pattern, replace_text, markdown_content)

    # Write the modified content back to the original file
    with open(file_path, 'w') as file:
        file.write(replaced_content)

    # Print the replaced content
    print(replaced_content)

    # Print the associative dictionary
    print("Associative Dictionary:")
    print(references)

    # User interaction loop
    for index in range(len(references)):
        user_input = input(f"What is the value at associative array index {index}? ")

        # Check if user input is correct
        if user_input == references[index]:
            print("Correct!")

            # Write back the correct value to the Markdown file
            replaced_content = replaced_content.replace(f'[[{"?" * (index + 3)}]]', f'[[{references[index]}]]', 1)
            with open(file_path, 'w') as file:
                file.write(replaced_content)
        else:
            while True:
                retry_input = input("Incorrect! Try again? (Y/N): ")
                if retry_input.upper() == 'Y':
                    user_input = input(f"What is the value at associative array index {index}? ")
                    if user_input == references[index]:
                        print("Correct!")

                        # Write back the correct value to the Markdown file
                        replaced_content = replaced_content.replace(f'[[{"?" * (index + 3)}]]', f'[[{references[index]}]]', 1)
                        with open(file_path, 'w') as file:
                            file.write(replaced_content)
                        break
                elif retry_input.upper() == 'N':
                    print("Moving to the next index.")

                    # Write back the value stored at the current index before moving to the next index
                    replaced_content = replaced_content.replace(f'[[{"?" * (index + 3)}]]', f'[[{references[index]}]]', 1)
                    with open(file_path, 'w') as file:
                        file.write(replaced_content)

                    break
                else:
                    print("Invalid input. Please enter Y or N.")

# Example usage:
file_path = '/home/matt/Documents/Obsidian Vault/TestFile.md'
parse_markdown(file_path)
