# flet-permission-handler

[![pypi](https://img.shields.io/pypi/v/flet-permission-handler.svg)](https://pypi.python.org/pypi/flet-permission-handler)
[![downloads](https://static.pepy.tech/badge/flet-permission-handler/month)](https://pepy.tech/project/flet-permission-handler)
[![license](https://img.shields.io/github/license/flet-dev/flet-permission-handler.svg)](https://github.com/flet-dev/flet-permission-handler/blob/main/LICENSE)

A [Flet](https://flet.dev) extension that simplifies working with device permissions.

It is based on the [permission_handler](https://pub.dev/packages/permission_handler) Flutter package
and brings similar functionality to Flet, including:

- Requesting permissions at runtime
- Checking the current permission status (e.g., granted, denied)
- Redirecting users to system settings to manually grant permissions

## Platform Support

This package supports the following platforms:

| Platform | Supported |
|----------|:---------:|
| Windows  |     ✅     |
| macOS    |     ❌     |
| Linux    |     ❌     |
| iOS      |     ✅     |
| Android  |     ✅     |
| Web      |     ✅     |

## Usage

### Installation

To install the `flet-permission-handler` package and add it to your project dependencies:

=== "uv"
   ```bash
   uv add flet-permission-handler
   ```

=== "pip"
   ```bash
   pip install flet-permission-handler  # (1)!
   ```

   1. After this, you will have to manually add this package to your `requirements.txt` or `pyproject.toml`.

=== "poetry"
   ```bash
   poetry add flet-permission-handler
   ```

### Declaring Permissions

Ensure that your app has the necessary [permissions declared](https://flet.dev/docs/publish#permissions).

## Example

```python title="main.py"
--8<-- "examples/permission_handler_example/src/main.py"
``` 

1. The [`PermissionHandler`][flet_permission_handler.permission_handler.PermissionHandler] instance must be added to the
   [`Page.services`][flet.Page.services] list to work properly.