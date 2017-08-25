import argparse
import os
import time
import datetime
parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output_dir')
parser.add_argument('--reference-genome')
parser.add_argument('--roi')
parser.add_argument('--wait-time', type=int, default=0)
args = parser.parse_args()
if args.wait_time:
    time.sleep(args.wait_time)
with open(args.input) as fp:
    initial_data = fp.read()

additional_data = '%s,%s,%s' % (os.environ['COUNSYL_SOFTWARE_VERSION'],
                                  datetime.datetime.utcnow(), time.time())
output_name = os.path.basename(args.input) + '.vcf'
with open(os.path.join(args.output_dir, output_name), 'w') as fp:
    fp.write(initial_data)
    fp.write('\n')
    fp.write(additional_data)
