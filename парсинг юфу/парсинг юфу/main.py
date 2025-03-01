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
        
        # Открываем файл для записи
        with open('output.txt', 'w', encoding='utf-8') as file:
            # Пример: извлечение всех заголовков (тегов <h1>, <h2>, и т.д.)
            headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            
            # Записываем заголовки в файл
            file.write("Заголовки:\n")
            for header in headers:
                file.write(header.text.strip() + '\n')
            
            # Пример: извлечение всех ссылок
            links = soup.find_all('a')
            
            # Записываем ссылки в файл
            file.write("\nСсылки:\n")
            for link in links:
                href = link.get('href')
                if href:  # Проверяем, что атрибут href существует
                    file.write(href + '\n')
                else:
                    file.write("N/A\n")  # Записываем "N/A", если атрибута нет
        
        print("Данные успешно записаны в файл 'output.txt'")
    else:
        print(f'Ошибка при запросе: {response.status_code}')
except requests.exceptions.RequestException as e:
    print(f'Ошибка при выполнении запроса: {e}')