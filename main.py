import PyPDF2
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def select_paper(in_dir):
    paper_names = []
    for fname in os.listdir(os.path.join(in_dir)):
        if fname.endswith('.pdf'):
            paper_names.append(fname)
    for i, name in enumerate(paper_names):
        print(f'{i}  {name}')
    while c := input('Please enter the index you want.\n'):
        if c.isdigit() and 0 <= int(c) < len(paper_names):
            selected = int(c)
            break
        print('Invalid pdf index.')
    print('Selected: ', paper_names[selected])
    return paper_names[selected].split('.')[0]


def ocr(paper_name, in_dir):
    # Open the PDF file
    pdf_file = open(os.path.join(in_dir, f'{paper_name}.pdf'), 'rb')
    
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    
    # Get the number of pages in the PDF file
    num_pages = pdf_reader.getNumPages()
    
    # Create a text file to write the extracted text
    with open(os.path.join(in_dir, '.tmp', f'{paper_name}.txt'), 'w', encoding='utf-8') as text_file:
        # Loop through all pages and extract text
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()
            # Write the extracted text to the text file
            text_file.write(text)
    
    # Close the PDF file
    pdf_file.close()
    

def open_ai():
    # 创建一个ChromeDriver对象
    driver = webdriver.Chrome()

    # 打开ai.com网页
    driver.get('https://ai.com/')

    try:
        # 等待登录按钮加载完成
        login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[contains(@class, "login-button")]')))

        # 点击登录按钮
        login_button.click()

        # 等待登录框加载完成
        login_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//form[contains(@class, "login-form")]')))

        # 输入用户名和密码
        username_field = login_form.find_element_by_name('username')
        username_field.send_keys('your_username')
        password_field = login_form.find_element_by_name('password')
        password_field.send_keys('your_password')
        password_field.send_keys(Keys.RETURN)

        # 等待登录完成
        success_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "success-message")]')))

        # 输出登录成功消息
        print('成功')
        
    except:
        # 如果登录失败，输出错误消息
        print('登录失败')

    # 关闭ChromeDriver对象
    driver.quit()
    

    
def main():
    # in_dir = 'paper'
    # out_dir = 'summary'
    # paper_name = select_paper(in_dir)
    # ocr(paper_name, in_dir)
    # os.remove(os.path.join(in_dir, '.tmp', f'{paper_name}.txt'))
    
    open_ai()

if __name__ == '__main__':
    main()