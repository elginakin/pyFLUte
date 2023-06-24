import subprocess
import sys
import os
import shutil
import argparse

# Install required packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

packages = ['shutil']

for package in packages:
    try:
        __import__(package)
    except ImportError:
        install(package)

# Parse command line arguments
parser = argparse.ArgumentParser(description='pyFLUte Script')
parser.add_argument('-i', '--input', help='Input directory for the FASTA file')
parser.add_argument('-o', '--output', help='Output directory for the extracted sequences')
parser.add_argument('-r', '--stats', action='store_true', help='Generates a report for each sorted segment file')
args = parser.parse_args()

# Display logo
logo = '''       
                 ____    __       __  __  __             
               /\  _`\ /\ \     /\ \/\ \/\ \__          
 _____   __  __\ \ \L\_\ \ \    \ \ \ \ \ \ ,_\    __   
/\ '__`\/\ \/\ \\ \  _\/\ \ \  __\ \ \ \ \ \ \/  /'__`\ 
\ \ \L\ \ \ \_\ \\ \ \/  \ \ \L\ \\ \ \_\ \ \ \_/\  __/ 
 \ \ ,__/\/`____ \\ \_\   \ \____/ \ \_____\ \__\ \____/
  \ \ \/  `/___/> \\/_/    \/___/   \/_____/\/__/\/____/
   \ \_\     /\___/                                     
    \/_/     \/__/                                      
 v1.0 by Elgin Akin
'''

print(logo)
print("")

# Set input and output directories
input_dir = args.input
output_dir = args.output

# Check if input directory is specified
if input_dir is None:
    print("Input directory is not specified. Exiting...")
    parser.print_help()
    sys.exit(1)

# Check if input directory exists
if not os.path.exists(input_dir):
    print(f"Input directory '{input_dir}' does not exist. Exiting...")
    sys.exit(1)

# Create output directory if it doesn't exist
if output_dir is None:
    output_dir = os.getcwd()
else:
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

# Define segments and their regex patterns
segments = {
    "1_PB2": ".*_1$|.*\|1$|.*\|PB2$",
    "2_PB1": ".*_2$|.*\|2$|.*\|PB1$",
    "3_PA": ".*_3$|.*\|3$|.*\|PA$",
    "4_HA": ".*_4$|.*\|4$|.*\|HA$",
    "5_NP": ".*_5$|.*\|5$|.*\|NP$",
    "6_NA": ".*_6$|.*\|6$|.*\|NA$",
    "7_M": ".*_7$|.*\|7$|.*\|M$",
    "8_NS": ".*_8$|.*\|8$|.*\|NS$"
}

# Loop through fasta and extract segments
for segment, regex in segments.items():
    output_file = os.path.join(output_dir, f"{segment}.fasta")
    command = f"seqkit grep -r -p '{regex}' {input_dir}/*.fasta > {output_file}"
    subprocess.run(command, shell=True)

print('segments sorted')

# Execute "seqkit stats *.fasta" in the output directory
if args.stats:
    os.chdir(output_dir)
    subprocess.run("seqkit stats *.fasta", shell=True)
