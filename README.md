# Tank Game

## Some Quick Notes

This is a work in progress. I will push significant updates to master, but it is by no
means complete.

When viewing the code, your linter might freak out regarding pygame. It may say 
something like "pygame has no member init." This is a lie, the member exists. If this is
the case, then "settings.json" in the ".vscode" folder needs to be updated.

```
    "python.linting.pylintArgs": [
        "--extension-pkg-whitelist=pygame" // comma separated
    ]
```
This whitelists the pygame extension, removing the linting error.
(Information via https://stackoverflow.com/questions/50569453/why-does-it-say-that-module-pygame-has-no-init-member)


## Controls

Arrow keys to move left and right. Avoid the blocks!

## Installation
Install information for <strong>pygame</strong> from https://www.pygame.org/wiki/GettingStarted

<p><strong>Pygame Installation</strong></p>
<p>Pygame requires Python; if you don't already have it, you can download it from python.org. Use python 3.6.1 or greater, because it is much friendlier to newbies, and additionally runs faster.

The best way to install pygame is with the pip tool (which is what python uses to install packages). Note, this comes with python in recent versions. We use the --user flag to tell it to install into the home directory, rather than globally.</p>

    python3 -m pip install -U pygame --user

To see if it works, run one of the included examples:

    python3 -m pygame.examples.aliens

If it works, you are ready to go!


## Running
Running information for <strong>pygame</strong> from https://artofproblemsolving.com/wiki/index.php/How_to_run_Pygame_Programs

<strong>Ubuntu/Linux</strong>
1. Open a terminal. (Gnome: Applications->Accessories->Terminal. Unity (Ubuntu 11.04): Applications ->Type 'terminal' in the search box -> Double click on the terminal application icon.)

2. Navigate to the folder where the Python program you want to run is located (Where "Tank_Game" folder is located).

3. Type 'python main.py' and press enter to run the program. Watch the terminal for any errors.

<strong>Mac</strong>
1. Open a terminal. (Command+Space, then type terminal in the search box and press enter.)

2. Navigate to the folder where the Python program you want to run is located. By default IDLE saves in your Documents folder, so enter 'cd Documents' into the terminal to get there.

3. Type 'python3 main.py' and press enter to run the program. Watch the terminal for any errors.
