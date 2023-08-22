VERSION = 1.1.65a1
WHEEL = dist/pyfactoriodata-$(VERSION)-py3-none-any.whl
SOURCES = pyfactoriodata/fluid.py pyfactoriodata/ingredient.py \
	pyfactoriodata/item.py pyfactoriodata/product.py \
	pyfactoriodata/recipe.py pyfactoriodata/technology.py

all: check $(WHEEL)

data.lua: data.raw raw-to-export.awk
	awk -f raw-to-export.awk < data.raw > data.lua

pyfactoriodata/data.json: data.lua util.lua
	LUA_PATH='?;?.lua;vendor/json.lua-0.1.2/?.lua' lua data.lua > pyfactoriodata/data.json

pyfactoriodata/__init__.py: pyfactoriodata/data.json generate.py
	rm -f pyfactoriodata/__init__.py
	touch pyfactoriodata/__init__.py
	PYTHONPATH=pyfactoriodata python3 generate.py \
          -j pyfactoriodata/data.json -o pyfactoriodata/__init__.py

$(WHEEL): pyfactoriodata/__init__.py pyfactoriodata/data.json $(SOURCES)
	python3 -m build

clean:
	rm -f data.lua pyfactoriodata/data.json pyfactoriodata/__init__.py
	rm -fr dist/* build/lib

check:
	(cd pyfactoriodata; python3 -m unittest discover)

distclean: clean
	rm -fr dist build pyfactorio.egg-info

