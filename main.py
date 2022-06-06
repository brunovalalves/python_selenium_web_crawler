from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

def obter_dano_granada(time,jogador):
    print('Iniciando o método de obter maior dano por granada do jogador '+str(jogador)+' do time '+str(time))
    driver.get (time)
    driver.implicitly_wait(5)
    driver.find_elements (By.CLASS_NAME, 'bodyshot-team-img')[jogador].click()
    driver.implicitly_wait(5)
    driver.find_element (By.CLASS_NAME, 'moreButton').click()
    driver.implicitly_wait(5)
    dano_da_granada = driver.find_elements (By.CLASS_NAME, 'stats-row')[5].find_elements(By.TAG_NAME,'span')[1].text
    print ('O valor do jogador '+str(jogador)+' é '+dano_da_granada+' do time '+str(time))
    return dano_da_granada

driver.get ('https://www.hltv.org/')
driver.implicitly_wait(10)
driver.find_element (By.CLASS_NAME, 'CybotCookiebotDialogBodyButton').click()
driver.implicitly_wait(10)
times = ['https://www.hltv.org/team/4411/nip','https://www.hltv.org/team/8297/furia','https://www.hltv.org/team/7461/copenhagen-flames']
jogadores = [0,1,2,3,4]
maior_dano_granada = 0
jogador_maior_dano = None
time_maior_dano = None
for t in times:
    for j in jogadores:
        d = float(obter_dano_granada(t,j))
        if d > maior_dano_granada:
            maior_dano_granada = d
            jogador_maior_dano = j
            time_maior_dano = t
            print('O valor '+str(d)+' é o maior encontrado até o momento')
        
print('O valor do maior dano de granada foi '+str(maior_dano_granada)+ ' do time '+time_maior_dano+' do jogador '+str(jogador_maior_dano))
        
        
    

#pesquisa = input('O que você deseja saber?')
#driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(pesquisa)
#driver.find_element (By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/a[1]/div/img').click()

input('ok?')

driver.close()

