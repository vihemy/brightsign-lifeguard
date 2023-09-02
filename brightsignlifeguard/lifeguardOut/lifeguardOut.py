import os
import json
import argparse
from copyfile import copyFile


def theprogram():
    # Set up arguments for terminal command use
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "presentation_directory",
        help="Root directory containing Brightsign presentation (local-sync.json + pool/).",
    )
    args = parser.parse_args()
    PRESENTATION_LOCATION = args.presentation_directory

    # Check if the path is a directory
    if os.path.isdir(PRESENTATION_LOCATION):
        if PRESENTATION_LOCATION[-1] != "/":
            PRESENTATION_LOCATION = PRESENTATION_LOCATION + "/"
    else:
        print("ERROR: Target not a valid directory. (Sorry)")
        exit()

    if not os.path.isdir(PRESENTATION_LOCATION + "kiddie_pool"):
        os.mkdir(PRESENTATION_LOCATION + "kiddie_pool")

    if not os.path.isfile(PRESENTATION_LOCATION + "local-sync.json"):
        print(
            """Presentation directory is missing a local-sync.json file.
            Probably not a full Brightsign Presentation folder"""
        )
        exit()

    # Load JSON data
    with open(
        PRESENTATION_LOCATION + "local-sync.json", "r", encoding="utf-8"
    ) as json_file:
        data = json.load(json_file)

    for download in data["files"]["download"]:
        name = download["name"]
        urlpath = download["link"]
        filepath = PRESENTATION_LOCATION + urlpath

        # Check if the file name ends with .bml and change the extension to .bpfx
        if name.endswith(".bml"):
            name = os.path.splitext(name)[0] + ".bpfx"
        copyFile(
            os.path.abspath(filepath),
            os.path.abspath(PRESENTATION_LOCATION + "kiddie_pool/" + name),
        )

    print("Adult swim is over. Presentation files are now in the kiddle_pool.")


# Call the function to run the script
theprogram()
