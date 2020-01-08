"""def p_decorador(func):
    def nova_func(num1,num2):
        return "<p>" + func(num1,num2) + "</p>"
    return nova_func


@p_decorador
def devolve_trecho(num1, num2):
    return "Result: %g"%(num1 * num2 )


def p_decorador(func):
    def nova_func(num1,num2):
        return "<p>" + func(num1,num2) + "</p>"
    return nova_func


def div_decorador(func):
    def nova_func(num1,num2):
        return "<div>" + func(num1,num2) + "</div>"
    return nova_func


def strong_decorador(func):
    def nova_func(num1,num2):
        return "<strong>" + func(num1,num2) + "</strong>"
    return nova_func


@p_decorador
@div_decorador
@strong_decorador
def devolve_trecho(num1, num2):
    return "Result: %g"%(num1 * num2 )
"""

def tags(nome_tag):
    def tags_decorador(func):
        def nova_func(num1,num2):
            return "<" + nome_tag + ">" + func(num1,num2) + "</" + nome_tag + ">"

        return nova_func
    return tags_decorador

@tags("p")

def devolve_trecho(num1, num2):
    return "Resultado: %g"%(num1 * num2)

print(devolve_trecho(1,2))

    
















    


