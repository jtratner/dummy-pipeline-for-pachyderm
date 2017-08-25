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
for i in range(args.num_samples):
    pth = os.path.join(args.output_dir, 's_%d_AAAA' % i)
    with open(pth, 'w') as fp:
        fp.write('%s,%s,%s' % (os.environ['COUNSYL_SOFTWARE_VERSION'],
                                 datetime.datetime.utcnow(), time.time()))
    print 'Wrote to %s' % pth
