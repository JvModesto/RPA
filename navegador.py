# importando as bibliotecas necessárias
import os
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


# abre o navegador chrome usando selenium, o headless=false serve para
# mostrar oq esta acontecendo durante a execução do código em tempo real.
def iniciar_navegador(headless=False):
    options = Options() # inicializa as opções do Chrome

    if headless:
        options.add_argument('--headless')

    user_data_dir = os.path.abspath("chrome_profile") # perfil de usuário real (isso ajuda a evitar detecção de bot)
    # o Chrome armazena os dados do usuário em um diretório específico, e eu estou dizendo ao selenium para usar esse diretório,
    # assim eu crio um perfil com dados reais, como histórico de navegação, cookies e etc. É importante ressaltar que
    # não é adequado usar o prórpio perfil, como por exemplo (C:\Users\Usuario\AppData\Local\Google\Chrome\UserData), pois isso
    # pode corromper o perfil e comprometer a segurança. Então, eu criei um diretório separado para armazenar os dados

    options.add_argument(f"--user-data-dir={user_data_dir}") # uso o diretório do perfil de usuário real
    options.add_argument("--profile-directory=Default")  # dentro do user-data_dir, o Chrome armazena os perfis de usuário em subdiretórios,
    # eu estou dizendo ao Selenium para usar o perfil "Default", mas poderia ser qualquer outro

    options.add_experimental_option("excludeSwitches", ["enable-automation"]) # remove a flag de automamação do selenium
    options.add_experimental_option("useAutomationExtension", False) # impede o selenium de carregar a extensão de automação
    # o add_argument é para colocar argumentos na linha de comando ao iniciar o chrome, já o add_experimental_option
    # altera configurações internas usadas pelo ChromeDriver e pelo Chrome ao serem iniciados automações.

    options.add_argument("--window-size=1920,1080") # tamanho da janela
    options.add_argument("--disable-blink-features=AutomationControlled")
    # essa opção desativa um recurso do Chrome que marca o navegador como "controlado por automação"
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")
    # aqui eu estou dizendo ao selenium para usar o mesmo agente de usuário que o Chrome normalmente usaria,
    # sem isso o selenium envia um user-agent padrão, que é facilmente detectável como um bot

    service = Service()  # serviço do ChromeDriver
    # esse age como uma ponte entre o código e o navegador, vai me ajudar a abrir páginas, clicar em botões e etc.

    driver = webdriver.Chrome(service=service, options=options)  # usa o serviço para inicializar o Chrome, com as opções definidas
    return driver
    # é importante resaltar que o Google já é bem inteligente para as proteções contra bots, mas pode ser que nem todos os métodos
    # utilizados sejam realmente necessários, mas ainda assim é bom para ter mais chance de não ser detectado.


## faz a pesquisa no google com o termo fornecido
def buscar_no_google(driver, termo):
    driver.get("https://www.google.com")  # abre a página do Google
    time.sleep(random.uniform(2.5, 4.5))  # delay mais realista

    caixa_pesquisa = driver.find_element(By.NAME, "q") # busco um certo elemento na pagina pelo nome,
    # utilizo "q" para achar a caixa de pesquisa pq no codigo fonte do google
    # o campo de pesquisa tem essa estrutura: <input type="text" name="q" class="search">

    caixa_pesquisa.send_keys(termo) # coloco o termo desejado na caixa de pesquisa
    time.sleep(random.uniform(0.5, 1.5))  # pequeno delay antes de enviar
    caixa_pesquisa.send_keys(Keys.RETURN)  # pressiono ENTER para buscar
    time.sleep(random.uniform(3, 5))


## pega os resultados da pesquisa (titulo, URL, dominio e resumo) e salva em uma lista
def extrair_resultados(driver, limite):
    resultados = []
    paginas_navegadas = set()  # controla quais páginas já foram visitadas
    pagina = 1

    while len(resultados) < limite:
        if pagina in paginas_navegadas:  # impede que uma página seja visitada mais de uma vez
            pagina += 1
            continue

        paginas_navegadas.add(pagina)  # adiciona a página atual ao conjunto de páginas navegadas

        # início da coleta de dados:
        blocos = driver.find_elements(By.CSS_SELECTOR, 'div.tF2Cxc')  # identifica blocos de resultados na página
        # obs: o Google organiza os resultados das pesquisas dentro de <div> que possuem a classe "tF2Cxc".
        # Onde cada um contém informações sobre um resultado da pesquisa, então ao fazer isso, eu estou pegando todos
        # os blocos de resultados sendo exibidos.

        for bloco in blocos:
            try:
                # coleta título, URL e domínio do resultado
                titulo = bloco.find_element(By.CSS_SELECTOR, 'h3').text.strip() # dentro do bloco, h3 é onde se encontra o titulo
                url = bloco.find_element(By.TAG_NAME, 'a').get_attribute('href').strip() # a tag <a> é onde se encontra o link e href contém a URL
                fonte = urlparse(url).netloc # urlparse divide a url em partes, e usando o netloc eu digo que quero só o domínio

                try: # como nem todos os resultados tem resumo, coloco um try/except e se nao tiver só deixo vazio
                    resumo = bloco.find_element(By.CSS_SELECTOR, 'div.VwiC3b').text.strip() # div.VwiC3b é onde se encontra o resumo
                except:
                    resumo = " "

                if titulo and url:
                    resultados.append({ # adiciona os resultados a lista usando um dicionário
                        "Título": titulo,
                        "URL": url,
                        "Resumo": resumo,
                        "Fonte": fonte
                    })
                    if len(resultados) >= limite:
                        print(f"Total de resultados coletados: {len(resultados)}")
                        return resultados  # retorna os resultados se atingir o limite

            except Exception:
                continue

        pagina += 1 # atualizando para a próxima página

        # navegação entre as páginas:
        try:
            numero_pagina = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"a[aria-label='Page {pagina}']"))
            )
            # espera até que o elemento da página desejada esteja clicável. Procuro um link <a> que o
            # atributo aria-label seja igual ao número da página desejada

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # rola a página até o fim
            # essa linha é mais uma preocaução para evitar que o elemento que eu quero clicar não esteja visível na tela

            time.sleep(random.uniform(2, 4))
            numero_pagina.click()  # clica no número da página
            time.sleep(random.uniform(2.5, 4.5))


        except Exception as e:
            print(f"Erro ao tentar mudar para a página {pagina}: {e}")
            break

    print(f"Total de resultados coletados: {len(resultados)}")
    return resultados
