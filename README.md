# CoreX

**Documentation des Outils Système**
Cette suite de scripts Python forme un ensemble d'outils dédiés à la gestion, sécurité, analyse, et maintenance d’un système informatique. Chaque module a un rôle spécifique, et l’ensemble vise à offrir une interface complète pour la surveillance et l’optimisation du système.

**1. diagnostics.py**
But : Effectuer une analyse complète du système.
Fonctionnalité :
Ce module collecte des informations en temps réel sur les ressources système (CPU, RAM, espace disque, température, etc.). Il peut être utilisé pour détecter les ralentissements, les erreurs ou les comportements anormaux du système.

**2. encryption.py**
But : Assurer la confidentialité des fichiers.
Fonctionnalité :
Permet de chiffrer et déchiffrer des fichiers à l’aide d’algorithmes de cryptographie (ex. AES). Il peut être utilisé pour sécuriser des données sensibles contre les accès non autorisés.

**3. file_cleaner.py**
But : Libérer de l’espace disque.
Fonctionnalité :
Ce script recherche et supprime automatiquement les fichiers inutiles (temporaires, logs, caches, etc.) pour maintenir un système propre et performant.

**4. file_manager.py**
But : Gérer les fichiers du système.
Fonctionnalité :
Offre des opérations de base sur les fichiers : déplacement, suppression, renommage, copie. Il peut également organiser les fichiers selon des critères définis (taille, date, type...).

**5. gui.py**
But : Fournir une interface utilisateur graphique.
Fonctionnalité :
Module principal de l’interface graphique. Il regroupe les différents outils dans une fenêtre intuitive et interactive, facilitant leur utilisation sans ligne de commande.

**6. main.py**
But : Gérer le fonctionnement global de l'application.
Fonctionnalité :
Point d’entrée principal de l’application. Ce script orchestre l'exécution des différents modules et assure leur communication entre eux.

**7. net_utils.py**
But : Fournir des outils pour le diagnostic réseau.
Fonctionnalité :
Analyse du réseau local, test de connectivité (ping, DNS, ports), détection des adresses IP connectées, surveillance de l’activité réseau. Utile pour détecter les coupures ou intrusions.

**8. password_generator.py**
But : Générer des mots de passe sécurisés.
Fonctionnalité :
Crée des mots de passe robustes et aléatoires selon des critères personnalisables (longueur, complexité, caractères spéciaux). Renforce la sécurité des comptes et données.

**9. proccess_monitor.py**
But : Surveiller l’activité des processus.
Fonctionnalité :
Affiche en temps réel les processus actifs, leur consommation mémoire et processeur. Permet de détecter des applications suspectes ou trop gourmandes, avec possibilité de les arrêter.

**10. setup.bat ( Executable avec le cmd de Windows/Linux )**
But : Préparer l’environnement de l'application.
Fonctionnalité :
Script de configuration automatique. Installe les dépendances Python nécessaires, initialise les paramètres par défaut et prépare le système pour l’exécution de l'application.

**11. start.bat ( Executable avec le cmd de Windows/Linux )**
But : Lancer l’application.
Fonctionnalité :
Script de démarrage rapide. Permet à l'utilisateur d’exécuter toute l’application d’un simple double-clic, sans avoir à entrer de commandes manuelles.

**12. system_info.py**
But : Afficher les informations système générales.
Fonctionnalité :
Récupère et affiche des données de base sur la machine : nom d’hôte, version du système d’exploitation, architecture, mémoire installée, etc. Sert à mieux comprendre le matériel utilisé.

Conclusion
Cette suite d’outils forme une boîte à outils numérique complète, idéale pour les administrateurs système, les développeurs ou les utilisateurs avancés souhaitant :

- Surveiller leur machine,

- Améliorer ses performances,

- Sécuriser leurs données,

- Diagnostiquer les problèmes.

