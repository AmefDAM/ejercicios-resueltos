def remove_html_markup(string):
    tag_mode = False
    quote_mode = False
    output = ""

    for character in string:
        if character == '<':
            tag_mode = True
        elif character == '>':
            tag_mode = False
        elif character == '"' or character == '"' and tag_mode:
            quote_mode = not quote_mode
        elif not tag_mode:
            output = output + character

    return output


# Casos test:

if __name__ == '__main__':
    # Test Cases:

    assert remove_html_markup('"<b>foo</b>"') == "foo"

    # assert remove_html_markup('"<meta charset="utf-8">"') == ""

    # assert remove_html_markup('"<!-- Breve descripción de la sección -->"') == ""

    # assert remove_html_markup('"<a href="#presentacion">Presentación</a>"') == "Presentación"

    # assert remove_html_markup('"<p> Saludos y <b>bienvenid@s</b>, hayáis llegado aquí como hayáis llegado. </p>"') == "Saludos y bienvenidos, hayáis llegado aquí como hayáis llegado."

    # assert remove_html_markup('"<section id="conocimiento-git">
    #                <h3>
    #                    Git y GitHub
    #                </h3>
    #                <article id="git-notes">
    #                    <h4>
    #                        Git Notes
    #                    </h4>
    #                    <p>
    #                        <span class="resource-type">Documentación</span>
    #                    </p>
    #                    <p>
    #                        Apuntes prácticos sobre Git y GitHub, comandos, flujos de trabajo y gestión de repositorios.
    #                    </p>
    #                    <p>
    #                        <a href="https://github.com/AmefDAM/gitnotes">Consultar apuntes</a>
    #                    </p>
    #                </article>
    #            </section>"') ==

    # assert remove_html_markup() ==

    # assert remove_html_markup() ==

    # assert remove_html_markup() ==

print("All tests passed!")