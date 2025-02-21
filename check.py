from googletrans import Translator
translator = Translator()
translated_text = translator.translate("Hello, how are you?", src="en", dest="es").text
print(translated_text)  # Output: Hola, ¿cómo estás?
