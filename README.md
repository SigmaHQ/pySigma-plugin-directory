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

The JSON file containing the plugin directory contains a map at its top level that separates into the three plugin
types:

```json
{
    "backends": { ... },
    "pipelines": { ... },
    "validators": { ... }
}
```

Each of these sections is another map that maps an identifier to the plugin specification:

```json
"UUID": {
    "id": "plugin-identifier",
    "description": "xxx backend converting into yyy queries ...",
    "package": "pySigma-backend-...",
    "state": "stable",
    "pysigma-version": "^0.8.1"
}
```

* *UUID* is a [RFC 4122](https://www.rfc-editor.org/rfc/rfc4122)-compliant unique identifier that is used as primary key
  for identification and reference of plugins. This UUID is intended to be used internally by tools to keep a link
  between local usage and the plugin directory. User interfaces should use the more user-friendly *id* identifier
  described below.
* *id* is a short identifier that can be used by other tools to refer to plugins for installation etc. It
  should be as short as possible and ideally only contain the target system name, e.g. `splunk`. In cases where multiple
  implementations of a plugin for the same backend exist, all backend identifiers are extended by a publisher or
  maintainer identifier: *target-publisher*. Because the identifier can change in the life of a plugin it shouldn't be
  used to refer to it technically. The plugin UUID is intended for this purpose.
* *description* is a short description of the plugin that should include the full name of the target system, most
  important output formats and other useful information. It should fit into not more than 120 characters, such that it
  should be possible to display it in one line in many working conditions.
* *package* is a pip package specifier. Most useful are PyPI package names like `pySigma-backend-splunk` and `git+https`
  URLs that contain a Git repository URL with a branch specifier. A PyPI package should be preferred because plugins
  only available via Git repositories have certain restricitons that can make the integration of a plugin into a script
  impossible.
* *project-url* is a URL to a project package. If the plugin source code is hosted on GitHub it is a good choice for
  this attribute.
* *report-issue-url* is a URL for reporting issues for the plugin. For projects hosted on GitHub or similar platforms
  this should be the link to the issue creation page of the project. Another possibility is a [`mailto:`
  URL](https://www.rfc-editor.org/rfc/rfc2368) with an e-mail address, subject etc.
* *state* describes the state of the plugin:
  * `stable` if the plugin is in a working state.
  * `testing` if the plugin is working but might have some issues because it is not yet finished.
  * `devel` if the plugin is under development and important functionality is missing.
  * `broken` if the plugin is in a dysfunctional state but still maintained. Broken plugins are not covered by tests and
    shouldn't be displayed to users in user interfaces.
  * `orphaned` is a state that described that the plugin is not maintained anymore. Such plugins shouldn't normally
    be displayed to the users.
* *pysigma-version* defines the required pySigma version in [PEP 440 version
  specifier](https://peps.python.org/pep-0440/#version-specifiers). This information can be used by other tools to
  verify compatibility of a plugin with their used version of pySigma.

In addition, the top-level map can contain an optional item *note* that can contain information intended for consumers
of the directory, e.g. deprecation notes etc. These should be displayed to the users of such frontend applications.

## Useful Resources

* [pySigma backend and pipeline cookiecutter template](https://github.com/SigmaHQ/cookiecutter-pySigma-backend/) for
  starting new projects.
* Micah Babinski's great [blog post about developing a backend](https://micahbabinski.medium.com/creating-a-sigma-backend-for-fun-and-no-profit-ed16d20da142).