name_file_output = "rewrite_file.txt"

list_files_to_open = [
  '1.txt',
  '2.txt',
  '3.txt',
]

list_of_dicts_output = []

def read_file(path_file):
  with open(file=path_file, mode="r", encoding="utf-8") as f:
    data = f.read()
    f.seek(0)
    count_strings = str(len(f.readlines()))
    name_file = path_file.rsplit("/", 1)[-1]
    dict_for_output = {
      'file_name': name_file,
      'count_strings': count_strings,
      'data': data,
    }
    return dict_for_output


def write_file(path_output, **kwargs):
  with open(file=path_output, mode="a", encoding="utf-8") as f:
    for element in list(kwargs.values()):
      f.write(element)
      f.write("\n")


for path_file in list_files_to_open:
  data_to_output = read_file(path_file)
  list_of_dicts_output.append(data_to_output)


sorted_list_of_dicts_output = sorted(list_of_dicts_output, key=lambda d: d['count_strings'])
for element in sorted_list_of_dicts_output:
  write_file(name_file_output, **element)