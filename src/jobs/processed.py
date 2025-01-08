from buisiness import utils
from poo import family

"""
 Livrets de famille ou actes de naissance de tous les enfants,         Done
 acte de mariage (si plusieurs mariages tous les actes)                Done
 carte de séjour,                                                      Done
 passeport ou titre de voyage,                                         Done
 dernière quittance de loyer (si locataire),                           Done ( à imprimer )
 attestation de propriété (si propriétaire) ou emprunt bancaire,
 pièce d’identité du conjoint français,                                Done   
 dernier bulletin de salaire ou justificatif de revenus pour les deux, Done ( à imprimer  le mien et celui d'Océ de Dec )
 contrats de travail pour les deux,                                    ( Contrat océ Done + SIRET/SIREN de mon coté)
 justificatifs de la CAF,                                              Pas besoin
 CV du demandeur de la nationalité française                           Done ( à imprimer )
 diplômes et formations obtenues,                                      Done ( à imprimer )
 dernier avis d’imposition (individuel et/ou du couple).               Done ( à imprimer ) 


"""

didi = family("Yosr Hachani", 30, 'Female', 'La Tunisie')

print(didi.prenom)
print(didi.age)
print(didi.gendre)
print(didi.location)
didi.sleep()