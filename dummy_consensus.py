import argparse
import os
import time
import datetime
parser = argparse.ArgumentParser()
parser.add_argument('--gatk-vcf')
parser.add_argument('--freebayes-vcf')
parser.add_argument('--probe-counts')
parser.add_argument('--out')
args = parser.parse_args()
if args.wait_time:
    time.sleep(args.wait_time)
additional_data = '%s,%s,%s' % (os.environ['COUNSYL_SOFTWARE_VERSION'],
                                  datetime.datetime.utcnow(), time.time())
initial_data = []
with open(args.gatk_vcf) as fp:
    initial_data.append('gatk: %s\n' % fp.read())
with open(args.freebayes_vcf) as fp:
    initial_data.append('freebayes: %s\n' % fp.read())
with open(args.probe_counts) as fp:
    initial_data.append('probe_counts: %s\n' % fp.read())
with open(args.out, 'w') as fp:
    for row in initial_data:
        fp.write(row)
    fp.write(additional_data)
