# ✨Vigilo Notebooks BaPaV ✨

>Des notebooks Jupyter pour l'analyse les données vigilo de Brest
>Fork réalisé depuis `jesuisundesdeux/vigilo-notebooks` pour BaPaV. 

Pour tester ces notebooks, 

## _Sous Linux_ (description à améliorer)

Utilisez l'image docker prévue à cet effet. Lancez la commande suivante

```
make jupyter
```

Placez vous dans le dossier de travail, et lancez la commande
```
jupyter-lab
```




**Note:** le premier lancement est assez long, allez boire un café :)

## _Sous Windows_ (description à mieux tester)

Ouvrir l'invité de commande Windows en tapant la commande  `cmd` dans l'explorateur Windows

Vérifiez si Python est intallé ou non avec la commande
```
python --version
```
Ne rien faire si une version s'affiche, sinon entrez la commande
```
python
```
Le Microsoft Store s'ouvrira alors pour vous proposer d'installer python. Installez le.
Une fois que c'est fait, le gestionnaire de packages python `pip` devrait être installé aussi. 

La prochaine étape consiste à installer jupyter-lab avec la commande
```
pip install jupyterlab
```
Pour pouvoir exécuter les notebooks de `vigilo-notebooks-bapav`, il faudra aussi installer manuellement toutes les librairies indiquées dans `vigilo-notebooks-bapav\requirements.txt` (`requests`, `pandas`,`matplotlib`, ...) avec la commande 
```
pip install NomDeLaLib
```
Enfin pour démarrer `jupyter`, il faut se déplacer dans le dossier `vigilo-notebooks-bapav` avec la commande `cd` puis lancer la commande 
```
python -m notebook
```
Vous devriez avoir accès à tous les fichiers se trouvant dans `vigilo-notebooks-bapav`. Dans le cas contraire, il se peut qu'il y ait un problème avec l'initialisation de l'URL, il faudra alors prendre l'autre URL indiqué dans l'inviter de commande. Vous pouvez maintenant exécuter les différentes cellules des notebooks jupyter avec la combinaison clavier `shift+enter`.