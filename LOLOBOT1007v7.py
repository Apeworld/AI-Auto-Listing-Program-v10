from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import filedialog, Text, StringVar, IntVar
from tkinter import filedialog, Listbox, Scrollbar, ttk
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from requests import ReadTimeout
from tkinter import messagebox
from selenium import webdriver
from time import sleep
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import tkinter as tk
import requests
import time
import pyperclip
import random
import openai
import sys
import textwrap
import os
import subprocess



root = tk.Tk()
root.title(" ILOLO 네이버 해외직구 상품등록 프로그램 V23.10.07.v7 : 등록 폴더 전용")


# Set variables
templit = StringVar()
category_2 = StringVar()
title = StringVar()
price = IntVar()
color_a = IntVar()
color = StringVar()
sku = StringVar()
brand = StringVar()
model_tip = StringVar()
fabric = StringVar()
sizet = StringVar()
made = StringVar()
info = StringVar()

ori = StringVar()
new_price = StringVar()

def find_max_folder_number():
    folder_path = 'C:/Users/ape0x/Desktop/상품등록봇/등록'
    time.sleep(random.uniform(0.5, 1))

    folders = []
    for folder in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, folder)):
            try:
                prefix, folder_number_str = folder[0], folder[1:]
                folder_number = int(folder_number_str)
                if prefix == 'a':
                    folders.append(folder_number)
            except ValueError:
                pass

    max_folder_num = max(folders)
    return max_folder_num

