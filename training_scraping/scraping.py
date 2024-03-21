# import undetected_chromedriver as uc
# from selenium import webdriver 
# from selenium.webdriver.common.by import By
# import time
# import urllib

# driver_path = '/home/riccardo/Downloads/chromedriver-linux64/chromedriver'

# options = webdriver.ChromeOptions()

# options.add_argument('--user-data-dir=/Users/riccardo/Library/Application Support/Google/Chrome/Default')
# driver = uc.Chrome(options=options)
# driver.minimize_window()

# url = 'https://www.google.com/search?sca_esv=34178eb96b5aeaa8&sxsrf=ACQVn08dLg6F8djUSfbUajZPtOPYVWuGfQ:1709575202979&q=toyota+supra&uds=AMwkrPuObbrOcJIkfdnXPIt8Ep0MzL7ljCkEr_8qygNQsPUFafYahMYCjzuLdbmAp289LZEmIW0X16h0w6kBQO6Du-RNJZL9o2OWJA39nlRemOAQDmrIru8iLqqOqOLpeyU4d5NUOZjO&udm=2&sa=X&sqi=2&ved=2ahUKEwj_wML1l9uEAxW2V6QEHZQHCWwQtKgLegQIDBAB&biw=1887&bih=926&dpr=1'

# driver.get(url)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(5)

# img_result = driver.find_element_by_xpath('//img[contains(@class, "Q4LuWd")]')

# image_urls = []
# for img in img_result:
#     image_urls.append(img.get_attribute('src'))

# folderPath = '/home/riccardo/Visual_Studio_Code/Grain-segmentation_prjt/dataset-full/martensite microstructure/'

# for i in range(20):
#     urllib.request.urlretrieve(str(image_urls[i]), folderPath +" supra_{}.jpg".format(i))

# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import undetected_chromedriver as uc
# import time
# import urllib.request
# import os

# # Chemin vers le répertoire de ChromeDriver et le dossier de sauvegarde
# driver_path = '/home/riccardo/Downloads/chromedriver-linux64/chromedriver'
# folderPath = '/home/riccardo/Visual_Studio_Code/Grain-segmentation_prjt/dataset-full/martensite microstructure/'

# options = webdriver.ChromeOptions()
# # Assurez-vous que le chemin vers le profil utilisateur est correct et accessible
# options.add_argument('--user-data-dir=/Users/riccardo/Library/Application Support/Google/Chrome/Default')

# # Initialiser le WebDriver
# driver = webdriver.Chrome(executable_path=driver_path, options=options)
# driver.minimize_window()

# # URL de la recherche
# url = 'https://www.google.com/search?q=toyota+supra&tbm=isch'

# driver.get(url)
# time.sleep(5)  # Laissez le temps à la page de charger

# # Récupération des URLs des images
# img_elements = driver.find_elements(By.XPATH, '//img[contains(@class, "Q4LuWd")]')
# image_urls = [img.get_attribute('src') for img in img_elements if img.get_attribute('src').startswith('http')]

# # Téléchargement des images
# for i, img_url in enumerate(image_urls[:20]):  # Limite à 20 images pour l'exemple
#     try:
#         path = os.path.join(folderPath, f"toyota_supra_{i}.jpg")
#         urllib.request.urlretrieve(img_url, path)
#         print(f"Image {i} téléchargée : {path}")
#     except Exception as e:
#         print(f"Erreur lors du téléchargement de l'image {i}: {e}")

# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
import time
import urllib.request
import os

# Chemin vers le répertoire de ChromeDriver et le dossier de sauvegarde
driver_path = '/home/riccardo/Downloads/chromedriver-linux64/chromedriver'
folderPath = '/home/riccardo/Visual_Studio_Code/Grain-segmentation_prjt/dataset-full/martensite microstructure/'

options = webdriver.ChromeOptions()
# Assurez-vous que le chemin vers le profil utilisateur est correct et accessible
options.add_argument('--user-data-dir=/home/riccardo/.config/google-chrome/Default')

# Utilisez Service pour spécifier le chemin du WebDriver
service = Service(executable_path=driver_path)

# Initialiser le WebDriver avec le Service
driver = webdriver.Chrome(service=service, options=options)
driver.minimize_window()

# URL de la recherche
url = 'https://www.google.com/search?q=toyota+supra&tbm=isch'

driver.get(url)
time.sleep(10)  # Laissez le temps à la page de charger

# Récupération des URLs des images
img_elements = driver.find_elements(By.XPATH, '//img[contains(@class, "Q4LuWd")]')
image_urls = [img.get_attribute('src') for img in img_elements if img.get_attribute('src') and img.get_attribute('src').startswith('http')]


# Téléchargement des images
for i, img_url in enumerate(image_urls[:20]):  # Limite à 20 images pour l'exemple
    try:
        path = os.path.join(folderPath, f"toyota_supra_{i}.jpg")
        urllib.request.urlretrieve(img_url, path)
        print(f"Image {i} téléchargée : {path}")
    except Exception as e:
        print(f"Erreur lors du téléchargement de l'image {i}: {e}")

driver.quit()
