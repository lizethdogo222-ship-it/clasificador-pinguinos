def clasificador_humano(bill_length, bill_depth, flipper_length, body_mass):
    """
    Sistema experto basado en reglas simples
    para clasificar especies de pingüinos.
    """

    if flipper_length > 205 and bill_depth <= 17:
        return "Gentoo"

    elif bill_length > 45 and bill_depth > 17:
        return "Chinstrap"

    else:
        return "Adelie"