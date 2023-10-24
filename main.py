import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"
#/*data = clipboard.paste()
#clipboard.copy("abc")

#print(data)

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}
    
def remove_data(filepath, key):
    # Read the JSON data from the file
    with open(filepath, "r") as f:
        data = json.load(f)

    # Remove the specified data
    if key in data:
        data.remove(key)

    # Write the updated data back to the file
    with open(filepath, "w") as f:
        json.dump(data, f)


if len(sys.argv) == 2:
    command = sys.argv[1]
    print(command)
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA,data)
        print("Data Saved.")

    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data Copied to Clipboard.")
        else:
            print("Key does not exist.")

    elif command == "list":
        print(data)

    elif command == "del":
        key = input("Enter a Key to Delete: ")
        if key in data:
            data[key] = clipboard.paste()
            remove_data(SAVED_DATA, key)
            print("Data Deleted.")
        else:
            print("Key does not exist.")
    else:
        print("Unknown Command")
else:
    print("Please enter a valid command")