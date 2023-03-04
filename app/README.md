# python_package_example

this one generates ids, passwords, etc..


how to use

some example commands here

whl: packaged binary version, contains everything all python package manager needs to know
to create the whl:

python setup.py bdist_wheel  (need to have pip install wheel first)
bdist means binary distribution
then it creates the build and dist folder where the dist folder contains the wheel
idgenerator-<version>-py3-none-any.whl

the build folder contains the build

the egg-info? containst the dependencies, the meta data(not sure if it still being used)

sdist means the source distribution (with the source people can rebuild)
python setup.py sdist, which creates the tar.gz file


