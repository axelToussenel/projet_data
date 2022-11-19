# projet_data

Ce répertoire GitHub est dédié à notre projet de Big Data et DataViz. <br /><br />
Il Contient : <br />
 
    - Notre diaporama de présentation <br />
    -Un dossier Spark-cluster contenant 
        un docker compose , 
        le dossier projet avec les différentes source de données et le code python du spark submit,
        le fichier ProjetData qui contient nos requêttes faites sur jupiter noteBook 
        Les dossiers de nos différents containers <br /><br /><br />
   

On a fait un traitement de nos données avec le fichier exec.py qui se trouve dans le dossier projet via un spark submit mais on arrive pas affiché la visualisation avec le fichier python car on a des erreurs au niveau de l'installation et de l'import de pandas et seaborn.
Voici la commande spark submit qui permet de run le code python : ' ./bin/spark-submit    --master spark-master    --deploy-mode client    hdfs://namenode:9000/bases/exec.py ' 


A noter que notre Spark-Submit ne marchait pas lors de la présentation ainsi que nos visualisation des jointures entre les dataframe du fait qu'un de nos machine était H-S lors de la présentation.

Auteurs : Diouf Mohammed, Khattab Youssef, Toussenel Axel
