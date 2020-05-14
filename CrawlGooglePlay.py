import pandas as pd
import play_scraper

data = []

apps = pd.read_excel("Sourcing Input List.xlsx")

print("Start searching Google Play...\nSearched Apps:")
for app in apps["Company Name"]:
    print(app)
    id = play_scraper.search(str(app), page=1)[0]['app_id']
    url = play_scraper.details(id)['url']
    score = play_scraper.details(id)['score']
    noInstalls = play_scraper.details(id)['installs']
    dev_url = play_scraper.details(id)['developer_url']
    tuple1 = (url, score, noInstalls, dev_url)
    data.append(tuple1)

df_result = pd.DataFrame(data, columns=['App Url', 'Score', 'No of Installs', 'Developer Url']) #Saving all results in a dataframe


