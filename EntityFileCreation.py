import os.path




def createFile(name_of_file, file_data,path):
    save_path = path

    complete_name = os.path.join(save_path, name_of_file + ".java")

    file1 = open(complete_name, "w")
    file1.write(file_data)
    file1.close()
