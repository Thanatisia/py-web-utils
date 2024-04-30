"""
Unit Test Benchmarker for py-webscraper-yt
"""
import os
import sys
from subprocess import Popen, PIPE, STDOUT
from pyutils.decorators.benchmark import benchmark, benchmark_custom

@benchmark_custom(return_result=True)
def benchmark_yt_obtain_url(cmd_list, stream_input="in-list.txt"):
    """
    Benchmark the command 'yt-obtain-url < [input-file-name]'
    """
    print("Command List: {}".format(cmd_list))
    print("Stream Input: {}".format(stream_input))

    # Initialize Variables
    stdout = ""
    stderr = ""
    retcode = -1

    try:
        # Open a subprocess process pipe and execute command in benchmark
        with Popen(cmd_list, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
            # Execute command and return standard output
            proc_res = proc.communicate(input=stream_input.encode("utf-8"))
            stdout = proc_res[0]
            stderr = proc_res[1]
            retcode = proc.returncode

            # Check for errors
            if retcode != 0:
                if stderr != None:
                    stderr = stderr.decode("utf-8")
            else:
                if stdout != None:
                    stdout = stdout.decode("utf-8")
    except Exception as ex:
        print("Exception: {}".format(ex))

    # Output/Return
    return stdout, stderr, retcode

def main():
    print("Starting benchmark for py-webscraper-yt")

    # Prepare command list
    cmd_list = ["yt-obtain-url"]

    # Read the input file
    with open("in-list.txt", "r") as f_read_urls:
        # Read all URLs into a input list
        input_data = f_read_urls.read()

    # Begin benchmark and run program
    stdout, stderr, retcode = benchmark_yt_obtain_url(cmd_list, stream_input=input_data)

    # Return/Output
    print("Return Code: {}".format(retcode))
    if retcode == 0:
        print("Standard Output: {}".format(stdout.strip()))
    else:
        print("Standard Error: [{}]".format(stderr.strip()))

if __name__ == "__main__":
    main()
