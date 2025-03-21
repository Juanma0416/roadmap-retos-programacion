"""
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
"""

from pathlib import Path
import xml.etree.ElementTree as XML


file_name_xml = "ignaciovihe.xml"

programmer = {
    "name": "ignacio",
    "age": "40",
    "date_of_birth": "23/02/1985",
    "languages": ["python", "Javascript", "GO"]
}


def create_xml():

    #Creo la estructura XML
    root = XML.Element("programmer")# Creo el elemento raiz <programmer>

    #Crear los subelementos
    for key, value in programmer.items():
        child = XML.SubElement(root, key)
        if isinstance(value, list):
            for language in value:
                XML.SubElement(child, "language").text = language
        else:
            child.text = value

    tree = XML.ElementTree(root) # Convertimos la estructura en un árbol XML
    tree.write(file_name_xml, encoding="utf-8", xml_declaration=True) # Guardamos el XML en un archivo.


def read_xml():

    # Cargar el archivo XML
    tree = XML.parse(file_name_xml) # Abre y analiza el archivo XML
    root = tree.getroot()  # Obtiene el elemento raíz del XML (<programmer> en este caso)

    # Recorrer los elementos 'libro' y extraer información
    for child in root:
        if len(child) == 0:
            print(f"{child.tag}: {child.text}")
        else:
            languages = ""
            for language in child:
                languages += (language.text + ", ")
            print(f"{child.tag}: {languages.strip(", ")}")


def delete_file(file_name):

    file = Path(file_name)
    if file.exists():
        file.unlink()

create_xml()
read_xml()
delete_file(file_name_xml)
