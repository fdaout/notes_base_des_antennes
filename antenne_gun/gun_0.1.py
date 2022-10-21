# -*- coding: utf-8 -*-

"""
F. Daout & J.C. Henaux
Etude d'une antenne End-Fire
Spring 2020
"""
from math import *
import easygui
import sys
from easygui import *
#*********************************************************************
# entree des caractéristiques de l'antenne
#*********************************************************************
easygui.msgbox(msg="                       ANTENNE END-FIRE OU GUN ANTENNA",image="intro.png",ok_button="continuer")
# entrée de la fréquence
freq=easygui.enterbox(msg="frequence de fonctionnement de l'antenne en GHz ?  \nformat x.xxx, pas de virgule décimale !." )
try:
    Freq_Giga=float(freq)
except:
    print("La fréquence est exprimée dans un mauvais format, exemple de format correct : 2.45, ou 4, ou 3.745\n des chiffres et au plus, un point")
    easygui.msgbox(msg="==>La fréquence est exprimée dans un mauvais format, et n'a pas pu être reconnue. \n  \n  exemples de format correct: \n=>2.45 \n=>4 \n=>3.745\n    des chiffres et au plus, un point.\n\n    la virgule est interdite !")
    sys.exit(0)
    
#entrée de la longueur du GOS     
ln=easygui.buttonbox(msg="longueur du GOS en unités longueurs d'onde :",choices=('1','2','3','4')) 
Ln=int(ln)

#entrée de la taille du réflecteur
ref=easygui.buttonbox(msg='La longueur du G.O.S. étant choisie, Choisir la taille du réflecteur: \n=> un réflecteur plus grand améliore la directivité (env +1.5dB)', title='choix du reflecteur', choices=('L', 'S',"cancel"), images=None, image=None, default_choice=None, cancel_choice=None, callback=None, run=True)



# =============================================================================
# Calcul grand reflecteur
# =============================================================================
if ref=="L":    
   
    if Ln==1:  #cas grand reflecteur, Ln=1 Calcul des dimensions
        r_sma=1.7e-3
        r_pin=0.75e-3
        ep_tole=0.5e-3
        lambda_0=3e8/Freq_Giga*1e-9
        ecart_disc=lambda_0/4
        espace=lambda_0/16
        patch_dia=(32.914+389.4*exp(-1.0063*Freq_Giga))*1e-3
        dist_patch=0.21*patch_dia/2
        dia_axe=0.09*patch_dia
        dia_ref=2*lambda_0
        ray_entree=patch_dia/2*(0.4185+0.62659*exp(-1.2251*Freq_Giga))      
        indice=(1.0083*Ln)/(-0.18119+Ln)
        dia_disc=(-0.58131+1.2681*indice-0.38934*(indice*indice))*lambda_0
        
# préparation des affichages  grand reflecteur, Ln=1
        
        l="longueur du G.O.S.: "+str(Ln)+"*longueur d'onde"+"\n"+"indice du G.O.S.:"+str( round(indice,3))
        a="Frequence de fonctionnement: "+str(Freq_Giga)+" GHz "+"\n"+"longueur d'onde: "+str(round(lambda_0*1000,2))+" mm"              
        b="longueur totale de l'antenne: "+str(round(lambda_0*1000*Ln+dist_patch*1000+espace*1000,1))+" mm"+"\n"+"******************************************"
        c="epaisseur de la tôle: 0.5 mm, non critique"
        d="diametre de l'axe: "+str(round(dia_axe*1000,1))+" mm ou valeur proche"
        e="diametre du patch: "+str(round(patch_dia*1000,2))+" mm  ($)"
        f="distance du centre du connecteur SMA à l'axe :"+str( round(ray_entree*1000,2))+" mm  ($)"
        g="diametre du reflecteur: "+ str(round(dia_ref*1000,1))+" mm"
        h="distance patch-reflecteur: "+str( round(dist_patch*1000,2))+" mm"
        i="espace entre le patch et le premier disque du GOS: "+str( round(espace*1000,2 ))+" mm"
        j="diametre des disques du GOS: "+str( round(dia_disc*1000,1))+" mm"
        k="distance entre les disques du GOS: "+str(round(ecart_disc*1000,1))+" mm"+"\n"+"******************************************"
        m="gain attendu : 13.6dB \n\n\n($) précision nécessaire +-0.4% de la longueur d'onde"
        
