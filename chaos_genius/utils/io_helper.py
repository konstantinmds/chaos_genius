import os
import shutil
import click

def cg_print(info, color=None):
    click.echo(info)


def which(program):
    """Find the program executable

    Args:
        program (str): program name

    Raises:
        ValueError: Raise if the program isn't found

    Returns:
        obj: program executable path
    """
    if _executable := shutil.which(program):
        return _executable
    else:
        raise ValueError(f"Executable {program} not found")


def is_file_exists(file_path, is_relative=True):
    """Check if the file exists at the given location

    Args:
        file_path (str): path of the file in the string
        is_relative (bool, optional): is the path relative or absolute. Defaults to True.

    Returns:
        str: Return the full path if file found, None if not found
    """
    if is_relative:
        file_path = os.path.join(os.getcwd(), file_path)
    return file_path if os.path.exists(file_path) else False
