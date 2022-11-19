# projet_data

Ce répertoire GitHub est dédié à notre projet de Big Data et DataViz. <br /><br />
Il Contient : <br />
    - Un unique fichier qui charge et requête les différents fichiers CSV stocké sur nos containers Hadoop, ainsi que des commandes de visualization pour afficher des graphiques via Pandas <br />
    - Un fichier contenant les variables d'environnement Hadoop <br />
    - Un docker-compose avec tous nos containers <br />
    - Des fichiers CSV contenant nos données <br /><br /><br />

On a un fichier exec.py dans le dossier projet qui permet de faire le traitement des données via un spark-submit mais on arrive pas à faire la visualisation avec le spark submit car on a des erreurs au niveau de l'import et de l'installation de pandas et seaborn.
voici la commande spark-submit pour le run : './bin/spark-submit --master spark-master --deploy-mode client hdfs://namenode:9000/bases/exec.py


Auteurs : Diouf Mohammed, Khattab Youssef, Toussenel Axel
