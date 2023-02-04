==============
Demand Forecast
==============

Para efetuar a previsão resolvi utilizar o modelo ARIMA disponibilizada através do pacote `statsmodels`, 
para manipulação de dados foi utilizado dataframees do `pandas`.

Versão do Python utilizada: 3.10.9


Fontes:
-------

* Stackoverflow: https://stackoverflow.com/questions/26097916/convert-pandas-series-to-dataframe
* Tutorial no _Youtube: https://www.youtube.com/watch?v=v7rZpT8NCbk
* Documentação official do _Statsmodels:`https://www.statsmodels.org/stable/user-guide.html
* Documentação official do _Python:`https://docs.python.org/3/
* Documentação official do _Pandas:`https://pandas.pydata.org/docs/user_guide/index.html


1. Para instalar dependencias

.. code-block::
    
    python -m venv .venv && . .venv/bin/activate
    python -m pip install -r requirements.txt

2. Para rodar o script

.. code-block::

    python script.py
