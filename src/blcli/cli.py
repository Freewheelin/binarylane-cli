import argparse
import functools
import os

prog_parser = argparse.ArgumentParser(
    prog="bl", description="bl is a command-line interface for the BinaryLane API"
)

command_action: "argparse._SubParsersAction" = prog_parser.add_subparsers(
    title="Available Commands", metavar=""
)


def _add_command(
        action: "argparse._SubParsersAction", prefix: str, name: str, help: str = None
):
    def wrap(func):
        command_name = (
            name[len(prefix) + 1:] if name.startswith(prefix + "_") else name
        )

        command_parser = action.add_parser(command_name, help=help)
        handler = func(command_parser)
        command_parser.set_defaults(func=handler)
        return func

    return wrap


def _add_group(
        action: "argparse._SubParsersAction", prefix: str, name: str, help: str = None
):
    def wrap(func):
        command_name = (
            name[len(prefix) + 1:] if name.startswith(prefix + "_") else name
        )

        group_parser = action.add_parser(command_name, help=help)
        group_action = group_parser.add_subparsers(title=func.__name__, metavar="")
        func.add_group = functools.partial(_add_group, group_action, command_name)
        func.add_command = functools.partial(_add_command, group_action, command_name)
        return func

    return wrap


add_group = functools.partial(_add_group, command_action, "")


def run(args):
    from .client import AuthenticatedClient

    client = AuthenticatedClient(
        "https://api.binarylane.com.au",
        open(os.path.expanduser("~/.config/python-blcli")).read().strip(),
    )

    parsed = prog_parser.parse_args(args)

    # Haven't reached a command
    if not "func" in parsed:
        prog_parser.parse_args(args + ["--help"])
        return

    # Run the command's handler
    handler = parsed.func
    del parsed.func

    parsed.client = client
    response = handler(**vars(parsed))
    if not response:
        prog_parser.parse_args(args + ["--help"])
        return

    # display response
    print(response)
    return
