from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql       import functions as D


spark1 = SparkSession.\
        builder.\
        appName("pyspark-notebook").\
        master("spark://spark-master:7077").\
        config("spark.executor.memory", "2g").\
        getOrCreate() 
path1 = 'hdfs://namenode:9000/bases/carbu.csv'
path2 = 'hdfs://namenode:9000/bases/loyer.csv'
path4 = 'hdfs://namenode:9000/bases/ecoles.csv'


df1 = spark1.read.format('csv').options(header=True).load(path1)
df2 = spark1.read.format('csv').options(header=True).load(path2)
df4 = spark1.read.format('csv').options(header=True).load(path4)

print('Nombre Ecole par commune')
dfEc = df4.groupBy('libelle_commune').agg(D.count(df4.numero_uai).alias('NbreEcole'))
dfEc.show()

print('Prix moyen du caburant par ville et par type de carburant')
dfCarMoy = df1.groupBy('prix_nom', 'ville').agg(D.avg(df1.prix_valeur))
dfCarMoy.show()


print('Prix max du caburant par région et par type de carburant')
dfCarMax = df1.groupBy('prix_nom', 'reg_name').agg(D.avg(df1.prix_valeur))
dfCarMax.show()


print('Date ouverture plus Anciennes Ecoles par Région ')
AncEc = (df4.groupBy('libelle_region').agg({'date_ouverture':'min'}))
AncEc.show()


print('Prix du loyer au m2 ')
temp = df2.withColumn("prix_m2",(df2.moyenne_loyer_mensuel/df2.surface_moyenne))
prix_m2 = temp.groupBy("agglomeration").agg(D.avg(temp.prix_m2).alias('locm2'))
prix_m2.show()


print('Jointure entre loyer et école')
LocEco = df2.join(df4, df2.agglomeration == df4.libelle_commune , 'inner')
LocEco.show()


print('Jointure entre prix loyer m2 et nombre école')
LocM2Eco = dfEc.join(prix_m2,dfEc.libelle_commune == prix_m2.agglomeration,'inner')
LocM2Eco.show()

print('Jointure entre prix loyer m2 et prix du carburant')
LocM2Car = dfCarMoy.join(prix_m2,dfCarMoy.ville == prix_m2.agglomeration,'inner')
LocM2Car.show()

   
print('Jointure entre caburant et loyer')
LocCar = df2.join(df1, df2.agglomeration == df1.ville , 'inner')
LocCar.show()

