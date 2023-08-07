#!/usr/bin/env -S awk -f

BEGIN {
    printf("#!/usr/bin/env lua\n");
    printf("local json = require \"json\"\n");
    printf("local util = require \"util\"\n");
}
NR == 1 {
    printf("local all_factorio_data = {\n");
}
NR != 1
END {
    printf("local patched = util.map_tree(util.patch)(all_factorio_data)\n");
    printf("print(json.encode(patched))\n");
}
