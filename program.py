import sys
from views import view
sys.stdout.reconfigure(encoding="utf-8")

# Como solicitado este programa irá permitir que consultores de uma imobiliária possam registar
# e gerir os imóveis que têm para venda.

if __name__ == "__main__":  #Execução do programa
    view.main()