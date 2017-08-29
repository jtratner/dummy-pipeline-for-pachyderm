### Dummy Pipeline for Pachyderm

This is a set of really basic JSON files and Docker images to test out running a
pachyderm pipeline with scatter/gather, etc.


To run it, create a local minikube instance following the instructions on the
pachyderm docs (or see below for instructions that worked for v1.5.3 and mac
OSX).

Next, run:

```
eval "$(minikube docker-env)"
```

to let you build docker images directly into kubernetes.

Then finally you can run `build_everything.py`, then `pachctl create-repo
flowcells$SUFFIX` and then run `ls
pipeline-v*/*.json | xargs -n 1 pachctl create-pipeline -f` a few times until
all of the pipelines build (they have to be built in a specific order, but this
can also be handled by rerunning).


Then just commit files to the dummy "Flowcell" to get started:

```
pachctl put-file -c -f flowcells$SUFFIX master whatever-input-file.txt FlowcellA/inpt_file.txt
```

Because we want to simulate demuxing, the demux step generates 5 files (named as
"/$Flowcell/$sample", then
each caller step generates a vcf per "sample" and the "consensus" caller joins
gatk and freebayes' calls and merges them together.

### Instructions for installing pachyderm on OSX (if you don't want to read the docs)


For those who don’t want to read docs - Get PACHYDERM RUNNING (with minikube):
1. Get homebrew - https://brew.sh/
2. Virtualbox: brew cask install virtualbox (you may already have this if you
have vagrant)
3. Tap pachyderm and install: brew tap pachyderm/tap && brew install
pachyderm/tap/pachctl@1.5
4. brew install cos  # note I don’t remember why this is here anymore
5. brew install kubectl
6. minikube start --vm-driver=virtualbox
7. set up docker image container: eval $(minikube docker-env) [optional - lets
you push images directly into minikube]
8. Next back to here -
http://docs.pachyderm.io/en/latest/getting_started/local_installation.html
9. brew install pachctl
10. pachctl deploy local
11. pachctl port-forward &
12. (optional) install OSX fuse at https://osxfuse.github.io/

12A. sudo mkdir /pfs
12B. pachtcl mount /pfs
