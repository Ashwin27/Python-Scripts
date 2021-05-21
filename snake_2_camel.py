from argparse import ArgumentParser
import os.path

def is_valid_file(file):
    if not os.path.exists(file):
      parser.error("The file %s does not exist!" % file)
      return False
    return True

parser = ArgumentParser(description="Snake 2 Camel Converter")
parser.add_argument("-i", dest="in_filename", required=True,
                    help="input file with snake case entries", metavar="FILE")
parser.add_argument("-o", dest="out_filename", required=True,
                    help="output file with camel case entries", metavar="FILE")

args = parser.parse_args()
in_filename = args.in_filename
out_filename = args.out_filename

def to_camel_case(snake_str):
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    #return components[0] + ''.join(x.title() for x in components[1:])
    return ''.join(x.title() for x in components)

print("Running conversion...\n")
print(in_filename, out_filename)

if not is_valid_file(in_filename) and is_valid_file(out_filename):
  exit(1)

with open(in_filename, 'r') as reader, open(out_filename, 'w') as writer:
  #No Walrus operator until 3.8 Python
  # while (line := reader.readline()):
  lines = reader.readlines()
  for line in lines:
    writer.write(to_camel_case(line))