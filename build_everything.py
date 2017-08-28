#!/usr/bin/python
import os
import jinja2
DEFAULT_VERSION="v2"
SUFFIX="3"
VERSION_MAP = {
    'demux': 'v3'
}
OUTPUT_DIR = os.path.join('.', 'pipelines-v%s' % SUFFIX)
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
for package in ['consensus', 'probe-counts', 'demux', 'freebayes', 'gatk', 'grouped']:
    version = VERSION_MAP.get(package, DEFAULT_VERSION)
    docker_file = 'Dockerfile.{package}'.format(package=package)
    if os.path.exists(docker_file):
        os.system('docker build -f Dockerfile.{package} --build-arg version={version} -t {package}:{version} .'.format(package=package, version=version))
    json_name = package + '.json'
    with open(os.path.join(OUTPUT_DIR, json_name), 'w') as fp:
        rendered = jinja2.Template(open(json_name).read()).render(suffix=SUFFIX, version=version)
        fp.write(rendered)
print 'Go to %s to see pipelines to update/create' % OUTPUT_DIR
