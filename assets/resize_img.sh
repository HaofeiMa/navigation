#!/bin/sh

find ./site -type f -name "*.png" | while read -r file; do
    size=$(identify -format "%wx%h" "$file" 2>/dev/null)  # 获取图像宽高信息，忽略错误输出
    if [ -n "$size" ]; then
        width=$(echo "$size" | cut -d'x' -f1)
        height=$(echo "$size" | cut -d'x' -f2)
        if [ "$width" -gt 128 ] || [ "$height" -gt 128 ]; then
            convert "$file" -resize 128x128 "$file"
        fi
    fi
done
