from animales import Gato
from animales import creador_gatos
# gato = Gato('Nuevo gato por paquete')
gato = creador_gatos('Nuevo gato por paquete') # al init va esto
print(gato.nombre)
