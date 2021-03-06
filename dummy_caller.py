#!/usr/bin/python
import argparse
import os
import time
import datetime
parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')
parser.add_argument('--reference-genome')
parser.add_argument('--roi')
parser.add_argument('--wait-time', type=int, default=0)
args = parser.parse_args()
print args
if args.wait_time:
    time.sleep(args.wait_time)
with open(args.input) as fp:
    initial_data = fp.read()

additional_data = '%s,%s,%s' % (os.environ['COUNSYL_SOFTWARE_VERSION'],
                                  datetime.datetime.utcnow(), time.time())
with open(os.path.join(args.output), 'w') as fp:
    print 'Writing to %s' % fp.name
    fp.write(initial_data)
    fp.write('\n')
    fp.write(additional_data)
