from name_function import get_formatted_name


print("Enter 'y' for yes or 'n' for no")
print("Enter 'q' at any time to quit.")

# register_voters = input("\nWould you like to register to vote? ")

while True:
    register_voters = input("\nWould you like to register to vote? ")
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

        
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")

    registered_voters = open('registered_voters.txt', 'a')
    registered_voters.write(formatted_name + '\n')
    registered_voters.close()
    print('Data appended to registered_voters.txt.')
    # registered_voters= open('registered_voters.txt', 'a')
    # save_results = input('Would you like to save your results? ')

    # if save_results == 'y':
        # Append the data to the file.
        # quiz_file.write(
        #     user + ': scored ' + str(score) + ' points : ' + str(current_time) + ' ' + str(current_date) + '\n')
        # Close the file.
    # registered_voters.close()
    # print('Data appended to quiz.txt.')


def all_registered_voters():
    # Open a file named philosophers.txt.
    infile = open('registered_voters.txt', 'r')

    # Read the file's contents.
    file_contents = infile.read()

    # Close the file.
    infile.close()

    # Print the data that was read into
    # memory.
    full_content = print(file_contents)