# affichage grand reflecteur, Ln=1
        
        z=("\n"+a+"\n"+l+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+f+"\n"+g+"\n"+h+"\n"+i+"\n"+j+"\n"+k+"\n"+"\n"+m)
        print(z)
        easygui.textbox(msg="Dimensions d'une antenne End Fire (antenne Gun) avec un grand reflecteur.(Diametre du reflecteur : 2fois la longueur d'onde)", text=z)
        
#*********************************************************************       
    elif Ln==2: #cas grand reflecteur, Ln=2  Calcul des dimensions
        r_sma=1.7e-3
        r_pin=0.75e-3
        ep_tole=0.5e-3
        lambda_0=3e8/Freq_Giga*1e-9
        ecart_disc=lambda_0/4
        espace=lambda_0/16
        patch_dia=(32.914+389.4*exp(-1.0063*Freq_Giga))*1e-3
        dist_patch=0.21*patch_dia/2
        dia_axe=0.09*patch_dia
        dia_ref=2*lambda_0
        ray_entree=patch_dia/2*(0.44462+0.5331*exp(-0.89585*Freq_Giga))
        indice=(1.0083*Ln)/(-0.18119+Ln)
        dia_disc=(-0.58131+1.2681*indice-0.38934*(indice*indice))*lambda_0
        
# préparation des affichages grand reflecteur, Ln=2
        
        l="longueur du G.O.S.: "+str(Ln)+"*longueur d'onde"+"\n"+"indice du G.O.S.:"+str( round(indice,3))
        a="Frequence de fonctionnement: "+str(Freq_Giga)+" GHz "+"\n"+"longueur d'onde: "+str(round(lambda_0*1000,2))+" mm"              
        b="longueur totale de l'antenne: "+str(round(lambda_0*1000*Ln+dist_patch*1000+espace*1000,1))+" mm"+"\n"+"******************************************"
        c="epaisseur de la tôle: 0.5 mm, non critique"
        d="diametre de l'axe: "+str(round(dia_axe*1000,1))+" mm ou valeur proche"
        e="diametre du patch: "+str(round(patch_dia*1000,2))+" mm($)"
        f="distance du centre du connecteur SMA à l'axe :"+str( round(ray_entree*1000,2))+" mm($)"
        g="diametre du reflecteur: "+ str(round(dia_ref*1000,1))+" mm"
        h="distance patch-reflecteur: "+str( round(dist_patch*1000,2))+" mm"
        i="espace entre le patch et le premier disque du GOS: "+str( round(espace*1000,2 ))+" mm"
        j="diametre des disques du GOS: "+str( round(dia_disc*1000,1))+" mm"
        k="distance entre les disques du GOS: "+str(round(ecart_disc*1000,1))+" mm"+"\n"+"******************************************"
        m="gain attendu : 14.9dB \n\n\n($) précision nécessaire +-0.4% de la longueur d'onde"
        
