#!/usr/bin/env python3
import time


def question_03():
    status = f"""
        +-----------------------------------------------------+
        |Question 3                                           |
        |Quelle commande affiche tous les CA d'une topologie ?|
        +-----------------------------------------------------+
    """
    ibhosts = "ibhosts"

    print(status)
    template = input("[root@ibswitch]#")

    if template == ibhosts:
        print(
            f"""
            Ca      : 0x0800380001389fcb ports 1 "c1016 HCA-1"
            Ca      : 0x0800380001389e91 ports 1 "c1015 HCA-1"
            Ca      : 0x0800380001389fbe ports 1 "c1012 HCA-1"
            Ca      : 0x080038000137467b ports 1 "c1011 HCA-1"
        """
        )

        time.sleep(1)
        print(
            f"""
            +--------------+
            |Bonne réponse!|
            +--------------+
        """
        )
    else:
        print(
            f"""
            +---------------------------------+
            |FAUX!                            |
            |La bonne réponse était 'ibhosts' |
            |Merci de ré-essayer              |
            +---------------------------------+
    -------------------------------------------------
        """
        )
        time.sleep(1)
        question_03()


if __name__ == "__main__":
    question_03()
