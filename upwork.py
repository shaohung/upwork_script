from selenium import webdriver
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time, random
class glb:
    options = None
    browser = None
    ua = UserAgent()

USERNAME = 'USERNAME HERE'
PASSWORD = 'PASS HERE'
cookies = [{'domain': 'www.upwork.com', 'expiry': 1519894824, 'httpOnly': False, 'name': '_px3', 'path': '/', 'secure': False, 'value': 'f52f9d2eded6f009cbc4108abb528feedf2b11fb2a347b80c6bd89cb46633c35:p/ddxveH7GRP55+1JF6223qMCGPOUv/EkBonrI9oErF2tlzk0cDW2O3anttw0ymen35U0WnKVNuoQAPmAKlf+A==:1000:N/CT7wszeEiFZsU97cCYLgC2/dUI99OxvQ8gEdfAYzziB8WoJhNvFKl2HLiDodtWBFH7PqLcPTMJq1iwNr6RKSoaXFZuKfnoaS6OwyJ+87xXngO8kQZ+K+4j0szzY+vf95WLbBwVTLek+f1WMhgwgLe8zM2m5Ab2ca4f5sfqZEQ='}, {'domain': '.upwork.com', 'expiry': 1551258023.486244, 'httpOnly': True, 'name': '__cfduid', 'path': '/', 'secure': False, 'value': 'df8b46e1a9299baa3d5e408ea148403ae1519722023'}, {'domain': '.upwork.com', 'expiry': 1522141223.977546, 'httpOnly': False, 'name': 'current_organization_uid', 'path': '/', 'secure': False, 'value': '968287179988762624'}, {'domain': '.upwork.com', 'expiry': 1522314024.5683, 'httpOnly': True, 'name': 'company_id', 'path': '/', 'secure': True, 'value': 'uhct65n81fy6igdehjmhnq'}, {'domain': '.upwork.com', 'expiry': 1551258023.977748, 'httpOnly': False, 'name': 'qt_visitor_id', 'path': '/', 'secure': False, 'value': '107.0.114.22.1519691480971806'}, {'domain': '.upwork.com', 'httpOnly': False, 'name': 'oauth2_global_js_token', 'path': '/', 'secure': True, 'value': 'oauth2v1_d674de497441a499108c6b797ca53585'}, {'domain': '.upwork.com', 'httpOnly': True, 'name': 'session_id', 'path': '/', 'secure': True, 'value': '4c98b0ce1cebb8f4ce4b5bf36272cb11'}, {'domain': '.upwork.com', 'expiry': 1551257871.966306, 'httpOnly': False, 'name': '_vhipo', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.upwork.com', 'expiry': 1519808424, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1178448534.1519721885'}, {'domain': '.upwork.com', 'expiry': 1896163200, 'httpOnly': False, 'name': '__ssid', 'path': '/', 'secure': False, 'value': 'dc7e2a2b-ecaf-442b-827d-62a82b495040'}, {'domain': '.upwork.com', 'expiry': 1529722022.21913, 'httpOnly': False, 'name': 'recognized', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.upwork.com', 'expiry': 1551258006.026728, 'httpOnly': False, 'name': 'sp', 'path': '/', 'secure': False, 'value': 'b48f2ebe-2ecd-4f5c-8c43-03cbccdf218e'}, {'domain': 'www.upwork.com', 'expiry': 1677488294, 'httpOnly': False, 'name': 'ki_r', 'path': '/', 'secure': False, 'value': ''}, {'domain': 'www.upwork.com', 'expiry': 1677488294, 'httpOnly': False, 'name': 'ki_t', 'path': '/', 'secure': False, 'value': '1519721894245%3B1519721894245%3B1519721894245%3B1%3B1'}, {'domain': '.upwork.com', 'expiry': 1519808292, 'httpOnly': False, 'name': '__troSYNC', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'www.upwork.com', 'expiry': 1677401893, 'httpOnly': False, 'name': 'sliguid', 'path': '/', 'secure': False, 'value': 'ba6f4fc6-fa72-4412-98c6-2727a0949395'}, {'domain': '.upwork.com', 'expiry': 1553846291, 'httpOnly': False, 'name': '__troRUID', 'path': '/', 'secure': False, 'value': 'bb2ad287-c3da-4bc9-bcdc-9e0633a147da'}, {'domain': '.upwork.com', 'expiry': 1522314024.568183, 'httpOnly': True, 'name': 'company_last_accessed', 'path': '/', 'secure': True, 'value': '4889213'}, {'domain': '.upwork.com', 'httpOnly': True, 'name': 'master_access_token', 'path': '/', 'secure': True, 'value': '2871a158.oauth2v1_83bbd2afcadd7ad5fef3b83c9b8e8ab8'}, {'domain': 'www.upwork.com', 'expiry': 1835081884, 'httpOnly': False, 'name': '_pxvid', 'path': '/', 'secure': False, 'value': '52794ed0-1b9c-11e8-9823-cb874f3752d9'}, {'domain': '.upwork.com', 'httpOnly': False, 'name': 'XSRF-TOKEN', 'path': '/', 'secure': False, 'value': 'e6150c4b75516d482c6cf998855203ad'}, {'domain': '.upwork.com', 'expiry': 1522141071.966239, 'httpOnly': True, 'name': 'device_view', 'path': '/', 'secure': False, 'value': 'full'}, {'domain': 'www.upwork.com', 'expiry': 1677401893, 'httpOnly': False, 'name': 'slirequested', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.upwork.com', 'expiry': 4673321891, 'httpOnly': False, 'name': '_br_uid_2', 'path': '/', 'secure': False, 'value': 'uid%3D7895844212845%3Av%3D11.8%3Ats%3D1519721891247%3Ahc%3D1'}, {'domain': '.upwork.com', 'expiry': 1582794024, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.541145958.1519721885'}, {'domain': '.upwork.com', 'expiry': 1551258022.219261, 'httpOnly': True, 'name': 'console_user', 'path': '/', 'secure': True, 'value': 'ca269fbe'}, {'domain': '.upwork.com', 'expiry': 1551258023.977443, 'httpOnly': False, 'name': 'visitor_id', 'path': '/', 'secure': False, 'value': '107.0.114.22.1519722005911749'}, {'domain': '.upwork.com', 'expiry': 1553846291, 'httpOnly': False, 'name': '__trossion', 'path': '/', 'secure': False, 'value': '1519721891_1800_1__bb2ad287-c3da-4bc9-bcdc-9e0633a147da%3A1519721891_1519721891_1'}, {'domain': '.upwork.com', 'expiry': 1835082024, 'httpOnly': False, 'name': 'optimizelyEndUserId', 'path': '/', 'secure': False, 'value': 'oeu1519721879008r0.550293804262779'}, {'domain': 'www.upwork.com', 'httpOnly': False, 'name': 'trctestcookie', 'path': '/', 'secure': False, 'value': 'ok'}]
def open_browser():
    options = webdriver.ChromeOptions()
    #options.add_argument('user-agent=' + 'wow')
    #options.add_argument('headless')
    glb.browser = webdriver.Chrome(chrome_options=options)

def login(cookies):
    glb.browser.get('https://www.upwork.com/')
    for c in cookies:
        glb.browser.add_cookie(c)
    #glb.browser.get('https://www.upwork.com/ab/account-security/login') # login
    time.sleep(random.randrange(1,4))
    #glb.browser.find_element_by_id('login_username').click()
    #glb.browser.find_element_by_id('login_username').send_keys(USERNAME)
    #time.sleep(5)
    #glb.browser.find_elements_by_css_selector('button.btn-primary')[1].click() # continue button
    #glb.browser.find_element_by_id('login_password').click()
    #glb.browser.find_element_by_id('login_password').send_keys(PASSWORD)
    #glb.browser.find_elements_by_css_selector('button.btn-primary')[3].click() # log in button
    #time.sleep(5)

def page(num):
    return 'https://www.upwork.com/ab/profiles/search/?pt=independent&loc=central-america,south-america&page='+str(num)+'&user_pref=1'

open_browser()
login(cookies)

f = open('upwork.csv', 'a')
#f.write('"Name","Country","HourlyRate","Skills"\n')
#glb.browser.get(page(36))
random.seed()
for i in range(47,57):
    glb.browser.get(page(i))
    time.sleep(random.randrange(1,4))
    for i in range(10):
        freelancers = glb.browser.find_elements_by_class_name('air-card-hover')
        freelancers[i].click()
        time.sleep(random.randrange(1,4))
        try:
            soup = BeautifulSoup(glb.browser.page_source, "html.parser")
            name = soup.find(attrs={'itemprop':'name'}).string.strip('\n')
            country = soup.find(attrs={'itemprop':'country-name'}).string.strip('\n')
            rate = soup.find(attrs={'itemprop':'pricerange'}).string.strip('\n')
            skills = []
            skill_iter = soup.find_all(attrs={'class':'o-tag-skill o-tag-certified'})
            for skill in skill_iter:
                skills.append(skill.text.strip('\n'))
            skill_set = ','.join(skills)
            glb.browser.find_element_by_class_name('close-overlay-button').click()
            f.write('%s,%s,%s,%s\n' % (name, country, rate, skill_set))
            time.sleep(random.randrange(1,4))
            print('done')
        except:
            glb.browser.find_element_by_class_name('close-overlay-button').click()
            print('error')
            pass

