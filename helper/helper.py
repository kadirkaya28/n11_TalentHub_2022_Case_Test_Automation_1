def launch_driver(driver: str):
    # pip install webdriver-manager
    match driver:
        case "chrome":
            from selenium.webdriver import Chrome
            from webdriver_manager.chrome import ChromeDriverManager
            from selenium.webdriver.chrome.service import Service as ChromeService

            service = ChromeService(ChromeDriverManager(log_level=0).install())
            return Chrome(service.path)

        case "firefox":
            from selenium.webdriver import Firefox
            from webdriver_manager.firefox import GeckoDriverManager
            from selenium.webdriver.firefox.service import Service as FirefoxService

            service = FirefoxService(GeckoDriverManager(log_level=0).install())
            return Firefox(service)

        case "edge":
            from selenium.webdriver import Edge
            from webdriver_manager.microsoft import EdgeChromiumDriverManager
            from selenium.webdriver.edge.service import Service as EdgeService

            service = EdgeService(EdgeChromiumDriverManager(log_level=0).install())
            return Edge(service.path)

        case "opera":
            from selenium.webdriver import Remote
            from webdriver_manager.opera import OperaDriverManager
            from selenium.webdriver.chrome.service import Service as ChromeService

            service = ChromeService(OperaDriverManager(log_level=0).install())
            service.start()
            return Remote(service.service_url)


def csv_writer(file_name: str, header: str, url_list: list) -> None:
    import csv

    with open(file_name, 'a', encoding='UTF8') as file:
        writer = csv.writer(file)
        for title, href in url_list:
            writer.writerow([header, title, href])


def text_similarity_ratio(text1, text2):
    # pip install fuzzywuzzy
    # pip install Levenshtein
    from fuzzywuzzy import fuzz
    return fuzz.partial_ratio(text1, text2)
