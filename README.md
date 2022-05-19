[![Pylint](https://github.com/Riffecs/inor/actions/workflows/pylint.yml/badge.svg)](https://github.com/Riffecs/inor/actions/workflows/pylint.yml)
[![Upload Python Package](https://github.com/Riffecs/inor/actions/workflows/pypi.yml/badge.svg)](https://github.com/Riffecs/inor/actions/workflows/pypi.yml)

# Inor 

## Installation
- ```pip install inor```
- The inor package can be downloaded via pip. This requires at least ``pip 21.0``.
### Tipp
Depending on the configuration of the Python installation, it is possible that inor was installed correctly but is outside the path. To solve this problem, please follow these steps.

- ```pip uninstall inor```
- ```export PATH="$HOME/.local/bin:$PATH"```
- ```pip install inor```

Finally, we uninstall the package and add the path to the default environment. After that we can install the package again. Normally a reinstallation is not necessary. But we still recommend it

## Usage

### Package installation
- ``inor install  package``
- With the above command you can install packages. If the corresponding package is not available you will get an error message 

### Search package
- ``inor search text``
- If you don't know the name of the package you are looking for, you can search the local database.
- The command searches only a local database. Therefore it makes sense to update this.: [update database](https://github.com/Riffecs/inor#update-package-list)

### Package Information
- ```inor info package``` 
- With the above command you get a short info about the specified package. This is very short and direct

### Update package list
- ```inor update ```
- The command updates the local list of packages. It only accesses the local database. It does not change any dependencies or packages.

### Update packages
- ```inor upgrade ```
- This command updates packages. Here it is to be noted that old versions are not overwritten. The new version is installed in parallel. It is important to say that packages are never removed here.

### Remove packages
- ```inor remove ```
- This is the only command that deletes packages. Once a package is deleted there is no way to restore it. It must be reinstalled.

### Instruction
- ``inor man``
-  This command displays the man file of the package. 

### Packet list
- ```inor list ```
- This command returns a list with all installed packages. However, this list is without versions.


### Packet version
- ```inor freeze ```
- In contrast to the command ``list`` you get here a list including versions. This is necessary, for example, if you want to replicate the system on another system. No attention is paid to dependencies with regard to a login. All packages are output.

### Check packages
- ``inor check``
- The command will check if all dependencies and packages are installed correctly. It does not correct any errors. The command only prints an error. 

### Customizing the Config 
- ``inor config``
- Various files are stored in the Config. Among other things, the login and access permissions for other packages. These can be viewed and checked with this command.

### Login
- ``inor login``
- With this command you can log in to the X-FAB servers