#affichage grand reflecteur, Ln=2
        z=("\n"+a+"\n"+l+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+f+"\n"+g+"\n"+h+"\n"+i+"\n"+j+"\n"+k+"\n"+"\n"+m)
        print(z)
        easygui.textbox(msg="Dimensions d'une antenne End Fire (antenne Gun) avec un grand reflecteur.(Diametre du reflecteur : 2fois la longueur d'onde)", text=z)

 #*********************************************************************   
    elif Ln==3: #cas grand reflecteur, Ln=3  Calcul des dimensions
        r_sma=1.7e-3
        r_pin=0.75e-3
        ep_tole=0.5e-3
        lambda_0=3e8/Freq_Giga*1e-9
        ecart_disc=lambda_0/4
        espace=lambda_0/16
        patch_dia=(32.914+389.4*exp(-1.0063*Freq_Giga))*1e-3
        dist_patch=0.21*patch_dia/2
        dia_axe=0.09*patch_dia
        dia_ref=2*lambda_0
        ray_entree=patch_dia/2*(0.4407+0.52206*exp(-0.72074*Freq_Giga))     
        indice=(1.0083*Ln)/(-0.18119+Ln)
        dia_disc=(-0.58131+1.2681*indice-0.38934*(indice*indice))*lambda_0

 # préparation des affichages grand reflecteur, Ln=3
       
        l="longueur du G.O.S.: "+str(Ln)+"*longueur d'onde"+"\n"+"indice du G.O.S.:"+str( round(indice,3))
        a="Frequence de fonctionnement: "+str(Freq_Giga)+" GHz "+"\n"+"longueur d'onde: "+str(round(lambda_0*1000,2))+" mm"              
        b="longueur totale de l'antenne: "+str(round(lambda_0*1000*Ln+dist_patch*1000+espace*1000,1))+" mm"+"\n"+"******************************************"
        c="epaisseur de la tôle: 0.5 mm, non critique"
        d="diametre de l'axe: "+str(round(dia_axe*1000,1))+" mm ou valeur proche"
        e="diametre du patch: "+str(round(patch_dia*1000,2))+" mm($)"
        f="distance du centre du connecteur SMA à l'axe :"+str( round(ray_entree*1000,2))+" mm($)"
        g="diametre du reflecteur: "+ str(round(dia_ref*1000,1))+" mm"
        h="distance patch-reflecteur: "+str( round(dist_patch*1000,2))+" mm"
        i="espace entre le patch et le premier disque du GOS: "+str( round(espace*1000,2 ))+" mm"
        j="diametre des disques du GOS: "+str( round(dia_disc*1000,1))+" mm"
        k="distance entre les disques du GOS: "+str(round(ecart_disc*1000,1))+" mm"+"\n"+"******************************************"
        m="gain attendu : 15.8 dB \n\n\n($) précision nécessaire +-0.4% de la longueur d'onde"
         #essai affichage
        z=("\n"+a+"\n"+l+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+f+"\n"+g+"\n"+h+"\n"+i+"\n"+j+"\n"+k+"\n"+"\n"+m)
        print(z)
        easygui.textbox(msg="Dimensions d'une antenne End Fire (antenne Gun) avec un grand reflecteur.(Diametre du reflecteur : 2fois la longueur d'onde)", text=z)

#*********************************************************************        
    elif Ln==4: #cas grand reflecteur, Ln=4  Calcul des dimensions
        r_sma=1.7e-3
        r_pin=0.75e-3
        ep_tole=0.5e-3
        lambda_0=3e8/Freq_Giga*1e-9
        ecart_disc=lambda_0/4
        espace=lambda_0/16
        patch_dia=(32.914+389.4*exp(-1.0063*Freq_Giga))*1e-3
        dist_patch=0.21*patch_dia/2
        dia_axe=0.09*patch_dia
        dia_ref=2*lambda_0
        ray_entree=patch_dia/2*(0.4407+0.52206*exp(-0.72074*Freq_Giga))
        indice=(1.0083*Ln)/(-0.18119+Ln)
        dia_disc=(-0.58131+1.2681*indice-0.38934*(indice*indice))*lambda_0

# préparation des affichages grand reflecteur, Ln=4
        
        l="longueur du G.O.S.: "+str(Ln)+"*longueur d'onde"+"\n"+"indice du G.O.S.:"+str( round(indice,3))
        a="Frequence de fonctionnement: "+str(Freq_Giga)+" GHz "+"\n"+"longueur d'onde: "+str(round(lambda_0*1000,2))+" mm"              
        b="longueur totale de l'antenne: "+str(round(lambda_0*1000*Ln+dist_patch*1000+espace*1000,1))+" mm"+"\n"+"******************************************"
        c="epaisseur de la tôle: 0.5 mm, non critique"
        d="diametre de l'axe: "+str(round(dia_axe*1000,1))+" mm ou valeur proche"
        e="diametre du patch: "+str(round(patch_dia*1000,2))+" mm($)"
        f="distance du centre du connecteur SMA à l'axe :"+str( round(ray_entree*1000,2))+" mm($)"
        g="diametre du reflecteur: "+ str(round(dia_ref*1000,1))+" mm"
        h="distance patch-reflecteur: "+str( round(dist_patch*1000,2))+" mm"
        i="espace entre le patch et le premier disque du GOS: "+str( round(espace*1000,2 ))+" mm"
        j="diametre des disques du GOS: "+str( round(dia_disc*1000,1))+" mm"
        k="distance entre les disques du GOS: "+str(round(ecart_disc*1000,1))+" mm"+"\n"+"******************************************"
        m="gain attendu : 16.7 dB \n\n\n($) précision nécessaire +-0.4% de la longueur d'onde"
        
