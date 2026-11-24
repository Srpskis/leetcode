"""
Given a list paths of directory info, including the directory path, and all the files with contents in this directory, return all the duplicate files in the file system in terms of their paths. You may return the answer in any order.

A group of duplicate files consists of at least two files that have the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
It means there are n files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content) respectively in the directory "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of groups of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"
 

Example 1:

Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Example 2:

Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
 

Constraints:

1 <= paths.length <= 2 * 104
1 <= paths[i].length <= 3000
1 <= sum(paths[i].length) <= 5 * 105
paths[i] consist of English letters, digits, '/', '.', '(', ')', and ' '.
You may assume no files or directories share the same name in the same directory.
You may assume each given directory info represents a unique directory. A single blank space separates the directory path and file info.
 

Follow up:

Imagine you are given a real file system, how will you search files? DFS or BFS?
If the file content is very large (GB level), how will you modify your solution?
If you can only read the file by 1kb each time, how will you modify your solution?
What is the time complexity of your modified solution? What is the most time-consuming part and memory-consuming part of it? How to optimize?
How to make sure the duplicated files you find are not false positive?


"""

# Thought process

from collections import defaultdict


paths1 = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
paths2 = ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]

data_split_by_blank_space = [
    ["root/a", "1.txt(abcd)", "2.txt(efgh)"],
    ["root/c", "3.txt(abcd)"],
    ["root/c/d", "4.txt(efgh)"],
    ["root", "4.txt(efgh)"]
]

extracted_paths = ["root/a", "root/c", "root/c/d", "root"];
file_info = [
    ["1.txt(abcd)", "2.txt(efgh)"],
    ["3.txt(abcd)"],
    ["4.txt(efgh)"],
    ["4.txt(efgh)"]
]

zipped = {
    "root/a": ["1.txt(abcd)", "2.txt(efgh)"],
    "root/c": ["3.txt(abcd)"],
    "root/c/d": ["4.txt(efgh)"],
    "root": ["4.txt(efgh)"]
}

refined = {
    "root/a/1.txt": "abcd",
    "root/a/2.txt": "efgh",
    "root/c/3.txt": "abcd",
    "root/c/d/4.txt": "efgh",
    "root/4.txt": "efgh"
}

refined_reverted = {
    "abcd": ["root/a/1.txt", "root/c/3.txt"],
    "efgh": ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"]
}


def findDuplicates(paths):
    # split paths by white space
    data_split_by_blank_space = []
    for path in paths:
        data_split_by_blank_space.append(path.split())

    # separate diractories and data
    directories = []
    data = []
    for entry in data_split_by_blank_space:
        directories.append(entry[0]);
        data.append(entry[1:])

    # zip directories and data
    directory_to_data = list(zip(directories, data))

    # split the data by ( and extract the file name to append to directory path
    path_to_data = {}
    for entry in directory_to_data:
        directory = entry[0]
        data = entry[1]
        for each in data:
            file_name, separator, data = each.partition("(");
            splitted_data = [file_name, separator + data]
            path_to_data[directory + "/" + splitted_data[0]] = splitted_data[1]

    # restructure the path_to_data so that the data is mapped to all paths
    data_to_path = {}
    for key, value in path_to_data.items():
        if value not in data_to_path:
            data_to_path[value] = [key]
        else:
            data_to_path[value].append(key)

    # extract result from data_to_path
    result = []
    for value in data_to_path.values():
        if len(value) > 1:
            result.append(value)
    return result


def findDuplicatesLessVerbose(paths):
    content_to_paths = defaultdict(list)
    for entry in paths:
        directory, *files = entry.split()
        for file in files:
            name, _, content = file.partition("(")
            content_to_paths[content].append(f"{directory}/{name}")
        return [group for group in content_to_paths.values() if len(group) > 1]

print(findDuplicates(paths1))
print(findDuplicates(paths2))