from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
desired_cap = {
    "deviceName": "4200b6c361b8c3eb",
    "platformName": "Android",
    "appPackage": "com.loginmodule.learning",
    "appWatchActivity": "com.loginmodule.learning.activities.LoginActivity",
    "app": "E:\\Selenium\\sample_android.apk"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

#klik belum punya akun
driver.find_element_by_id("com.loginmodule.learning:id/textViewLinkRegister").click()

#mengisi form
driver.find_element_by_id("com.loginmodule.learning:id/textInputEditTextName").send_keys("Bagus Muhammad Iqbal")
driver.find_element_by_id("com.loginmodule.learning:id/textInputEditTextEmail").send_keys("iqbal@gmail.com")
driver.find_element_by_id("com.loginmodule.learning:id/textInputEditTextPassword").send_keys("samsung12@")
driver.find_element_by_id("com.loginmodule.learning:id/textInputEditTextConfirmPassword").send_keys("samsung12@")

#untuk Scroll kebawah
driver.swipe(150, 400, 150, 200, 1000)

driver.find_element_by_id("com.loginmodule.learning:id/appCompatButtonRegister").click()
