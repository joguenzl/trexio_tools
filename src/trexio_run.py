#!/usr/bin/env python3
"""
Set of tools to interact with trexio files.

Usage:
      trexio check-basis TREXIO_FILE

"""

import trexio
import os


def main(filename, args):
    """Main entry point"""

    print("File name: %s"%filename)
    print("File exists: ", os.path.exists(filename))

    trexio_file = trexio.open(filename, 'r', trexio.TREXIO_TEXT)
    print (trexio_file)
    if trexio_file is None:
        raise IOError

    if arguments["check-basis"]:
        import check_basis
        check_basis.run(trexio_file)

    else:
        pass

    trexio.close(filename)


if __name__ == '__main__':
    from docopt import docopt
    args = docopt(__doc__)
    filename = args["TREXIO_FILE"]
    main(filename, args)


