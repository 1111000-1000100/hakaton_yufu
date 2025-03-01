import requests
from bs4 import BeautifulSoup

# URL сайта
url = 'https://sfedu.ru/'

try:
    # Отправляем GET-запрос к сайту с тайм-аутом
    response = requests.get(url, timeout=10)  # Тайм-аут 10 секунд
    
    # Проверяем, что запрос был успешным
    if response.status_code == 200:
        # Получаем HTML-код страницы
        html = response.text
        
        # Создаем объект BeautifulSoup для анализа HTML
        soup = BeautifulSoup(html, 'html.parser')
        
        # Находим все блоки (например, <div>, <section>, <article>)
        blocks = soup.find_all(['div', 'section', 'article'])
        
        # Сохраняем результат в файл
        with open('sfedu_blocks.txt', 'w', encoding='utf-8') as file:
            for i, block in enumerate(blocks, start=1):
                # Извлекаем заголовки, абзацы и списки внутри блока
                headers = block.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
                paragraphs = block.find_all('p')
                lists = block.find_all(['ul', 'ol'])
                
                # Если блок содержит хотя бы один элемент, записываем его в файл
                if headers or paragraphs or lists:
                    file.write(f"=== Блок {i} ===\n")
                    
                    # Записываем заголовки
                    if headers:
                        file.write("Заголовки:\n")
                        for header in headers:
                            file.write(f"{header.name}: {header.text.strip()}\n")
                    
                    # Записываем абзацы
                    if paragraphs:
                        file.write("\nАбзацы:\n")
                        for paragraph in paragraphs:
                            file.write(paragraph.text.strip() + '\n')
                    
                    # Записываем списки
                    if lists:
                        file.write("\nСписки:\n")
                        for list_item in lists:
                            for item in list_item.find_all('li'):
                                file.write(f"- {item.text.strip()}\n")
                    
                    file.write("\n" + "=" * 30 + "\n")  # Разделитель между блоками
        
        print("Текст успешно сохранен в файл 'sfedu_blocks.txt'")
    else:
        print(f'Ошибка при запросе: {response.status_code}')
except requests.exceptions.RequestException as e:
    print(f'Ошибка при выполнении запроса: {e}')