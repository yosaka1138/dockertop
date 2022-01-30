import click
from tabulate import tabulate


def truncate(text, width=15, placeholder="..."):
    w = width - len(placeholder)
    return (text[:w] + placeholder) if len(text) > width else text


def modify_info(data):
    ret = []
    for r in data:
        del r[6:12]
        r[0] = truncate(r[0], 16, "")
        r[1] = truncate(r[1], 20, "")
        r[6] = truncate(r[6], 20)
        ret.append(r)
    return ret


@click.command()
@click.option(
    "-name",
    "--container_name",
    "name",
    default="",
    help="container name. you can get it with `docker ps`. if it is not set, display all containers.",
)
@click.option(
    "-incl",
    "--is_include",
    "incl",
    is_flag=True,
    help="Display all information about containers that contain the name specified by `container_name`.",
)
@click.option(
    "-p",
    "--pid",
    "pid",
    default=-1,
    help="Display only the specified PID.",
)
def main(name, incl, pid):
    from dockerpid.core import dockerpid

    data = dockerpid(name, incl, pid)
    headers = ["Container ID", "Container Name", "User", "PID", "%CPU", "%Mem", "CMD"]
    data = modify_info(data)
    click.echo(tabulate(data, headers))


if __name__ == "__main__":
    main()
