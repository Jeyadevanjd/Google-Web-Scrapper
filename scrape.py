from selenium import webdriver
def search(query):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    a = webdriver.Chrome("  your chromedriver or any other webdriver for your webbrowser  ",options=op)
    a.get("https://www.google.com/search?q="+query.lower())
    try:
        data = a.find_element_by_xpath('//*[@id="kx"]/div/div/div')
        print(data.text)
    except:
        data = a.find_element_by_xpath('//*[@id="gsr"]')
        data1 = data.text
        breakdown = data1.splitlines()
        sa = "Description"
        if sa in breakdown:
            split = breakdown.index(sa)
            after = breakdown[split+1:]
            print(after[1])
        else:
            print(breakdown[17])
            print(breakdown[19])
            print(breakdown[20])
