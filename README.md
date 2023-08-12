# pyfactoriodata

This is a set of scripts that can take the raw data export from Factorio, as found
on the [Factorio Wiki](https://wiki.factorio.com/Data.raw), and produce a set of
Python libraries that can be used for further scripting.

# Prerequisites

1. `make`
2. `awk`
3. `lua`
4. `python3`
5. `pip3`
6. `virtualenv` (on my system this was a system package called
   `python3.10-venv`)

Then you can:
```
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt .
```

# Instructions

If you want to start all the way from the beginning, download the raw
data export, and call this `data.raw`. Then, run `make`. This will:

1. Convert `data.raw` into `data.lua`, a Lua script that can export the
   raw data as JSON. There are various cleanup activities that must be
   done to accomplish this successfully, most of which are in `util.lua`,
   including:
   * Substituting `inf` or `-inf` into numbers that are valid JSON.
   * Turning sparse arrays into dictionaries/tables keyed by the string
     representations of the original integer array indices.
   * Converting mixed tables (i.e. ones that have keys that suggest they
     can be treated as Lua arrays as well as keys (usually strings) for
     other properties.

2. Run `data.lua` to output `data.json`.

3. Run `generate.py` to create the hardcoded instances/constants of various
   Python classes. [WIP]

4. Run `python3 -m build` to produce the distributable Python packages.


