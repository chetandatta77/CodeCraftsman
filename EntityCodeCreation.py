from EntityUseFullFunctions import *
from EntityData import *
from EntityFileCreation import createFile
from EntityPaths import *


def create_all_entities(text, path):
    rows = [i for i in text.split("\n") if i]
    for row in rows:
        val = [i.strip() for i in row.split('→')]
        cols = [i.strip() for i in val[1].split(',')]
        col_array = []
        a = val[0]
        for col in cols:
            col_array.append(column_code(col))
        name_file = file_name(a)
        file_data = file_total_code(a, col_array)
        createFile(name_file, file_data, path)


def create_all_repositories(text, path):
    rows = [i for i in text.split("\n") if i]
    for row in rows:
        val = [i.strip() for i in row.split('→')]
        a = val[0]
        name_file = file_name(a)
        file_data = file_total_repo_code(a)
        createFile(name_file + "Repository", file_data, path)


def service_code(text,path):
    file_data = ""
    rows = [i for i in text.split("\n") if i]
    for row in rows:
        val = [i.strip() for i in row.split('→')]

        a = val[0]
        ans = [''] * 12
        ans[0] = file_name(a)
        ans[1] = ans[0]
        ans[2] = column_name(a)
        ans[3] = ans[2]
        ans[4] = ans[0].upper()
        ans[5] = ans[2]
        ans[6] = ans[5]
        ans[7] = ans[6]
        ans[8] = ans[4]
        ans[9] = ans[6]
        ans[10] = ans[0]
        ans[11] = ans[0]

        file_data += service_bolier_code.format(*ans)

    name_file = 'serCode'
    createFile(name_file, file_data, path)


def autowired_code(text,path):
    file_data = ""
    rows = [i for i in text.split("\n") if i]
    for row in rows:
        val = [i.strip() for i in row.split('→')]

        a = val[0] + '_repository'
        ans = [''] * 2
        ans[0] = file_name(a)
        ans[1] = column_name(a)

        file_data += autboiler_code.format(*ans)

    name_file = 'AutoCode'
    createFile(name_file, file_data, path)


def load_code_lines(text,path):
    file_data = ""
    rows = [i for i in text.split("\n") if i]
    for row in rows:
        val = [i.strip() for i in row.split('→')]

        a = val[0]
        ans = [''] * 1
        ans[0] = file_name(a)

        file_data += load_boiler_code.format(*ans)

    name_file = 'loadCode'
    createFile(name_file, file_data, path)


# service_code(extra_text,actual_service_path)
# autowired_code(extra_text,actual_service_path)
# load_code_lines(extra_text,actual_service_path)
create_all_entities(extra_text, actual_entity_path)
# create_all_repositories(extra_text,actual_repository_path)