def save_values():
    values = [
        templit.get(),
        title.get(),
        price.get(),
        sku.get(),
        color.get(),
        color_a.get(),
        category_2.get(),
        brand.get(),
        model_tip.get(),
        fabric.get(),
        sizet.get(),
        made.get(),
        ori.get(),
        info.get(),
        new_price.get(),
    ]
    selected_folders = folders_listbox.curselection()
    if selected_folders:
        folder_numbers = [int(folders_listbox.get(folder)[1:]) for folder in selected_folders]
    else:
        progress_text.insert(tk.END, "폴더를 선택해주세요.\n")
        return

    save_directories = [f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{folder_number}' for folder_number in folder_numbers]
    save_file_name = "a.txt"

    for save_directory in save_directories:
        save_path = os.path.join(save_directory, save_file_name)
        with open(save_path, 'w', encoding='utf-8') as file:
            for value in values:
                file.write(f"{value}\n")

        progress_text.insert(tk.END, f"상품 정보를 저장했습니다. {save_path}\n")
    
    

templit_options = [
    "멘즈샵 신발",
    "멘즈샵 의류",
    "멘즈샵 잡화",
    "",
    "기본 신발",
    "기본 의류",
    "기본 잡화",
    "---------------",
    "멘즈 NEW 신발",
    "멘즈 NEW 의류",
    "멘즈 NEW 잡화",
    "",
    "기본 NEW 신발",
    "기본 NEW 의류",
    "기본 NEW 잡화",
    
]

model_tip_options = [
    "US9 착용시 편안하게 잘 맞았습니다.",
    "US8.5 착용시 편안하게 딱 맞았습니다.",
    "S 사이즈 착용시 딱 맞게 예쁜핏으로 맞았습니다.",
    "31 사이즈 착용시 딱 잘 맞았습니다.",
    "32 사이즈 착용시 엉덩이에 걸쳐지는 핏으로 맞았습니다.",
    "M 사이즈 착용시 딱 예쁘게 잘 맞았습니다",
    "M 사이즈 착용시 예쁜핏으로 잘 맞았습니다.",
    "M 사이즈 착용시 여유있는 핏으로 맞았습니다.",
    "L 사이즈 착용시 루즈하게 맞았습니다.",
    "",
    "US9 착용했으며 잘 맞았습니다.",
    "US8.5 착용했으며 딱 맞았습니다.",
    "S 사이즈 착용했으며 딱 맞게 예쁜핏으로 맞았습니다.",
    "M 사이즈 착용했으며 딱 예쁘게 잘 맞았습니다.",
    "31 사이즈 착용했으며 딱 잘 맞았습니다.",
    "32 사이즈 착용했으며 엉덩이에 걸쳐지는 핏으로 맞았습니다.",
    "M 사이즈 착용했으며 예쁜핏으로 잘 맞았습니다.",
    "M 사이즈 착용했으며 여유있는 핏으로 맞았습니다.",
    "L 사이즈 착용했으며 루즈하게 맞았습니다.",
    "---------------------------------------------------",
    "US7 착용시 편안하게 잘 맞았습니다.",
    "26 사이즈 착용시 편안하게 잘 맞았습니다.",
    "S 사이즈 착용시 예쁜핏으로 잘 맞았습니다.",
    "M 사이즈 착용시 루즈하게 맞았습니다",
    "",
    "US7 착용했으며 편안하게 잘 맞았습니다.",
    "XS 사이즈 착용했으며 예쁜핏으로 잘 맞았습니다.",
    "S 사이즈 착용했으며 예쁜핏으로 잘 맞았습니다.",
    "",
    "0 사이즈 착용했으며 편안하게 잘 맞았습니다.",
    "26 사이즈 착용했으며 편안하게 잘 맞았습니다.",
    "",
    "M 사이즈 착용했으며 루즈하게 맞았습니다",
    "S 사이즈 착용했으며 루즈하게 맞았습니다",
    "---------------------------------------------------",
    "누구나 활용하기 좋은 사이즈로 편안하게 잘 맞았습니다.",
    "공용 사이즈로 예쁜 핏으로 잘 맞았습니다.",
    "사이즈 감이 데일리로 활용하기 좋았습니다.",
]

category_2_options = [
    "워킹화",
    "스니커즈",
    "슬리퍼",
    "샌들",
    "슬립온",
    "로퍼",
    "뮬",
    "하이힐",
    "웨지힐",
    "펌프스",
    "부츠",
    "",
    "재킷",
    "점퍼",
    "카디건",
    "코트",
    "티셔츠",
    "니트",
    "셔츠",
    "블라우스",
    "원피스",
    "스커트",
    "청바지",
    "바지",
    "팬티",
    "브라",
    "홈웨어",
    "",
    "스포츠양말",
    "장갑",
    "",
    "야구모자 일반캡",
    "야구모자 메시캡",
    "스냅백 일반캡",
    "스냅백 메시캡",
    "비니",
    "페도라",
    "헌팅캡",
    "사파리모자",
    "",
    "선글라스",
    "메탈시계",
    "가죽시계",
    "우레탄시계",
    "",
    "반지갑",
    "중지갑",
    "장지갑",
    "동전지갑",
    "머니클립",
    "카드지갑",
    "지갑세트",
    "열쇠지갑",
    "",
    "토트백",
    "숄더백",
    "크로스백",
    "힙색",
    "클러치",
    "백팩",
    "키홀더",
    "",
    "귀걸이",
    "주얼리케이스",
    "팔찌",
    "반지",
    "발찌",
    "목걸이",
    "헤어핀",
]

made_options = [
  "China",
  "China 외",
  "",
  "Vietnam",
  "Vietnam 외",
  "",
  "Indonesia",
  "India",
  "",
  "Bangladesh",
  "U.S.A.",
  "Canada",
  "Turkey",
  "ITALY",
  "",
  "Pakistan",
  "Sri Lanka",
  "",
  "Jordan",
  "Thailand",
  "Guatemala",
  "",
  "Egypt",
  "Taiwan",
  "",
  "Nicaragua",
  "Mexico",
  "",
  "Myanmar",
  "Nicaragua",
  "Malaysia",
  "",
  "Cambodia",
  "Phillipines",
  "Honduras",
  ]

brand_options = [
  "나이키",
  "아디다스",
  "바나나리퍼블릭",
  "DKNY",
  "리바이스",
  "아식스",
  "캘빈클라인",
  "노스페이스",
  "",
  "팩선",
  "크록스",
  "얼반아웃피터스",
  "뉴발란스",
  "반스",
  "아이엔씨인터내셔날컨셉스",
  "유니클로",
  "",
  "오베이",
  "스케처스",
  "칼라거펠드",
  "타미힐피거",
  "코튼온",
  "마이클코어스",
  "아메리칸이글",
  "앤드나우디스",
  "",
  "게스",
  "BDG",
  "47브랜드",
  "RSQ",
  "허프",
  "포에버21",
  "LOVISA",
  "랙앤본",
  "존갈트",
  "컨버스",
  "칼하트",
  "파타고니아",
  "매든걸",
  "",
  "뉴에라",
  "MLB",
  "지샥",
  "틸리스",
  "어그",
  "로렌 랄프로렌",
  "폴로 랄프로렌",
  "",
  "지방시",
  "발렌시아가",
  "알렉산더맥퀸",
  "프라다",
  "돌체앤가바나",
  "마르니",
  "페레가모",
  "몽클레어",
]

fabric_options = [
  "Cotton",
  "Cotton 외",
  "",
  "Polyester",
  "Polyester 외",
  "",
  "Cotton / Polyester",
  "Cotton / Polyester 외",
  "---------------",
  "Nylon",
  "Nylon 외",
  "Acrylic",
  "Acrylic 외",
  "",
  "Cotton / Spandex",
  "Cotton / Polyester / Spandex / Nylon",
  "",
  "Wool",
  "Cotton / Wool",
  "Wool 외",
  "Modal 외",
  "---------------",
  "Calf Leather",
  "",
  "Polyurethane",
  "PU",
  "PU 외",
  "Faux Leather",
  "---------------",
  "Leather Upper 외",
  "Mesh Upper 외",
  "Synthetic Upper 외",
  "",
  "Textile Upper 외",
  "Canvas Upper 외",
  "Suede Upper 외",
  "",
  "Rubber Sole 외",
  "---------------",
  "Set in gold-tone mixed metal",
  "Set in silver-tone mixed metal",
  "Set in Rose gold-tone mixed metal",
  "925 Silver",
  "Sterling Silver, Gold Plated",
]

sizet_options = [
  "ONE SIZE",
  "FREE",
  "---------------",
  "남성 공용 사이즈",
  "",
  "여성 공용 사이즈",
  "",
  "남녀 공용 사이즈",
  "---------------",
  "XS/S , M/L , L/XL 세가지 사이즈로 나오는 제품입니다.",
  "",
  "평균적으로 44-XS, 55-S, 66-M, 77-L 정도로 착용하시면 만족도가 가장 높습니다. 다만 개인마다 체형 및 핏이 다르므로 참고 부탁드립니다.",
  "",
  "평균적으로 95-S 100-M 105-L 110-XL 정도로 주문하시면 만족도가 가장 높습니다. 다만 개인마다 체형 및 핏이 다르므로 참고 부탁드립니다.",
]

ori_options = [
  "팩선",
  "틸리스",
  "자라",
  "주메즈",
  "H&M",
  "피니쉬라인",
  "슈팔라스",
  "절니",
  "바나나리퍼블릭",
  "풋락커",
  "AX",
  "얼반아웃피터스",
  "메이시",
  "랙룸",
  "아메리칸이글",
  "게스",
  "메이시",
  "놀스트롬",
  "딕스스포츠",
  "포에버21",
  "히벳",
  "유니클로",
  "LOVISA",
  "------------------------",
  "ORANGE OUTLET 오렌지",
  "",
  "O 반스",
  "O 나이키",
  "O 아디다스",
  "O SAK5FF",
  "O 니먼",
  "O DKNY",
  "O 주메즈",
  "O 슈팔라스",
  "O 피니쉬",
  "O 팩선",
  "O 틸리스",
  "O H&M",
  "O 랙룸",
  "O 캘빈 언더",
  "O 바나나리퍼블릭",
  "O 리바이스",
  "O 캘빈 언더",
  "O 캘빈클라인",
  "O 타미힐피거",
  "O 게스",
  "O 아메리칸이글",
  "O 컨버스",
  "O 포에버21",
  "O LOVISA",
  "------------------------",
  "CITADEL OUTLET 시타델",
  "",
  "C 반스",
  "C 나이키",
  "C 아디다스",
  "C 뉴발란스",
  "C 슈퍼드라이",
  "C DKNY",
  "C 틸리스",
  "C CK",
  "C 바나나리퍼블릭",
  "C 코치",
  "C 아메리칸이글",
  "C AX",
  "C 리바이스",
]

color_a_options = [
    "1 레드",
    "2 버건디",
    "3 오렌지",
    "4 골드",
    "5 옐로우",
    "",
    "6 라임",
    "7 그린",
    "8 올리브",
    "9 민트",
    "10 스카이",
    "",
    "11 블루",
    "12 네이비",
    "13 퍼플",
    "14 바이올렛",
    "15 핑크",
    "",
    "16 퓨샤",
    "17 베이지",
    "18 카멜",
    "19 브라운",
    "20 화이트",
    "",
    "21 아이보리",
    "22 라이트 그레이",
    "23 그레이",
    "24 차콜",
    "25 블랙",
    "",
    "26 클리어",
    "27 멀티",
]


def color_a_update_template(value):
    if value == "1 레드":
        color_a.set(1)
    elif value == "2 버건디":
        color_a.set(2)
    elif value == "3 오렌지":
        color_a.set(3)
    elif value == "4 골드":
        color_a.set(4)
    elif value == "5 옐로우":
        color_a.set(5)
    elif value == "6 라임":
        color_a.set(6)
    elif value == "7 그린":
        color_a.set(7)
    elif value == "8 올리브":
        color_a.set(8)
    elif value == "9 민트":
        color_a.set(9)
    elif value == "10 스카이":
        color_a.set(10)
    elif value == "11 블루":
        color_a.set(11)
    elif value == "12 네이비":
        color_a.set(12)
    elif value == "13 퍼플":
        color_a.set(13)
    elif value == "14 바이올렛":
        color_a.set(14)
    elif value == "15 핑크":
        color_a.set(15)
    elif value == "16 퓨샤":
        color_a.set(16)
    elif value == "17 베이지":
        color_a.set(17)
    elif value == "18 카멜":
        color_a.set(18)
    elif value == "19 브라운":
        color_a.set(19)
    elif value == "20 화이트":
        color_a.set(20)
    elif value == "21 아이보리":
        color_a.set(21)
    elif value == "22 라이트 그레이":
        color_a.set(22)
    elif value == "23 그레이":
        color_a.set(23)
    elif value == "24 차콜":
        color_a.set(24)
    elif value == "25 블랙":
        color_a.set(25)
    elif value == "26 클리어":
        color_a.set(26)
    elif value == "27 멀티":
        color_a.set(27)


# Set variable
templit = tk.StringVar()
templit.set("")

model_tip = tk.StringVar()
model_tip.set("")

category_2 = tk.StringVar()
category_2.set("")

made = tk.StringVar()
made.set("")

brand = tk.StringVar()
brand.set("")

fabric = tk.StringVar()
fabric.set("")

sizet = tk.StringVar()
sizet.set("")

ori = tk.StringVar()
ori.set("")

color_a = tk.IntVar()
color_a.set(0)

# Create label and dropdown menu
tk.Label(root, text="템플릿").grid(row=0, column=0, sticky='E')
template_dropdown = tk.OptionMenu(root, templit, *templit_options)
template_dropdown.grid(row=0, column=1)

# Create label and dropdown menu
tk.Label(root).grid(row=1, column=5, sticky='E')
color_a_dropdown = tk.OptionMenu(root, color_a, *color_a_options, command=color_a_update_template)
color_a_dropdown.grid(row=5, column=2)

# Create label and dropdown menu
tk.Label(root).grid(row=1, column=6, sticky='E')
category_2_tip_dropdown = tk.OptionMenu(root, category_2, *category_2_options)
category_2_tip_dropdown.grid(row=6, column=2)

# Create label and dropdown menu
tk.Label(root).grid(row=8, column=1, sticky='E')
model_tip_dropdown = tk.OptionMenu(root, model_tip, *model_tip_options)
model_tip_dropdown.grid(row=8, column=2)

# Create label and dropdown menu
tk.Label(root).grid(row=11, column=1, sticky='E')
made_dropdown = tk.OptionMenu(root, made, *made_options)
made_dropdown.grid(row=11, column=2)

# Create label and dropdown menu
tk.Label(root).grid(row=7, column=1, sticky='E')
brand_dropdown = tk.OptionMenu(root, brand, *brand_options)
brand_dropdown.grid(row=7, column=2)

# Create label and dropdown menu
tk.Label(root).grid(row=9, column=1, sticky='E')
fabric_dropdown = tk.OptionMenu(root, fabric, *fabric_options)
fabric_dropdown.grid(row=9, column=2)

# Create label and dropdown menu
tk.Label(root).grid(row=10, column=1, sticky='E')
sizet_dropdown = tk.OptionMenu(root, sizet, *sizet_options)
sizet_dropdown.grid(row=10, column=2)


tk.Label(root).grid(row=12, column=1, sticky='E')
ori_dropdown = tk.OptionMenu(root, ori, *ori_options)
ori_dropdown.grid(row=12, column=2)

def start_product_registration():
    
# Configure Chrome options
    chrome_options = Options()

    # Add experimental option to allow clipboard access
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.clipboard": 1
    })

    # Set up ChromeDriver with options
    #driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

    driver_path = r"C:\Users\ape0x\Desktop\상품등록봇\chromedriver.exe"

    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

    # Navigate to a website using the proxy server
    driver.get("https://sell.smartstore.naver.com/")

    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(3)

    driver.set_window_size(1280, 1440)
    
    openai.api_key = "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"

    folder_path = 'C:/Users/ape0x/Desktop/상품등록봇/등록'
    time.sleep(random.uniform(0.5, 2.0))

    folders = []
    for folder in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, folder)):
            try:
                prefix, folder_number_str = folder[0], folder[1:]
                folder_number = int(folder_number_str)
                if prefix == 'a':
                    folders.append(folder_number)
            except ValueError:
                pass  # 폴더 이름이 'a'로 시작하지 않거나 숫자로만 구성되어 있지 않은 경우 무시합니다.

    # Find the maximum folder number
    max_folder_num = max(folders)
    print(f"작업 할 상품을 {max_folder_num}개 찾았습니다.")

    elem = driver.find_element(By.XPATH, '/html/body/ui-view[1]/div[2]/div[2]/div/div[1]/div[2]/button[1]')
    elem.click()
    time.sleep(random.uniform(0.5, 2.0))
    elem_1 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div[4]/div[1]/ul/li[2]/button')
    time.sleep(random.uniform(0.5, 2.0))
    elem_1.click()
    print('로그인 시도중..')
    time.sleep(random.uniform(2.0, 3.0))
    driver.switch_to.window(driver.window_handles[1])

    id_value = entry_id.get()
    pw_value = entry_pw.get()
    #######################################################
    #id_value = '' 아이디와 패스워드 넣는게 귀찮으시면
    #pw_value = '' 여기에 아이디와 패스워드를 입력하면 됩니다.
    #######################################################

    pyperclip.copy(id_value)
    time.sleep(random.uniform(0.5, 1.0))
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[2]/div[1]/input')))
    elem_id = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[2]/div[1]/input')
    elem_id.click()
    time.sleep(random.uniform(0.5, 1.0))
    elem_id.send_keys(Keys.CONTROL, "v")
    elem_pw = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[2]/div[2]/input')
    pyperclip.copy(pw_value)
    elem_pw.click()
    time.sleep(random.uniform(0.5, 1.0))
    elem_pw.send_keys(Keys.CONTROL, "v")
    time.sleep(random.uniform(0.5, 1.0))
    driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
    time.sleep(random.uniform(0.5, 1.0))
  
    try:
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="new.save"]')))
        # 요소를 찾았으므로 작업을 수행합니다.
        element.click()
    except :
        pass

    print('로그인 성공!!')
    
    ###작업
    driver.switch_to.window(driver.window_handles[0])

    time.sleep(7)
    
    try:
        popup_button11 = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.modal.fade.seller-layer-modal.has-close-check-box.data-target-complete-window.in > div > div > div.modal-footer > div.seller-btn-area > button')))
        print('등급 팝업을 찾았어요!')
        popup_button11.click()
        print('팝업 EXIT')
        time.sleep(2)
    except (NoSuchElementException, TimeoutException):
        print('등급 팝업이 없습니다.')
        pass

    try:
        popup_button2 = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.modal.fade.seller-layer-modal.modal-no-space.modal-transparent.in > div > div > div.modal-header.bg-primary > button')))
        print('팝업을 찾았어요!')
        popup_button2.click()
        print('팝업 EXIT')
        time.sleep(2)
    except (NoSuchElementException, TimeoutException):
        print('팝업이 없습니다.')
        pass

    try:
        pop_up1 = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="seller-content"]/div/div/div/div[1]/ncp-manager-notice-view/ng-transclude/button')))
        print('공지사항 팝업을 찾았어요')
        
        pop_up2 = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.modal.fade.seller-layer-modal.in > div > div > div.modal-header.bg-primary > button')))
        print('? 팝업을 찾았어요')    
        pop_up2.click()
           
        pop_up1.click()
        print('공지사항 팝업을 닫았어요')     
    except (NoSuchElementException, TimeoutException):
        print('공지사항 팝없이 없습니다.')
        pass
    

    
    
    product_menu = driver.find_element(By.XPATH, '//*[@id="seller-lnb"]/div/div[1]/ul/li[1]/a')
    product_menu.click()
    time.sleep(random.uniform(0.5, 2.0))
    
    product_list = driver.find_element(By.XPATH, '//*[@id="seller-lnb"]/div/div[1]/ul/li[1]/ul/li[1]/a')
    product_list.click()
    time.sleep(random.uniform(4, 5))
    product_list_pop = driver.find_element(By.XPATH, '//*[@id="seller-content"]/div/div/div/div[1]/ncp-manager-notice-view/ng-transclude/button')
    product_list_pop.click()
    time.sleep(random.uniform(0.5, 2.0))

    # Modify the range function to go up to the maximum folder number
    for i in range(1, max_folder_num + 1):
        # Your existing code to process each folder
        print(f'{i}번 상품 작업을 시작합니다.')

        with open(f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            templit = lines[0].strip()
            title = lines[1].strip()
            price = int(lines[2].strip())
            sku = lines[3].strip()
            color = lines[4].strip()
            color_a = int(lines[5].strip())
            category_2 = lines[6].strip()
            brand = lines[7].strip()
            model_tip = lines[8].strip()
            fabric = lines[9].strip()
            sizet = lines[10].strip()
            made = lines[11].strip()
            ori = lines[12].strip()
            info = lines[13].strip()
            new_price = lines[14].strip()

        print("Template:", templit)
        print("Category:", category_2)
        print("Title:", title)
        print("Price:", price)
        print("Color:", color)
        print("SKU:", sku)
        print("Brand:", brand)
        print("Origin:", made)



#템플릿 구분
        if templit == '멘즈샵 신발':
            print('템플릿 코드 01 >> 남성 신발')
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div/ui-view[1]/div[2]/form/div[2]/div/button[2]').click()
            time.sleep(1)
            template_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#prd_name')))
            time.sleep(1)
            template_name_input.send_keys('멘즈샵 - 신발 템플릿')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/ui-view[1]/div[2]/form/div[1]/div/ul/li[6]/div/div/ncp-datetime-range-picker2/div[1]/div/div/button[7]').click()
            time.sleep(1)
            save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(1)')))
            time.sleep(1)
            save_button.click()
            time.sleep(1)
            temp_copy = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div:nth-child(1) > div > div:nth-child(3)')))
            time.sleep(1)
            temp_copy.click()
        elif templit == '기본 신발':
            print('템플릿 코드 02 >> 여성 신발')
            driver.find_element(By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(2)').click()
            time.sleep(1)
            template_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#prd_name')))
            time.sleep(1)
            template_name_input.send_keys('기본 - 신발 템플릿')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/ui-view[1]/div[2]/form/div[1]/div/ul/li[6]/div/div/ncp-datetime-range-picker2/div[1]/div/div/button[7]').click()
            time.sleep(1)
            save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(1)')))
            time.sleep(1)
            save_button.click()
            time.sleep(1)
            temp_copy = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div:nth-child(1) > div > div:nth-child(3)')))
            time.sleep(1)
            temp_copy.click()
        elif templit == '멘즈샵 의류':
            print('템플릿 코드 03 >> 남성 의류')
            driver.find_element(By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(2)').click()
            time.sleep(1)
            template_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#prd_name')))
            time.sleep(1)
            template_name_input.send_keys('멘즈샵 - 의류 템플릿')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/ui-view[1]/div[2]/form/div[1]/div/ul/li[6]/div/div/ncp-datetime-range-picker2/div[1]/div/div/button[7]').click()
            time.sleep(1)
            save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(1)')))
            time.sleep(1)
            save_button.click()
            time.sleep(1)
            temp_copy = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div:nth-child(1) > div > div:nth-child(3)')))
            time.sleep(1)
            temp_copy.click()
        elif templit == '기본 의류':
            print('템플릿 코드 04 >> 여성 의류')
            driver.find_element(By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(2)').click()
            time.sleep(1)
            template_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#prd_name')))
            time.sleep(1)
            template_name_input.send_keys('기본 - 의류 템플릿')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/ui-view[1]/div[2]/form/div[1]/div/ul/li[6]/div/div/ncp-datetime-range-picker2/div[1]/div/div/button[7]').click()
            time.sleep(1)
            save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(1)')))
            time.sleep(1)
            save_button.click()
            time.sleep(1)
            temp_copy = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div:nth-child(1) > div > div:nth-child(3)')))
            time.sleep(1)
            temp_copy.click()   
        elif templit == '멘즈샵 잡화':
            print('템플릿 코드 05 >> 남성 잡화')
            driver.find_element(By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(2)').click()
            time.sleep(1)
            template_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#prd_name')))
            time.sleep(1)
            template_name_input.send_keys('멘즈샵 - 지갑, 가방, 잡화 템플릿')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/ui-view[1]/div[2]/form/div[1]/div/ul/li[6]/div/div/ncp-datetime-range-picker2/div[1]/div/div/button[7]').click()
            time.sleep(1)
            save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(1)')))
            time.sleep(1)
            save_button.click()
            time.sleep(1)
            temp_copy = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div:nth-child(1) > div > div:nth-child(3)')))
            time.sleep(1)
            temp_copy.click()
        elif templit == '기본 잡화':
            print('템플릿 코드 06 >> 여성 잡화')
            driver.find_element(By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(2)').click()
            time.sleep(1)
            template_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#prd_name')))
            time.sleep(1)
            template_name_input.send_keys('기본 - 지갑, 가방, 잡화 템플릿')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/ui-view[1]/div[2]/form/div[1]/div/ul/li[6]/div/div/ncp-datetime-range-picker2/div[1]/div/div/button[7]').click()
            time.sleep(1)
            save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(1)')))
            time.sleep(1)
            save_button.click()
            time.sleep(1)
            temp_copy = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div:nth-child(1) > div > div:nth-child(3)')))
            time.sleep(1)
            temp_copy.click()
        elif templit == '멘즈 NEW 신발':
            print('템플릿 코드 07 >> 남성 NEW 신발')
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div/ui-view[1]/div[2]/form/div[2]/div/button[2]').click()
            time.sleep(1)
            template_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#prd_name')))
            time.sleep(1)
            template_name_input.send_keys('멘즈 샵 - 신발 NEW 템플릿')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/ui-view[1]/div[2]/form/div[1]/div/ul/li[6]/div/div/ncp-datetime-range-picker2/div[1]/div/div/button[7]').click()
            time.sleep(1)
            save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(1)')))
            time.sleep(1)
            save_button.click()
            time.sleep(1)
            temp_copy = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div:nth-child(1) > div > div:nth-child(3)')))
            time.sleep(1)
            temp_copy.click()
        elif templit == '멘즈 NEW 의류':
            print('템플릿 코드 08 >> 남성 NEW 의류')
            driver.find_element(By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(2)').click()
            time.sleep(1)
            template_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#prd_name')))
            time.sleep(1)
            template_name_input.send_keys('멘즈 샵 - 의류 NEW 템플릿')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/ui-view[1]/div[2]/form/div[1]/div/ul/li[6]/div/div/ncp-datetime-range-picker2/div[1]/div/div/button[7]').click()
            time.sleep(1)
            save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(1)')))
            time.sleep(1)
            save_button.click()
            time.sleep(1)
            temp_copy = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div:nth-child(1) > div > div:nth-child(3)')))
            time.sleep(1)
            temp_copy.click()
        elif templit == '멘즈 NEW 잡화':
            print('템플릿 코드 09 >> 남성 NEW 잡화')
            driver.find_element(By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(2)').click()
            time.sleep(1)
            template_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#prd_name')))
            time.sleep(1)
            template_name_input.send_keys('멘즈 샵 - 지갑, 가방, 잡화 NEW 템플릿')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/ui-view[1]/div[2]/form/div[1]/div/ul/li[6]/div/div/ncp-datetime-range-picker2/div[1]/div/div/button[7]').click()
            time.sleep(1)
            save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(1)')))
            time.sleep(1)
            save_button.click()
            time.sleep(1)
            temp_copy = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div:nth-child(1) > div > div:nth-child(3)')))
            time.sleep(1)
            temp_copy.click()
        elif templit == '기본 NEW 신발':
            print('템플릿 코드 10 >> 여성 NEW 신발')
            driver.find_element(By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(2)').click()
            time.sleep(1)
            template_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#prd_name')))
            time.sleep(1)
            template_name_input.send_keys('기 본 NEW - 신발 신상 템플릿')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/ui-view[1]/div[2]/form/div[1]/div/ul/li[6]/div/div/ncp-datetime-range-picker2/div[1]/div/div/button[7]').click()
            time.sleep(1)
            save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(1)')))
            time.sleep(1)
            save_button.click()
            time.sleep(1)
            temp_copy = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div:nth-child(1) > div > div:nth-child(3)')))
            time.sleep(1)
            temp_copy.click()
        elif templit == '기본 NEW 의류':
            print('템플릿 코드 11 >> 여성 신상 의류')
            driver.find_element(By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(2)').click()
            time.sleep(1)
            template_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#prd_name')))
            time.sleep(1)
            template_name_input.send_keys('기 본 NEW - 의류 신상 템플릿')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/ui-view[1]/div[2]/form/div[1]/div/ul/li[6]/div/div/ncp-datetime-range-picker2/div[1]/div/div/button[7]').click()
            time.sleep(1)
            save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(1)')))
            time.sleep(1)
            save_button.click()
            time.sleep(1)
            temp_copy = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div:nth-child(1) > div > div:nth-child(3)')))
            time.sleep(1)
            temp_copy.click()  
        elif templit == '기본 NEW 잡화':
            print('템플릿 코드 12 >> 여성 NEW 잡화')
            driver.find_element(By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(2)').click()
            time.sleep(1)
            template_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#prd_name')))
            time.sleep(1)
            template_name_input.send_keys('기 본 NEW - 지갑, 가방, 잡화 신상 템플릿')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/ui-view[1]/div[2]/form/div[1]/div/ul/li[6]/div/div/ncp-datetime-range-picker2/div[1]/div/div/button[7]').click()
            time.sleep(1)
            save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(1) > div:nth-child(2) > form > div:nth-child(2) > div > button:nth-child(1)')))
            time.sleep(1)
            save_button.click()
            time.sleep(1)
            temp_copy = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > ui-view > div > ui-view:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div:nth-child(1) > div > div:nth-child(3)')))
            time.sleep(1)
            temp_copy.click()

        else:
            print('템플릿 넘버 에러!! 확인해주세요!!')

        time.sleep(7)
        
        try:
            popup_button1 = driver.find_element(By.CSS_SELECTOR, 'body > div.modal.seller-layer-modal.fade.in > div > div > div.modal-footer > div > button')
            print('팝업을 찾았어요!')
            popup_button1.click()
            print('팝업 EXIT')
            time.sleep(2)
        except NoSuchElementException:
            pass

        print('상세 정보 입력을 시작합니다.')   
        time.sleep(1)
        try:
            popup_button2 = driver.find_element(By.CSS_SELECTOR, 'body > div.modal.seller-layer-modal.fade.in > div > div > div.modal-footer > div > button')
            print('또 팝업을 찾았어요!')
            popup_button2.click()
            print('또 팝업 EXIT')
            time.sleep(1)
        except NoSuchElementException:
            pass
        
        time.sleep(random.uniform(3, 4))
        driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[1]/div[1]/div/label[2]').click()    
    ####    ###############################    ###############################    ###############################    ###############################    ###############################
    ####### 카테고리 카테고리 카테고리 카테고리 카테고리 카테고리 # 카테고리 카테고리 카테고리 카테고리 카테고리 카테고리 # 카테고리 카테고리 카테고리 카테고리 카테고리 카테고리 # 카테고리 카테고리 카테고리 카테고리 카테고리 카테고리 
    ####    ###############################    ###############################    ###############################    ###############################    ###############################
    ####### 카테고리 카테고리 카테고리 카테고리 카테고리 카테고리 # 카테고리 카테고리 카테고리 카테고리 카테고리 카테고리 # 카테고리 카테고리 카테고리 카테고리 카테고리 카테고리 # 카테고리 카테고리 카테고리 카테고리 카테고리 카테고리 
    ###    ###############################    ###############################    ###############################    ###############################    ###############################
        time.sleep(2)
        
        if any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '워킹화':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[3]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[12]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[5]').click()
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '워킹화':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[12]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[5]').click()
        
        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '샌들':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[3]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[7]').click()
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '샌들':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[12]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[6]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[4]').click()
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '뮬':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[12]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[6]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[3]').click()
        
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '하이힐':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[12]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[11]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[10]').click()
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '웨지힐':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[12]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[11]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[6]').click()
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '펌프스':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[12]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[11]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[9]').click()
        
        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '스니커즈':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[3]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[8]').click()
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '스니커즈':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[12]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[3]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[4]').click()
        
        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '부츠':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[3]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[6]').click()
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '부츠':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[12]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[4]').click()
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '미들부츠':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[12]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[3]').click()
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '롱부츠':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[12]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[2]').click()

        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '슬립온':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[3]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[10]').click()
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '슬립온':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[12]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[3]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[5]').click()


        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '슬리퍼':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[3]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[9]').click()
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '슬리퍼':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[12]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[7]').click()
        
        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '로퍼':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[3]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[2]').click()
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '로퍼':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[12]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[3]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[2]').click()
        
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '스포츠양말':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[5]').click()
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '스포츠양말':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[3]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[8]').click()
        
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '가죽시계':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[8]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[6]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[2]').click()
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '가죽시계':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[8]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[6]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[2]').click()
        
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '메탈시계':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[8]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[6]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[5]').click()
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '메탈시계':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[8]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[6]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[5]').click()
        
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '우레탄시계':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[8]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[6]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[8]').click()
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '우레탄시계':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[8]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[6]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[8]').click()
        
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '스커트':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[5]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[7]').click()
                    
        
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '원피스':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[5]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[8]').click()
              
        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"])  and category_2 == '팬티':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[2]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[7]').click()
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '팬티':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[4]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[11]').click()
        
        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"])  and category_2 == '카디건':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[3]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[13]').click()
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '카디건':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[5]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[16]').click()
            
        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"])  and category_2 == '청바지':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[3]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[12]').click()
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '청바지':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[5]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[15]').click()
            
        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '티셔츠':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[3]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[17]').click()
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '티셔츠':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[5]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[20]').click()

        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '홈웨어':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[6]').click()
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '홈웨어':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[10]').click()
    
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '브라':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[4]').click()
             
        
        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '셔츠':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[3]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[5]').click()
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '셔츠':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[5]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[6]').click()
        
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '블라우스':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[5]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[6]').click()

        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '코트':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[3]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[15]').click()
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '코트':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[5]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[18]').click()
           
             
        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '바지':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[3]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[4]').click()
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '바지':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[5]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[5]').click()
        
        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '재킷':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[3]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[7]').click()
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '재킷':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[5]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[10]').click()
        
        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '점퍼':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[3]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[8]').click()
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '점퍼':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[5]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[11]').click()
        

        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '니트':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[3]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[2]').click()
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '니트':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul/li[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[5]').click()
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[2]').click()
                
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '크로스백':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[6]').click()
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '크로스백':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[11]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[6]').click()
        
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '클러치':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[6]').click()
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '클러치':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[11]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[6]').click()
        
        
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '힙색':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[9]').click()
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '힙색':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[11]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[9]').click()
         
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '토트백':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[8]').click()
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '토트백':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[11]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[8]').click()
        
         
        elif category_2 == '페도라':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[13]').click()
           
        elif category_2 == '헌팅캡':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[14]').click()
           
        elif category_2 == '사파리모자':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[9]').click()
        elif category_2 == '비니':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[8]').click()

        elif category_2 == '스냅백 메시캡':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[11]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[2]').click()
        elif category_2 == '스냅백 일반캡':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[11]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[3]').click()
            
        elif category_2 == '야구모자 메시캡':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[12]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[2]').click()
        elif category_2 == '야구모자 일반캡':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[12]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[3]').click()
        
        elif category_2 == '선글라스':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[6]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[2]').click()

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '장갑':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[14]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[2]').click()

        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '장갑':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[14]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[4]').click()

        
        elif category_2 == '귀걸이':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[15]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[11]').click()
        
        elif category_2 == '주얼리케이스':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[15]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[7]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[3]').click()
         
        elif category_2 == '팔찌':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[15]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[8]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[6]').click()
        
        elif category_2 == '반지':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[15]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[11]').click()
        
        elif category_2 == '발찌':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[15]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[5]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[3]').click()
        
        
        elif category_2 == '목걸이':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[15]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[3]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[11]').click()
        
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '백팩':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[2]').click()
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '백팩':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[11]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[3]').click()
         
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '숄더백':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[4]').click()
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '숄더백':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[11]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[4]').click()
          

        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '헤어핀':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[18]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[6]').click()


        
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '반지갑':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[16]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[2]').click()
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '반지갑':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[16]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[5]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[2]').click()
        
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '중지갑':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[16]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[4]').click()
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '중지갑':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[16]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[5]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[4]').click()
        
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '장지갑':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[16]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[3]').click()
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '장지갑':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[16]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[5]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul/li[3]').click()
       
        elif category_2 == '동전지갑':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[16]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[3]').click()
        elif category_2 == '머니클립':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[16]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[4]').click()
        elif category_2 == '카드지갑':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[16]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[8]').click()
        elif category_2 == '지갑세트':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[16]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[7]').click()
        elif category_2 == '열쇠지갑':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[16]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[6]').click()

        elif category_2 == '키홀더':
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div/div/category-search/div[3]/div[1]/ul/li[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '/html/body/div[1]/div/div/div[2]/div/span[2]/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul/li[17]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,  '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul/li[19]').click()


        print('카테고리 선택 완료!')   
        
        
        
        try:
            popup_button3 = driver.find_element(By.CSS_SELECTOR, 'body > div.modal.seller-layer-modal.fade.in > div > div > div.modal-footer > div > button')
            print('팝업을 찾았어요!')
            popup_button3.click()
            print('팝업 EXIT')
            time.sleep(2)
        except NoSuchElementException:
            pass
        try:
            popup_button4 = driver.find_element(By.CSS_SELECTOR, 'body > div.modal.seller-layer-modal.fade.in > div > div > div.modal-footer > div > button')
            print('팝업을 찾았어요!')
            popup_button4.click()
            print('팝업 EXIT')
            time.sleep(1)
        except NoSuchElementException:
            pass
    ###############################    ###############################    ###############################    ###############################    ###############################
    ###############################    ###############################    ###############################    ###############################    ###############################
        
        driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[7]/div/div[2]/div/div/div/div/div/div/input').clear()
        driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[7]/div/div[2]/div/div/div/div/div/div/input').send_keys(title)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="prd_price2"]').clear()
        driver.find_element(By.XPATH, '//*[@id="prd_price2"]').send_keys(price)
        body = driver.find_element(By.TAG_NAME, 'body')
        body.click()
        time.sleep(2)
        body.click()
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        
      ###############################    ###############################    ###############################    ###############################    ###############################
    ###############################    ###############################    ###############################    ###############################    ###############################
        print('옵션 정보를 입력합니다.')   
        
        
        if category_2 == '귀걸이':
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/div/div/div/a').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[1]/div/div/div/div/label[2]').click()
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 570);")
            time.sleep(1)    
        elif category_2 in ['주얼리케이스', '팔찌', '반지', '목걸이', '키홀더', '발찌', '가죽시계', '메탈시계', '우레탄시계', '선글라스','장갑']:
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/div/div/div/a').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[1]/div/div/div/div/label[2]').click()
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 570);")
            time.sleep(1)
        else:    
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/div/div/div/a').click()
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[1]/div[3]/div[1]/ul/li[{color_a}]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[1]/div[3]/div[2]/div/button').click()
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, 'body > div.modal.fade.seller-layer-modal.modal-no-space.in > div > div > div.modal-body > div.modal-body > div.pd-xlg.mg-bottom-xlg > form > div > div.seller-input-wrap.form-group > input').send_keys(color)
            driver.find_element(By.CSS_SELECTOR, 'body > div.modal.fade.seller-layer-modal.modal-no-space.in > div > div > div.modal-body > div.modal-footer > div > span:nth-child(2) > button').click()
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 570);")
            time.sleep(2)
            pass


 
    ###############################
    ###############################
    ##      사이즈 옵션             ##    ###############################    ###############################    ###############################    ###############################
    ###############################
    ###############################    
        
        if any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '팬티':
            for op in range(5,10):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '팬티':
            for op in range(4,9):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        

        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '브라':
            for op in range(4,9):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        
        
        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '워킹화':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(9,20):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()
            #driver.execute_script("window.scrollBy(0, 700);")
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '워킹화':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(5,16):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()
            #driver.execute_script("window.scrollBy(0, 700);")
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
    
        elif category_2 == '하이힐':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(5,16):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif category_2 == '웨지힐':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(5,16):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif category_2 == '펌프스':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(5,16):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
    
    
        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '샌들':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(9,20):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '샌들':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(5,16):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '뮬':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(5,16):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)

        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '스니커즈':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(9,20):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '스니커즈':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(5,16):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
    
        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '슬립온':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(9,20):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '슬립온':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(5,16):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
    
        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '로퍼':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(9,20):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '로퍼':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(5,16):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
    
        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '부츠':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(9,20):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '부츠':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(5,16):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
    
        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '미들부츠':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(9,20):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '미들부츠':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(5,16):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '롱부츠':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(9,20):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '롱부츠':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(5,16):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
    
        
        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '슬리퍼':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(9,20):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '슬리퍼':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(5,16):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
            
        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '티셔츠':
            for op in range(6,11):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '티셔츠':
            for op in range(5,10):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)

        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '카디건':
            for op in range(6,11):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '카디건':
            for op in range(5,10):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '코트':
            for op in range(6,11):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '코트':
            for op in range(5,10):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)


        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '홈웨어':
            for op in range(5,10):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '홈웨어':
            for op in range(4,9):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
            
        
        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '셔츠':
            for op in range(6,11):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '셔츠':
            for op in range(5,10):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '블라우스':
            for op in range(5,10):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        
        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '청바지':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_UP)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(8,16):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()
 
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '청바지':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_UP)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(4,15):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
                
        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '바지':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(6,11):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()
 
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '바지':
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').click()
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(Keys.ENTER)
            for op in range(5,10):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)   
            
        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '재킷':
            for op in range(6,11):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '재킷':
            for op in range(5,10):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        
        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '점퍼':
            for op in range(6,11):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '점퍼':
            for op in range(5,10):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
            
        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '니트':
            for op in range(6,11):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '니트':
            for op in range(5,10):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
            
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '원피스':
            for op in range(5,10):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()


            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '스커트':
            for op in range(5,10):
                time.sleep(1)
                driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[{op}]').click()


            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
          
        
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '숄더백':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
         
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)   
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '숄더백':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
  
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)

            
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '힙색':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
 
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)        
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '힙색':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
   
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '스포츠양말':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
    
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)      
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '스포츠양말':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '백팩':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)   
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '백팩':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '클러치':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
      
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)   
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '클러치':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)

        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '헤어핀':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
     
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)   

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '반지갑':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
    
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)   
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '반지갑':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '중지갑':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
  
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)   
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '중지갑':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '장지갑':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
     
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)   
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '장지갑':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '동전지갑':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)   
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '동전지갑':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '머니클립':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)   
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '머니클립':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
  
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '카드지갑':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
        
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)   
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '카드지갑':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '지갑세트':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
        
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)   
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '지갑세트':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
 
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '동전지갑':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
     
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)   
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '동전지갑':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '열쇠지갑':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)   
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '열쇠지갑':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '크로스백':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
                      
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)   
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '크로스백':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
               
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '토트백':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
                 
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)        
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '토트백':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
               
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
    
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '페도라':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
                
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '페도라':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
                 
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)             

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '스냅백 메시캡':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()

            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '스냅백 메시캡':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
            
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '스냅백 일반캡':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
            
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '스냅백 일반캡':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
            
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '헌팅캡':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
            
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '헌팅캡':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
            
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '야구모자 메시캡':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
            
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '야구모자 메시캡':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
            
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '야구모자 일반캡':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
            
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '야구모자 일반캡':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
            
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '사파리모자':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
            
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '사파리모자':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
            
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '비니':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
            
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '비니':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
            
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '선글라스':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
            
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '선글라스':
            time.sleep(1)
            driver.find_element(By.XPATH, f'//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/ul/li[1]').click()
            
            driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div/div/button').click()
            time.sleep(1)

    ###############################
    ###############################     
    ###############################
    ###############################    ###############################    ###############################    ###############################    ###############################
    ###############################     
    ###############################
    ###############################    
        print('대표 썸네일 업로드') 
        
        driver.execute_script("window.scrollBy(0, 420);")
        time.sleep(1)
        point1 = driver.find_element(By.XPATH, '//*[@id="representImage"]/div/div[1]//p/a[2]')
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView();", point1)
        
        #대표 썸네일 첨부
        driver.find_element(By.XPATH, '//*[@id="representImage"]/div/div[1]//p/a[2]').click()
        time.sleep(2)

        driver.find_element(By.XPATH, '/html/body/label/input').send_keys(f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a1.jpg')
        time.sleep(5)
        point1 = driver.find_element(By.XPATH, '//*[@id="optionalImages"]/div/div[1]/div/ul/li/div/a')
        print('추가 썸네일 업로드') 
            ##############
            #추가 썸네일 첨부#
            ##############
        for j in range(2, 11):
            if j > 7 and not os.path.exists(f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a{j}.jpg'):
                break
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", point1)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="optionalImages"]/div/div[1]/div/ul/li/div/a').click()
            time.sleep(2)
            driver.find_element(By.XPATH, '/html/body/label/input').send_keys(f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a{j}.jpg')
            time.sleep(7)
            print('진행중..')   
        
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        no16 = driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]')
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 700);")
        no16.click()
        time.sleep(3)
        print('브랜드 및 제조사 입력')   
        #브랜드 입력
        brand_1 = driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/ncp-naver-shopping-search-info/div[2]/div/div[1]/div/ncp-brand-manufacturer-input/div/div/div/div/div/div[1]/input')
        brand_2 = driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/ncp-naver-shopping-search-info/div[2]/div/div[2]/div/ncp-brand-manufacturer-input/div/div/div/div/div/div[1]/input')


        brand_1.send_keys(brand)
        time.sleep(2)
        brand_1.send_keys(Keys.ENTER)
        body.send_keys(Keys.ESCAPE)
        time.sleep(1)
        brand_2.send_keys(brand)
        time.sleep(2)
        brand_2.send_keys(Keys.ENTER)
        body.send_keys(Keys.ESCAPE)
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 700);")
        
        print('상품주요 정보를 선택합니다.')   
        
        ####################################################################################    ####################################################################################
        ####################################################################################    ####################################################################################
        ############################  상품주요 정보 상품별로 다르게 지정  ###########################    ####################################################################################
        ####################################################################################    ####################################################################################
        ####################################################################################    ####################################################################################
        
        if any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '워킹화':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[17]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)       
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[3]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[4]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div[1]/label[9]').click()
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '워킹화':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[17]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)       
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[3]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[4]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div[1]/label[9]').click()

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '가죽시계':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div[1]/label[7]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div[1]/label[23]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[3]/td/div/div/div[1]/label[18]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[2]/td/div/div/div[1]/label[24]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)

            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '가죽시계':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div[1]/label[7]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div[1]/label[23]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[3]/td/div/div/div[1]/label[18]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[2]/td/div/div/div[1]/label[24]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
         
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '메탈시계':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[7]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div[1]/label[23]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[3]/td/div/div/div[1]/label[18]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[2]/td/div/div/div[1]/label[24]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)     
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '메탈시계':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[7]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div[1]/label[23]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[3]/td/div/div/div[1]/label[18]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[2]/td/div/div/div[1]/label[24]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
       
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '우레탄시계':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div[1]/label[7]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div[1]/label[8]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[3]/td/div/div/div[1]/label[10]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[2]/td/div/div/div[1]/label[24]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)     
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '우레탄시계':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div[1]/label[7]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div[1]/label[8]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[3]/td/div/div/div[1]/label[10]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[2]/td/div/div/div[1]/label[24]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[4]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[5]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)     
        
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '스커트':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[45]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[15]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)

        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '샌들':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[18]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)       
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[23]').click()        
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '샌들':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[18]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[23]').click()
            time.sleep(1)
        
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '뮬':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[10]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div[1]/label[18]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[23]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        
        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '스니커즈':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[17]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)       
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div[1]/label[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[4]').click()
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '스니커즈':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[17]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)       
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div[1]/label[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[4]').click()

        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '슬립온':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[18]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[4]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[23]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)      
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '슬립온':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[18]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[4]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[23]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)      
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)

        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '로퍼':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[18]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[23]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div[1]/label[4]').click()
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '로퍼':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[18]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[23]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[4]').click()        
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)      
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)

        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '부츠':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[18]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[11]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div[1]/label[4]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[5]/td/div/div/div[1]/label[23]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '부츠':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[18]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[11]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[10]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div[1]/label[4]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[5]/td/div/div/div[1]/label[23]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)

        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '미들부츠':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[18]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[11]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div[1]/label[4]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[5]/td/div/div/div[1]/label[23]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '미들부츠':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[18]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[11]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[10]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div[1]/label[4]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[5]/td/div/div/div[1]/label[23]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)

        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '롱부츠':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[18]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[11]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div[1]/label[4]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[5]/td/div/div/div[1]/label[23]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '롱부츠':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[18]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[11]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[10]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div[1]/label[4]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[5]/td/div/div/div[1]/label[23]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)


        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '스포츠양말':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '스포츠양말':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)

        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '헤어핀':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[6]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[8]').click()
        
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '반지갑':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[5]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div[1]/label[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '반지갑':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[5]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div[1]/label[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '중지갑':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[5]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div[1]/label[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '중지갑':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[5]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div[1]/label[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '장지갑':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[5]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div[1]/label[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '장지갑':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[5]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div[1]/label[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '동전지갑':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[10]').click()
            time.sleep(1)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '동전지갑':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[10]').click()
            time.sleep(1)
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '머니클립':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '머니클립':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '지갑세트':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[5]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '지갑세트':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[5]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '카드지갑':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[5]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div[1]/label[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '카드지갑':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[5]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[4]/td/div/div/div[1]/label[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '열쇠지갑':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '열쇠지갑':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)

        elif any(item in templit for item in ["멘즈샵 신발", "멘즈 NEW 신발"]) and category_2 == '슬리퍼':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[17]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[4]').click()
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)       
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[23]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[4]').click()
        elif any(item in templit for item in ["기본 신발", "기본 NEW 신발"]) and category_2 == '슬리퍼':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[17]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[4]').click()
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)       
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[23]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[4]').click()
    
        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '팬티':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/div').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
        
            # templit이 "03"이고 category_2가 "티셔츠"일 때 실행할 코드
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '팬티':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[7]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
        
        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '티셔츠':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[47]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)     
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == "티셔츠":
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[47]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)     
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)

        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '카디건':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[47]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div[1]/label[12]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == "카디건":
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[47]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div[1]/label[12]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 


        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '청바지':
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[13]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[20]').click()   
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '청바지':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[13]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[20]').click()   
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 

        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '점퍼':
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[47]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[11]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)     
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == "점퍼":
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[47]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[11]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)     
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 

        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '코트':
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[47]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div[1]/label[19]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)     
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == "코트":
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[47]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div[1]/label[19]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)     
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)

  



        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '셔츠':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[47]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)     
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '셔츠':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[9]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div[1]/label[47]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[20]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)     
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
       
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '블라우스':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[9]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div[1]/label[45]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[15]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)     
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)

        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '바지':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)   
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN) 
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)       
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)     
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)     
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[13]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div[1]/label[47]').click()   
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()          
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[20]').click()
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '바지':
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[6]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)   
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN) 
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)       
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)     
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)     
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div[1]/label[47]').click()   
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()          
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[20]').click()

        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '재킷':
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[47]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[7]/td/div/div/div[1]/label[22]').click()
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)     
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[8]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[8]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[8]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[8]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[8]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[8]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[8]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[8]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[8]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == "재킷":
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[47]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[7]/td/div/div/div[1]/label[22]').click()
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)     
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[8]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[8]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[8]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[8]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[8]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[8]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[8]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[8]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[8]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)

        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '니트':
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[47]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div[1]/label[12]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)     
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == "니트":
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[47]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div[1]/label[12]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)     
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)

        elif any(item in templit for item in ["멘즈샵 의류", "멘즈 NEW 의류"]) and category_2 == '홈웨어':
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div[1]/label[13]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
                        
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)     
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == "홈웨어":
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div[1]/label[13]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
                        
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)     
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)

        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == "원피스":
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[45]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[8]/td/div/div/div[1]/label[9]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[15]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)     
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[7]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '크로스백':
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[29]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[22]').click()   
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[14]').click()   
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[4]').click()           
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '크로스백':
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[29]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[22]').click()   
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[14]').click()   
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[4]').click()           
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)     

        elif any(item in templit for item in ["기본 의류", "기본 NEW 의류"]) and category_2 == '브라':
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[13]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()           
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[3]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '클러치':
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[22]').click()   
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[10]').click()   
          
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '클러치':
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[22]').click()   
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[10]').click()   
          
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            time.sleep(1)    

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '힙색':
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[29]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[22]').click()   
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[14]').click()   
       
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '힙색':
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[20]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[22]').click()   
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[10]').click()   
        
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            #driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[4]').click() 
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == "백팩":
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[29]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[4]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div[1]/label[14]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)    
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == "백팩":
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[29]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[4]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div[1]/label[14]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)    

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == "숄더백":
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[29]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[14]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == "숄더백":
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[29]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[14]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)    

        elif category_2 == "하이힐":
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[10]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[4]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[5]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[7]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div[1]/label[18]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[23]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)    
        elif category_2 == "웨지힐":
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[10]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[18]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div[1]/label[4]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div[1]/label[5]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div[1]/label[7]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[23]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)    
        elif category_2 == "펌프스":
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[10]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[18]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div[1]/label[4]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div[1]/label[5]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div[1]/label[7]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[23]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)    
       
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == '토트백':
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[27]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[22]').click()   
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[14]').click()   
        
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[4]').click()   
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == '토트백':
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[27]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[22]').click()   
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[14]').click()   
        
            time.sleep(1)       
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)     
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div[1]/label[4]').click()   
         
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == "페도라":
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[27]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == "페도라":
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[27]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == "스냅백 일반캡":
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[32]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == "스냅백 일반캡":
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[32]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)   

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == "스냅백 메시캡":
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[32]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == "스냅백 메시캡":
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[27]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)   
    
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == "야구모자 일반캡":
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[32]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)       
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == "야구모자 일반캡":
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[32]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == "야구모자 메시캡":
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[32]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == "야구모자 메시캡":
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[32]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)   
    
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == "헌팅캡":
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[27]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == "헌팅캡":
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[27]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == "사파리모자":
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[32]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == "사파리모자":
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[32]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == "비니":
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[32]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH,'//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH,'//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH,'//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH,'//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == "비니":
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div[1]/label[32]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[1]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[2]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[3]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div[1]/label[4]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[13]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH,'//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH,'//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH,'//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH,'//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[6]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == "장갑":
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[7]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH,'//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH,'//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == "장갑":
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[2]/td/div/div/div[1]/label[22]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[2]/tr[3]/td/div/div/div[1]/label[7]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH,'//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH,'//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)


        elif category_2 == "귀걸이":

            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[6]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif category_2 == "주얼리케이스":
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[9]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)

        elif category_2 == "키홀더":
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[9]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[18]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == "발찌":
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[13]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[7]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == "발찌":
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[13]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[7]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
       
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == "팔찌":

            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[13]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[7]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[7]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == "팔찌":

            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[13]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[7]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[7]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
        
        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == "반지":

            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[8]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)   
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == "반지":

            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[8]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == "목걸이":
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[7]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[6]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[12]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)   
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == "목걸이":
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[2]/td/div/div/div[1]/label[7]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[3]/td/div/div/div[1]/label[6]').click()
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[4]/td/div/div/div[1]/label[12]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody/tr[5]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)  

        elif any(item in templit for item in ["멘즈샵 잡화", "멘즈 NEW 잡화"]) and category_2 == "선글라스":
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div[1]/label[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
        elif any(item in templit for item in ["기본 잡화", "기본 NEW 잡화"]) and category_2 == "선글라스":
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[5]/td/div/div/div[1]/label[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[4]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[3]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ARROW_DOWN)
            driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/div[1]/div/ncp-product-attribute-table/div[2]/table/tbody[1]/tr[2]/td/div/div/div/div/div[1]/input').send_keys(Keys.ENTER) 

      
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/ncp-origin-area/div/div/div/div/div/div[1]/div[4]/div/div/input').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/ncp-origin-area/div/div/div/div/div/div[1]/div[4]/div/div/input').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/ncp-origin-area/div/div/div/div/div/div[1]/div[4]/div/div/input').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/ncp-origin-area/div/div/div/div/div/div[1]/div[4]/div/div/input').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/ncp-origin-area/div/div/div/div/div/div[1]/div[4]/div/div/input').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/ncp-origin-area/div/div/div/div/div/div[1]/div[4]/div/div/input').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/ncp-origin-area/div/div/div/div/div/div[1]/div[4]/div/div/input').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/ncp-origin-area/div/div/div/div/div/div[1]/div[4]/div/div/input').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/ncp-origin-area/div/div/div/div/div/div[1]/div[4]/div/div/input').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/ncp-origin-area/div/div/div/div/div/div[1]/div[4]/div/div/input').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="_prod-attr-section"]/div[2]/div/ncp-origin-area/div/div/div/div/div/div[1]/div[4]/div/div/input').send_keys(brand)

        #####################################################################################    ####################################################################################
        ####################################################################################    ####################################################################################
        ####################################################################################    ####################################################################################
        ####################################################################################    ####################################################################################
        ####################################################################################    ####################################################################################
        print('판매자 상품코드 업데이트')   
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 900);")
        time.sleep(1)   
        driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[24]').click()
        
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(Keys.BACKSPACE)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(sku)
        time.sleep(0.5)        
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(Keys.SPACE)
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(ori)
        time.sleep(0.5)        
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(Keys.SPACE)
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="seller-code1"]').send_keys(new_price)
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="seller-code2"]').send_keys(sku)
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="seller-code3"]').send_keys(ori)
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="seller-code4"]').send_keys(new_price)
        time.sleep(0.5)
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 999);")
        driver.execute_script("window.scrollBy(0, 999);")
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[25]/div/div[2]/div/div[2]/div/div[2]/ng-include/div/div[3]/div/div/div/label[1]').click()
        print('전시상태 >> 전시중으로 설정 완료')
        
        #driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[25]/div/div[2]/div/div[1]/div/div[1]/div[2]/div').click()
        #print('쇼핑윈도 >> 오픈클릭')
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, -590);")
        time.sleep(1)
        
        ####################################################################################    ####################################################################################
        ####################################################################################    ####################################################################################
        # 태그 설정 태그 설정 태그 설정 태그 설정 태그 설정 태그 설정 태그 설정 태그 설정 태그 설정 태그 설정 태그 설정 태그 설정 태그 설정 태그 설정 태그 설정 태그 설정 태그 설정 태그 설정 태그 설정 태그 설정 태그 설정 태그 설정
        #####################################################################################    ####################################################################################
        ####################################################################################    ####################################################################################

        driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[23]').click()
    
        # ng-repeat로 시작하는 요소를 찾음
        #elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li[ng-repeat^='tagInfo in vm.viewData.emotionTags'] a")))

        #if len(elements) >= 9:
        #    random_elements = random.sample(elements, 9)
        #else:
        #    random_elements = elements

        #clicked_elements = set()  # 클릭한 요소들의 고유 ID를 저장할 set

        # 무작위로 선택된 요소들을 하나씩 클릭
        #for element in random_elements:
        #    if element.id not in clicked_elements:  # 해당 요소가 이미 클릭되었는지 확인
        #        element.click()
        #        clicked_elements.add(element.id)  # 클릭한 요소를 set에 추가
        #        time.sleep(0.5)  # 각 클릭 사이에 0.5초간 대기

        #time.sleep(1)
        driver.execute_script("window.scrollBy(0, -999);")
        driver.execute_script("window.scrollBy(0, -999);")
        driver.execute_script("window.scrollBy(0, -999);")
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="productForm"]/ng-include/ui-view[14]/div/div[2]/div/div/ncp-editor-form/div[1]/div/p[4]/button').click()
        
        time.sleep(2)
        
        print('스마트 에디터 실행')   
        
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ################  스마트 에디터  ##############################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ################  스마트 에디터  ##############################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################

        driver.switch_to.window(driver.window_handles[1])
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#one-editor')))
        time.sleep(7)
        print('스마트 에디터 접속 완료')   
