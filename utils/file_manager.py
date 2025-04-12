# Save/load .agileflow files

def save_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

def load_file(filename):
    with open(filename, 'r') as f:
        return f.read()