# Sublime Artisan Test

This package extends [Sublime PHPUnit](https://github.com/adamwathan/sublime-phpunit) and its installation is required for this package to be functional.

## Installation

Installation is as simple as cloning the repository into your Sublime Text install's `Packages` folder:

```bash
git clone https://github.com/bradenkeith/sublime-artisan-test ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/sublime-artisan-test
```

## Available Commands & Example Keybindings

You can find the commands in the command palette under "Artisan Test", or map any of these commands to whatever shortcuts you want:

Here's the full list of commands:

```
run_artisan_test
run_artisan_tests_in_dir
run_single_artisan_test
run_all_artisan_tests
````

Here are some example keybindings:

```json
[
    { "keys": ["alt+t"], "command": "run_artisan_test"},
    { "keys": ["super+alt+t"], "command": "run_single_artisan_test"},
    { "keys": ["super+shift+t"], "command": "run_artisan_tests_in_dir"},
    { "keys": ["super+shift+ctrl+t"], "command": "run_all_artisan_tests"},
]

```

## Using iTerm2 instead of Terminal.app or fish shell

This package obeys the terminal selection set in [Sublime PHPUnit](https://github.com/adamwathan/sublime-phpunit).
