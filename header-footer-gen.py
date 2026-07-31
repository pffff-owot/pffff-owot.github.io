import os


def get_files_to_change(directory: str):
    files=[]
    for thing in os.scandir(directory):
        if thing.is_file and thing.name.endswith(".html"):
            #print(thing.path)
            #print(thing.name)
            files.append(thing.path)
    return files

def replace_balise_in_file(changed_file_filepath: str,template_file: str, balise: str):
    new_header = get_balise_from_file(balise,template_file)[1]
    file_content = get_balise_from_file(balise,changed_file_filepath)
    changed_file = file_content[0] + new_header + file_content[2]
    return changed_file
    

def get_balise_from_file(balise: str, filepath: str):
    in_balise = 0 #0=before, 1=in, 2=after
    balise_content=["", "", ""] #balise_content[0]=file content before the balise, ...[1]=in, ...[2]=after
    file_content=open(filepath, encoding="utf-8")
    for line in file_content:
        if f"<{balise}>" in line:
            in_balise = 1
        balise_content[in_balise] = balise_content[in_balise] + line
        if f"</{balise}>" in line:
            in_balise = 2
    file_content.close()
    return balise_content


for file_to_change in get_files_to_change("."):
    new_content=replace_balise_in_file(file_to_change, "./template", "header")
    file=open(file_to_change, "w")
    file.write(new_content)
    file.close()
    new_content=replace_balise_in_file(file_to_change, "./template", "footer")
    file=open(file_to_change, "w")
    file.write(new_content)
    file.close()
    