############################################################################################################################################################################################################################
        if templit == '멘즈샵 신발':
            print('템플릿 코드 (1) 남성 신발')
            
            image_upload = driver.find_element(By.CLASS_NAME, 'se-toolbar-label')
            time.sleep(1)
            html_li = driver.find_element(By.CSS_SELECTOR, 'button.se-shopping-html-toolbar-button')
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(brand)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(title)
            time.sleep(2)
            
            try:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/button').click()
            except:
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-b8c12a54-6a18-4da6-b509-77fe2ff37cf5"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-b8c12a54-6a18-4da6-b509-77fe2ff37cf5"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(made)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-2480888d-113e-4be8-b035-649aab6f87cb"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-2480888d-113e-4be8-b035-649aab6f87cb"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(fabric)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-484c0ab9-7663-4130-bf20-7ba2ba985b59"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-484c0ab9-7663-4130-bf20-7ba2ba985b59"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-345869b4-8d8f-4ba1-bf7f-e65b4b8024dd"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-345869b4-8d8f-4ba1-bf7f-e65b4b8024dd"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(sizet)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-90bccff5-fe79-49e7-a30b-5e8698b1bae9"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-90bccff5-fe79-49e7-a30b-5e8698b1bae9"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(model_tip)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-d66d69db-3011-4b3c-88cb-1dead2b96800"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-d66d69db-3011-4b3c-88cb-1dead2b96800"]/div/div/div/div/span').click()
            time.sleep(1)
            image_upload.click()
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/label/input').send_keys(f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a1.jpg')
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span').click()
            #
            #
            #
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            #
            #
            prompt = (title)
            prompt += f" 해당 상품에 대해서 제품 설명 작성해줘. 제품 특징은 {color}, {fabric}, {info} 한글로 작성해줘"

            print("입력한 질문 : ", prompt)
            # max_tokens 답변을 받을 수 있는 길이 (낮은 수로 설정해둔다면 말하다 끊김)
            response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=1,
            max_tokens=1285,
            top_p=0.85,
            frequency_penalty=0.85,
            presence_penalty=0.85
            )

            generated_text = response['choices'][0]['message']['content']
            print(generated_text)
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            generated_text = textwrap.fill(generated_text, width=100, replace_whitespace=False)
            #generated_text = '<p>' + generated_text.replace('\n', '</p><p>') + '</p>'
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            time.sleep(1)

            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(generated_text)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)


            point = driver.find_element(By.XPATH, '//*[@id="SE-d62164ca-5efb-44aa-8639-dcd4cad1cba4"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            point.click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))
            
            def count_images(folder_path, extensions=['.jpg', '.jpeg', '.png', '.gif']):
                image_count = 0
                for file_name in os.listdir(folder_path):
                    if any(file_name.lower().endswith(ext) for ext in extensions):
                        image_count += 1
                return image_count

            folder_path = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}'
            time.sleep(2)
            image_count = count_images(folder_path)
            print(f">>>>>>>>>> 해당 상품 이미지 {image_count}개 찼았으며 업로드 시작합니다.")

            #상세설명 이미지 대량 첨부
            for i1 in range(2, image_count + 1):
                image_upload.click()
                time.sleep(random.uniform(0.9, 1.2))
                file_name = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a{i1}.jpg'
                driver.find_element(By.XPATH, '/html/body/label/input').send_keys(file_name)
                time.sleep(8)
                html_li.click()
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
                time.sleep(random.uniform(0.9, 1.2))
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
                time.sleep(random.uniform(0.9, 1.2))
                
                
            driver.find_element(By.XPATH, '/html/body/ui-view[1]/ncp-editor-launcher/div[1]/div/button/span[1]/i').click()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)

        # 등록하기
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/div[2]/button[2]/span[1]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/button[2]').click()
            print('등록 완료')  
            time.sleep(4)
