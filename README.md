docker-projects
===============

This is my repo for various docker builds

Every folders beside this repo is a docker build project. So you can clone it, chdir into it and build your own. 
Generaly the structure is follow


```
name 
   |_files
   |  |_required files to build
   |_Dockerfile
   |_Makefile
```
 
the process to build is :
 * make build => build the image
 * make run => interactive test which launch /bin/bash
 * make clean => remove the image and the container
