import sys
from arghandler import ArgumentHandler
from argparse import RawDescriptionHelpFormatter

from Classifier.classifier_model import train_model_cli


def main(args=sys.argv[1:]):  # noqa  pragma: no cover
    """Parse the args, run the commands."""

    handler = ArgumentHandler(
        epilog="description",
        formatter_class=RawDescriptionHelpFormatter,
    )

    handler.set_subcommands({
        'train': train_model_cli,
        # 'help': subcmd_help
    })

    handler.run(args, context_fxn={})


if __name__ == "__main__":
    main()