############################################################################################################################################################################################################################
        elif templit == '기본 신발':
            print('템플릿 코드 (2) 여성 신발')
            
            point = driver.find_element(By.XPATH, '//*[@id="SE-5c09ffb4-3b6c-4e7a-aa0e-ef06e018b4c9"]/div/div/div/div/span')
            image_upload = driver.find_element(By.CLASS_NAME, 'se-toolbar-label')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-db1e53c7-326a-422a-908d-5983c8fba9b6"]').click()
            time.sleep(1)
            image_upload.click()
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/label/input').send_keys(f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a1.jpg')
            time.sleep(3)
            html_li = driver.find_element(By.CSS_SELECTOR, 'button.se-shopping-html-toolbar-button')
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-5c09ffb4-3b6c-4e7a-aa0e-ef06e018b4c9"]/div/div/div/div/span').click()
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(brand)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(title)
            time.sleep(2)
            
            try:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/button').click()
            except:
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
                
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-b8c12a54-6a18-4da6-b509-77fe2ff37cf5"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-b8c12a54-6a18-4da6-b509-77fe2ff37cf5"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(made)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="SE-2480888d-113e-4be8-b035-649aab6f87cb"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(fabric)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)  
            point = driver.find_element(By.XPATH, '//*[@id="SE-484c0ab9-7663-4130-bf20-7ba2ba985b59"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-484c0ab9-7663-4130-bf20-7ba2ba985b59"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-669c8989-e916-4a93-9fe2-77e9935b5c77"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-669c8989-e916-4a93-9fe2-77e9935b5c77"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(sizet)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-90bccff5-fe79-49e7-a30b-5e8698b1bae9"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-90bccff5-fe79-49e7-a30b-5e8698b1bae9"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(model_tip)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span')
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", point)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span').click()
            time.sleep(1)
            #
            #
            #
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            #
            #
            prompt = (title)
            prompt += f" 해당 상품에 대해서 제품 설명 작성해줘. 제품 특징은 {color}, {fabric}, {info} 한글로 작성해줘"

            print("입력한 질문 : ", prompt)
            # max_tokens 답변을 받을 수 있는 길이 (낮은 수로 설정해둔다면 말하다 끊김)
            response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=1,
            max_tokens=1589,
            top_p=0.85,
            frequency_penalty=0.85,
            presence_penalty=0.85
            )

            generated_text = response['choices'][0]['message']['content']
            print(generated_text)
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            generated_text = textwrap.fill(generated_text, width=100, replace_whitespace=False)
            #generated_text = '<p>' + generated_text.replace('\n', '</p><p>') + '</p>'
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            time.sleep(1)

            html_li.click()
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(generated_text)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            
    #############
    #############
    #############

            point = driver.find_element(By.XPATH, '//*[@id="SE-d62164ca-5efb-44aa-8639-dcd4cad1cba4"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            point.click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))

            def count_images(folder_path, extensions=['.jpg', '.jpeg', '.png', '.gif']):
                image_count = 0
                for file_name in os.listdir(folder_path):
                    if any(file_name.lower().endswith(ext) for ext in extensions):
                        image_count += 1
                return image_count

            folder_path = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}'
            time.sleep(2)
            image_count = count_images(folder_path)
            print(f">>>>>>>>>> 해당 상품 이미지 {image_count}개 찼았으며 업로드 시작합니다.")

            #상세설명 이미지 대량 첨부
            for i1 in range(2, image_count + 1):
                image_upload.click()
                time.sleep(random.uniform(0.9, 1.2))
                file_name = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a{i1}.jpg'
                driver.find_element(By.XPATH, '/html/body/label/input').send_keys(file_name)
                time.sleep(8)
                html_li.click()
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
                time.sleep(random.uniform(0.9, 1.2))
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
                time.sleep(random.uniform(0.9, 1.2))
                
                

            time.sleep(1)

            '''recommend = driver.find_element(By.CSS_SELECTOR, '#SE-fcf481f5-6ea7-4e81-80b7-88357d22ea8d')
            driver.execute_script("arguments[0].scrollIntoView();", recommend)


            driver.execute_script("window.open('about:blank', 'second_tab');")
            driver.switch_to.window("second_tab")
            time.sleep(1)
            driver.get('https://shopping.naver.com/foreign/stores/100344199')
            time.sleep(3)
            driver.execute_script("window.scrollBy(0, 700);")
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(2)
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(2)
            driver.execute_script("window.scrollBy(0, 700);")
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(2)
            
            elements1 = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "._3FUicfNemK")))

            if len(elements1) >= 5:
                random_elements = random.sample(elements1, 5)
            else:
                random_elements = elements
                

        #### 해외직구 추천상품 링크복사 ########
            # 무작위로 선택된 요소들의 링크를 저장할 빈 리스트 생성
            links = []

            # 무작위로 선택된 요소들을 하나씩 링크 복사
            for element in random_elements:
                # 각 요소에서 링크를 추출
                link = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
                # 링크를 리스트에 추가
                links.append(link)
                time.sleep(1)

            # 링크 출력
            print(links)

            driver.switch_to.window(driver.window_handles[1])
            time.sleep(5)

            # 에디터를 찾아서 element 변수에 저장
            editor = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#SE-fcf481f5-6ea7-4e81-80b7-88357d22ea8d > div > div.se-drop-indicator > div')))

            # 에디터에 포커스
            editor.click()
            
            link_up = driver.find_element(By.CSS_SELECTOR, 'button.se-oglink-toolbar-button')
            # 저장된 링크를 하나씩 특정 위치에 붙여넣기
            for link in links:
                # 링크를 클립보드에 복사
                pyperclip.copy(link)
                time.sleep(1)
                link_up.click()
                time.sleep(12)
                driver.find_element(By.XPATH, '/html/body/ui-view/ncp-editor-launcher/div/div/div/div/div/div/div/button').click()
                time.sleep(1)
                
            if len(driver.window_handles) >= 3:
                driver.switch_to.window(driver.window_handles[2])
                driver.close()
                time.sleep(1)
            
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(1)'''
            driver.find_element(By.XPATH, '/html/body/ui-view[1]/ncp-editor-launcher/div[1]/div/button/span[1]/i').click()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)

        # 등록하기
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/div[2]/button[2]/span[1]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/button[2]').click()
            print('등록 완료')  
            time.sleep(4)  
