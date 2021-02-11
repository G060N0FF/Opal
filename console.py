# import our language
import pinite

# read lines from console
print("Welcome to Pinite. Type 'quit' to exit.")
while True:
    line = input("Pinite > ")
    if line == "quit":
        break
    line_reader = pinite.Pinite(line)
    print(line_reader.get_tokens())
