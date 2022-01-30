# dockertop

Dockertop makes it easy to get the PID information of a container.
Dockertop is implemented in Python3.x and binary files are available.

# How To Use

The OS to be used is assumed to be Linux.
Just clone this repository and pass it to your computer to use.
```bash
git clone git@github.com:yosaka1138/dockertop.git
export PATH="`pwd`/dockertop/bin:$PATH"
```

## Specified Container name
```bash
dockertop -name {{container_name}}
```
If you want to show all containers with the specified name, use the argument `-incl`.
```bash
dockertop -name {{container_name}} -incl
```



## Specified PID
```bash
dockertop -p 1234
```