def write_file(file_name, file_content):
    file = open(f"{file_name}.txt", mode='w')
    file.write(file_content)

def append_file(file_name, append_content):
    open(f"{file_name}.txt", mode='a').write(append_content)

def read_file(file_name):
    return open(f"{file_name}.txt").read()
