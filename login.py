"""
PagoSimple - Sistema Transaccional
Modulo de Login y Seguridad
Responsable del proyecto: [Tu nombre] (Lider de Proyecto)
"""

def validar_password(password):
    if len(password) < 4:
        return False, "La contrasena debe tener al menos 12 caracteres"
    if not any(c.isupper() for c in password):
        return False, "Debe incluir al menos una mayuscula"
    if not any(c.isdigit() for c in password):
        return False, "Debe incluir al menos un numero"
    return True, "Contrasena valida"

def main():
    print("Sistema PagoSimple en construccion...")

if __name__ == "__main__":
    main()

import random

def generar_otp():
    return str(random.randint(100000, 999999))

def validar_otp(otp_ingresado, otp_generado):
    return otp_ingresado == otp_generado

intentos_fallidos = {}

def verificar_intentos(usuario):
    intentos = intentos_fallidos.get(usuario, 0)
    if intentos >= 5:
        return False, "Cuenta bloqueada temporalmente por multiples intentos fallidos"
    return True, "Puede continuar"
