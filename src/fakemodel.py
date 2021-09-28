import sys
import csv
import argparse


def calculate_growth(photosynthesis_rate):
    r"""Calculate the plant growth rate from the photosynthesis rate.

    Args:
        photosynthesis_rate (float): Rate of photosynthesis.

    Returns:
        float: Growth rate.

    """
    return 0.5 * photosynthesis_rate


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Growth model')
    parser.add_argument('--yggdrasil', action='store_true',
                        help='Run the model using yggdrasil.')
    args = parser.parse_known_args()[0]
    if args.yggdrasil:
        from yggdrasil.interface import YggInput, YggOutput
        from yggdrasil.units import add_units
        from yggdrasil.tools import print_encoded
        input = YggInput('photosynthesis_rate')
        output = YggOutput('growth_rate', '%f\n')

        while True:
            flag, prate = input.recv()
            if not flag:
                print('growth: No more input.')
                break
            grate = calculate_growth(*prate)
            grate *= add_units(1.0, "cm*m**2/umol")
            print_encoded(
                f'growth: photosynthesis rate = {prate[0]} ---> '
                f'growth rate = {grate}')
            flag = output.send(grate)
            if not flag:
                print('growth: Error sending growth rate.')
                sys.exit(-1)
    else:
        parser.add_argument('input_file', help='Input file.', nargs=1)
        parser.add_argument('output_file', help='Output file.', nargs=1)
        args = parser.parse_known_args()[0]

        input_fd = open(args.input_file[0], newline='')
        output_fd = open(args.output_file[0], 'w', newline='')

        output = []
        input_reader = csv.reader(filter(lambda row: row[0] != '#', input_fd),
                                  delimiter='\t', quoting=csv.QUOTE_NONNUMERIC)
        output_writer = csv.writer(output_fd, delimiter='\t',
                                   lineterminator='\n')
        output_writer.writerow(['# growth_rate'])
        output_writer.writerow(['# cm/s'])
        for prate in input_reader:
            grate = calculate_growth(*prate)
            print('growth: photosynthesis rate = %f ---> growth rate = %f' % (
                prate[0], grate))
            output_writer.writerow([grate])

        input_fd.close()
        output_fd.close()

    sys.exit(0)
