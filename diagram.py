# diagram.py
from diagrams import Diagram, Cluster
from diagrams.programming.language import Python

with Diagram("Python Comunity", show=False, direction="TB"):
    EventoNacional = Python("Python Brasil")
    with Cluster('Eventos Regionais'): 
        pythonSul = Python("Python Sul")
        pythonSudeste = Python("Python Sudeste")
        pythonCentro = Python("Python Centro Oeste")
        pythonNordeste = Python("Python Nordeste")
        pythonNorte = Python("Python Norte")

        with Cluster('Eventos Sul'): 
            [
                Python("GruPy-PR"),
                Python("Pug-SC"),
                Python("GruPy Blumenau"),
                Python("Python Floripa"),
                Python("PyCaxias"),
                Python("PyTchê")
            ] >> pythonSul

        with Cluster('Eventos Sudeste'): 
            [
                Python("PythonOnRio"),
                Python("GruPy-ES"),
                Python("GruPy-Campinas"),
                Python("GruPy-ABC"),
                Python("GrupyBauru"),
                Python("GruPy-SP"),
                Python("Python Sorocaba"),
                Python("grupy-sanca"),
                Python("GruPy Sul Fluminense"),
                Python("GruPy-RP"),
                Python("Py013"),
                Python("Pug-MG")
            ] >> pythonSudeste

        with Cluster('Eventos Centro'): 
            [
                Python("GruPy-GO"),
                Python("GruPy-DF"),
                Python("Pydata BSB"),
                Python("GruPy-MT")
            ] >> pythonCentro

        with Cluster('Eventos Nordeste'): 
            [
                Python("Pug-SE"),
                Python("GruPy-RN"),
                Python("GruPy-BA"),
                Python("Pug-CE"),
                Python("GruPy-Al"),
                Python("Pug-PI"),
                Python("Pug-PE"),
                Python("PUG-PB"),
                Python("Pug-MA"),
            ] >> pythonNordeste

        with Cluster('Eventos Norte'): 
            [
                Python("PyNorte"),
                Python("Pug-Am"),
                Python("GruPy-RO")
            ] >> pythonNorte

        [
            pythonSul, 
            pythonSudeste, 
            pythonCentro, 
            pythonNordeste, 
            pythonNorte, 
        ] >> EventoNacional