############################################################################################################################################################################################################################
        elif templit == '멘즈샵 의류':
            print('템플릿 코드 (3) 남성 의류')
            
            image_upload = driver.find_element(By.CLASS_NAME, 'se-toolbar-label')
            time.sleep(1)
            html_li = driver.find_element(By.CSS_SELECTOR, 'button.se-shopping-html-toolbar-button')
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(brand)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(title)
            time.sleep(2)
            try:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/button').click()
            except:
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-b8c12a54-6a18-4da6-b509-77fe2ff37cf5"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-b8c12a54-6a18-4da6-b509-77fe2ff37cf5"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(made)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-2480888d-113e-4be8-b035-649aab6f87cb"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-2480888d-113e-4be8-b035-649aab6f87cb"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(fabric)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)   
            point = driver.find_element(By.XPATH, '//*[@id="SE-484c0ab9-7663-4130-bf20-7ba2ba985b59"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-484c0ab9-7663-4130-bf20-7ba2ba985b59"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-582552b3-f5f7-46ea-acf1-5639bf405ef2"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-582552b3-f5f7-46ea-acf1-5639bf405ef2"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(sizet)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-90bccff5-fe79-49e7-a30b-5e8698b1bae9"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-90bccff5-fe79-49e7-a30b-5e8698b1bae9"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(model_tip)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-d66d69db-3011-4b3c-88cb-1dead2b96800"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-d66d69db-3011-4b3c-88cb-1dead2b96800"]/div/div/div/div/span').click()
            time.sleep(1)
            image_upload.click()
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/label/input').send_keys(f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a1.jpg')
            time.sleep(2)
            
            #
            #
            #
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            #
            #
            prompt = (title)
            prompt += f" 해당 상품에 대해서 제품 설명 작성해줘. 제품 특징은 {color}, {fabric}, {info} 한글로 작성해줘"

            print("입력한 질문 : ", prompt)
            # max_tokens 답변을 받을 수 있는 길이 (낮은 수로 설정해둔다면 말하다 끊김)
            response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=1,
            max_tokens=1589,
            top_p=0.85,
            frequency_penalty=0.85,
            presence_penalty=0.85
            )

            generated_text = response['choices'][0]['message']['content']
            print(generated_text)
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            generated_text = textwrap.fill(generated_text, width=100, replace_whitespace=False)
            #generated_text = '<p>' + generated_text.replace('\n', '</p><p>') + '</p>'
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################
            point = driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            point.click()
            time.sleep(0.5)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(generated_text)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)


            point = driver.find_element(By.XPATH, '//*[@id="SE-d62164ca-5efb-44aa-8639-dcd4cad1cba4"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            point.click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))

            def count_images(folder_path, extensions=['.jpg', '.jpeg', '.png', '.gif']):
                image_count = 0
                for file_name in os.listdir(folder_path):
                    if any(file_name.lower().endswith(ext) for ext in extensions):
                        image_count += 1
                return image_count

            folder_path = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}'
            time.sleep(2)
            image_count = count_images(folder_path)
            print(f">>>>>>>>>> 해당 상품 이미지 {image_count}개 찼았으며 업로드 시작합니다.")

            #상세설명 이미지 대량 첨부
            for i1 in range(2, image_count + 1):
                image_upload.click()
                time.sleep(random.uniform(0.9, 1.2))
                file_name = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a{i1}.jpg'
                driver.find_element(By.XPATH, '/html/body/label/input').send_keys(file_name)
                time.sleep(8)
                html_li.click()
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
                time.sleep(random.uniform(0.9, 1.2))
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
                time.sleep(random.uniform(0.9, 1.2))
                
                
            driver.find_element(By.XPATH, '/html/body/ui-view[1]/ncp-editor-launcher/div[1]/div/button/span[1]/i').click()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)

        # 등록하기
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/div[2]/button[2]/span[1]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/button[2]').click()
            print('등록 완료')  
            time.sleep(4)
