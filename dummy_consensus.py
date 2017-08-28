#!/usr/bin/python
import argparse
import os
import time
import datetime
parser = argparse.ArgumentParser()
parser.add_argument('--gatk-vcf', required=True)
parser.add_argument('--freebayes-vcf', required=True)
parser.add_argument('--probe-counts', required=True)
parser.add_argument('--out', required=True)
parser.add_argument('--wait-time', default=0, type=int)
args = parser.parse_args()
print args
if args.wait_time:
    time.sleep(args.wait_time)
additional_data = '%s,%s,%s' % (os.environ['COUNSYL_SOFTWARE_VERSION'],
                                datetime.datetime.utcnow(), time.time())
initial_data = []
for vcf_path in [args.gatk_vcf, args.freebayes_vcf, args.probe_counts]:
    with open(vcf_path) as fp:
        for line in fp:
            initial_data.append('%s: %s' % (vcf_path, line))
with open(args.out, 'w') as fp:
    for row in initial_data:
        fp.write(row)
    fp.write(additional_data)
