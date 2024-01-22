
import re
import os
import time

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
        question_marks = '?' * (len(references))  # Append two extra question marks for each replacement
        return f'[[{question_marks}]]'

    replaced_content = re.sub(pattern, replace_text, markdown_content)

    # Write the modified content back to the original file
    with open(file_path, 'w') as file:
        file.write(replaced_content)

    # Check other markdown files in the parent directory
    parent_directory_path = os.path.dirname(file_path)

    for filename in os.listdir(parent_directory_path):
        if filename.endswith('.md') and filename != os.path.basename(file_path):
            original_filename = os.path.splitext(filename)[0]

            # Check if the file name is a reference
            if original_filename in references.values():
                position = list(references.values()).index(original_filename)
                associated_string = '?' * (position + 1)
                new_file_path = os.path.join(parent_directory_path, associated_string + '.md')
                os.rename(os.path.join(parent_directory_path, filename), new_file_path)

    start_time = time.time()

    # Prompt the user to resolve references
    skipped_indices = []

    for index in range(len(references)):
        user_input = input(f"\nWhat is the subject for {'?' * (index + 1)}\n ").lower()

        # Check if user input is correct
        if user_input == references[index].lower():
            print("\nCorrect!")

            # Write back the correct value to the Markdown file
            replaced_content = replaced_content.replace(f'[[{"?" * (index + 1)}]]', f'[[{references[index]}]]', 1)
            with open(file_path, 'w') as file:
                file.write(replaced_content)

            # Rename the file back to the correct value
            restored_filename = os.path.join(parent_directory_path, references[index] + '.md')
            os.rename(new_file_path, restored_filename)

            question_marks = '?' * (index + 2)
            filename_without_extension, extension = os.path.splitext(restored_filename)
            new_path = os.path.dirname(filename_without_extension) + '/'
            new_file_path = f'{new_path}{question_marks}.md'

        else:
            skipped_indices.append(index)
            while True:
                retry_input = input("\nIncorrect! Try again? (Y/N):").lower()
                if retry_input == 'y':
                    user_input = input(f"\nWhat is the subject for {'?' * (index + 1)}\n ").lower()
                    if user_input == references[index].lower():
                        print("\nCorrect!")

                        # Write back the correct value to the Markdown file
                        replaced_content = replaced_content.replace(f'[[{"?" * (index + 1)}]]', f'[[{references[index]}]]', 1)
                        with open(file_path, 'w') as file:
                            file.write(replaced_content)

                        # Rename the file back to the correct value
                        restored_filename = os.path.join(parent_directory_path, references[index] + '.md')
                        os.rename(new_file_path, restored_filename)

                        question_marks = '?' * (index + 2)
                        filename_without_extension, extension = os.path.splitext(restored_filename)
                        new_path = os.path.dirname(filename_without_extension) + '/'
                        new_file_path = f'{new_path}{question_marks}.md'

                        # Remove the index from skipped_indices since the user got it correct after retrying
                        if index in skipped_indices:
                            skipped_indices.remove(index)

                        break
                elif retry_input == 'n':
                    print("\nMoving to the next index.")

                    restored_filename = os.path.join(parent_directory_path, references[index] + '.md')

                    question_marks = '?' * (index + 2)
                    filename_without_extension, extension = os.path.splitext(restored_filename)
                    new_path = os.path.dirname(filename_without_extension) + '/'
                    new_file_path = f'{new_path}{question_marks}.md'

                    break
                else:
                    print("Invalid input. Please enter Y or N.")

        # Process skipped indices
    for skipped_index in skipped_indices:
        # Write back the correct value to the Markdown file for skipped indices
        replaced_content = replaced_content.replace(f'[[{"?" * (skipped_index + 1)}]]', f'[[{references[skipped_index]}]]', 1)

        # Rename the file back to the correct value for skipped indices
        restored_filename = os.path.join(parent_directory_path, references[skipped_index] + '.md')
        new_file_path = os.path.join(parent_directory_path, '?' * (skipped_index + 1) + '.md')
        os.rename(new_file_path, restored_filename)

    # Write back the correct values for skipped indices to the Markdown file
    with open(file_path, 'w') as file:
        file.write(replaced_content)

    end_time = time.time()
    elapsed_time = end_time - start_time
    retention_rate = (len(references) - len(skipped_indices)) / len(references) if len(references) != 0 else 0

    print(f"\nTime taken to finish: {elapsed_time:.2f} seconds")
    print(f"Retention rate: {retention_rate * 100:.2f}% (Correct: {len(references) - len(skipped_indices)}/{len(references)})")

# Example usage:
file_path = '/home/matt/Documents/obsidian_bubble_vault/bubble_trainer/History.md'
parse_markdown(file_path)
