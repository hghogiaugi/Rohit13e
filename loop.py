import os
import signal
import time
import subprocess


# Join :- @tanmaypaul21 # Set the path to the script you want to restart
script_to_restart = "new.py"

def restart_script():
    # Join :- @tanmaypaul21 # Run the script
    print("RaJa ka ddos hai bc.....")
    process = subprocess.Popen(["python3", script_to_restart], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def main():
    process = restart_script()
    while True:
        time.sleep(480)  # Join :- @tanmaypaul21 # Sleep for 30 seconds
        # Join :- @tanmaypaul21 # Send Ctrl+C signal to the process
        process.send_signal(signal.SIGINT)
        # Join :- @tanmaypaul21 # Wait for the process to terminate
        process.wait()
        # Join :- @tanmaypaul21 # Restart the script
        process = restart_script()

if __name__ == "__main__":
    main()