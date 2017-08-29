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

Because we want to simulate demuxing effectively.
