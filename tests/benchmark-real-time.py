"""
Unit Test Benchmarker for py-webscraper-yt@feature-concurrency
"""
import os
import sys
from threading import Thread
from queue import SimpleQueue
from subprocess import Popen, PIPE, STDOUT
from pyutils.decorators.benchmark import benchmark, benchmark_custom

def read_stdout(proc, stdout_buffer):
    """
    Read stdout from the subprocess in a separate thread.
    """
    for line in proc.stdout:
        output = line.decode().strip()
        if output:
            print(output)
        stdout_buffer.append(output)

@benchmark_custom(return_result=True)
def benchmark_yt_obtain_url(cmd_list, stream_input, ttl_threshold=0):
    """
    Benchmark the command 'yt-obtain-url < [input-file-name]'
    """
    print("Command List: {}".format(cmd_list))
    print("Stream Input: {}".format(stream_input))

    # Initialize Variables
    stdout_buffer = []
    line = ""
    stdout = ""
    stderr = ""
    retcode = -1
    ttl_counter = 0

    try:
        # Open a subprocess process pipe and execute command in benchmark
        proc = Popen(cmd_list, stdin=PIPE, stdout=PIPE, stderr=PIPE)

        # Write standard input stream (stdin) into the subprocess
        if stream_input is not None:
            for element in stream_input:
                # Write the standard input data into the pipe's stream
                proc.stdin.write("{}\n".format(element).encode("utf-8"))

            # Close the standard input pipe after writing to stop deadlock
            proc.stdin.close()

        # Start a thread to read stdout
        # stdout_reader_thread = Thread(target=read_stdout, args=(proc, stdout_buffer))
        # stdout_reader_thread.start()

        # Create a while loop to keep looping until there are no more output/not polling (aka a return code is produced (0 = Success, > 0 = Error))
        print("Polling...", flush=True)

        while True:
            # Check if the subprocess standard output stream has data
            if proc.stdout != None:
                # Read the next line
                line = proc.stdout.readline()

            # Break Condition: Check if the process is still running (status code not produced yet) and if there are output
            if not line and proc.poll() is not None:
                # If the output is empty AND process is no longer running
                break

            # Time-to-Live (TTL) Condition: Check if the process is still running after a set amount of lines has passed
            if ttl_threshold > 0:
                if not line and proc.poll() is None:
                    # Check if counter has reached the threshold
                    if ttl_counter == ttl_threshold:
                        # Exit
                        break

                    # Increment counter
                    ttl_counter += 1

            # Null Validation: Check line is found
            if line != "":
                # Decode the encoded string
                line = line.decode().rstrip()
                print("{}".format(line))
                # Write the line to the standard output
                stdout += line

        # Wait for the process to finish and get return code
        retcode = proc.wait()

        # Wait for the stdout reader thread to finish
        # stdout_reader_thread.join()

        # Read/Format standard output
        # stdout = '\n'.join(stdout_buffer)

        # Read remaining stderr
        """
        remaining_stderr = proc.stderr.read().decode()
        if remaining_stderr:
            print(remaining_stderr, file=sys.stderr)
            stderr += remaining_stderr
        """
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
    # Prepare command list
    cmd_list = ["yt-obtain-url"]
    # cmd_list = ["ip", "a", "s"]
    # cmd_list = ["ping", "-c", "5", "8.8.8.8"]

    # Read the input file
    with open("in-list.txt", "r") as f_read_urls:
        # Read all URLs into a input list
        input_data = f_read_urls.read().strip().split("\n")
        print(input_data)

    try:
        # Begin benchmark and run program
        print("Starting Benchmark for: yt-obtain-url")
        stdout, stderr, retcode = benchmark_yt_obtain_url(cmd_list, stream_input=input_data, ttl_threshold=4)
        print("Return Code: {}".format(retcode))
    except Exception as ex:
        print("Exception: {}".format(ex))

if __name__ == "__main__":
    main()

