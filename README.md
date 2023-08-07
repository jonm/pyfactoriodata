# pyfactoriodata

This is a set of scripts that can take the raw data export from Factorio, as found
on the [Factorio Wiki](https://wiki.factorio.com/Data.raw), and produce a set of
Python libraries that can be used for further scripting.

# Prerequisites

1. You'll need [`awk`](https://en.wikipedia.org/wiki/AWK#:~:text=AWK%20(awk%20%2F%C9%94%CB%90k%2F,most%20Unix%2Dlike%20operating%20systems.) for the script to convert the raw data extract into a self-exporting
Lua script.
2. You'll need a [lua](https://www.lua.org/) interpreter available to run the self-export script
  and produce JSON output.
3. You'll need [`python3`](https://www.python.org/) and [`pip3`](https://pypi.org/project/pip/) to
  run the remainder of the generation scripts.

Instructions for installing the above are highly system dependent, but they are available
for many platforms. Releases of this package will also include the resulting JSON output from the
first two steps, so if that works for you, you can skip them.

# Instructions

If you want to start all the way from the beginning, download the raw data export, and call this
`data.raw`.

Next, convert this into a self-exporting Lua script by running:
