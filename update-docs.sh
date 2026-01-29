#!/bin/bash

# Script to update API documentation in README.md
# Copies everything after "## Documentation for API Endpoints" from README-NEW.md to README.md

echo "Обновление API документации в README.md..."

# Define file paths
SOURCE_FILE="README-NEW.md"
TARGET_FILE="README.md"
TEMP_FILE="temp_readme.md"

# Check if source file exists
if [ ! -f "$SOURCE_FILE" ]; then
    echo "Ошибка: Исходный файл $SOURCE_FILE не найден!"
    exit 1
fi

# Check if target file exists
if [ ! -f "$TARGET_FILE" ]; then
    echo "Ошибка: Целевой файл $TARGET_FILE не найден!"
    exit 1
fi

# Find the line number where "## Documentation for API Endpoints" is located in both files
SOURCE_API_LINE=$(grep -n "^## Documentation for API Endpoints" "$SOURCE_FILE" | cut -d: -f1)
TARGET_API_LINE=$(grep -n "^## Documentation for API Endpoints" "$TARGET_FILE" | cut -d: -f1)

# Check if the section exists in both files
if [ -z "$SOURCE_API_LINE" ]; then
    echo "Ошибка: Раздел '## Documentation for API Endpoints' не найден в $SOURCE_FILE!"
    exit 1
fi

if [ -z "$TARGET_API_LINE" ]; then
    echo "Ошибка: Раздел '## Documentation for API Endpoints' не найден в $TARGET_FILE!"
    exit 1
fi

# Get the content before "## Documentation for API Endpoints" from the target file
head -n "$TARGET_API_LINE" "$TARGET_FILE" > "$TEMP_FILE"

# Get the content after "## Documentation for API Endpoints" from the source file
tail -n +$((SOURCE_API_LINE + 1)) "$SOURCE_FILE" >> "$TEMP_FILE"

# Replace the original target file with the updated content
mv "$TEMP_FILE" "$TARGET_FILE"

echo "API документация успешно обновлена в $TARGET_FILE"
