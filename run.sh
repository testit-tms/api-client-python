#!/bin/bash

# Настройка переменных
FILE_NAME="cloud-swagger.json"
NEW_VERSION="7.5.3"
GENERATOR="openapi-generator-cli-6.6.0.jar"

if [ ! -f ".swagger/$FILE_NAME" ]; then
    echo "Ошибка: .swagger/$FILE_NAME не найден!"
    exit 1
fi

if [ ! -f "genConfig.yml" ]; then
    echo "Ошибка: genConfig.yml не найден!"
    exit 1
fi

echo "Начало генерации Python API клиента..."

# Обновление версии в genConfig.yml
echo "Обновление версии в genConfig.yml..."
sed -i "s/packageVersion: .*/packageVersion: $NEW_VERSION/" genConfig.yml

echo "Обновление версии в setup.py..."
sed -i "s/VERSION = .*/VERSION = \""$NEW_VERSION"\"/" setup.py

# Очистка предыдущей генерации
echo "Очистка предыдущей генерации..."
rm -rf new

# Генерация Python API клиента
echo "Генерация Python API клиента..."

java -jar .vendor/$GENERATOR generate \
  -i .swagger/$FILE_NAME \
  -g python-prior \
  -o new \
  --skip-validate-spec \
  -c genConfig.yml

# Проверка успешности генерации
if [ ! -d "new" ]; then
    echo "Ошибка: Не удалось сгенерировать клиент!"
    exit 1
fi


# Удаление старых исходных файлов
echo "Удаление старых исходных файлов..."
rm -rf src/testit_api_client/*


# Создание директорий если они не существуют
mkdir -p src/testit_api_client

# Копирование новых исходных файлов
echo "Копирование новых исходных файлов..."
if [ -d "new/testit_api_client" ]; then
    cp -r new/testit_api_client/* src/testit_api_client/
fi

# Копирование model_utils.py из .reserved с заменой
if [ -f ".reserved/model_utils.py" ]; then
    echo "Копирование model_utils.py из .reserved..."
    cp .reserved/model_utils.py src/testit_api_client/
fi


# Копирование документации если она была сгенерирована
if [ -d "new/docs" ]; then
    echo "Копирование документации..."
    rm -rf docs/* || true
    cp -r new/docs/* docs/ || true
fi

# Выполнение замен в сгенерированных файлах
echo "Выполнение замен в сгенерированных файлах..."

# test_result_response.py
if [ -f "src/testit_api_client/model/test_result_response.py" ]; then
    echo "Замена в test_result_response.py..."
    sed -i 's/'\''test_point'\'': (TestPoint,),  # noqa: E501/'\''test_point'\'': (TestPoint, none_type,),  # noqa: E501 run.sh autofix/' src/testit_api_client/model/test_result_response.py
fi

# link_model.py
if [ -f "src/testit_api_client/model/link_model.py" ]; then
    echo "Замена в link_model.py..."
    sed -i 's/'\''type'\'': (LinkType,),  # noqa: E501/'\''type'\'': (LinkType, none_type,),  # noqa: E501 run.sh autofix/' src/testit_api_client/model/link_model.py
fi

# link_post_model.py
if [ -f "src/testit_api_client/model/link_post_model.py" ]; then
    echo "Замена в link_post_model.py..."
    sed -i 's/'\''type'\'': (LinkType,),  # noqa: E501/'\''type'\'': (LinkType, none_type,),  # noqa: E501 run.sh autofix/' src/testit_api_client/model/link_post_model.py
fi

# link_put_model.py
if [ -f "src/testit_api_client/model/link_put_model.py" ]; then
    echo "Замена в link_put_model.py..."
    sed -i 's/'\''type'\'': (LinkType,),  # noqa: E501/'\''type'\'': (LinkType, none_type,),  # noqa: E501 run.sh autofix/' src/testit_api_client/model/link_put_model.py
fi

# Замена некорректного максимального значения long на правильное значение MaxValue для Int64
# Это необходимо, потому что OpenAPI генератор иногда использует -9223372036854775616 либо 9223372036854776000 вместо правильного 9223372036854775807
echo "Замена -9223372036854775616 на 9223372036854775807 в сгенерированных моделях..."
find src/testit_api_client/model -name "*.py" -exec sed -i 's/-9223372036854775616/9223372036854775807/g' {} +



# Частичное обновление README.md
echo "Частичное обновление README.md..."
if [ -f "new/README.md" ]; then
    # Создаем копию нового README для обновления
    cp new/README.md README-NEW.md
    # Предполагается, что update-docs.sh обрабатывает Python README
    ./update-docs.sh
fi

echo "Генерация Python API клиента завершена успешно!"
