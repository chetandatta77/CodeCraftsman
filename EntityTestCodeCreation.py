from EntityData import *
from EntityFileCreation import createFile
from EntityPaths import *
from EntityUseFullFunctions import *
import os


def test_files():
    # only_list = ['BusinessUnit.java']
    for filename in os.listdir(actual_entity_path):
        # if filename not in only_list:
        #     continue
        # print(filename)
        with open(os.path.join(actual_entity_path, filename), 'r') as f:
            data = f.read()
            name_file = class_name(data)
            var_name = class_var_name(name_file)
            file_data = segregate_setters_getters(data,var_name)

            createFile(name_file+'Test',junit_boiler_code.format(name_file,var_name,file_data), actual_test_path)
    # pass


def test_service_code():
    for filename in os.listdir(actual_service_path):
        with open(os.path.join(actual_service_path, filename), 'r') as f:
            data = f.read()
            file_data = test_service_code_lines(data)

            part = when_code_lines(data)
            file_data = part[0] + part[1] + part[2] + part[3]
        createFile('xyz', file_data, actual_service_test_path)
        # break


def contructor_code(data):
    file_data = ''
    data = data.split('\n')
    for line in data:
        if line:
            file_data += constructor_boiler_code.format(line.strip()[:-1])
    createFile('xyz', file_data, service_test_path)


# test_service_code()
test_files()