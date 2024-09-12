# Abrimos o arquivo "meus_livros.csv" no modo de escrita ('w' para write), 
# o que significa que, se o arquivo já existir, ele será sobrescrito.
# O "with" garante que o arquivo será fechado automaticamente após a escrita.
with open('meus_livros.csv', 'w') as arquivo:
    
    # Escrevemos o cabeçalho da planilha com os títulos das colunas:
    # Título, Autor, Ano de publicação, Número de páginas
    # Os valores estão separados por vírgula (formato CSV).
    # O '\n' no final garante que após o cabeçalho seja feita uma quebra de linha.
    arquivo.write('Título,Autor,Ano de publicação,Número de páginas\n')
    
    # Escrevemos os dados de cada livro em uma nova linha.
    # Cada linha contém as informações do livro separadas por vírgula.
    arquivo.write('Dom Quixote,Miguel de Cervantes,1605,1072\n')
    arquivo.write('1984,George Orwell,1949,328\n')
    arquivo.write('O Apanhador no Campo de Centeio,J.D. Salinger,1951,277\n')
    arquivo.write('A Metamorfose,Franz Kafka,1915,201\n')
    arquivo.write('O Sol é Para Todos,Harper Lee,1960,336\n')
    arquivo.write('Orgulho e Preconceito,Jane Austen,1813,432\n')
    arquivo.write('Cem Anos de Solidão,Gabriel García Márquez,1967,417\n')
    arquivo.write('A Revolução dos Bichos,George Orwell,1945,112\n')
    arquivo.write('O Hobbit,J.R.R. Tolkien,1937,310\n')
    arquivo.write('A Divina Comédia,Dante Alighieri,1320,798\n')
    
# Após o bloco 'with', o arquivo é automaticamente fechado.
# Agora, o arquivo 'meus_livros.csv' está criado com os dados e pode ser aberto 
# em um programa como o Excel ou Google Sheets para visualização.
