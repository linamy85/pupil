from __future__ import print_function
import argparse


def main():
    parser = argparse.ArgumentParser(description='Sort gaze recording log.')
    parser.add_argument('-i', '--input', required=True,
                        help='Input recording log file. (csv)')
    parser.add_argument('-o', '--output',
                        help='Output parsed file. (Replace input file if not set)')
    opt = parser.parse_args()

    header = ""
    logs = set()
    with open(opt.input, 'r') as file:
        header = file.readline()
        line = file.readline()
        while line:
            x = line[:-1].split(',', 2)
            logs.add((int(x[0]), float(x[1]), x[2]))
            line = file.readline()
    
    logs = list(logs)
    logs.sort(key=lambda x: (x[0], x[1]))

    output_file = opt.input if not opt.output else opt.output
    with open(output_file, 'w') as file:
        file.write(header)
        for ts, conf, pt in logs:
            file.write('%d,%f,%s\n' % (ts, conf, pt))


if __name__ == '__main__':
    main()
