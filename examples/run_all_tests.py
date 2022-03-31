import os
import subprocess as sp
import sys

# Each element should be a pair
# - First element is the directory and executable name (these two should be the same)
# - Second element is the input file (None if no input file is required)
# (The input file should be in the data directory at the same level as this file
examples = [
    ["custom_format", None],
    ["custom_order", "com-dblp.uedgelist"],
    #["degree_distribution", "com-dblp.uedgelist"],
    ["degree_order", "com-dblp.uedgelist"],
    ["format_conversion", None],
    ["rcm_order", "com-dblp.uedgelist"],
    ["sparse_feature", "ash958.mtx"],
    ["csr_coo", "ash958.mtx"],
    ["sparse_reader", "ash958.mtx"],
]

def RunExample(exe_filename, data_filename):
    exe_path = os.path.join(exe_filename, exe_filename)
    cmd = [exe_path]

    if data_filename is not None:
        data_path = os.path.join("data", data_filename)
        cmd.append(data_path)

    result = sp.run(cmd)

    if result.returncode != 0:
        print("cmd=", cmd, "has failed!!!")
        sys.exit(1)

if __name__ == "__main__":
    for name, data in examples:
        RunExample(name, data)