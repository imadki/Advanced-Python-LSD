## Assistant de Texte Intelligent Avancé

### Objectif

Créer une application POO qui lit des textes, détecte la langue, effectue une analyse approfondie en utilisant la théorie des graphes pour identifier les éléments clés, propose des corrections orthographiques, génère un résumé et crée des questions à choix multiples basées sur le texte.

### Composants du Projet

- Détecteur de Langue
    - Classe : LanguageDetector
    - Fonctionnalités : Identifie la langue du texte en utilisant des bibliothèques spécialisées.

- Analyseur de Texte Avancé
    - Classe : AdvancedTextAnalyzer
    - Fonctionnalités : Combine l'analyse de texte traditionnelle (corrections orthographiques, identification des répétitions) avec une analyse basée sur la théorie des graphes pour extraire des mots et phrases clés, et pour générer des résumés.

- Générateur de Résumé
    - Classe : SummaryGenerator
    - Fonctionnalités : Utilise des algorithmes de théorie des graphes pour sélectionner les phrases les plus pertinentes du texte et générer un résumé cohérent.

- Générateur de Questions
    - Classe : QuestionGenerator
    - Fonctionnalités : Crée des questions à choix multiples en se basant sur les informations clés identifiées dans le texte.
 

### Technologies et Outils Suggérés
- Langage de Programmation : Python.
- Outils d'Accélération : multiprocessing pour l'exécution parallèle, Numba pour la compilation JIT de fonctions critiques.
