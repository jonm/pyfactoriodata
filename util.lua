-- utility functions

local util = {}
local json = require "json"

-- render data structure as string
function dump(o)
  if type(o) == 'table' then
    local s = '{ '
    for k,v in pairs(o) do
      if type(k) ~= 'number' then k = '"'..k..'"' end
      s = s .. '['..k..'] = ' .. dump(v) .. ','
    end
    return s .. '} '
  else
    return tostring(o)
  end
end
util.dump = dump

function size(l)
  local n = 0
  for k,v in pairs(l) do
    n = n + 1
  end
  return n
end

function empty(t)
  return size(t) == 0
end

function map(f)
  return function(l)
    local out = {}
    for _,v in ipairs(l) do
      table.insert(out, f(v))
    end
    return out
  end
end

function filter(f)
  return function(l)
    local out = {}
    for _,v in ipairs(l) do
      if f(v) then
        table.insert(out, v)
      end
    end
    return out
  end
end

function keys(t)
  local out = {}
  for k,v in pairs(t) do
    table.insert(out, k)
  end
  return out
end
util.keys = keys

function map_tree(f)
  return function(t)
    if type(t) ~= 'table' then return f(t) end
    local temp = f(t)
    if type(temp) ~= 'table' then return temp end
    local out = {}
    for k,v in pairs(temp) do
      out[k] = map_tree(f)(v)
    end
    return out
  end
end
util.map_tree = map_tree

function encode_infinity(x)
  if x == 1e309 then return 2147483647 end
  if x == -1e309 then return -2147483648 end
  return x
end

function map_keys(f)
  return function(t)
    if type(t) ~= 'table' then return t end
    local out = {}
    for k,v in pairs(t) do
      out[f(k)] = v
    end
    return out
  end
end

function compose(f,g)
  return (function (x) return g(f(x)) end)
end

function mixed_keys_p(t)
  local ks = keys(t)
  local number_keys = filter(function (k) return type(k) == "number" end)(ks)
  local n_numbers = size(number_keys)
  return n_numbers > 0 and n_numbers < size(ks)
end

function fix_mixed_keys(t)
  if type(t) ~= 'table' then return t end
  if not mixed_keys_p(t) then return t end
  local out = {}
  out.elements = {}
  for k,v in pairs(t) do
    if type(k) == 'number' then
      out.elements[k] = v
    else
      out[k] = v
    end
  end
  return out
end
util.fix_mixed_keys = fix_mixed_keys

function sparse_array_p(t)
  if type(t) ~= 'table' then return false end
  if mixed_keys_p(t) then return false end
  if empty(t) then return false end
  if type(keys(t)[1]) ~= 'number' then return false end
  return size(t) ~= #t
end

function fix_sparse_array(t)
  if type(t) ~= 'table' then return t end
  if not sparse_array_p(t) then return t end
  return map_keys(function (k) return tostring(k) end)(t)
end
util.fix_sparse_array = fix_sparse_array

function patch(t)
  return compose(encode_infinity, compose(fix_mixed_keys, fix_sparse_array))(t)
end
util.patch = patch

function find_problem(t, path)
  if type(t) == 'table' then
    if pcall(function () json.encode(t) end) then
      -- ok
    else
      print("problem at", dump(path))
      for tk,tv in pairs(t) do
        next_path = {}
	for k,v in pairs(path) do
	  next_path[k] = v
	end
	table.insert(next_path,tk)
	find_problem(tv,next_path)
      end
    end
  end
end
util.find_problem = find_problem
return util





