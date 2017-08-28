export VERSION=v1
docker build -f Dockerfile.consensus --build-arg version=$VERSION -t consensus:$VERSION
docker build -f Dockerfile.counter --build-arg version=$VERSION -t probe-counts:$VERSION
docker build -f Dockerfile.demux --build-arg version=$VERSION -t demux:$VERSION
docker build -f Dockerfile.freebayes --build-arg version=$VERSION -t freebayes:$VERSION
docker build -f Dockerfile.gatk --build-arg version=$VERSION -t gatk:$VERSION

