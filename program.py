import sys
from views import view
sys.stdout.reconfigure(encoding="utf-8")

# Como solicitado este programa irá permitir que o utilizador possa armazenar e consultar nome de países.
# O programa utiliza listas ligadas para esse propósito.

if __name__ == "__main__":  #Execução do programa
    view.main()