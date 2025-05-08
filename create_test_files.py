import os

# 建立測試用的目錄和檔案
base_dir = "test_codebase"
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

# 測試檔案內容
files_content = {
    "file1.py": """
def calculate_sum(a, b):
    return a + b

# 這是一個簡單的加法函數
""",
    "file2.js": """
function greet(name) {
    console.log('Hello, ' + name);
}

// 打招呼函數
""",
    "file3.go": """
package main

import "fmt"

func main() {
    fmt.Println(\"Hello, World!\")
}

// 主函數
""",
    "file4.java": """
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println(\"Hello, Java!\");
    }
}

// Java 主程式
""",
    "file5.rs": """
fn main() {
    println!(\"Hello, Rust!\");
}

// Rust 主函數
"""
}

# 建立檔案
for filename, content in files_content.items():
    with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)

print(f"建立測試檔案完成，目錄：{base_dir}")
