# Guion docente · Ciclo de vida y serialización de modelos 🤖

Duración sugerida: 35–45 minutos. El objetivo es que el grupo comprenda por qué un modelo entrenado debe guardarse y pueda recuperarlo sin volver a entrenarlo.

## 1. Inicio 👋 · 3 minutos

**Idea central:** un modelo no termina cuando se entrena; después debe evaluarse, guardarse y usarse para predecir.

**Puedes decir:** “Hoy vamos a seguir el viaje de un modelo: desde los datos hasta una predicción. La pregunta que resolveremos es: ¿qué pasa con todo el aprendizaje si cerramos Python?”

Invita a observar el mapa de la clase y anticipa que al final resolverán un reto en Colab.

## 2. Ciclo de vida 🔄 · 7 minutos

Recorre el flujo: datos, preparación, entrenamiento, evaluación, serialización, producción y predicción. Usa el simulador para detenerte en dos momentos:

- **Entrenamiento:** el algoritmo aprende patrones a partir de ejemplos.
- **Serialización:** el modelo ya entrenado se convierte en un archivo para conservarlo.

**Pregunta al grupo:** “¿En qué etapa aparecen Pickle y Joblib?” Deja que respondan y usa **Comprobar respuesta** solo después de que se comprometan con una opción.

**Transición:** “Ya sabemos cuándo se guarda el modelo; ahora veamos por qué es necesario hacerlo.”

## 3. Serialización 📦 · 8 minutos

Presenta el problema: cerrar Python elimina los objetos que viven en RAM. Muestra la analogía de guardar una partida de videojuego.

**Puedes decir:** “Entrenar puede costar horas; serializar permite pagar ese costo una vez y reutilizar el resultado.”

Haz la pregunta inicial, y después explica la diferencia entre memoria temporal y archivo persistente. En el mini quiz remarca que serializar no mejora la precisión: permite **guardar y reutilizar**.

## 4. Pickle vs Joblib ⚖️ · 7 minutos

Explica que ambas herramientas guardan objetos de Python, pero Joblib es especialmente práctico para modelos y arreglos grandes de NumPy.

**Regla sencilla para clase:** Pickle es una opción general y sencilla; Joblib suele ser la elección cómoda para modelos de Scikit-Learn con muchos datos.

**Pregunta al grupo:** “¿Cuál elegirían para un modelo grande?” Pide una justificación antes de comprobar. Menciona la regla de seguridad: nunca cargar archivos Pickle o Joblib de origen desconocido.

## 5. Quiz final 🎯 · 7 minutos

Indica que el quiz es individual o en parejas. Las respuestas no aparecen marcadas y la calificación solo se habilita al completar las diez preguntas.

Al revisar resultados, no te limites al puntaje: pide explicar una respuesta incorrecta y relacionarla con la página correspondiente.

## 6. Reto Colab 🏆 · 10–15 minutos

En **Reto Colab**, descarga el cuaderno y súbelo a Google Colab. El cuaderno ofrece pistas progresivas, pero el código clave debe ser escrito por el estudiante.

**Consigna:** “Entrena un árbol de decisión con Iris, mide su accuracy, guarda el modelo en dos formatos, recupéralo y úsalo para hacer una predicción.”

**Pistas que puedes liberar en orden:**

1. Revisa los imports y el dataset que ya están disponibles.
2. Para separar datos, consulta `train_test_split` y usa `random_state=42`.
3. El flujo de entrenamiento es crear el clasificador, usar `.fit()` y luego `.predict()`.
4. Pickle usa `open(..., "wb")` y `pickle.dump`; Joblib usa `dump`.
5. Recuperar es el proceso inverso: `pickle.load` o `joblib.load`.

## Cierre ✅ · 3 minutos

Pide que respondan: “¿Por qué no debemos entrenar un modelo cada vez que llega una predicción?”

Concluye: “Entrenamos una vez, serializamos de forma segura y reutilizamos el modelo cuando lo necesitamos.”
