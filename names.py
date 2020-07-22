from name_function import get_formatted_name

from datetime import datetime, date

now = datetime.now()
today = date.today()
# Time abbreviation, hour min, and second
current_time = now.strftime("%H:%M:%S")
# Date abbreviation, day and year
current_date = today.strftime("%b-%d-%Y")

full_datetime = print("Time and Date =", current_time, current_date)

print("Enter 'y' for yes or 'n' for no")
print("Enter 'q' at any time to quit.")

# register_voters = input("\nWould you like to register to vote? ")

while True:
    register_voters = input("\nWould you like to register to vote? ")
    if register_voters == 'q':
        break
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