############################################################################################################################################################################################################################
        elif templit == '기본 의류':
            print('템플릿 코드 (4) 여성 의류')
            
            point = driver.find_element(By.XPATH, '//*[@id="SE-5c09ffb4-3b6c-4e7a-aa0e-ef06e018b4c9"]/div/div/div/div/span')
            image_upload = driver.find_element(By.CLASS_NAME, 'se-toolbar-label')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-db1e53c7-326a-422a-908d-5983c8fba9b6"]').click()
            time.sleep(1)
            image_upload.click()
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/label/input').send_keys(f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a1.jpg')
            time.sleep(3)
            html_li = driver.find_element(By.CSS_SELECTOR, 'button.se-shopping-html-toolbar-button')
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-5c09ffb4-3b6c-4e7a-aa0e-ef06e018b4c9"]/div/div/div/div/span').click()
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(brand)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(title)
            time.sleep(2)
            try:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/button').click()
            except:
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-9a282220-45b6-4d04-887f-39cc00d885d1"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-9a282220-45b6-4d04-887f-39cc00d885d1"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(made)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="SE-c2977f90-6d46-4c6a-9d1f-5f320fb5fbf9"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(fabric)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)   
            point = driver.find_element(By.XPATH, '//*[@id="SE-3d2658eb-629e-4188-ae4c-01dfc48ac63e"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-3d2658eb-629e-4188-ae4c-01dfc48ac63e"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-582552b3-f5f7-46ea-acf1-5639bf405ef2"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-582552b3-f5f7-46ea-acf1-5639bf405ef2"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(sizet)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-90bccff5-fe79-49e7-a30b-5e8698b1bae9"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-90bccff5-fe79-49e7-a30b-5e8698b1bae9"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(model_tip)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span')
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", point)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span').click()
            time.sleep(1)
            #
            #
            #
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            #
            #
            prompt = (title)
            prompt += f" 해당 상품에 대해서 제품 설명 작성해줘. 제품 특징은 {color}, {fabric}, {info} 한글로 작성해줘"

            print("입력한 질문 : ", prompt)
            # max_tokens 답변을 받을 수 있는 길이 (낮은 수로 설정해둔다면 말하다 끊김)
            response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=1,
            max_tokens=1589,
            top_p=0.85,
            frequency_penalty=0.85,
            presence_penalty=0.85
            )
            
            generated_text = response['choices'][0]['message']['content']
            print(generated_text)
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            generated_text = textwrap.fill(generated_text, width=100, replace_whitespace=False)
            #generated_text = '<p>' + generated_text.replace('\n', '</p><p>') + '</p>'
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            time.sleep(1)

            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(generated_text)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            
    #############
    #############
    #############

            point = driver.find_element(By.XPATH, '//*[@id="SE-d62164ca-5efb-44aa-8639-dcd4cad1cba4"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            point.click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))
            
            def count_images(folder_path, extensions=['.jpg', '.jpeg', '.png', '.gif']):
                image_count = 0
                for file_name in os.listdir(folder_path):
                    if any(file_name.lower().endswith(ext) for ext in extensions):
                        image_count += 1
                return image_count

            folder_path = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}'
            time.sleep(2)
            image_count = count_images(folder_path)
            print(f">>>>>>>>>> 해당 상품 이미지 {image_count}개 찼았으며 업로드 시작합니다.")

            #상세설명 이미지 대량 첨부
            for i1 in range(2, image_count + 1):
                image_upload.click()
                time.sleep(random.uniform(0.9, 1.2))
                file_name = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a{i1}.jpg'
                driver.find_element(By.XPATH, '/html/body/label/input').send_keys(file_name)
                time.sleep(8)
                html_li.click()
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
                time.sleep(random.uniform(0.9, 1.2))
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
                time.sleep(random.uniform(0.9, 1.2))
                
                
            driver.find_element(By.XPATH, '/html/body/ui-view[1]/ncp-editor-launcher/div[1]/div/button/span[1]/i').click()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)

        # 등록하기
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/div[2]/button[2]/span[1]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/button[2]').click()
            print('등록 완료')  
            time.sleep(4)  
############################################################################################################################################################################################################################
        elif templit == '멘즈샵 잡화':
            print('템플릿 코드 (5) >> 남성 잡화')
            
            image_upload = driver.find_element(By.CLASS_NAME, 'se-toolbar-label')
            time.sleep(1)
            html_li = driver.find_element(By.CSS_SELECTOR, 'button.se-shopping-html-toolbar-button')
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(brand)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(title)
            time.sleep(2)
            try:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/button').click()
            except:
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-9a282220-45b6-4d04-887f-39cc00d885d1"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-9a282220-45b6-4d04-887f-39cc00d885d1"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(made)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-c2977f90-6d46-4c6a-9d1f-5f320fb5fbf9"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-c2977f90-6d46-4c6a-9d1f-5f320fb5fbf9"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(fabric)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2) 
            point = driver.find_element(By.XPATH, '//*[@id="SE-3d2658eb-629e-4188-ae4c-01dfc48ac63e"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-3d2658eb-629e-4188-ae4c-01dfc48ac63e"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-582552b3-f5f7-46ea-acf1-5639bf405ef2"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-582552b3-f5f7-46ea-acf1-5639bf405ef2"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(sizet)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-90bccff5-fe79-49e7-a30b-5e8698b1bae9"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-90bccff5-fe79-49e7-a30b-5e8698b1bae9"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(model_tip)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-d66d69db-3011-4b3c-88cb-1dead2b96800"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-d66d69db-3011-4b3c-88cb-1dead2b96800"]/div/div/div/div/span').click()
            time.sleep(1)
            image_upload.click()
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/label/input').send_keys(f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a1.jpg')
            time.sleep(2)
            
            point = driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span').click()
            #
            #
            #
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            #
            #
            prompt = (title)
            prompt += f" 해당 상품에 대해서 제품 설명 작성해줘. 제품 특징은 {color}, {fabric}, {info} 한글로 작성해줘"

            print("입력한 질문 : ", prompt)
            # max_tokens 답변을 받을 수 있는 길이 (낮은 수로 설정해둔다면 말하다 끊김)
            response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=1,
            max_tokens=1589,
            top_p=0.85,
            frequency_penalty=0.85,
            presence_penalty=0.85
            )

            generated_text = response['choices'][0]['message']['content']
            print(generated_text)
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            generated_text = textwrap.fill(generated_text, width=100, replace_whitespace=False)
            #generated_text = '<p>' + generated_text.replace('\n', '</p><p>') + '</p>'
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            time.sleep(1)

            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(generated_text)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)


            point = driver.find_element(By.XPATH, '//*[@id="SE-d62164ca-5efb-44aa-8639-dcd4cad1cba4"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            point.click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))

            def count_images(folder_path, extensions=['.jpg', '.jpeg', '.png', '.gif']):
                image_count = 0
                for file_name in os.listdir(folder_path):
                    if any(file_name.lower().endswith(ext) for ext in extensions):
                        image_count += 1
                return image_count

            folder_path = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}'
            time.sleep(2)
            image_count = count_images(folder_path)
            print(f">>>>>>>>>> 해당 상품 이미지 {image_count}개 찼았으며 업로드 시작합니다.")

            #상세설명 이미지 대량 첨부
            for i1 in range(2, image_count + 1):
                image_upload.click()
                time.sleep(random.uniform(0.9, 1.2))
                file_name = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a{i1}.jpg'
                driver.find_element(By.XPATH, '/html/body/label/input').send_keys(file_name)
                time.sleep(8)
                html_li.click()
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
                time.sleep(random.uniform(0.9, 1.2))
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
                time.sleep(random.uniform(0.9, 1.2))
                
                
            driver.find_element(By.XPATH, '/html/body/ui-view[1]/ncp-editor-launcher/div[1]/div/button/span[1]/i').click()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)

        # 등록하기
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/div[2]/button[2]/span[1]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/button[2]').click()
            print('등록 완료')  
            time.sleep(4)
############################################################################################################################################################################################################################    
        elif templit == '기본 잡화':
            print(' 템플릿 코드 (6) 여성 잡화')
            
            point = driver.find_element(By.XPATH, '//*[@id="SE-5c09ffb4-3b6c-4e7a-aa0e-ef06e018b4c9"]/div/div/div/div/span')
            image_upload = driver.find_element(By.CLASS_NAME, 'se-toolbar-label')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-db1e53c7-326a-422a-908d-5983c8fba9b6"]').click()
            time.sleep(1)
            image_upload.click()
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/label/input').send_keys(f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a1.jpg')
            time.sleep(3)
            html_li = driver.find_element(By.CSS_SELECTOR, 'button.se-shopping-html-toolbar-button')
            time.sleep(2)
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-5c09ffb4-3b6c-4e7a-aa0e-ef06e018b4c9"]/div/div/div/div/span').click()
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(brand)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(title)
            time.sleep(1)

            try:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/button').click()
            except:
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()

            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-9a282220-45b6-4d04-887f-39cc00d885d1"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-9a282220-45b6-4d04-887f-39cc00d885d1"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(made)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="SE-2480888d-113e-4be8-b035-649aab6f87cb"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(fabric)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)    
            point = driver.find_element(By.XPATH, '//*[@id="SE-484c0ab9-7663-4130-bf20-7ba2ba985b59"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-484c0ab9-7663-4130-bf20-7ba2ba985b59"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-345869b4-8d8f-4ba1-bf7f-e65b4b8024dd"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-345869b4-8d8f-4ba1-bf7f-e65b4b8024dd"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(sizet)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-12fcf2d1-a3d1-49b1-824a-a877af0ae9b3"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-12fcf2d1-a3d1-49b1-824a-a877af0ae9b3"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(model_tip)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span')
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", point)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span').click()
            time.sleep(1)
            #
            #
            #
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            #
            #
            prompt = (title)
            prompt += f" 해당 상품 제품 설명 작성해줘. 제품 특징은 {title}, {info} 한글로 작성해줘 :)"

            print("입력한 질문 : ", prompt)
            # max_tokens 답변을 받을 수 있는 길이 (낮은 수로 설정해둔다면 말하다 끊김)
            response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=1,
            max_tokens=1589,
            top_p=0.85,
            frequency_penalty=0.85,
            presence_penalty=0.85
            )

            generated_text = response['choices'][0]['message']['content']
            print(generated_text)
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            generated_text = textwrap.fill(generated_text, width=100, replace_whitespace=False)
            #generated_text = '<p>' + generated_text.replace('\n', '</p><p>') + '</p>'
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            time.sleep(1)

            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(generated_text)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            
    #############
    #############
    #############

            point = driver.find_element(By.XPATH, '//*[@id="SE-d62164ca-5efb-44aa-8639-dcd4cad1cba4"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            point.click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)

            def count_images(folder_path, extensions=['.jpg', '.jpeg', '.png', '.gif']):
                image_count = 0
                for file_name in os.listdir(folder_path):
                    if any(file_name.lower().endswith(ext) for ext in extensions):
                        image_count += 1
                return image_count

            folder_path = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}'
            time.sleep(2)
            image_count = count_images(folder_path)
            print(f">>>>>>>>>> 해당 상품 이미지 {image_count}개 찼았으며 업로드 시작합니다.")

            #상세설명 이미지 대량 첨부
            for i1 in range(2, image_count + 1):
                image_upload.click()
                time.sleep(random.uniform(0.9, 1.2))
                file_name = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a{i1}.jpg'
                driver.find_element(By.XPATH, '/html/body/label/input').send_keys(file_name)
                time.sleep(8)
                html_li.click()
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
                time.sleep(random.uniform(0.9, 1.2))
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
                time.sleep(random.uniform(0.9, 1.2))
                
                
            driver.find_element(By.XPATH, '/html/body/ui-view[1]/ncp-editor-launcher/div[1]/div/button/span[1]/i').click()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)
         
        # 등록하기
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/div[2]/button[2]/span[1]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/button[2]').click()
            print('등록 완료')  
            time.sleep(4)  
############################################################################################################################################################################################################################
        elif templit == '멘즈 NEW 신발':
            print('템플릿 코드 (7) 남성 NEW 신발')
            
            point = driver.find_element(By.XPATH, '//*[@id="SE-5c09ffb4-3b6c-4e7a-aa0e-ef06e018b4c9"]/div/div/div/div/span')
            image_upload = driver.find_element(By.CLASS_NAME, 'se-toolbar-label')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-db1e53c7-326a-422a-908d-5983c8fba9b6"]').click()
            time.sleep(1)
            image_upload.click()
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/label/input').send_keys(f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a1.jpg')
            time.sleep(3)
            html_li = driver.find_element(By.CSS_SELECTOR, 'button.se-shopping-html-toolbar-button')
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-5c09ffb4-3b6c-4e7a-aa0e-ef06e018b4c9"]/div/div/div/div/span').click()
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(brand)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(title)
            time.sleep(2)
            
            try:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/button').click()
            except:
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
                
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-b8c12a54-6a18-4da6-b509-77fe2ff37cf5"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-b8c12a54-6a18-4da6-b509-77fe2ff37cf5"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(made)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))
            driver.find_element(By.XPATH, '//*[@id="SE-2480888d-113e-4be8-b035-649aab6f87cb"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(fabric)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)  
            point = driver.find_element(By.XPATH, '//*[@id="SE-484c0ab9-7663-4130-bf20-7ba2ba985b59"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-484c0ab9-7663-4130-bf20-7ba2ba985b59"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-669c8989-e916-4a93-9fe2-77e9935b5c77"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-669c8989-e916-4a93-9fe2-77e9935b5c77"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(sizet)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-90bccff5-fe79-49e7-a30b-5e8698b1bae9"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-90bccff5-fe79-49e7-a30b-5e8698b1bae9"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(model_tip)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span')
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", point)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span').click()
            time.sleep(1)
            #
            #
            #
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            #
            #
            prompt = (title)
            prompt += f" 해당 상품에 대해서 제품 설명 작성해줘. 제품 특징은 {color}, {fabric}, {info} 한글로 작성해줘"

            print("입력한 질문 : ", prompt)
            # max_tokens 답변을 받을 수 있는 길이 (낮은 수로 설정해둔다면 말하다 끊김)
            response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=1,
            max_tokens=1589,
            top_p=0.85,
            frequency_penalty=0.85,
            presence_penalty=0.85
            )

            generated_text = response['choices'][0]['message']['content']
            print(generated_text)
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            generated_text = textwrap.fill(generated_text, width=100, replace_whitespace=False)
            #generated_text = '<p>' + generated_text.replace('\n', '</p><p>') + '</p>'
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            time.sleep(1)

            html_li.click()
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(generated_text)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            
    #############
    #############
    #############

            point = driver.find_element(By.XPATH, '//*[@id="SE-d62164ca-5efb-44aa-8639-dcd4cad1cba4"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            point.click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))

            def count_images(folder_path, extensions=['.jpg', '.jpeg', '.png', '.gif']):
                image_count = 0
                for file_name in os.listdir(folder_path):
                    if any(file_name.lower().endswith(ext) for ext in extensions):
                        image_count += 1
                return image_count

            folder_path = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}'
            time.sleep(2)
            image_count = count_images(folder_path)
            print(f">>>>>>>>>> 해당 상품 이미지 {image_count}개 찼았으며 업로드 시작합니다.")

            #상세설명 이미지 대량 첨부
            for i1 in range(2, image_count + 1):
                image_upload.click()
                time.sleep(random.uniform(0.9, 1.2))
                file_name = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a{i1}.jpg'
                driver.find_element(By.XPATH, '/html/body/label/input').send_keys(file_name)
                time.sleep(8)
                html_li.click()
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
                time.sleep(random.uniform(0.9, 1.2))
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
                time.sleep(random.uniform(0.9, 1.2))
                
                

            time.sleep(1)

            '''recommend = driver.find_element(By.CSS_SELECTOR, '#SE-fcf481f5-6ea7-4e81-80b7-88357d22ea8d')
            driver.execute_script("arguments[0].scrollIntoView();", recommend)


            driver.execute_script("window.open('about:blank', 'second_tab');")
            driver.switch_to.window("second_tab")
            time.sleep(1)
            driver.get('https://shopping.naver.com/foreign/stores/100344199')
            time.sleep(3)
            driver.execute_script("window.scrollBy(0, 700);")
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(2)
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(2)
            driver.execute_script("window.scrollBy(0, 700);")
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(2)
            
            elements1 = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "._3FUicfNemK")))

            if len(elements1) >= 5:
                random_elements = random.sample(elements1, 5)
            else:
                random_elements = elements
                

        #### 해외직구 추천상품 링크복사 ########
            # 무작위로 선택된 요소들의 링크를 저장할 빈 리스트 생성
            links = []

            # 무작위로 선택된 요소들을 하나씩 링크 복사
            for element in random_elements:
                # 각 요소에서 링크를 추출
                link = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
                # 링크를 리스트에 추가
                links.append(link)
                time.sleep(1)

            # 링크 출력
            print(links)

            driver.switch_to.window(driver.window_handles[1])
            time.sleep(5)

            # 에디터를 찾아서 element 변수에 저장
            editor = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#SE-fcf481f5-6ea7-4e81-80b7-88357d22ea8d > div > div.se-drop-indicator > div')))

            # 에디터에 포커스
            editor.click()
            
            link_up = driver.find_element(By.CSS_SELECTOR, 'button.se-oglink-toolbar-button')
            # 저장된 링크를 하나씩 특정 위치에 붙여넣기
            for link in links:
                # 링크를 클립보드에 복사
                pyperclip.copy(link)
                time.sleep(1)
                link_up.click()
                time.sleep(12)
                driver.find_element(By.XPATH, '/html/body/ui-view/ncp-editor-launcher/div/div/div/div/div/div/div/button').click()
                time.sleep(1)
                
            if len(driver.window_handles) >= 3:
                driver.switch_to.window(driver.window_handles[2])
                driver.close()
                time.sleep(1)
            
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(1)'''
            driver.find_element(By.XPATH, '/html/body/ui-view[1]/ncp-editor-launcher/div[1]/div/button/span[1]/i').click()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)

        # 등록하기
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/div[2]/button[2]/span[1]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/button[2]').click()
            print('등록 완료')  
            time.sleep(4)  
