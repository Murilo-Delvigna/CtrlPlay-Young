try:
    f = open('arquivo.txt', 'w')
    f.write('Tente escrever isso')

except IOError:
    print('Não foi possivel localizar o arquivo')
else:
    print('Texto escrito com sucesso')
    f.close()

finally:
    print('Sempre execute os comandos do bloco finally')