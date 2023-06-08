from EntityData import *


def column_name(a):
    ans = ''
    i = 0
    while i < len(a):
        if a[i] == '_':
            i += 1
            ans += a[i].upper()
        else:
            ans += a[i]
        i += 1
    return ans


def file_name(a):
    a = a[0].upper() + a[1:]
    a = column_name(a)
    return a


def table_name(a):
    return a.upper()


def data_type(a):
    if 'date' in a:
        return 'Timestamp'
    if 'id' in a:
        return 'Integer'
    return 'String'


def column_code(a):
    return column_boiler_code.format(a, data_type(a), column_name(a))


def column_code_id(a):
    a += "_id"
    return id_boiler_code.format(a, column_name(a))


def file_skelton_code(a):
    return boiler_code.format(table_name(a), file_name(a))


def file_total_code(a, col_array):
    ans = file_skelton_code(a)
    ans += "{\n"
    ans += column_code_id(a)
    for col in col_array:
        ans += col
    ans += "}"
    return ans


def file_total_repo_code(a):
    a = file_name(a)
    ans = repo_boiler_code.format(a, a, a)
    ans += "{\n\n}"
    return ans


def class_name(data):
    val = 'public class '
    try:
        i = data.index(val)
    except Exception:
        return "xyz"
    i += len(val)
    ans = ''
    for k in range(i, len(data)):
        if data[k] == ' ':
            # print(ans)
            return ans
        ans += data[k]


def class_var_name(name):
    return name[0].lower() + name[1:]


def segregate_setters_getters(data, var_name):
    data = data.split(' ')
    setters = ''
    getters = ''
    for word in data:
        if 'set' in word:
            setters += setter_code(word, var_name)
        elif 'get' in word and 'get_' not in word and 'getClass' not in word and 'target' not in word:
            getters += getter_code(word, var_name)
    ans = setters + "\n" + getters
    # print(ans)
    return ans


def setter_code(word, var_name):
    actual = ''
    for i in word:
        if i == '(':
            break
        else:
            actual += i

    return "\t" * 2 + setter_boiler_code.format(var_name, actual) + "\n"


def getter_code(word, var_name):
    ans = "\t" * 2 + getter_boiler_code.format(var_name, word) + "\n"
    # print(ans)
    return ans


def class_type(chunk):
    return chunk[5:-1]


def when_code_lines(data):
    data = data.split('\n')
    when_ans = ''
    mock_ans = ''
    obj_ans = ''
    red_ans = ''
    for line in data:
        if 'List<' in line:

            words = [i.strip() for i in line.split(' ')]
            name = class_type(words[0])
            when_ans += test_when_boiler_code.format(words[3][:-1], words[1])
            mock_ans += test_mock_boiler_code.format(name, words[1])
            obj_ans += test_new_object.format(words[1], name)
        elif 'delete' in line:
            red_ans += redis_boiler_delete.format(line.split('"')[1])

    return [mock_ans, obj_ans, when_ans, red_ans]


def test_method_name(row):
    i = row.index('(')
    return row[:i]


def parts_code(row):
    data = row.split('\n')
    when_ans = ''
    mock_ans = ''
    obj_ans = ''
    red_ans = ''
    for line in data:
        if 'List<' in line:

            words = [i.strip() for i in line.split(' ')]
            name = class_type(words[0])
            when_ans += test_when_boiler_code.format(words[3][:-1], words[1])
            obj_ans += test_new_object.format(words[1], name)
        elif 'delete' in line:
            red_ans += redis_boiler_delete.format(line.split('"')[1])
    null_ans = when_ans.split('thenReturn')[0]
    return [obj_ans, when_ans, red_ans, null_ans]


def test_service_code_lines(data):
    ans = ''
    data = data.split('public void')[1:]
    for i in range(len(data)):
        row = data[i].strip()
        # print(row)
        test_name = test_method_name(row)
        obj_code = parts_code(row)
        ans += test_function_boiler_code.format(test_name, obj_code[0], obj_code[1], obj_code[2], obj_code[3])
        # break
    return ans
