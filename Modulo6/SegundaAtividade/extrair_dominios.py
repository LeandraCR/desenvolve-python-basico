# Lista de URLs de exemplo (todas começam com 'www.' e terminam com '.com')
urls = ["www.google.com", "www.facebook.com", "www.amazon.com"]

# Utilizamos uma compreensão de lista para criar a lista 'dominios'
# Para cada URL na lista 'urls', removemos os 4 primeiros e os 4 últimos caracteres
# 'url[4:-4]' remove "www." do começo e ".com" do final da URL
dominios = [url[4:-4] for url in urls]

# Exibimos a lista 'dominios' resultante, contendo apenas os nomes principais dos domínios
print(dominios)
