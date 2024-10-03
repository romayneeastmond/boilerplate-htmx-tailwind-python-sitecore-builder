# Boilerplate Sitecore XM Cloud Component Builder

Quickly reduce the amount of time needed to generate Sitecore XM Cloud components. Simply enter the data type, field name, template field name, and renderer type on a single line and then press submit to have the boilerplate code generated with the necessary imports, component properties, rendering fields, and JSX element output. Also generates a representation of the item using GraphQL syntax.

## HTMX, Tailwind CSS, and Flash (Python) Environment

Demonstration written by serving an HTMX index file with Flask (Python) and styled using Tailwind CSS. The HTMX binds the forms submit event to an endpoint on the Flask instance, and then accepts the boilerplate code to be displayed within the inner HTML of a div element. Tailwind CSS creates the responsive design that also supports dark mode detection.

## Examples

Provide a component name for the fields and then seperate each field definition on a new line. Use Type, Field Name, Label, Renderer format.

##### Text rendering
* object, firstName, First Name, Text

##### RichText rendering
* object, content, Content, RichText

##### Link rendering
* object, url, Url, Link

##### Image rendering
* object, backgroundImage, Background Image, Image

##### Date rendering
* object, publishDate, Publish Date, Date

##### File rendering
* object, pdf, Pdf, File

##### No rendering
* string, category, Category, None

## Copyright and Ownership

All terms used are copyright to their original authors.

## Live Demo

Live demo hosted in Microsoft Azure, PHP 7.4 App Service [Boilerplate Sitecore XM Cloud Component Builder](https://dev-python-boilerplate-sitecore.azurewebsites.net/).

Azure F1 instances are :snowflake: ice cold. That first load will need some :sun_with_face: warming up.