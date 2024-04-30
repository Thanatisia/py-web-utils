"""
Unit Test Benchmarker for py-webscraper-yt@feature-concurrency
"""
import os
import sys
from subprocess import Popen, PIPE, STDOUT
from pyutils.decorators.benchmark import benchmark, benchmark_custom

@benchmark_custom(return_result=True)
def benchmark_yt_obtain_url(cmd_list, stream_input):
    """
    Benchmark the command 'yt-obtain-url < [input-file-name]'
    """
    print("Command List: {}".format(cmd_list))
    print("Stream Input: {}".format(stream_input))

    # Initialize Variables
    line = ""
    stdout = ""
    stderr = ""
    retcode = -1

    try:
        # Open a subprocess process pipe and execute command in benchmark
        with Popen(cmd_list, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
            # Write standard input stream (stdin) into the subprocess
            if stream_input != None:
                # Write the standard input data into the pipe's stream
                proc.stdin.write(stream_input.encode("utf-8"))

                # Flush the standard input pipe after writing
                proc.stdin.close()

            # Create a while loop to keep looping until there are no more output/not polling (aka a return code is produced (0 = Success, > 0 = Error))
            print("Polling...", flush=True)
            if proc.stdout != None:
                for line in proc.stdout:
                    # Null Validation: Check line is found
                    if line != "":
                        # Decode the encoded string
                        line = line.decode().strip()
                        print("{}".format(line))
                        # Write the line to the standard output
                        stdout += line

                # Get return code
                retcode = proc.wait()
    except Exception as ex:
        print("Exception detected: {}".format(ex))

    # Output/Return
    return stdout, stderr, retcode

def display_results(stdout, stderr, retcode):
    # Return/Output
    print("Return Code: {}".format(retcode))
    if retcode == 0:
        print("Standard Output: {}".format(stdout.strip()))
    else:
        print("Standard Error: [{}]".format(stderr.strip()))

def main():
    print("Starting benchmark for py-webscraper-yt")

    # Prepare command list
    cmd_list = ["yt-obtain-url"]
    # cmd_list = ["ip", "a", "s"]
    # cmd_list = ["ping", "-c", "5", "8.8.8.8"]

    # Read the input file
    with open("in-list.txt", "r") as f_read_urls:
        # Read all URLs into a input list
        input_data = f_read_urls.read()

    try:
        # Begin benchmark and run program
        print("Starting Benchmark for: yt-obtain-url")
        stdout, stderr, retcode = benchmark_yt_obtain_url(cmd_list, stream_input=input_data)
        print("Return Code: {}".format(retcode))
    except Exception as ex:
        print("Exception: {}".format(ex))

if __name__ == "__main__":
    main()

