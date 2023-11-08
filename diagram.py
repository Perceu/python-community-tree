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
                Python("PyCaxias"),
                Python("PyTchê")
            ] >> pythonSul

        # with Cluster('Eventos Sudeste'): 

        # with Cluster('Eventos Centro'): 

        # with Cluster('Eventos Nordeste'): 

        # with Cluster('Eventos Norte'): 

        [
            pythonSul, 
            pythonSudeste, 
            pythonCentro, 
            pythonNordeste, 
            pythonNorte, 
        ] >> EventoNacional