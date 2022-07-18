Starting tomorrow, this git will be available as read only. This git will be removed from GitHub at the end of July.
Who wants a copy of the source code can fork this. 

# Disclaimer
<span style="color: red">
 We strongly advise all interested users not to implement it. The project is not finished and has serious security vulnerabilities. We distance ourselves fundamentally from the project and any resulting damage. You are welcome to use the project for your own projects, but this is on your own responsibility. 
</span>

# Inor

## Installation
- ```pip install Inor```
- The Inor package can be downloaded via pip. This requires at least ``pip 21.0``.
### Tipp
Depending on the configuration of the Python installation, it is possible that Inor was installed correctly but is outside the path. To solve this problem, please follow these steps.

- ```pip uninstall inor```
- ```export PATH="$HOME/.local/bin:$PATH"```
- ```pip install inor```

Finally, we uninstall the package and add the path to the default environment. After that we can install the package again. Normally a reinstallation is not necessary. But we still recommend it


### Info
The Current Release is not a stable release. It is only used for testing and to protect the name.
If you want to install the latest version from the source code, please use the following command.
```
pip install git+https://github.com/Riffecs/inor.git#egg=inor
```
No new releases will be published until the final release.
