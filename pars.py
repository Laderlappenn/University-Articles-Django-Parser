import requests

# AUID = int(input())
# url = f"https://api.elsevier.com/content/search/scopus?query=AU-ID({AUID})&apiKey=f0097b56b4ed057a6d01f4a20620c3d0"


def get_publication_info(url):
    response = requests.get(url)
    publications_info = []
    count = 0
    if response.status_code == 200:
        data = response.json()
        entries = data.get("search-results").get("entry")
        for entry in entries:
            title = entry.get("dc:title")
            creator = entry.get("dc:creator")
            publicationName = entry.get("prism:publicationName")

            affil_name = entry["affiliation"][0]["affilname"]
            affiliation_city = entry["affiliation"][0]["affiliation-city"]
            affiliation_country = entry["affiliation"][0]["affiliation-country"]

            articles_info = {
                "title": title,
                "creator": creator,
                "publicationName": publicationName,
                "affil_name": affil_name,
                "affiliation_city": affiliation_city,
                "affiliation_country": affiliation_country
            }


            publications_info.append(articles_info)
    else:
        print("Request failed with status code", response.status_code)

    return publications_info


