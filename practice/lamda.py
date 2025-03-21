import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Set up Firefox WebDriver (Fixed settings)
firefox_options = Options()
firefox_options.add_argument("--headless")  # Optional: run without UI
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-dev-shm-usage")
firefox_options.add_argument("--disable-gpu")

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=firefox_options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
input("Press Enter after scanning QR code...")

# Function to open a group chat
def open_group(group_name):
    search_box = driver.find_element(By.XPATH, "//div[@title='Search input textbox']")
    search_box.click()
    search_box.clear()
    search_box.send_keys(group_name)
    time.sleep(2)
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)

# Function to extract group members
def extract_members(group_name):
    members_list = []
    
    # Open Group Info
    driver.find_element(By.XPATH, "//span[@data-icon='menu']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[text()='Group info']").click()
    time.sleep(3)

    members = driver.find_elements(By.XPATH, "//div[contains(@class, 'selectable-text')]")

    for member in members:
        try:
            name = member.text
            phone_number = name if name.startswith("+") else "Unknown"
            members_list.append({"Group Name": group_name, "Name": name, "Phone Number": phone_number})
        except Exception as e:
            print("Error:", e)

    # Close group info panel
    driver.find_element(By.XPATH, "//div[@role='button'][@title='Back']").click()
    time.sleep(2)

    return members_list

# Main Execution
group_names = input("Enter WhatsApp Group Names (comma-separated): ").split(",")
all_members_data = []

for group in group_names:
    group = group.strip()
    open_group(group)
    time.sleep(3)
    members_data = extract_members(group)
    all_members_data.extend(members_data)

# Save to CSV
df = pd.DataFrame(all_members_data)
df.to_csv("whatsapp_multiple_groups.csv", index=False)
print("Data saved successfully in whatsapp_multiple_groups.csv")

# Close the driver
driver.quit()
