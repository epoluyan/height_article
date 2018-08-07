from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

path_to_extension = r'./3.32.1_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)


driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()

maxim_url = open('maxim_url.txt','r')
wday_url = open('wday_url.txt','r')
height_article_maxim = open('height_article_maxim.txt','w')
height_article_wday = open('height_article_wday.txt','w')

'''
# Убирает кавычки из ссылок

for line in maxim_url:

    string=line.rstrip()

    if string.startswith('"') and string.endswith('"'):
    
        string = string[1:-1]
        print(string)
        file_height_article.write(string + '\n')
'''
'''
#maxim

for line in maxim_url:

    url_maxim_string = line.rstrip()
    #print(url_maxim_string)
    driver.get(url_maxim_string)
    weight_article_maxim_string = driver.execute_script("return document.querySelector('.article').offsetHeight")
    print(weight_article_maxim_string)
    height_article_maxim.write(url_maxim_string + ',' + str(weight_article_maxim_string) + '\n')
    '''

#wday

for line in wday_url:

    url_wday_string=line.rstrip()
    #print(url_wday_string)
    driver.get(url_wday_string)
    weight_article_wday = driver.execute_script("return document.querySelector('.content__body').offsetHeight") 
    print(weight_article_wday)
    height_article_wday.write(url_wday_string + ',' + str(weight_article_wday) + '\n')



'''
    with open('url+weight.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(zip(a, str(weight_article)))
'''

maxim_url.close()
wday_url.close()
height_article_maxim.close()
height_article_wday.close()






