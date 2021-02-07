import shutil
import subprocess


shutil.rmtree('build')
shutil.rmtree('dict_to_object.egg-info')
shutil.rmtree('dist')

subprocess.run(['python3', 'setup.py', 'sdist', 'bdist_wheel']).check_returncode()
subprocess.run(['python3', '-m', 'twine', 'upload', 'dist/*']).check_returncode()