##############################
        elif templit == '멘즈 NEW 의류':
            print('템플릿 코드 (8) 멘즈샵 신상 의류')
            
            point = driver.find_element(By.XPATH, '//*[@id="SE-5c09ffb4-3b6c-4e7a-aa0e-ef06e018b4c9"]/div/div/div/div/span')
            image_upload = driver.find_element(By.CLASS_NAME, 'se-toolbar-label')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-db1e53c7-326a-422a-908d-5983c8fba9b6"]').click()
            time.sleep(1)
            image_upload.click()
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/label/input').send_keys(f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a1.jpg')
            time.sleep(3)
            html_li = driver.find_element(By.CSS_SELECTOR, 'button.se-shopping-html-toolbar-button')
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-5c09ffb4-3b6c-4e7a-aa0e-ef06e018b4c9"]/div/div/div/div/span').click()
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(brand)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(title)
            time.sleep(2)
            try:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/button').click()
            except:
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-9a282220-45b6-4d04-887f-39cc00d885d1"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-9a282220-45b6-4d04-887f-39cc00d885d1"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(made)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))
            driver.find_element(By.XPATH, '//*[@id="SE-c2977f90-6d46-4c6a-9d1f-5f320fb5fbf9"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(fabric)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)   
            point = driver.find_element(By.XPATH, '//*[@id="SE-3d2658eb-629e-4188-ae4c-01dfc48ac63e"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-3d2658eb-629e-4188-ae4c-01dfc48ac63e"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-582552b3-f5f7-46ea-acf1-5639bf405ef2"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-582552b3-f5f7-46ea-acf1-5639bf405ef2"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(sizet)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-90bccff5-fe79-49e7-a30b-5e8698b1bae9"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-90bccff5-fe79-49e7-a30b-5e8698b1bae9"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(model_tip)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span')
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", point)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span').click()
            time.sleep(1)
            #
            #
            #
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            #
            #
            prompt = (title)
            prompt += f" 해당 상품에 대해서 제품 설명 작성해줘. 제품 특징은 {color}, {fabric}, {info} 한글로 작성해줘"

            print("입력한 질문 : ", prompt)
            # max_tokens 답변을 받을 수 있는 길이 (낮은 수로 설정해둔다면 말하다 끊김)
            response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=1,
            max_tokens=1589,
            top_p=0.85,
            frequency_penalty=0.85,
            presence_penalty=0.85
            )
            
            generated_text = response['choices'][0]['message']['content']
            print(generated_text)
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            generated_text = textwrap.fill(generated_text, width=100, replace_whitespace=False)
            #generated_text = '<p>' + generated_text.replace('\n', '</p><p>') + '</p>'
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            time.sleep(1)

            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(generated_text)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            
    #############
    #############
    #############

            point = driver.find_element(By.XPATH, '//*[@id="SE-d62164ca-5efb-44aa-8639-dcd4cad1cba4"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            point.click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))
            
            def count_images(folder_path, extensions=['.jpg', '.jpeg', '.png', '.gif']):
                image_count = 0
                for file_name in os.listdir(folder_path):
                    if any(file_name.lower().endswith(ext) for ext in extensions):
                        image_count += 1
                return image_count

            folder_path = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}'
            time.sleep(2)
            image_count = count_images(folder_path)
            print(f">>>>>>>>>> 해당 상품 이미지 {image_count}개 찼았으며 업로드 시작합니다.")

            #상세설명 이미지 대량 첨부
            for i1 in range(2, image_count + 1):
                image_upload.click()
                time.sleep(random.uniform(0.9, 1.2))
                file_name = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a{i1}.jpg'
                driver.find_element(By.XPATH, '/html/body/label/input').send_keys(file_name)
                time.sleep(8)
                html_li.click()
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
                time.sleep(random.uniform(0.9, 1.2))
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
                time.sleep(random.uniform(0.9, 1.2))
                
                
            driver.find_element(By.XPATH, '/html/body/ui-view[1]/ncp-editor-launcher/div[1]/div/button/span[1]/i').click()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)

        # 등록하기
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/div[2]/button[2]/span[1]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/button[2]').click()
            print('등록 완료')  
            time.sleep(4)  
##############################

        elif templit == '멘즈 NEW 잡화':
            print(' 템플릿 코드 (9) 멘즈샵 NEW 잡화')
            
            point = driver.find_element(By.XPATH, '//*[@id="SE-5c09ffb4-3b6c-4e7a-aa0e-ef06e018b4c9"]/div/div/div/div/span')
            image_upload = driver.find_element(By.CLASS_NAME, 'se-toolbar-label')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-db1e53c7-326a-422a-908d-5983c8fba9b6"]').click()
            time.sleep(1)
            image_upload.click()
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/label/input').send_keys(f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a1.jpg')
            time.sleep(3)
            html_li = driver.find_element(By.CSS_SELECTOR, 'button.se-shopping-html-toolbar-button')
            time.sleep(2)
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-5c09ffb4-3b6c-4e7a-aa0e-ef06e018b4c9"]/div/div/div/div/span').click()
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(brand)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(title)
            time.sleep(1)

            try:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/button').click()
            except:
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()

            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-9a282220-45b6-4d04-887f-39cc00d885d1"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-9a282220-45b6-4d04-887f-39cc00d885d1"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(made)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="SE-2480888d-113e-4be8-b035-649aab6f87cb"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(fabric)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)    
            point = driver.find_element(By.XPATH, '//*[@id="SE-484c0ab9-7663-4130-bf20-7ba2ba985b59"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-484c0ab9-7663-4130-bf20-7ba2ba985b59"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-345869b4-8d8f-4ba1-bf7f-e65b4b8024dd"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-345869b4-8d8f-4ba1-bf7f-e65b4b8024dd"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(sizet)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-12fcf2d1-a3d1-49b1-824a-a877af0ae9b3"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-12fcf2d1-a3d1-49b1-824a-a877af0ae9b3"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(model_tip)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span')
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", point)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span').click()
            time.sleep(1)
            #
            #
            #
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            #
            #
            prompt = (title)
            prompt += f" 해당 상품 제품 설명 작성해줘. 제품 특징은 {title}, {info} 한글로 작성해줘 :)"

            print("입력한 질문 : ", prompt)
            # max_tokens 답변을 받을 수 있는 길이 (낮은 수로 설정해둔다면 말하다 끊김)
            response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=1,
            max_tokens=1589,
            top_p=0.85,
            frequency_penalty=0.85,
            presence_penalty=0.85
            )

            generated_text = response['choices'][0]['message']['content']
            print(generated_text)
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            generated_text = textwrap.fill(generated_text, width=100, replace_whitespace=False)
            #generated_text = '<p>' + generated_text.replace('\n', '</p><p>') + '</p>'
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            time.sleep(1)

            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(generated_text)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            
    #############
    #############
    #############

            point = driver.find_element(By.XPATH, '//*[@id="SE-d62164ca-5efb-44aa-8639-dcd4cad1cba4"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            point.click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)

            def count_images(folder_path, extensions=['.jpg', '.jpeg', '.png', '.gif']):
                image_count = 0
                for file_name in os.listdir(folder_path):
                    if any(file_name.lower().endswith(ext) for ext in extensions):
                        image_count += 1
                return image_count

            folder_path = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}'
            time.sleep(2)
            image_count = count_images(folder_path)
            print(f">>>>>>>>>> 해당 상품 이미지 {image_count}개 찼았으며 업로드 시작합니다.")

            #상세설명 이미지 대량 첨부
            for i1 in range(2, image_count + 1):
                image_upload.click()
                time.sleep(random.uniform(0.9, 1.2))
                file_name = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a{i1}.jpg'
                driver.find_element(By.XPATH, '/html/body/label/input').send_keys(file_name)
                time.sleep(8)
                html_li.click()
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
                time.sleep(random.uniform(0.9, 1.2))
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
                time.sleep(random.uniform(0.9, 1.2))
                
                
            driver.find_element(By.XPATH, '/html/body/ui-view[1]/ncp-editor-launcher/div[1]/div/button/span[1]/i').click()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)
         
        # 등록하기
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/div[2]/button[2]/span[1]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/button[2]').click()
            print('등록 완료')  
            time.sleep(4)  
##############################
        elif templit == '기본 NEW 신발':
            print('템플릿 코드 (10) 여성 NEW 신발')
            
            point = driver.find_element(By.XPATH, '//*[@id="SE-5c09ffb4-3b6c-4e7a-aa0e-ef06e018b4c9"]/div/div/div/div/span')
            image_upload = driver.find_element(By.CLASS_NAME, 'se-toolbar-label')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-db1e53c7-326a-422a-908d-5983c8fba9b6"]').click()
            time.sleep(1)
            image_upload.click()
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/label/input').send_keys(f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a1.jpg')
            time.sleep(3)
            html_li = driver.find_element(By.CSS_SELECTOR, 'button.se-shopping-html-toolbar-button')
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-5c09ffb4-3b6c-4e7a-aa0e-ef06e018b4c9"]/div/div/div/div/span').click()
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(brand)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(title)
            time.sleep(2)
            
            try:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/button').click()
            except:
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
                
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-b8c12a54-6a18-4da6-b509-77fe2ff37cf5"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-b8c12a54-6a18-4da6-b509-77fe2ff37cf5"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(made)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="SE-2480888d-113e-4be8-b035-649aab6f87cb"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(fabric)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)  
            point = driver.find_element(By.XPATH, '//*[@id="SE-484c0ab9-7663-4130-bf20-7ba2ba985b59"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-484c0ab9-7663-4130-bf20-7ba2ba985b59"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-669c8989-e916-4a93-9fe2-77e9935b5c77"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-669c8989-e916-4a93-9fe2-77e9935b5c77"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(sizet)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-90bccff5-fe79-49e7-a30b-5e8698b1bae9"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-90bccff5-fe79-49e7-a30b-5e8698b1bae9"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(model_tip)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span')
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", point)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span').click()
            time.sleep(1)
            #
            #
            #
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            #
            #
            prompt = (title)
            prompt += f" 해당 상품에 대해서 제품 설명 작성해줘. 제품 특징은 {color}, {fabric}, {info} 한글로 작성해줘"

            print("입력한 질문 : ", prompt)
            # max_tokens 답변을 받을 수 있는 길이 (낮은 수로 설정해둔다면 말하다 끊김)
            response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=1,
            max_tokens=1589,
            top_p=0.85,
            frequency_penalty=0.85,
            presence_penalty=0.85
            )

            generated_text = response['choices'][0]['message']['content']
            print(generated_text)
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            generated_text = textwrap.fill(generated_text, width=100, replace_whitespace=False)
            #generated_text = '<p>' + generated_text.replace('\n', '</p><p>') + '</p>'
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            time.sleep(1)

            html_li.click()
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(generated_text)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            
    #############
    #############
    #############

            point = driver.find_element(By.XPATH, '//*[@id="SE-d62164ca-5efb-44aa-8639-dcd4cad1cba4"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            point.click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))

            def count_images(folder_path, extensions=['.jpg', '.jpeg', '.png', '.gif']):
                image_count = 0
                for file_name in os.listdir(folder_path):
                    if any(file_name.lower().endswith(ext) for ext in extensions):
                        image_count += 1
                return image_count

            folder_path = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}'
            time.sleep(2)
            image_count = count_images(folder_path)
            print(f">>>>>>>>>> 해당 상품 이미지 {image_count}개 찼았으며 업로드 시작합니다.")

            #상세설명 이미지 대량 첨부
            for i1 in range(2, image_count + 1):
                image_upload.click()
                time.sleep(random.uniform(0.9, 1.2))
                file_name = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a{i1}.jpg'
                driver.find_element(By.XPATH, '/html/body/label/input').send_keys(file_name)
                time.sleep(8)
                html_li.click()
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
                time.sleep(random.uniform(0.9, 1.2))
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
                time.sleep(random.uniform(0.9, 1.2))
                
                

            time.sleep(1)

            '''recommend = driver.find_element(By.CSS_SELECTOR, '#SE-fcf481f5-6ea7-4e81-80b7-88357d22ea8d')
            driver.execute_script("arguments[0].scrollIntoView();", recommend)


            driver.execute_script("window.open('about:blank', 'second_tab');")
            driver.switch_to.window("second_tab")
            time.sleep(1)
            driver.get('https://shopping.naver.com/foreign/stores/100344199')
            time.sleep(3)
            driver.execute_script("window.scrollBy(0, 700);")
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(2)
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(2)
            driver.execute_script("window.scrollBy(0, 700);")
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(2)
            
            elements1 = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "._3FUicfNemK")))

            if len(elements1) >= 5:
                random_elements = random.sample(elements1, 5)
            else:
                random_elements = elements
                

        #### 해외직구 추천상품 링크복사 ########
            # 무작위로 선택된 요소들의 링크를 저장할 빈 리스트 생성
            links = []

            # 무작위로 선택된 요소들을 하나씩 링크 복사
            for element in random_elements:
                # 각 요소에서 링크를 추출
                link = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
                # 링크를 리스트에 추가
                links.append(link)
                time.sleep(1)

            # 링크 출력
            print(links)

            driver.switch_to.window(driver.window_handles[1])
            time.sleep(5)

            # 에디터를 찾아서 element 변수에 저장
            editor = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#SE-fcf481f5-6ea7-4e81-80b7-88357d22ea8d > div > div.se-drop-indicator > div')))

            # 에디터에 포커스
            editor.click()
            
            link_up = driver.find_element(By.CSS_SELECTOR, 'button.se-oglink-toolbar-button')
            # 저장된 링크를 하나씩 특정 위치에 붙여넣기
            for link in links:
                # 링크를 클립보드에 복사
                pyperclip.copy(link)
                time.sleep(1)
                link_up.click()
                time.sleep(12)
                driver.find_element(By.XPATH, '/html/body/ui-view/ncp-editor-launcher/div/div/div/div/div/div/div/button').click()
                time.sleep(1)
                
            if len(driver.window_handles) >= 3:
                driver.switch_to.window(driver.window_handles[2])
                driver.close()
                time.sleep(1)
            
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(1)'''
            driver.find_element(By.XPATH, '/html/body/ui-view[1]/ncp-editor-launcher/div[1]/div/button/span[1]/i').click()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)

        # 등록하기
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/div[2]/button[2]/span[1]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/button[2]').click()
            print('등록 완료')  
            time.sleep(4)  
