# pySigma-plugin-directory
Directory of pySigma backend, processing pipeline and validator projects.

## Purpose

[pySigma](https://github.com/SigmaHQ/pySigma) is a library for handling and conversion of [Sigma
rules](https://github.com/SigmaHQ/sigma). It is extensible by design and support for particular target query languages
(so-called backends) and processing pipelines that transform Sigma rules between data models are implemented as separate
projects to keep the pySigma core as small as possible. In addition, Sigma rule validators can be also implemented as
separate projects and should be if the implemented checks have a special purpose or a backend-specific.

## Usage

The directory is contained in `pySigma-plugins-v0.json`. Generation of a human readable directory is planned. Use it for
finding the backend you need or for your own Sigma frontend. [Sigma CLI](https://github.com/SigmaHQ/sigma-cli) will use
it for installation of additional components as plugins instead of being a bloated monolithic project that brings all
backends with it while you only need few of them.

## Versioning

The `v0` in the file name refers to the format version like APIs do. Versions from 1 will be always backwards compatible and
contain only additions. Breaking changes will increase the version number.

Version 0 has a special role for work in progress until the plugin system is done and working to have some flexibility
while development. You can use it, but things might break in the initial release. Version 0 shouldn't exist for more
than few months (pessimistic estimate).

## Format

tbd

## Useful Resources

* [pySigma backend and pipeline cookiecutter template](https://github.com/SigmaHQ/cookiecutter-pySigma-backend/) for
  starting new projects.
* Micah Babinski's great [blog post about developing a backend](https://micahbabinski.medium.com/creating-a-sigma-backend-for-fun-and-no-profit-ed16d20da142).