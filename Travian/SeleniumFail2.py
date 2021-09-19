# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

################
# import org.openqa.selenium.By;
# import org.openqa.selenium.WebDriver;
# import org.openqa.selenium.WebElement;
# import org.openqa.selenium.chrome.ChromeDriver;
# import org.testng.Assert;
# import org.testng.annotations.Test;
# public class LoginAutomation {
#     @Test
#     public void login() {
#         System.setProperty("webdriver.chrome.driver", "C:\Users\USER\AppData\Local\Programs\Python\Python39");
#         WebDriver driver=new ChromeDriver();
#         driver.manage().window().maximize();
#         driver.get("https://www.browserstack.com/users/sign_in");
#         WebElement username=driver.findElement(By.id("user_email_Login"));
#         WebElement password=driver.findElement(By.id("user_password"));
#         WebElement login=driver.findElement(By.name("commit"));
#         username.sendKeys("abc@gmail.com");
#         password.sendKeys("your_password");
#         login.click();
#         String actualUrl="https://live.browserstack.com/dashboard";
#         String expectedUrl= driver.getCurrentUrl();
#         Assert.assertEquals(expectedUrl,actualUrl);
#     }
# }

################
# #Simple assignment
# from selenium.webdriver import Chrome

# driver = Chrome()

# #Or use the context manager
# from selenium.webdriver import Chrome

# with Chrome() as driver:
#     #your code inside this indent
#     Chrome(executable_path='C:\Users\USER\AppData\Local\Programs\Python\Python39\usr\bin')


################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()