#!/usr/bin/python
import argparse
import datetime
import os
import time
parser = argparse.ArgumentParser()
parser.add_argument('input_dir')
parser.add_argument('output_dir')
parser.add_argument('--num-samples', type=int, default=5)
parser.add_argument('--wait-time', type=int, default=0)
args = parser.parse_args()
if args.wait_time:
    time.sleep(args.wait_time)

input_data = []
output_directory = args.output_dir
for root, _, files in os.walk(args.input_dir):
    for f in files:
        o = os.path.join(root, f)
        with open(o) as fp:
            input_data.append(fp.read())
            output_directory = os.path.join(args.output_dir, os.path.basename(root))

for i in range(args.num_samples):
    pth = os.path.join(output_directory, 's_%d_AAAA' % i)
    with open(pth, 'w') as fp:
        for i in input_data:
            fp.write(i)
        fp.write('%s,%s,%s' % (os.environ['COUNSYL_SOFTWARE_VERSION'],
                                 datetime.datetime.utcnow(), time.time()))
    print 'Wrote to %s' % pth
