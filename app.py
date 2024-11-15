import openai

# Ustawienie klucza API (Pamiętaj, by ustawić swój klucz API)
openai.api_key = 'API KEY'

def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def generate_html_from_article(article_text):
    prompt = f"""
    Zajmij się poniższym artykułem, który ma zostać przekształcony w HTML. 
    Użyj odpowiednich tagów HTML do strukturyzacji treści. 
    Gdzie to możliwe, wstaw obrazy w miejsce, które można wykorzystać do generowania wizualizacji, 
    oznaczone tagiem <img src="image_placeholder.jpg" alt="prompt do generowania obrazu">.
    Wstaw także podpisy pod obrazkami.

    Poniżej znajduje się artykuł:

    {article_text}

    Proszę wygenerować odpowiedni kod HTML bez tagów <html>, <head>, <body> (tylko zawartość <body>).
    """

    # Poprawione wywołanie API OpenAI
    response = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500,
        temperature=0.7
    )
    
    return response.choices[0].message.content.strip()

def save_html_to_file(html_content, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

def main():
    article_file = 'artykul.txt'
    output_file = 'artykul.html'

    article_text = read_article(article_file)

    generated_html = generate_html_from_article(article_text)

    save_html_to_file(generated_html, output_file)

    print(f"HTML został zapisany do {output_file}")

if __name__ == "__main__":
    main()