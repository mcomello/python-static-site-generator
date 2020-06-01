import typer
from ssg.site import Site
import ssg.parsers


def main(source="content", dest="dist"):
    config = {
        "source": source,
        "parsers": (ssg.parsers.ResourceParser()),
        "dest": dest,
    }
    Site(**config).build()


typer.run(main)
