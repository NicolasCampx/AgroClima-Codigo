# AgroClima Monitor 2.0 — código do app final

Abra esta pasta no VS Code. Execute instalar.bat e depois executar.bat.
Com o ambiente virtual ativado, também pode executar python main.py.
Recomendado: Python 3.12 x64, Windows 10/11.

Inclui o aplicativo PySide6 completo: Dashboard, Gráficos, Configurações,
serial Arduino, demonstração, estatísticas, SQLite e meteorologia corrigida.
O banco data/agroclima.db e os logs são criados automaticamente na execução.
A configuração inicial foi preservada. Ícones são gerados pelo próprio código.

Feche o Monitor Serial da Arduino IDE ao usar a mesma porta COM no aplicativo.
A instalação das dependências e a meteorologia precisam de internet.

Este pacote contém somente o aplicativo e seus arquivos de execução.
Não inclui firmware Arduino, testes, relatórios de validação ou executáveis.
