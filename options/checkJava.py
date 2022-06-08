"""Determine Java Version installed"""
import subprocess

def get_current_java_version():
    java_version = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)
    print(java_version)

get_current_java_version()
