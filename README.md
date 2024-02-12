# Apps Gestión Hospitalaria

Este trabajo fue propuesto por el profesor Edwin Puertas para ver qué nivel de conocimientos en Python teníamos (aplicando PEP8 y los conceptos vistos de UX), el documento de contexto del caso se encuentra [aquí](files\docs\Apps%20Gestion%20Hospitalaria.pdf). Ahora, del tema de hospitales realmente tengo demasiado desconocimiento, no sé cómo funcionan, por lo que, es normal que quizás mucho de lo que se pida no tenga sentido, no obstante, vista mi limitación, traté de hacer lo mejor en cuanto a código se refiera.

Para ejecutar el programa, no es completamente necesario tener imágenes diagnósticas, solamente hay una condición, si la carpeta no está vacía, sí o sí para todos los pacientes tienen que colocarse imágenes, no importa que sea la misma, tampoco importa qué contengan las imágenes, para los datos de prueba, las imágenes fueron sacado de los siguientes lugares:

- [123456.png](files\diagnostics_images\123456.png). [https://www.researchgate.net/figure/Figura-3-Ejemplo-de-imagenes-diagnosticas-incluidas-en-los-ejercicios-de-simulacion-de_fig6_309885486](https://www.researchgate.net/figure/Figura-3-Ejemplo-de-imagenes-diagnosticas-incluidas-en-los-ejercicios-de-simulacion-de_fig6_309885486).
- [234567.jpg](files\diagnostics_images\234567.jpg). [https://vetxana.com/diagnostico-por-imagen/](https://vetxana.com/diagnostico-por-imagen/).
- [345678.jpeg](files\diagnostics_images\345678.jpeg). [https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSypNcKR5c1k4tVqe4f9lCnsPvPBT7hyQfT7gUCocbZQv4LeAUgdJTOBvHfhECCEDB3XNY&amp;usqp=CAU](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSypNcKR5c1k4tVqe4f9lCnsPvPBT7hyQfT7gUCocbZQv4LeAUgdJTOBvHfhECCEDB3XNY&usqp=CAU).
- [456789.jpg](files\diagnostics_images\456789.jpg). [https://www.teknon.es/es/pruebas-diagnosticas/diagnostico-imagen/radiologia-convencional-digitalizada/columna/rx-sacro-coccix](https://www.teknon.es/es/pruebas-diagnosticas/diagnostico-imagen/radiologia-convencional-digitalizada/columna/rx-sacro-coccix).
- [567890.jpg](files\diagnostics_images\567890.jpg). [https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSn_9YOlJUwQDUM3mIn-16ZighKOWFygLaVoSqAdVPwl_vst-BA42VM5sLg8uCRan2hlA0&amp;usqp=CAU](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSn_9YOlJUwQDUM3mIn-16ZighKOWFygLaVoSqAdVPwl_vst-BA42VM5sLg8uCRan2hlA0&usqp=CAU).

El archivo [patients.csv](files\patients.csv) es vítal, ese debe estar sí o sí, sugiero que este nunca se toque, aunque de hecho, en un contexto de la vida real, los usuarios no deberían tener acceso directo a este archivo, por la misma razón, no hubo tantas validaciones a la hora de leer mencionado archivo.

Para ejecutar el programa, se tiene que hacer en el archivo [app.py](app.py), este contendrá la función `main()` y dentro de la misma, se utilizan todos los demás archivos que fueron creados.
