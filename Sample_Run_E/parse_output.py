output_file = open('slurm-1922.out', 'r').readlines()

last = len(output_file)
output = (output_file[last-5:last-1])
print(output)
#print(output_file.readlines())
