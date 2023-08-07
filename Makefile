all: data.json

data.lua: data.raw raw-to-export.awk
	awk -f raw-to-export.awk < data.raw > data.lua

data.json: data.lua util.lua
	LUA_PATH='?;?.lua;vendor/json.lua-0.1.2/?.lua' lua data.lua > data.json

clean:
	rm -f data.lua data.json
