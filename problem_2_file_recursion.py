"""
For this problem, the goal is to write code for finding all files under a directory
(and all directories beneath it) that end with ".c"
Note: os.walk() is a handy Python method which can achieve this task very easily.
However, for this problem you are not allowed to use os.walk().
"""

import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if os.path.exists(path):
        files = []
        dir_path = [path]
        while dir_path:
            temp = dir_path.pop(0) # Removing the first file
            all_dirs = os.listdir(temp)
            for file in all_dirs:
                file = os.path.join(temp, file)
                if file.endswith(suffix):
                    files.append(file)
                elif os.path.isdir(file):
                    dir_path.append(file)
        return files

print(find_files(".c", "testdir"))





