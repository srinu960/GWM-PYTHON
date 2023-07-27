import hashlib
url_mapping = {}
def shorten_url(url):
    hash_object = hashlib.sha256(url.encode())
    short_code = hash_object.hexdigest()[:8]
    url_mapping[short_code] = url
    return short_code
def main():
    original_url = "https://www.coursera.com/some/long/url/to/be/shortened"
    
    # Shorten the URL
    short_code = shorten_url(original_url)
    print(f"Original URL: {original_url}")
    print(f"Shortened URL: http://studylink.com/{short_code}")
    
if __name__ == "__main__":
    main()