# affichage grand reflecteur, Ln=4
        z=("\n"+a+"\n"+l+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+f+"\n"+g+"\n"+h+"\n"+i+"\n"+j+"\n"+k+"\n"+"\n"+m)
        print(z)
        easygui.textbox(msg="Dimensions d'une antenne End Fire (antenne Gun) avec un grand reflecteur.(Diametre du reflecteur : 2fois la longueur d'onde)", text=z)
         
    else : # Ln, doit être un entier
        sys.exit(0) 



    
# =============================================================================
#  Calcul petit reflecteur
# =============================================================================
#cas petit reflecteur,  Ln=1
         
elif ref=="S":
       
    if Ln==1:   # petit reflecteur, Ln=1 calcul des dimensions
        r_sma=1.7e-3
        r_pin=0.75e-3
        ep_tole=0.5e-3
        lambda_0=3e8/Freq_Giga*1e-9
        ecart_disc=lambda_0/4
        espace=lambda_0/16
        patch_dia=(33.41+404.72*exp(-1.0282*Freq_Giga))*1e-3
        dist_patch=0.21*patch_dia/2
        dia_axe=0.09*patch_dia
        dia_ref=1.23*patch_dia
        ray_entree=patch_dia/2*(0.42511+1.3595*exp(-1.754*Freq_Giga))
        indice=(1.0083*Ln)/(-0.18119+Ln)
        dia_disc=(-0.58131+1.2681*indice-0.38934*(indice*indice))*lambda_0
        
#preparation des affichages petit reflecteur, Ln=1

        l="longueur du G.O.S.: "+str(Ln)+"*longueur d'onde"+"\n"+"indice du G.O.S.:"+str( round(indice,3))
        a="Frequence de fonctionnement: "+str(Freq_Giga)+" GHz "+"\n"+"longueur d'onde: "+str(round(lambda_0*1000,2))+" mm"              
        b="longueur totale de l'antenne: "+str(round(lambda_0*1000*Ln+dist_patch*1000+espace*1000,1))+" mm"+"\n"+"******************************************"
        c="epaisseur de la tôle: 0.5 mm, non critique"
        d="diametre de l'axe: "+str(round(dia_axe*1000,1))+" mm ou valeur proche"
        e="diametre du patch: "+str(round(patch_dia*1000,2))+" mm($)"
        f="distance du centre du connecteur SMA à l'axe :"+str( round(ray_entree*1000,2))+" mm($)"
        g="diametre du reflecteur: "+ str(round(dia_ref*1000,1))+" mm"
        h="distance patch-reflecteur: "+str( round(dist_patch*1000,2))+" mm"
        i="espace entre le patch et le premier disque du GOS: "+str( round(espace*1000,2 ))+" mm"
        j="diametre des disques du GOS: "+str( round(dia_disc*1000,1))+" mm"
        k="distance entre les disques du GOS: "+str(round(ecart_disc*1000,1))+" mm"+"\n"+"******************************************"
        m="gain attendu : 12dB \n\n\n($) précision nécessaire +-0.4% de la longueur d'onde"
        
# affichage petit reflecteur, Ln=1
        
        z=("\n"+a+"\n"+l+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+f+"\n"+g+"\n"+h+"\n"+i+"\n"+j+"\n"+k+"\n"+"\n"+m)
        print(z)
        easygui.textbox(msg="Dimensions d'une antenne End Fire (antenne Gun) avec un petit reflecteur.(Diametre du reflecteur :1.2 fois la longueur d'onde)", text=z)
        
