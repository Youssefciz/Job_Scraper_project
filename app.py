import requests
import time
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def scrape_linkedin(keyword='', page=0):
    base_url = f"https://www.linkedin.com/jobs/search/?keywords={keyword}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    jobs = []
    for p in range(page + 1): 
        url = f"{base_url}&start={p * 25}" 
        response = requests.get(url, headers=headers)
        print(f"Response status code for LinkedIn page {p + 1}: {response.status_code}")
        
        if response.status_code == 429:
            print("Rate limit reached, sleeping for 10 seconds...")
            time.sleep(10)  
            response = requests.get(url, headers=headers)
            print(f"Retrying... Response status code for LinkedIn page {p + 1}: {response.status_code}")
        
        if response.status_code != 200:
            print(f"Failed to retrieve LinkedIn page {p + 1}, status code: {response.status_code}")
            return jobs
        
        soup = BeautifulSoup(response.content, 'html.parser')
        job_cards = soup.find_all('div', class_='base-card')
        print(f"Number of job cards found on LinkedIn page {p + 1}: {len(job_cards)}")
        
        for card in job_cards:
            try:
                title = card.find('h3', class_='base-search-card__title').get_text(strip=True)
                company = card.find('h4', class_='base-search-card__subtitle').get_text(strip=True) if card.find('h4', class_='base-search-card__subtitle') else "N/A"
                location = card.find('span', class_='job-search-card__location').get_text(strip=True) if card.find('span', class_='job-search-card__location') else "N/A"
                link = card.find('a', class_='base-card__full-link')['href']
                jobs.append({'title': title, 'company': company, 'location': location, 'link': link})
                print(f"Job found: {title}, {company}, {location}, {link}")
            except Exception as e:
                print(f"Error parsing job card: {e}")

        time.sleep(1)  

    return jobs

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape_jobs', methods=['GET'])
def scrape_jobs():
    keyword = request.args.get('keyword', '')
    page = int(request.args.get('page', 0))
    jobs = scrape_linkedin(keyword=keyword, page=page)
    job_count = len(jobs)
    return jsonify({'jobs': jobs, 'job_count': job_count})

if __name__ == '__main__':
    app.run(debug=True)
