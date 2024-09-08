from scraping.StartPainel import StartPanel

folder='scraping/logs'
name='scraping_backgroud'

new_scraping = StartPanel(name, folder, True)
new_scraping.start_project()