#*********************************************************************
    
    elif Ln==2: #cas petit reflecteur, Ln=2 calcul des dimensions
        r_sma=1.7e-3
        r_pin=0.75e-3
        ep_tole=0.5e-3
        lambda_0=3e8/Freq_Giga*1e-9
        ecart_disc=lambda_0/4
        espace=lambda_0/16
        patch_dia=(33.41+404.72*exp(-1.0282*Freq_Giga))*1e-3
        dist_patch=0.21*patch_dia/2
        dia_axe=0.09*patch_dia
        dia_ref=1.23*patch_dia
        ray_entree=patch_dia/2*(0.43986+0.84856*exp(-1.0541*Freq_Giga))
        indice=(1.0083*Ln)/(-0.18119+Ln)
        dia_disc=(-0.58131+1.2681*indice-0.38934*(indice*indice))*lambda_0
        
# préparation des affichages petit reflecteur, Ln=2      
        
        l="longueur du G.O.S.: "+str(Ln)+"*longueur d'onde"+"\n"+"indice du G.O.S.:"+str( round(indice,3))
        a="Frequence de fonctionnement: "+str(Freq_Giga)+" GHz "+"\n"+"longueur d'onde: "+str(round(lambda_0*1000,2))+" mm"              
        b="longueur totale de l'antenne: "+str(round(lambda_0*1000*Ln+dist_patch*1000+espace*1000,1))+" mm"+"\n"+"******************************************"
        c="epaisseur de la tôle: 0.5 mm, non critique"
        d="diametre de l'axe: "+str(round(dia_axe*1000,1))+" mm ou valeur proche"
        e="diametre du patch: "+str(round(patch_dia*1000,2))+" mm($)"
        f="distance du centre du connecteur SMA à l'axe :"+str( round(ray_entree*1000,2))+" mm($)"
        g="diametre du reflecteur: "+ str(round(dia_ref*1000,1))+" mm"
        h="distance patch-reflecteur: "+str( round(dist_patch*1000,2))+" mm"
        i="espace entre le patch et le premier disque du GOS: "+str( round(espace*1000,2 ))+" mm"
        j="diametre des disques du GOS: "+str( round(dia_disc*1000,1))+" mm"
        k="distance entre les disques du GOS: "+str(round(ecart_disc*1000,1))+" mm"+"\n"+"******************************************"
        m="gain attendu : 13.3dB \n\n\n($) précision nécessaire +-0.4% de la longueur d'onde"
        
# affichage petit reflecteur, Ln=2
        
        z=("\n"+a+"\n"+l+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+f+"\n"+g+"\n"+h+"\n"+i+"\n"+j+"\n"+k+"\n"+"\n"+m)
        print(z)
        easygui.textbox(msg="Dimensions d'une antenne End Fire (antenne Gun) avec un petit reflecteur.(Diametre du reflecteur :1.2 fois la longueur d'onde)", text=z)
   
    

#*********************************************************************    
    elif Ln==3: #cas petit reflecteur,  Ln=3 calcul des dimensions
        r_sma=1.7e-3
        r_pin=0.75e-3
        ep_tole=0.5e-3
        lambda_0=3e8/Freq_Giga*1e-9
        ecart_disc=lambda_0/4
        espace=lambda_0/8
        patch_dia=(33.41+404.72*exp(-1.0282*Freq_Giga))*1e-3
        dist_patch=0.21*patch_dia/2
        dia_axe=0.09*patch_dia
        dia_ref=1.23*patch_dia
        ray_entree=patch_dia/2*(0.44213+1.0672*exp(-1.169*Freq_Giga))
        indice=(1.0083*Ln)/(-0.18119+Ln)
        dia_disc=(-0.58131+1.2681*indice-0.38934*(indice*indice))*lambda_0
        
# préparation des affichages petit reflecteur, Ln=3
        
        l="longueur du G.O.S.: "+str(Ln)+"*longueur d'onde"+"\n"+"indice du G.O.S.:"+str( round(indice,3))
        a="Frequence de fonctionnement: "+str(Freq_Giga)+" GHz "+"\n"+"longueur d'onde: "+str(round(lambda_0*1000,2))+" mm"              
        b="longueur totale de l'antenne: "+str(round(lambda_0*1000*Ln+dist_patch*1000+espace*1000,1))+" mm"+"\n"+"******************************************"
        c="epaisseur de la tôle: 0.5 mm, non critique"
        d="diametre de l'axe: "+str(round(dia_axe*1000,1))+" mm ou valeur proche"
        e="diametre du patch: "+str(round(patch_dia*1000,2))+" mm($)"
        f="distance du centre du connecteur SMA à l'axe :"+str( round(ray_entree*1000,2))+" mm($)"
        g="diametre du reflecteur: "+ str(round(dia_ref*1000,1))+" mm"
        h="distance patch-reflecteur: "+str( round(dist_patch*1000,2))+" mm"
        i="espace entre le patch et le premier disque du GOS: "+str( round(espace*1000,2 ))+" mm"
        j="diametre des disques du GOS: "+str( round(dia_disc*1000,1))+" mm"
        k="distance entre les disques du GOS: "+str(round(ecart_disc*1000,1))+" mm"+"\n"+"******************************************"
        m="gain attendu : 14.1 dB \n\n\n($) précision nécessaire +-0.4% de la longueur d'onde"

