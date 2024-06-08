import os

def print_directory_structure(directory):
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        if 'env' in dirs:
            dirs.remove('env')  # Excluir la carpeta 'env'
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")

directory = "D:/LLEVARME/git/InmoFinanzasAGV/server"
print_directory_structure(directory)
