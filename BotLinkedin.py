#Importación de librerias

import pandas #Para la lectura de credenciales

import time #Para pausar la ejecución del código

from selenium import webdriver #Para la manipulación de la página

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec

from selenium.common.exceptions import NoSuchElementException

excel_credenciales = r'C:\Users\Dunkan\Desktop\Leo\Facultad\Quinto cuatrimestre\Integración tecnológica\BotLinkedin\acceso.xlsx' #Ruta donde está almacenado el Excel con las credenciales

df = pandas.read_excel(excel_credenciales) #Lectura de las credenciales

#Definición de las variables

user = df['usuario'][0]

psw = df['contraseña'][0]

jobs = df['empleo'][0]

salary = df['sueldo'][0]

url = 'https://www.zonajobs.com.ar/'



# selectores: Aca se les asigna una variable a cada objeto HTML que será manipulado

boton_inicio_sesion = '/html/body/header/div/div/div/nav/div[2]/ul/li[6]/a' #Selecciona el botón "ingresar" para loggearte a la página

selector_usuario = '#username' #imput donde se ingresa el usuario

selector_contraseña = '#password' #input donde se ingresa la contraseña

boton_login = '/html/body/div[5]/div/div/div[3]/div/a' #Boton para ingresar las credenciales

selector_buscador = '/html/body/div[3]/div/div/div/div/div[2]/div/form/div[1]/input' #Input donde buscamos el tipo de empleo deseado 

boton_buscar = '/html/body/div[3]/div/div/div/div/div[2]/div/form/button' #boton para buscar empleo

selector_sueldo = '/html/body/div[4]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[4]/div[1]/div[1]/input' #Input donde ingresamos el sueldo pretendido

boton_postularme = '/html/body/div[4]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[4]/div[2]/a' #Boton para postularse	
			

# Abrir el navegador

driver = webdriver.Chrome()

# Maximizar la ventana y pasarle la página que deseamos abrir

driver.maximize_window()
driver.get(url)

# Iniciar sesión en la página

driver.find_element_by_xpath(boton_inicio_sesion).click()

#Ingresar credenciales 

driver.find_element_by_css_selector(selector_usuario).send_keys(user)
time.sleep(1)
driver.find_element_by_css_selector(selector_contraseña).send_keys(psw)
time.sleep(1)
driver.find_element_by_xpath(boton_login).click()
time.sleep(2)

#Paso el parámetro de búsqueda laboral en el buscador y filtro

driver.find_element_by_xpath(selector_buscador).send_keys(jobs)
time.sleep(1)
driver.find_element_by_xpath(boton_buscar).click()
time.sleep(2)


#Ciclo for para iterar en cada búsqueda laboral

for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
	url1 = driver.current_url

	selector_oferta = f'/html/body/div[3]/div[2]/div[5]/div[2]/div[2]/div/div[{i}]' #Recorre cada búsqueda laboral y va actualizando la variable i para avanzar a la siguiente busqueda
						

	time.sleep(2)

	driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(selector_oferta))
	time.sleep(2)

	try:
		driver.find_element_by_xpath(selector_sueldo).clear()
		driver.find_element_by_xpath(selector_sueldo).send_keys('100000')
		time.sleep(1)
		driver.find_element_by_xpath(boton_postularme).click()
		time.sleep(2)

		
		driver.get(url1)
	except NoSuchElementException:
		driver.get(url1)
		i = i + 1

	


														
	
	