{
  # NOTE: 'module_name' and 'module_path' come from the 'binary' property in package.json
  # node-pre-gyp handles passing them down to node-gyp when you build from source
  "targets": [
    {
      "target_name": "<(module_name)",
      "sources": [
        "src/main.c"
      ],
      'conditions': [
        ['OS == "linux"', {
          "include_dirs": [
            '<!@(pkg-config --cflags glib-2.0 | sed s/-I//g)'
          ],
          "libraries": [
            '<!@(pkg-config glib-2.0 --libs)'
          ]
        }]
      ],
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [
        "<(module_name)"
      ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ],
      'conditions': [
        ['OS == "win"', {
            "copies": [
              {
                "files": [
                  "<(PRODUCT_DIR)/glib-2.dll",
                  "<(PRODUCT_DIR)/libcharset.dll",
                  "<(PRODUCT_DIR)/libiconv.dll",
                  "<(PRODUCT_DIR)/libintl.dll",
                  "<(PRODUCT_DIR)/pcre.dll"
                ],
                "destination": "<(module_path)"
              }
            ]
        }]
      ],
    }
  ]
}