# affichage petit reflecteur, Ln=3
        z=("\n"+a+"\n"+l+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+f+"\n"+g+"\n"+h+"\n"+i+"\n"+j+"\n"+k+"\n"+"\n"+m)
        print(z)
        easygui.textbox(msg="Dimensions d'une antenne End Fire (antenne Gun) avec un petit reflecteur.(Diametre du reflecteur :1.2 fois la longueur d'onde)", text=z)

#*********************************************************************   
    elif Ln==4: #cas petit reflecteur, Ln=4 calcul des dimensions
        r_sma=1.7e-3
        r_pin=0.75e-3
        ep_tole=0.5e-3
        lambda_0=3e8/Freq_Giga*1e-9
        ecart_disc=lambda_0/4
        espace=lambda_0/8
        patch_dia=(33.41+404.72*exp(-1.0282*Freq_Giga))*1e-3
        dist_patch=0.21*patch_dia/2
        dia_axe=0.09*patch_dia
        dia_ref=1.23*patch_dia
        ray_entree=patch_dia/2*(0.44213+1.0672*exp(-1.169*Freq_Giga))
        indice=(1.0083*Ln)/(-0.18119+Ln)
        dia_disc=(-0.58131+1.2681*indice-0.38934*(indice*indice))*lambda_0
        
# préparation des affichages   petit reflecteur, Ln=4      
                
        l="longueur du G.O.S.: "+str(Ln)+"*longueur d'onde"+"\n"+"indice du G.O.S.:"+str( round(indice,3))
        a="Frequence de fonctionnement: "+str(Freq_Giga)+" GHz "+"\n"+"longueur d'onde: "+str(round(lambda_0*1000,2))+" mm"              
        b="longueur totale de l'antenne: "+str(round(lambda_0*1000*Ln+dist_patch*1000+espace*1000,1))+" mm"+"\n"+"******************************************"
        c="epaisseur de la tôle: 0.5 mm, non critique"
        d="diametre de l'axe: "+str(round(dia_axe*1000,1))+" mm ou valeur proche"
        e="diametre du patch: "+str(round(patch_dia*1000,2))+" mm($)"
        f="distance du centre du connecteur SMA à l'axe :"+str( round(ray_entree*1000,2))+" mm($)"
        g="diametre du reflecteur: "+ str(round(dia_ref*1000,1))+" mm"
        h="distance patch-reflecteur: "+str( round(dist_patch*1000,2))+" mm"
        i="espace entre le patch et le premier disque du GOS: "+str( round(espace*1000,2 ))+" mm"
        j="diametre des disques du GOS: "+str( round(dia_disc*1000,1))+" mm"
        k="distance entre les disques du GOS: "+str(round(ecart_disc*1000,1))+" mm"+"\n"+"******************************************"
        m="gain attendu : 14.7 dB \n\n\n($) précision nécessaire +-0.4% de la longueur d'onde"

# affichage petit reflecteur, Ln=4
        
        z=("\n"+a+"\n"+l+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+f+"\n"+g+"\n"+h+"\n"+i+"\n"+j+"\n"+k+"\n"+"\n"+m)
        print(z)
        easygui.textbox(msg="Dimensions d'une antenne End Fire (antenne Gun) avec un petit reflecteur.(Diametre du reflecteur :1.2 fois la longueur d'onde)", text=z)
  
    else : # Ln, doit être un entier
        sys.exit(0)  
#********************************************************************* 

else :  #La dimension du reflecteur est incorrecte
   sys.exit(0)

