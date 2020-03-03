from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class Client:
    def __init__(self, debug=False):
        options = Options()
        if not debug:
            options.headless = True
        options.set_preference("browser.privatebrowsing.autostart", True)
        self.driver = webdriver.Firefox(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, username, password):
        self.driver.get("https://www.fxp.co.il/")
        self.driver.find_element_by_id("navbar_username").send_keys(username)
        self.driver.execute_script(
            f'var element = document.getElementById("navbar_password"); element.value = "{password}";')
        self.driver.find_element_by_class_name("bluelogin").click()

    def create_user(self, nickname, password, logout=False):
        self.driver.get("https://www.fxp.co.il/register.php")
        elem = self.driver.find_element_by_id('regusername')
        elem.send_keys(nickname)
        elem = self.driver.find_element_by_id('password')
        elem.send_keys(password)
        elem = self.driver.find_element_by_id('passwordconfirm')
        elem.send_keys(password)
        elem = self.driver.find_element_by_id('email')
        elem.send_keys(f"{nickname}@gmail.com")
        elem = self.driver.find_element_by_id('cb_rules_agree')
        elem.click()
        elem = self.driver.find_element_by_xpath(
            "//input[@value='השלם הרשמה']")
        elem.click()
        # Once you have created a user, you will remain automatically logged in unless you want to log out.
        if logout:
            self.logout()

    def logout(self):
        self.driver.find_element_by_id('yui-gen1').click()
        self.driver.find_element_by_link_text("התנתקות").click()
        self.driver.get("https://www.fxp.co.il/")

    def change_profile_picture(self, profile_path):
        self.driver.get("https://www.fxp.co.il/")
        self.driver.find_element_by_css_selector(".profileimage").click()
        self.driver.find_element_by_id(
            "uploadfileforumdisplay").send_keys(profile_path)
        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.cropper-view-box')))
        self.driver.find_element_by_css_selector(".save-user-pic").click()

    def is_logged_in(self):
        self.driver.get("https://www.fxp.co.il/")
        return bool(len(self.driver.find_elements_by_class_name("log_in6")))

    def validate_user(self, username):
        self.driver.get(
            "https://www.fxp.co.il/member.php?username=" + str(username))
        return bool(len(self.driver.find_elements_by_class_name("member_username")))

    def like_comments_by_page(self, page_link):
        self.driver.get(page_link)  # You must use full link!
        comments = self.driver.find_elements_by_xpath(
            "//*[@onclick='makelike(this.id);']")
        comments = comments[:10]  # Each bot can only give 10 likes
        for comment in comments:
            comment.click()

    def like_comment(self, comment_id):
        self.driver.get("https://www.fxp.co.il/showthread.php?p=" + str(comment_id))
        x_path = "//*[starts-with(@id, '" + str(comment_id) + "_')]"
        self.driver.find_element_by_xpath(x_path).click()

    def create_thread(self, forum_id, subject, content, tag_text):
        self.driver.get(
            "https://www.fxp.co.il/newthread.php?do=newthread&f=" + str(forum_id))
        select = Select(self.driver.find_element_by_id('prefixfield'))
        select.select_by_visible_text(tag_text)
        elem = self.driver.find_element_by_id('subject')
        elem.send_keys(subject)
        # Enter the text editor
        elem = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="cke_contents_vB_Editor_001_editor"]/iframe')))
        self.driver.switch_to.frame(elem)
        elem = self.driver.find_element_by_tag_name('body')
        elem.send_keys(content)
        self.driver.switch_to.default_content()
        # Outside of the text editor
        elem = self.driver.find_element_by_id('vB_Editor_001_save')
        elem.click()

    def comment(self, thread_link, comment_content):
        self.driver.get(thread_link)
        # Enter the Vb QR editor
        elem = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="cke_contents_vB_Editor_QR_editor"]/iframe')))
        self.driver.switch_to.frame(elem)
        elem = self.driver.find_element_by_tag_name('body')
        elem.send_keys(comment_content)
        self.driver.switch_to.default_content()
        # Outside of the Vb QR editor
        self.driver.find_element_by_id('qr_submit').click()

    def Quit(self):
        self.driver.quit()
