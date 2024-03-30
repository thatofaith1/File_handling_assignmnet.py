# handle file assignment 

def write_to_file(filename):
    try:
        with open(filename, "w") as f:
            f.write("This weekend I'm going to spend it all\n")
            f.write("This is my number 0722284487\n")
            f.write("Weekend special is on me\n")

    except FileNotFoundError:
        print(f"Error: file '{filename}' not found")
    except PermissionError:
        print(f"Error: Permission denied to write '{filename}',")
    except Exception as e:
        print(f"Error:{e}")
    else:
        print("File created and written successfully.")

def read_and_display(filename):
    try: 
        with open(filename, "r") as f:
            contents = f.read()
            print("Contents of 'my_file.txt', ")
            print(contents)

    except FileNotFoundError:
        print(f"Error: file '{filename}' not found")
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}',")
    except Exception as e:
        print(f"Error:{e}")


def append_to_file(filename):
    try:
        with open(filename, "a") as f:
            f.write("\n This is where I draw the line")
            f.write("\n 0719753442 I changed my number")
            f.write("\n The weekend is over, back to reality")

    except FileNotFoundError:
        print(f"Error: file '{filename}' not found")
    except PermissionError:
        print(f"Error: Permission denied to append '{filename}',")
    except Exception as e:
        print(f"Error:{e}")

    else:
        print("File created and appended successfully.")

if __name__ == "__main__":
    filename = "my_file.txt"  

    # writing the file
    write_to_file(filename)

    # reading and displaying the file
    read_and_display(filename)

    # appending the file
    append_to_file(filename)

    # reading and displaying the uodated file
    read_and_display(filename)


 

        