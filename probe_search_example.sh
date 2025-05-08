#!/bin/bash

# 先建立測試檔案
python3 create_test_files.py

# 使用 probe 搜尋包含 "Hello" 的程式碼
probe search "Hello" ./test_codebase

# 使用 probe 搜尋包含 "main" 的程式碼
probe search "main" ./test_codebase

# 使用 probe 搜尋包含 "greet" 的程式碼
probe search "greet" ./test_codebase

# 使用 probe 搜尋包含 "calculate" 的程式碼
probe search "calculate" ./test_codebase
