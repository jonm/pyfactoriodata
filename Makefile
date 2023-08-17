VERSION = 1.1.65a1
WHEEL = dist/pyfactoriodata-$(VERSION)-py3-none-any.whl

all: check $(WHEEL)

data.lua: data.raw raw-to-export.awk
	awk -f raw-to-export.awk < data.raw > data.lua

pyfactoriodata/data.json: data.lua util.lua
	LUA_PATH='?;?.lua;vendor/json.lua-0.1.2/?.lua' lua data.lua > pyfactoriodata/data.json

$(WHEEL): pyfactoriodata/__init__.py pyfactoriodata/data.json
	python3 -m build

clean:
	rm -f data.lua pyfactoriodata/data.json
	rm -fr dist/* build/lib

check:
	(cd pyfactoriodata; python3 -m unittest discover)

distclean: clean
	rm -fr dist build pyfactorio.egg-info

