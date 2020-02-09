# coding=utf-8
a=[
		{
			"label": "Vehículo incendiado"
		},
		{
			"label": "Parking subterráneo"
		},
		{
			"label": "Faltan ruedas : 4"
		},
		{
			"label": "Check Véhicule :  https://imamobile.recette.ima.eu/es/CheckVehicule/O1X3BVs4SK "
		}
]
print ",".join(map(lambda it:it["label"],a))
