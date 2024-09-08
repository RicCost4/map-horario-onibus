from scraping.StartPainel import StartPanel

folder='scraping/logs'
name='scraping'

new_scraping = StartPanel(name, folder, False)
new_scraping.start_project()