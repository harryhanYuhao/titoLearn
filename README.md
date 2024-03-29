# copr-tito-quickdoc

This repository contains the `hellocopr` program used as an example in the 
[*How to Publish your Software on Copr, Fedora’s User Repository*]( https://docs.fedoraproject.org/en-US/quick-docs/publish-rpm-on-copr/) quick doc.
Hellocopr itself is a very simple demonstration python3 program that does
nothing but display some text on the command line. It (needlessly) uses python
setuptools & imports some python libraries to better illustrate the packaging
process.

The associated Copr repository can be found [here](https://copr.fedorainfracloud.org/coprs/lcts/hellocopr/).

## What is where?

The `master` branch contains all files as used in the quick doc. The quick doc itself as well as an
extensively annotated version of the specfile can be found in the `doc` folder.
The `foreign-sources` branch contains a version of the project adapted for when sources are located
elsewhere, e.g. when you're packaging someone else's tarballs.

The `step-N` tags mark the state of all files *at the end* of the corresponding *Step N*-sections
in the quick doc.

The `hellocopr-<version>-<release>` tags correspond to the released packages available in Copr.