############################
        elif templit == '기본 NEW 의류':
            print('템플릿 코드 (11) 여성 NEW 의류')
            
            point = driver.find_element(By.XPATH, '//*[@id="SE-5c09ffb4-3b6c-4e7a-aa0e-ef06e018b4c9"]/div/div/div/div/span')
            image_upload = driver.find_element(By.CLASS_NAME, 'se-toolbar-label')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-db1e53c7-326a-422a-908d-5983c8fba9b6"]').click()
            time.sleep(1)
            image_upload.click()
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/label/input').send_keys(f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a1.jpg')
            time.sleep(3)
            html_li = driver.find_element(By.CSS_SELECTOR, 'button.se-shopping-html-toolbar-button')
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-5c09ffb4-3b6c-4e7a-aa0e-ef06e018b4c9"]/div/div/div/div/span').click()
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(brand)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(title)
            time.sleep(2)
            try:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/button').click()
            except:
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-9a282220-45b6-4d04-887f-39cc00d885d1"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-9a282220-45b6-4d04-887f-39cc00d885d1"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(made)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="SE-c2977f90-6d46-4c6a-9d1f-5f320fb5fbf9"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(fabric)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)   
            point = driver.find_element(By.XPATH, '//*[@id="SE-3d2658eb-629e-4188-ae4c-01dfc48ac63e"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-3d2658eb-629e-4188-ae4c-01dfc48ac63e"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-582552b3-f5f7-46ea-acf1-5639bf405ef2"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-582552b3-f5f7-46ea-acf1-5639bf405ef2"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(sizet)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-90bccff5-fe79-49e7-a30b-5e8698b1bae9"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-90bccff5-fe79-49e7-a30b-5e8698b1bae9"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(model_tip)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span')
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", point)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span').click()
            time.sleep(1)
            #
            #
            #
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            #
            #
            prompt = (title)
            prompt += f" 해당 상품에 대해서 제품 설명 작성해줘. 제품 특징은 {color}, {fabric}, {info} 한글로 작성해줘"

            print("입력한 질문 : ", prompt)
            # max_tokens 답변을 받을 수 있는 길이 (낮은 수로 설정해둔다면 말하다 끊김)
            response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=1,
            max_tokens=1589,
            top_p=0.85,
            frequency_penalty=0.85,
            presence_penalty=0.85
            )
            
            generated_text = response['choices'][0]['message']['content']
            print(generated_text)
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            generated_text = textwrap.fill(generated_text, width=100, replace_whitespace=False)
            #generated_text = '<p>' + generated_text.replace('\n', '</p><p>') + '</p>'
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            time.sleep(1)

            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(generated_text)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            
    #############
    #############
    #############

            point = driver.find_element(By.XPATH, '//*[@id="SE-d62164ca-5efb-44aa-8639-dcd4cad1cba4"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            point.click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))
            
            def count_images(folder_path, extensions=['.jpg', '.jpeg', '.png', '.gif']):
                image_count = 0
                for file_name in os.listdir(folder_path):
                    if any(file_name.lower().endswith(ext) for ext in extensions):
                        image_count += 1
                return image_count

            folder_path = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}'
            time.sleep(2)
            image_count = count_images(folder_path)
            print(f">>>>>>>>>> 해당 상품 이미지 {image_count}개 찼았으며 업로드 시작합니다.")

            #상세설명 이미지 대량 첨부
            for i1 in range(2, image_count + 1):
                image_upload.click()
                time.sleep(random.uniform(0.9, 1.2))
                file_name = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a{i1}.jpg'
                driver.find_element(By.XPATH, '/html/body/label/input').send_keys(file_name)
                time.sleep(8)
                html_li.click()
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
                time.sleep(random.uniform(0.9, 1.2))
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
                time.sleep(random.uniform(0.9, 1.2))
                
                
            driver.find_element(By.XPATH, '/html/body/ui-view[1]/ncp-editor-launcher/div[1]/div/button/span[1]/i').click()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)

        # 등록하기
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/div[2]/button[2]/span[1]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/button[2]').click()
            print('등록 완료')  
            time.sleep(4)  
#########################
        elif templit == '기본 NEW 잡화':
            print(' 템플릿 코드 (12) 여성 NEW 잡화')
            
            point = driver.find_element(By.XPATH, '//*[@id="SE-5c09ffb4-3b6c-4e7a-aa0e-ef06e018b4c9"]/div/div/div/div/span')
            image_upload = driver.find_element(By.CLASS_NAME, 'se-toolbar-label')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-db1e53c7-326a-422a-908d-5983c8fba9b6"]').click()
            time.sleep(1)
            image_upload.click()
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/label/input').send_keys(f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a1.jpg')
            time.sleep(3)
            html_li = driver.find_element(By.CSS_SELECTOR, 'button.se-shopping-html-toolbar-button')
            time.sleep(2)
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-5c09ffb4-3b6c-4e7a-aa0e-ef06e018b4c9"]/div/div/div/div/span').click()
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(brand)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(title)
            time.sleep(1)

            try:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/button').click()
            except:
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()

            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-9a282220-45b6-4d04-887f-39cc00d885d1"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-9a282220-45b6-4d04-887f-39cc00d885d1"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(made)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="SE-2480888d-113e-4be8-b035-649aab6f87cb"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(fabric)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)    
            point = driver.find_element(By.XPATH, '//*[@id="SE-484c0ab9-7663-4130-bf20-7ba2ba985b59"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-484c0ab9-7663-4130-bf20-7ba2ba985b59"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(random.uniform(1, 1.2))
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-345869b4-8d8f-4ba1-bf7f-e65b4b8024dd"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-345869b4-8d8f-4ba1-bf7f-e65b4b8024dd"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(sizet)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-12fcf2d1-a3d1-49b1-824a-a877af0ae9b3"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            driver.find_element(By.XPATH, '//*[@id="SE-12fcf2d1-a3d1-49b1-824a-a877af0ae9b3"]/div/div/div/div/span').click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(model_tip)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            point = driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span')
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView();", point)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="SE-9f9fe7d6-6dc0-4448-af3a-c354572b18a2"]/div/div/div/div/span').click()
            time.sleep(1)
            #
            #
            #
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            # GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT GPT 
            #
            #
            prompt = (title)
            prompt += f" 해당 상품 제품 설명 작성해줘. 제품 특징은 {title}, {info} 한글로 작성해줘 :)"

            print("입력한 질문 : ", prompt)
            # max_tokens 답변을 받을 수 있는 길이 (낮은 수로 설정해둔다면 말하다 끊김)
            response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=1,
            max_tokens=1589,
            top_p=0.85,
            frequency_penalty=0.85,
            presence_penalty=0.85
            )

            generated_text = response['choices'][0]['message']['content']
            print(generated_text)
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            generated_text = textwrap.fill(generated_text, width=100, replace_whitespace=False)
            #generated_text = '<p>' + generated_text.replace('\n', '</p><p>') + '</p>'
            
        ###########################################################################################################################################################
        ###########################################################################################################################################################

            time.sleep(1)

            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(generated_text)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)
            
    #############
    #############
    #############

            point = driver.find_element(By.XPATH, '//*[@id="SE-d62164ca-5efb-44aa-8639-dcd4cad1cba4"]/div/div/div/div/span')
            driver.execute_script("arguments[0].scrollIntoView();", point)
            point.click()
            time.sleep(1)
            html_li.click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys(color)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
            time.sleep(2)

            def count_images(folder_path, extensions=['.jpg', '.jpeg', '.png', '.gif']):
                image_count = 0
                for file_name in os.listdir(folder_path):
                    if any(file_name.lower().endswith(ext) for ext in extensions):
                        image_count += 1
                return image_count

            folder_path = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}'
            time.sleep(2)
            image_count = count_images(folder_path)
            print(f">>>>>>>>>> 해당 상품 이미지 {image_count}개 찼았으며 업로드 시작합니다.")

            #상세설명 이미지 대량 첨부
            for i1 in range(2, image_count + 1):
                image_upload.click()
                time.sleep(random.uniform(0.9, 1.2))
                file_name = f'C:/Users/ape0x/Desktop/상품등록봇/등록/a{i}/a{i1}.jpg'
                driver.find_element(By.XPATH, '/html/body/label/input').send_keys(file_name)
                time.sleep(8)
                html_li.click()
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("<br><br>")
                time.sleep(random.uniform(0.9, 1.2))
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()
                time.sleep(random.uniform(0.9, 1.2))
                
                
            driver.find_element(By.XPATH, '/html/body/ui-view[1]/ncp-editor-launcher/div[1]/div/button/span[1]/i').click()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)
         
        # 등록하기
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="seller-content"]/ui-view/div[2]/div[2]/button[2]/span[1]').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/button[2]').click()
            print('등록 완료')  
            time.sleep(4)  
###########################
        else:
            print('템플릿 넘버 에러!! 확인해주세요!!')
        
        ###작업 종료
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################
    ############################################################################################################################################################################################################################

labels = [
    '상품명 : ', '가격 : ', '판상코 : ', '컬러명 : ',
     '컬러 코드 : ', '카테고리', '브랜드', '모델 팁', '소재', '사이즈', '원산지','Location' ,'제품 정보 : '
]

variables = [
    title, price, sku, color, 
     color_a, category_2, brand, model_tip, fabric, sizet, made, ori , info
]

for i, (label, variable) in enumerate(zip(labels, variables)):
    tk.Label(root, text=label).grid(row=i+1, column=0, sticky='E',)
    entry = tk.Entry(root, textvariable=variable)
    entry.grid(row=i+1, column=1)
    
variables1 = [new_price]
entry = tk.Entry(root, textvariable=variables1)
entry.grid(row=2, column=3)

def copy_login_info():
    id_value = entry_id.get()
    pw_value = entry_pw.get()

    login_info = f"ID: {id_value}\nPassword: {pw_value}"
    print(login_info)
    print("로그인 정보가 복사되었습니다.")
    progress_text.insert(tk.END, "로그인 정보를 저장 했습니다. 해당 정보로 로그인 합니다.\n")  

def open_selected_folder():
    selected_folders = folders_listbox.curselection()
    if not selected_folders:
        messagebox.showerror("Error", "폴더를 선택해주세요.")
        return
    
    selected_folder = selected_folders[0]  # 첫 번째 선택된 폴더만 열기
    folder_name = folders_listbox.get(selected_folder)
    folder_path = f"C:/Users/ape0x/Desktop/상품등록봇/등록/{folder_name}"

    if sys.platform == "win32":
        os.startfile(folder_path)
    elif sys.platform == "darwin":
        subprocess.Popen(["open", folder_path])
    else:
        subprocess.Popen(["xdg-open", folder_path])

open_folder_button = tk.Button(root, text="선택한 폴더 열기", command=open_selected_folder)
open_folder_button.grid(row=18, column=1)

# Add "Save Values" button
save_button = tk.Button(root, text="입력한 상품 정보 저장하기", command=save_values)
save_button.grid(row=15, column=1, pady=30)

start_button = tk.Button(root, text="상품등록 START", command=start_product_registration)
start_button.grid(row=15, column=3)

def file_name_reset ():
    selected_folders = folders_listbox.curselection()
    if not selected_folders:
        messagebox.showerror("Error", "폴더를 선택해주세요.")
        return
    
    selected_folder = selected_folders[0]  # 첫 번째 선택된 폴더만 열기
    folder_name = folders_listbox.get(selected_folder)
    dir_path = f"C:/Users/ape0x/Desktop/상품등록봇/등록/{folder_name}"
    file_list = os.listdir(dir_path)

    print(file_list)

    str_name = 'zzz'
    num = 0

    for old_name in file_list :
        index = old_name.find('.')
        # name_front = old_name[:index]
        file_extension = old_name[index:]
        num += 1
        new_name = str_name + str(num) + file_extension
        print(new_name)
        os.rename(dir_path + '/' + old_name, dir_path + '/' + new_name)

    progress_text.insert(tk.END, "파일 이름을 리셋 했습니다. 이름 변경을 실행하세요.\n")

file_name_reset = tk.Button(root, text="파일 이름 리셋", command=file_name_reset)
file_name_reset.grid(row=16, column=0)

def file_name_change ():
    selected_folders = folders_listbox.curselection()
    if not selected_folders:
        messagebox.showerror("Error", "폴더를 선택해주세요.")
        return
    
    selected_folder = selected_folders[0]  # 첫 번째 선택된 폴더만 열기
    folder_name = folders_listbox.get(selected_folder)
    dir_path = f"C:/Users/ape0x/Desktop/상품등록봇/등록/{folder_name}"
    file_list = os.listdir(dir_path)

    print(file_list)

    str_name = 'a'
    num = 0

    for old_name in file_list :
        index = old_name.find('.')
        # name_front = old_name[:index]
        file_extension = old_name[index:]
        num += 1
        new_name = str_name + str(num) + file_extension
        print(new_name)
        os.rename(dir_path + '/' + old_name, dir_path + '/' + new_name)

    progress_text.insert(tk.END, "파일 이름을 작업에 최적화 되도록 변경했습니다.\n")

file_name_change = tk.Button(root, text="파일 이름 변경", command=file_name_change)
file_name_change.grid(row=16, column=1)


def reset ():
    templit.set(0)
    category_2.set("")
    title.set("")
    price.set(0)
    color_a.set(0)
    color.set("")
    sku.set("")
    info.set("")
    brand.set("")
    model_tip.set("")
    fabric.set("")
    sizet.set("")
    made.set("")
    ori.set("")

reset_button = tk.Button(root, text="작업 초기화", command=reset)
reset_button.grid(row=0, column=2)

max_folder_num = find_max_folder_number()

# Add "Select Folders" label and listbox
select_folders_label = tk.Label(root, text="상품 목록")
select_folders_label.grid(row=17, column=0, sticky='E')

# Add folders to listbox with scrollbar
folders_scrollbar = Scrollbar(root)
folders_scrollbar.grid(row=17, column=2, sticky='NS')

folders_listbox = tk.Listbox(root, selectmode=tk.EXTENDED, yscrollcommand=folders_scrollbar.set)
folders_listbox.grid(row=17, column=1)

folders_scrollbar.config(command=folders_listbox.yview)


# Add folders to listbox
for folder_number in range(1, max_folder_num + 1):
    folder_name = f"a{folder_number}"
    folders_listbox.insert(tk.END, folder_name)
    
progress_text = Text(root, wrap=tk.WORD, height=13, width=70)
progress_text.grid(row=17, column=3, columnspan=1, pady=10)

tk.Label(root, text="스마트스토어 아이디 :").grid(row=20, column=3, sticky='W')
entry_id = tk.Entry(root)
entry_id.grid(row=20, column=3)

tk.Label(root, text="스마트스토어 패스워드 :").grid(row=21, column=3, sticky='W')
entry_pw = tk.Entry(root, show="*")
entry_pw.grid(row=21, column=3)

# 복사 버튼
copy_button = tk.Button(root, text="로그인", command=copy_login_info)
copy_button.grid(row=22, column=3, pady=5)

root.rowconfigure(0, minsize=50)
root.rowconfigure(23, minsize=50)
root.columnconfigure(10, minsize=30)


root.mainloop()