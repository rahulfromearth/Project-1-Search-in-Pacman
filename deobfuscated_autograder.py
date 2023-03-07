import binascii
import math


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsnp(msg, pubkey):
    v1_int = int(math.log(pubkey[1], 256))
    v2_int = v1_int + 1
    v3_str = "%%0%dx" % (v2_int * 2,)
    v4_msg_enc = msg.encode()
    v5_list = []
    for v6_int in range(0, len(v4_msg_enc), v1_int,):
        v7_enc_bytes = v4_msg_enc[v6_int : v6_int + v1_int]
        v7_enc_bytes += b"\\x00" * (v1_int - len(v7_enc_bytes))
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkslpB = int(
            binascii.hexlify(v7_enc_bytes), 16
        )
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkslnp = pow(
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkslpB, *pubkey
        )
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkslnB = binascii.unhexlify(
            (v3_str % JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkslnp).encode()
        )
        v5_list.append(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkslnB)
    return b"".join(v5_list)


"""
submission_autograder.py: Local autograder client.
See README.md for a summary of how this program works.
Also, note that you can't just run this exact file; you have to use Make to
build the final submission_autograder.py file, then run that.
The build process (Makefile) #includes header.py and rsa.py here:
* header.py replaces the print statement with the Python 3 print() function.
* header.py replaces open with codecs.open; this must be done in header.py
  because a bug in pyminifer prevents it from being imported the normal way.
* rsa.py imports binascii and math.
* rsa.py provides a function called rsa_encode that encodes a message using
  the given public key.
"""

import base64
import hashlib
import json
import logging
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib2
import zipfile

JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkslBp = time.time()
JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkslBn = "search"
JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksnpl = {
    "tutorial": "http://s3-us-west-2.amazonaws.com/cs188websitecontent/projects/release/tutorial/v1/001/tutorial.zip",
    "search": "https://s3-us-west-2.amazonaws.com/cs188websitecontent/projects/release/search/v1/001/search.zip",
    "multiagent": "https://s3-us-west-2.amazonaws.com/cs188websitecontent/projects/release/multiagent/v1/005/multiagent.zip",
    "reinforcement": "https://s3-us-west-2.amazonaws.com/cs188websitecontent/projects/release/reinforcement/v1/002/reinforcement.zip",
    "bayesnets": "https://s3-us-west-2.amazonaws.com/cs188websitecontent/projects/sp16/bayesNets2/bayesNets2.zip",
    "tracking": "https://s3-us-west-2.amazonaws.com/cs188websitecontent/projects/sp16/tracking/tracking.zip",
    "classification": "https://s3-us-west-2.amazonaws.com/cs188websitecontent/projects/sp16/classification_sp16/classification_sp16.zip",
}
JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksnpB = {
    "tutorial": ["shopSmart.py", "buyLotsOfFruit.py", "addition.py"],
    "search": ["searchAgents.py", "search.py"],
    "multiagent": ["multiAgents.py"],
    "reinforcement": ["analysis.py", "qlearningAgents.py", "valueIterationAgents.py"],
    "bayesnets": ["factorOperations.py", "inference.py"],
    "tracking": ["bustersAgents.py", "inference.py"],
    "classification": [
        "perceptron.py",
        "answers.py",
        "solvers.py",
        "search_hyperparams.py",
        "features.py",
    ],
}
JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksnlp = False
JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksnlB = "1.3.1"
JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksnBp = 5000000
JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksnBl = [
    sys.executable or "python",
    "autograder.py",
    "--mute",
    "--no-graphics",
    "--edx-output",
]
JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksBpl = 79
JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksBpn = "%A, %B %d, %Y, %H:%M:%S"
JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksBlp = (
    33751518165820762234153612797743228623,
    56285023496349038954935919614579038707,
)
JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksBln = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksnpl[
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkslBn
].replace(
    "https://", "http://"
)
JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksBnp = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksnpB[
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkslBn
]


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsnl(
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpsln,
    width=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksBpl,
    indent=0,
    right_margin=5,
):
    print(
        " " * indent
        + JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpsln
        + "."
        * (
            width
            - len(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpsln)
            - right_margin
            - indent
        ),
        end="",
    )
    sys.stdout.flush()


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpsl(msg="DONE", indent=1):
    print(" " * indent + msg)
    sys.stdout.flush()


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpsn(file_path, block_size=65536):
    if not os.path.isfile(file_path):
        return "(not file)"
    if os.path.getsize(file_path) > JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksnBp:
        return "(file too big)"
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpsBl = hashlib.sha256()
    with open(file_path, "rb") as f:
        for v7_enc_bytes in iter(lambda: f.read(block_size), b""):
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpsBl.update(v7_enc_bytes)
    return JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpsBl.hexdigest()


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpls(file_path, mode="r"):
    if not os.path.isfile(file_path):
        return "(not file)"
    with open(file_path, mode) as f:
        return f.read()


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpln():
    print("-" * JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksBpl, end="\n\n")
    print("CS 188 Local Submission Autograder")
    print("Version " + JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksnlB, end="\n\n")
    print("-" * JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksBpl, end="\n\n")


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpns():
    if JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksnlp:
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpsBn = "submission_autograder.log"
        logging.basicConfig(
            format="%(asctime)s - %(levelname)s - %(message)s",
            level=logging.DEBUG,
            stream=open(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpsBn, "w"),
        )
    else:
        logging.basicConfig(format="\nERROR - %(message)s", level=logging.CRITICAL)


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpnl():
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplsn = os.path.dirname(
        os.path.realpath(__file__)
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplsB = os.getcwd()
    if (
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplsB
        != JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplsn
    ):
        print(
            "WARNING - Your current directory does not appear to be the project directory"
        )


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBlsp():
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsnl("Setting up environment")
    try:
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplns = tempfile.mkdtemp(
            prefix="cs188-"
        )
        logging.debug(
            "Temporary directory created at "
            + JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplns
        )
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpsl()
        return JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplns
    except Exception as e:
        logging.critical("Could not create temp directory: " + str(e))
        sys.exit(104)


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBlsn(
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBsp, dest_dir
):
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsnl("Downloading autograder")
    logging.debug(
        "Downloading from " + JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBsp
    )
    try:
        f = urllib2.urlopen(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBsp)
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplnB = os.path.join(
            dest_dir,
            os.path.basename(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBsp),
        )
        with open(
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplnB, "wb"
        ) as JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplBs:
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplBs.write(f.read())
    except Exception as e:
        logging.critical("Download failed: " + str(e))
        sys.exit(101)
    logging.debug("Downloaded to " + JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplnB)
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpsl()
    return JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplnB


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBlps(
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBnl, dest_dir
):
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsnl("Extracting autograder")
    logging.debug("Extracting " + JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBnl)
    with zipfile.ZipFile(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBnl) as f:
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplBn = f.namelist()
        if len(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplBn) == 0:
            logging.critical("ZIP archive contains no files")
            sys.exit(102)
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnsl = os.path.join(
            dest_dir, f.namelist()[0]
        )
        try:
            f.extractall(dest_dir)
        except Exception as e:
            logging.critical("Extraction from zip file failed: " + str(e))
            sys.exit(105)
    logging.debug(
        "Extracted inner directory "
        + JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnsl
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpsl()
    return JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnsl


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBlpn(dest_dir):
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsnl("Preparing student files")
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplBn = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksnpB[
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkslBn
    ]
    for f in JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplBn:
        if not os.path.isfile(f):
            logging.critical("Could not find required file: " + f)
            sys.exit(201)
        shutil.copyfile(f, os.path.join(dest_dir, f))
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpsl()


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBlns(
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklspn,
):
    print("Running tests (this may take a while):")
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnsB = (
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnBs
    ) = ""
    try:
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnls = subprocess.Popen(
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksnBl,
            stdout=subprocess.PIPE,
            cwd=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklspn,
        )
        for JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnlB in iter(
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnls.stdout.readline, b""
        ):
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnsB += (
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnlB
            )
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnlB = (
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnlB.strip()
            )
            if re.match(
                r"Question q\\d+$", JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnlB
            ):
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsnl(
                    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnlB,
                    width=40,
                    indent=2,
                )
            elif re.match(
                r"### Question q\\d+: \\d+/\\d+ ###",
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnlB,
            ):
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpsl(
                    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnlB.split(": ")[
                        1
                    ].strip("#")
                )
            elif (
                "*** NOTE: Make sure to complete"
                in JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnlB
            ):
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpsl("skipped")
            elif re.match(
                r"Total: \\d+/\\d+$", JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnlB
            ):
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnBs = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnlB.split(
                    ": "
                )[
                    1
                ]
    except Exception as e:
        logging.critical("Autograder invocation failed: " + str(e))
        sys.exit(103)
    finally:
        if JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnls.poll() is None:
            try:
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnls.kill()
            except OSError:
                pass
    return (
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnsB,
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnBs,
    )


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBlnp(
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklspn,
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnsB,
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnBs,
):
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsnl("Generating submission token")
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnBl = os.listdir(
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklspn
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBsl = [
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpsn(
            os.path.join(
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklspn,
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpsln,
            )
        )
        for JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpsln in JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnBl
    ]
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBsn = [
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpls(
            os.path.join(
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklspn,
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpsln,
            )
        )
        for JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpsln in JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksBnp
    ]
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBls = {
        "project": JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkslBn,
        "local_time": time.strftime(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksBpn),
        "gmt_time": time.strftime(
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksBpn, time.gmtime()
        ),
        "duration_sec": time.time()
        - JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkslBp,
        "score": JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnBs,
        "raw_output": JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnsB,
        "self_contents": JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpls(__file__),
        "current_dir": os.getcwd(),
        "current_dir_ls": os.listdir("."),
        "work_dir": JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklspn,
        "work_dir_ls": JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnBl,
        "work_dir_checksums": JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBsl,
        "work_dir_student_files": JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBsn,
        "env": str(os.environ),
        "os": platform.uname(),
    }
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBln = (
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkslBn + ".token"
    )
    with open(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBln, "w", "utf-8") as f:
        f.write(
            unicode(
                binascii.b2a_base64(
                    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsnp(
                        json.dumps(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBls),
                        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksBlp,
                    )
                )
            )
        )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpsl()
    return JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBln


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnsp(
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnBs,
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBln,
):
    print("\n" + "-" * JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksBpl, end="\n\n")
    print("Final score: " + JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnBs)
    print(
        "Token file: " + JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBln, end="\n\n"
    )
    print(
        "Please make sure that this score matches the result produced by autograder.py.",
        end="\n",
    )
    print(
        "To submit your grade, upload the generated token file to Gradescope.",
        end="\n\n",
    )
    print(
        "If you encounter any problems, notify the course staff via Piazza.", end="\n\n"
    )
    print("-" * JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksBpl)


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnsl():
    if len(sys.argv) > 1:
        print("This program does not accept any arguments.")
        sys.exit(1)
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpln()
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpns()
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBpnl()
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBns = (
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBlsp()
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBnl = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBlsn(
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLksnpl[
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkslBn
        ],
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBns,
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklspn = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBlps(
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBnl,
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBns,
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBlpn(
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklspn
    )
    (
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnsB,
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnBs,
    ) = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBlns(
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklspn
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBln = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBlnp(
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklspn,
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnsB,
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnBs,
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnsp(
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnBs,
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpBln,
    )


if __name__ == "__main__":
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnsl()


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnps(choices):
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklspB = sum(w for c, w in choices)
    r = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.uniform(
        0, JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklspB
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklsnp = 0
    for c, w in choices:
        if JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklsnp + w >= r:
            return c
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklsnp += w
    assert False, "Shouldn't get here"


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnpl(p=0.5):
    return JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.random() < p


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnls(value, p=0.5):
    return value if JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnpl(p) else None


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnlp(
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpsn, n, nonempty=False
):
    if nonempty:
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklsnB = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.randrange(
            1, n
        )
    else:
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklsnB = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.randrange(
            n
        )
    return [
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpsn()
        for _ in range(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklsnB)
    ]


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskpln(
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpsn,
    n,
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklsBn,
):
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklsBp = collections.OrderedDict()
    while len(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklsBp) < n:
        v = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpsn()
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklsBp[
            getattr(v, JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklsBn)
        ] = v
    return JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklsBp.values()


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskplB():
    def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskpnl():
        def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskpnB(w):
            if JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnpl(0.9):
                return w
            return JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.choice(
                ["`{}`", "_{}_", "*{}*"]
            ).format(w)

        return " ".join(
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskpnB(w)
            for w in loremipsum.get_sentence().split()
        )

    def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskpBl():
        return "{0} {1}".format(
            "#" * JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.randrange(1, 7),
            loremipsum.get_sentence(),
        )

    def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskpBn():
        return "```{0}```".format(
            "\n".join(
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnlp(
                    loremipsum.get_sentence, 4
                )
            )
        )

    def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsklpn():
        return "\n".join(
            "* " + s
            for s in JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnlp(
                loremipsum.get_sentence, 4
            )
        )

    def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsklpB():
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpsn = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnps(
            [
                (JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskpnl, 7),
                (JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskpBl, 1),
                (JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskpBn, 1),
                (JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsklpn, 1),
            ]
        )
        return JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpsn()

    return "\n\n".join(
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnlp(
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsklpB, 4, nonempty=True
        )
    )


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsklnp():
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpns = names.get_full_name()
    (
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpnB,
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpBs,
    ) = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpns.lower().split(" ")
    return JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpBn(
        name=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnls(
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpns, 0.5
        ),
        email="{0}{1}{2}{3}@{4}".format(
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.choice(
                [
                    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpnB,
                    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpnB[0],
                ]
            ),
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.choice(
                string.ascii_lowercase
            )
            if JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnpl()
            else ",JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.choice([JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpBs,JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpBs[0]]),JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.randrange(10)if JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnpl()else ",
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.choice(
                ["berkeley.edu", "gmail.com"]
            ),
        ),
        is_admin=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnpl(0.05),
    )


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsklnB():
    return JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklnsp(
        offering="{0}/{1}/{2}{3}".format(
            "cal",
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.choice(
                ["cs61a", "ds88"]
            ),
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.choice(
                ["sp", "su", "fa"]
            ),
            str(
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.randrange(100)
            ).zfill(2),
        ),
        institution="UC Berkeley",
        display_name="{0} {1}{2}".format(
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.choice(
                ["CS", "Data Science"]
            ),
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.randrange(100),
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.choice(["", "A"]),
        ),
        active=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnpl(0.3),
    )


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsklBp(
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlsB,
):
    if JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnpl(0.5):
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklnps = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.choice(
            ["Hog", "Hog Contest", "Maps", "Ants", "Scheme"]
        )
    else:
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklnps = "{0} {1}".format(
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.choice(
                ["Homework", "Lab", "Quiz"]
            ),
            str(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.randrange(15)).zfill(
                2
            ),
        )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpsln = (
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlsB.offering
        + "/"
        + JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklnps.lower().replace(" ", "")
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklnpB = datetime.datetime.utcnow().replace(
        hour=0, minute=0, second=0, microsecond=0
    ) - datetime.timedelta(
        seconds=1
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklnpB = (
        pytz.timezone("America/Los_Angeles")
        .localize(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklnpB)
        .astimezone(pytz.utc)
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklnBs = (
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklnpB
        + datetime.timedelta(
            days=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.randrange(-100, 100)
        )
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklnBp = (
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklnBs
        + JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.choice(
            [datetime.timedelta(minutes=15), datetime.timedelta(days=1)]
        )
    )
    return JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklBsp(
        name=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpsln,
        course_id=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlsB.id,
        display_name=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklnps,
        due_date=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklnBs,
        lock_date=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklnBp,
        max_group_size=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.randrange(
            1, 3
        ),
        revisions_allowed=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnpl(0.3),
        files={"fizzbuzz.py": original_file},
    )


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsklBn(
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlpB,
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlsB,
):
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklBsn = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnps(
        [("student", 100), ("grader", 2), ("staff", 20), ("instructor", 2),]
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklBps = "".join(
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.choice(string.digits)
        for _ in range(8)
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklBpn = "{0}-{1}".format(
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlsB.offering.split("/")[1],
        "".join(
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.choice(
                string.ascii_lowercase
            )
            for _ in range(3)
        ),
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklBns = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.randrange(
        30
    )
    return JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklBnp(
        user_id=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlpB.id,
        course_id=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlsB.id,
        role=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklBsn,
        sid=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnls(
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklBps, 0.4
        ),
        class_account=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnls(
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklBpn, 0.4
        ),
        section=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnls(
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklBns, 0.4
        ),
    )


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsknpl(
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlpB,
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlBs,
):
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknspB = {
        "file_contents": {
            "fizzbuzz.py": modified_file,
            "moby_dick": "Call me Ishmael.",
        },
        "analytics": {},
    }
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslp = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnpl(
        0.1
    )
    if JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslp:
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknspB["file_contents"][
            "submit"
        ] = ""
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBsl(
        created=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlBs.due_date
        - datetime.timedelta(
            seconds=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.randrange(
                -100000, 100
            )
        ),
        submitter_id=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlpB.id,
        assignment_id=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlBs.id,
        submit=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslp,
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB.messages = [
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknsBp(kind=k, contents=m)
        for k, m in JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknspB.items()
    ]
    return JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsknpB(
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB,
):
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknpsl = datetime.datetime.now() - datetime.timedelta(
        minutes=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.randrange(100)
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplBn = (
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB.files()
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknpsB = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.choice(
        list(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplBn)
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklsnB = len(
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkplBn[
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknpsB
        ].splitlines()
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnlB = (
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.randrange(
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklsnB
        )
        + 1
    )
    return JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknpls(
        created=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknpsl,
        backup_id=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB.id,
        author_id=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB.submitter.id,
        filename=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknpsB,
        line=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnlB,
        message=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskplB(),
    )


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsknlp(
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB,
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBpl,
    kind="autograder",
):
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknpsl = datetime.datetime.now() - datetime.timedelta(
        minutes=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.randrange(100)
    )
    if kind == "composition":
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnBs = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.randrange(
            2
        )
    else:
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnBs = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.uniform(
            0, 100
        )
    return JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknplB(
        created=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknpsl,
        backup_id=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB.id,
        assignment_id=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB.assignment.id,
        grader_id=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBpl.id,
        kind=kind,
        score=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnBs,
        message=loremipsum.get_sentence(),
    )


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsknlB(
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB,
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBspn,
):
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknpsl = datetime.datetime.now() - datetime.timedelta(
        minutes=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.randrange(100)
    )
    return JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknpBs(
        created=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknpsl,
        backup=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB,
        assignment=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB.assignment,
        course=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB.assignment.course,
        grader=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBspn,
    )


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsknBp():
    print("Seeding users...")
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknpBl = [
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpBn(
            email="okstaff@okpy.org", is_admin=True
        )
    ]
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknpBl.extend(
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskpln(
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsklnp, 30, "email"
        )
    )
    db.session.add_all(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknpBl)
    db.session.commit()


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsknBl():
    print("Seeding courses...")
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlsp = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskpln(
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsklnB, 4, "offering"
    )
    db.session.add_all(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlsp)
    db.session.commit()


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskBpl():
    print("Seeding assignments...")
    for (
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlsB
    ) in JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklnsp.query.all():
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlps = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskpln(
            functools.partial(
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsklBp,
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlsB,
            ),
            5,
            "name",
        )
        db.session.add_all(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlps)
    db.session.commit()


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskBpn():
    print("Seeding enrollments...")
    for (
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlpB
    ) in JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpBn.query.all():
        for (
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlsB
        ) in JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklnsp.query.all():
            if not JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnpl(0.9):
                continue
            db.session.add(
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsklBn(
                    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlpB,
                    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlsB,
                )
            )
    db.session.commit()


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskBlp():
    for (
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlpB
    ) in JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpBn.query.all():
        print(
            "Seeding backups for user {0}...".format(
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlpB.email
            )
        )
        for (
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlBs
        ) in JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklBsp.query.all():
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlBp = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnlp(
                functools.partial(
                    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsknpl,
                    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlpB,
                    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlBs,
                ),
                30,
            )
            db.session.add_all(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknlBp)
        db.session.commit()


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskBln():
    print("Seeding version...")
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBsp = (
        "https://github.com/Cal-CS-61A-Staff/ok-client/releases/download/v1.5.4/ok"
    )
    ok = Version(
        name="ok-client",
        current_version="v1.5.4",
        download_link=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBsp,
    )
    db.session.add(ok)


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskBnp():
    print("Seeding comments...")
    for (
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB
    ) in JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBsl.query.filter_by(
        submit=True
    ).all():
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBps = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBnlp(
            functools.partial(
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsknpB,
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB,
            ),
            6,
        )
        db.session.add_all(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBps)
    db.session.commit()


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskBnl():
    print("Seeding scores...")
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBpl = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklpBn.query.filter_by(
        is_admin=True
    ).first()
    for (
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB
    ) in JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBsl.query.filter_by(
        submit=True
    ).all():
        if JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.choice([True, False]):
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnBs = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsknlp(
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB,
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBpl,
            )
            db.session.add(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkpnBs)
    db.session.commit()


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLspkln():
    print("Seeding queues...")
    for (
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBls
    ) in JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklBsp.query.filter(
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLklBsp.id % 2 == 0
    ):
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBlp = (
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBls.course.get_staff()
        )
        if not JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBlp:
            print(
                "No staff for ",
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBls.course,
            )
            continue
        JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBspl = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBsl.query.filter_by(
            submit=True, assignment=JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBls
        )
        for (
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB
        ) in JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBspl.all():
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBspn = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.choice(
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknBlp
            )
            JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBslp = JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsknlB(
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLknslB,
                JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBspn.user,
            )
            db.session.add(JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBslp)
    db.session.commit()


def JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLspklB():
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLkBsln.JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLspklB(
        0
    )
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsknBp()
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLsknBl()
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskBpl()
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskBpn()
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskBlp()
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskBnp()
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLspkln()
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskBnl()
    JraTyeQNtXgCjfVMPhUKIAcYORSuoDbxGvqWzFmHEidwLskBln()

