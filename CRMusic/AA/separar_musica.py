import os
import re


def separar_arquivo(caminho_arquivo, pasta_saida='arquivos_separados'):
  # Cria a pasta de saída se ela não existir
  os.makedirs(pasta_saida, exist_ok=True)

  with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    conteudo = f.read()

  # Divide o conteúdo por linhas que contêm 5 ou mais sublinhados
  blocos = re.split(r'\n_{5,}\n?', conteudo)

  for i, bloco in enumerate(blocos):
    bloco = bloco.strip()
    if not bloco:
      continue

    linhas = bloco.splitlines()
    # A primeira linha é usada como o nome do arquivo
    primeira_linha = linhas[0].strip()

    # Remove caracteres inválidos do nome do arquivo
    nome_arquivo_sanitizado = re.sub(r'[\\/*?:"<>|]', '_', primeira_linha)

    if not nome_arquivo_sanitizado:
      nome_arquivo_sanitizado = f'musica_{i+1}'

    caminho_saida = os.path.join(
        pasta_saida, f'{nome_arquivo_sanitizado}.md'
    )

    with open(caminho_saida, 'w', encoding='utf-8') as f_out:
      f_out.write(bloco)

    print(f'Arquivo gerado: {caminho_saida}')


if __name__ == '__main__':
  # Coloque aqui o nome do seu arquivo de texto original
  separar_arquivo('musicas.txt')
